# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import weather_pb2 as weather__pb2


class WeatherServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTemperature = channel.unary_unary(
                '/weather.WeatherService/GetTemperature',
                request_serializer=weather__pb2.City.SerializeToString,
                response_deserializer=weather__pb2.Temperature.FromString,
                )
        self.GetHumidity = channel.unary_unary(
                '/weather.WeatherService/GetHumidity',
                request_serializer=weather__pb2.City.SerializeToString,
                response_deserializer=weather__pb2.RelHumidity.FromString,
                )
        self.GetDetailed = channel.unary_unary(
                '/weather.WeatherService/GetDetailed',
                request_serializer=weather__pb2.City.SerializeToString,
                response_deserializer=weather__pb2.Detailed.FromString,
                )


class WeatherServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetTemperature(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetHumidity(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDetailed(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WeatherServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTemperature': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTemperature,
                    request_deserializer=weather__pb2.City.FromString,
                    response_serializer=weather__pb2.Temperature.SerializeToString,
            ),
            'GetHumidity': grpc.unary_unary_rpc_method_handler(
                    servicer.GetHumidity,
                    request_deserializer=weather__pb2.City.FromString,
                    response_serializer=weather__pb2.RelHumidity.SerializeToString,
            ),
            'GetDetailed': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDetailed,
                    request_deserializer=weather__pb2.City.FromString,
                    response_serializer=weather__pb2.Detailed.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'weather.WeatherService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class WeatherService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetTemperature(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/weather.WeatherService/GetTemperature',
            weather__pb2.City.SerializeToString,
            weather__pb2.Temperature.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetHumidity(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/weather.WeatherService/GetHumidity',
            weather__pb2.City.SerializeToString,
            weather__pb2.RelHumidity.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDetailed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/weather.WeatherService/GetDetailed',
            weather__pb2.City.SerializeToString,
            weather__pb2.Detailed.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
