import grpc
import weather_pb2_grpc as pb2_grpc
import weather_pb2 as pb2


class WeatherClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.WeatherServiceStub(self.channel)

    def get_temperature(self, city):
        """
        Client function to call the rpc for GetTemperature
        """
        print(f"Fetching temperature for {city}")
        return self.stub.GetTemperature(pb2.City(name=city))

    def get_rel_humidity(self, city):
        """
        Client function to call the rpc for GetHumidity
        """
        print(f"Fetching temperature for {city}")
        return self.stub.GetHumidity(pb2.City(name=city))
    
    def get_detailed(self, city):
        """
        Client function to call the rpc for GetHumidity
        """
        print(f"Fetching detailed weather for {city}")
        return self.stub.GetDetailed(pb2.City(name=city))


if __name__ == '__main__':
    client = WeatherClient()
    result = client.get_temperature("New York")
    print(f'{result}')
    print("---------------------------------------------")
    result = client.get_rel_humidity("Boston")
    print(f'{result}')
    print("---------------------------------------------")
    result = client.get_detailed("Chennai")
    print(f'{result}')