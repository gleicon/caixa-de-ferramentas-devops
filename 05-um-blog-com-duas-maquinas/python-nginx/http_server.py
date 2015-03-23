#!/usr/bin/python

import SimpleHTTPServer
import SocketServer
import cgi
import socket

PORT=10000

class ReuseAddrTCPServer(SocketServer.TCPServer):
    def server_bind(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):

        self.wfile.write("<html><body><form action='/' method=POST>")
        self.wfile.write("<textarea name=msg rows='10' cols='100'></textarea>")
        self.wfile.write("<br><input type='submit' name='submit'>")
        self.wfile.write("</form></body></html>")
        return

    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })

        for field in form.keys():
            self.wfile.write('\t%s=%s\n' % (field, form[field].value))

        return

ReuseAddrTCPServer(("", PORT), ServerHandler).serve_forever()

