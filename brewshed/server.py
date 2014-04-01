from brewshed import server_name
from brewshed import server_port
from paste import httpserver
from brewshed.calculator import app


def main():
    httpserver.serve(app, host=server_name, port=server_port)

if __name__ == '__main__':
    main()