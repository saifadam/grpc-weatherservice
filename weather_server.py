import grpc
from concurrent import futures
import weather_pb2_grpc as pb2_grpc
import weather_pb2 as pb2
from weather_utils import get_temperature, get_rel_humidity

class WeatherService(pb2_grpc.WeatherServiceServicer):
 
    def __init__(self, *args, **kwargs):
        pass

    def GetTemperature(self, request, context):
        city_name = request.name
        print("Temperature request for : {}".format(city_name))
        # get the string from the incoming request
        tf, tc = get_temperature(city_name)
        return pb2.Temperature(fahrenheit = tf, celcius = tc)

    def GetHumidity(self, request, context):
        city_name = request.name
        print("Humidity request for : {}".format(city_name))
        relhum = get_rel_humidity(city_name)
        return pb2.RelHumidity(percentage=relhum)

    def GetDetailed(self, request, context):
        city_name = request.name
        print("Humidity request for : {}".format(city_name))
        tf, tc = get_temperature(city_name)
        relhum = get_rel_humidity(city_name)
        t1 = pb2.Temperature(celcius=tc, fahrenheit=tf)
        rh = pb2.RelHumidity(percentage=relhum)
        return pb2.Detailed(temperature=t1, rel_humidity=rh)

 
def serve():
   server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
   pb2_grpc.add_WeatherServiceServicer_to_server(WeatherService(), server)
   server.add_insecure_port('[::]:50051')
   server.start()
   server.wait_for_termination()
 
 
if __name__ == '__main__':
   serve()