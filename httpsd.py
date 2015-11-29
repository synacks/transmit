#!/usr/bin/python

import BaseHTTPServer, SimpleHTTPServer
import ssl

httpd = BaseHTTPServer.HTTPServer(('0.0.0.0', 443), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='/etc/nginx/ssl/nginx.key',
certfile='/etc/nginx/ssl/nginx.crt', server_side=True)
httpd.serve_forever()