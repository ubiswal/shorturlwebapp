from http.server import BaseHTTPRequestHandler
import socketserver
import os
from src.server.home_html import home_page_html, short_url_redirect_html, not_found_html
from src.database.localdao import LocalDAO
from src.logic.generate_url import generate_tiny_url
from src.logic.get_full_url import get_full_url


if __name__ == "__main__":
    port = 8080
    with LocalDAO("shorturl") as localdao:
        class ShortUrlRequestHandler(BaseHTTPRequestHandler):
            def extract_body(self):
                content_len = int(self.headers.get('Content-Length'))
                return self.rfile.read(content_len)

            def do_GET(self):
                if self.path == "/":
                    self.send_response(200, "OK")
                    self.send_header("Content-type", "text/html")
                    self.send_header("Access-Control-Allow-Origin", "*")
                    self.end_headers()
                    self.wfile.write(bytes(home_page_html, "utf-8"))
                else:
                    try:
                        full_url = get_full_url(self.path[1:], localdao)
                        if not full_url.startswith("https://"):
                            full_url = "https://{}".format(full_url)
                        my_response = short_url_redirect_html.replace("{{url}}", full_url)
                        self.send_response(200, "OK")
                        self.send_header("Content-type", "text/html")
                        self.send_header("Access-Control-Allow-Origin", "*")
                        self.end_headers()
                        self.wfile.write(bytes(my_response, "utf-8"))
                    except KeyError:
                        self.send_response(404, "OK")
                        self.send_header("Content-type", "text/html")
                        self.send_header("Access-Control-Allow-Origin", "*")
                        self.end_headers()
                        self.wfile.write(bytes(not_found_html, "utf-8"))

            def do_POST(self):
                # extract the body of the request
                content = self.extract_body().decode("utf-8")
                self.send_response(200, "OK")
                self.send_header("Content-type", "text/html")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(bytes(generate_tiny_url(content, localdao), "utf-8"))

        with socketserver.TCPServer(("", port), ShortUrlRequestHandler) as httpd:
            print("serving at port", port)
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("Shutting down server.")
                httpd.server_close()
