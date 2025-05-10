from src.http_server import MyServer
from http.server import HTTPServer


def main() -> None:

    hostname = "localhost"
    serverport = 8080

    webserver = HTTPServer((hostname, serverport), MyServer)
    print("Server started http://%s:%s" % (hostname, serverport))

    try:
        webserver.serve_forever()
    except KeyboardInterrupt:
        pass

    webserver.server_close()
    print("Server stopped.")


if __name__ == "__main__":
    main()
