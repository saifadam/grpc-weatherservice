import grpc
from concurrent import futures
import weather_pb2_grpc as pb2_grpc
import weather_pb2 as pb2
 
class WeatherService(pb2_grpc.WeatherServiceServicer):
 
    def __init__(self, *args, **kwargs):
        pass


    def GetTemperature(self, request, context):
        city_name = request.name
        print("Temperature request for : {}".format(city_name))
        # get the string from the incoming request
        return pb2.Temperature(fahrenheit = 77.8, celcius = 21.3)

    def GetHumidity(self, request, context):
        city_name = request.name
        print("Humidity request for : {}".format(city_name))
        return pb2.RelHumidity(percentage=85.0)

    def GetDetailed(self, request, context):
        city_name = request.name
        print("Humidity request for : {}".format(city_name))
        t1 = pb2.Temperature(celcius=18.1, fahrenheit=57.3)
        rh = pb2.RelHumidity(percentage=73)
        return pb2.Detailed(temperature=t1, rel_humidity=rh)

 
def serve():
   server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
   pb2_grpc.add_WeatherServiceServicer_to_server(WeatherService(), server)
   server.add_insecure_port('[::]:50051')
   server.start()
   server.wait_for_termination()
 
 
if __name__ == '__main__':
   serve()