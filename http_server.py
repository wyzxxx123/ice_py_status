#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus
from global_var import server_list

import threading

import Ice

Ice.loadSlice('servoStatus.ice')
import service


class RequestThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("开始线程：" + self.name)
        run()
        print("退出线程：" + self.name)


# HTTPRequestHandler class
class HTTPServerRequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
        self.handle_http_request()

    def do_POST(self):
        self.handle_http_request()

    def handle_http_request(self):
        try:
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()

            str_value = "<html><body><title>Servers</title><h2>服务器列表：</h2><ul>"

            for k, v in server_list.items():
                t_value = "{"
                if isinstance(v, service.ServerReportProfile):
                    ser = v.__dict__
                    for k_x, x in ser.items():
                        """
                         status是枚举，如果有必要的话对每个类型中文化
                        """
                        if str(k_x) == "status":
                            pass
                        t_value += str(k_x) + ":\'" + str(x) + "\'   "
                else:
                    t_value += str(v)
                t_value += "}"
                str_value += "<li><span style='color:green'>{0} </span> : {1} </li>".format(k, t_value)

            str_value += "</ul></body></html>"

            self.wfile.write(bytes(str_value, 'utf-8'))
            self.wfile.flush()
            # self.finish()
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)


def run():
    port = 10401
    print('starting http, port', port)

    # Server settings
    server_address = ('', port)
    httpd = HTTPServer(server_address, HTTPServerRequestHandler)
    print('running http...')
    httpd.serve_forever()
