## Steps to test/run the service

1. 'pip -V'
2. If pip is not installed, then run 'pip install virtualenv'
3. virtualenv -p python3 env (First time only)
4. source env/bin/activate (on windows, this activates the virtual env)
5. pip install grpcio grpcio-tools (one time setup)
6. After making changes to the proto file, you have to run below to generate the stubs. `python -m grpc_tools.protoc --proto_path=. ./weather.proto --python_out=. --grpc_python_out=.`


