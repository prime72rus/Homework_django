import os
import urllib.parse
from http.server import BaseHTTPRequestHandler


class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за
    обработку входящих запросов от клиентов
    """

    def get_contact_page(self) -> str:
        """
        Метод чтения HTML-файла
        """
        file_path = os.path.join(os.path.dirname(__file__), "html", "contacts.html")
        with open(file_path, "r", encoding="utf-8") as file:
            html_content = file.read()
        return html_content

    def do_GET(self) -> None:
        """
        Метод для обработки входящих GET-запросов
        """
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(self.get_contact_page(), "utf-8"))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

    def do_POST(self) -> None:
        """
        Метод для обработки входящих POST-запросов
        """
        try:
            content_length = int(self.headers["Content-Length"])
            body = self.rfile.read(content_length).decode("utf-8")
            parsed_data = urllib.parse.parse_qs(body)

            for key, value in parsed_data.items():
                print(f"{key}: {value[0]}")

            self.send_response(303)
            self.send_header("Location", "/")
            self.end_headers()
        except Exception as e:
            print(f"Ошибка при обработке POST-запроса: {e}")
            self.send_response(500)
            self.end_headers()

        # class MyServer(BaseHTTPRequestHandler):
        #     """
        #     Специальный класс, который отвечает за
        #     обработку входящих запросов от клиентов
        #     """
        #     def get_contact_page(self) -> str:
        #         """Метод чтения HTML-файла"""
        #         file_path = os.path.join(os.path.dirname(__file__), "html", "contacts.html")
        #         with open(file_path, "r", encoding="utf-8") as file:
        #             html_content = file.read()
        #         return html_content
        #
        #     def do_GET(self):
        #         """
        #         Метод для обработки входящих GET-запросов
        #         """
        #         self.send_response(200)
        #         self.send_header("Content-type", "text/html")
        #         self.end_headers()
        #         self.wfile.write(bytes(self.get_contact_page(), "utf-8"))
        #
        #     def do_POST(self):
        """
        Метод для обработки входящих POST-запросов
        """


#         content_length = int(self.headers["Content-Length"])
#         body = self.rfile.read(content_length).decode("utf-8")
#         parsed_data = urllib.parse.parse_qs(body)
#
#         # Выводим данные в консоль
#         for key, value in parsed_data.items():
#             print(f"{key}: {value[0]}")
#         self.send_response(200)
#         self.send_header("Content-type", "text/html")
#         self.end_headers()
#         response_html = self.get_contact_page()
#         self.wfile.write(bytes(response_html, "utf-8"))
