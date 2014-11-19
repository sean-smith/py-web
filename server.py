import BaseHTTPServer
import SimpleHTTPServer
import SocketServer
from optparse import OptionParser
import os
import time
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

changed = False

class Py_Web:
    def __init__(self):
        """
        Gets command line inputs and parses them
        """
        self.time = time.time()
        parser = OptionParser()
        parser.add_option("-i","--ip", dest="host",
                  help="Specify ip to serve at", default="127.0.0.1")
        parser.add_option("-p", "--port", dest="PORT", default=5000,
                  help="Specify Port")
        parser.add_option("-r", "--reload", dest="reload", default="True",
                  help="Reload Automatically True/False, default is True")
        (options, args) = parser.parse_args()
        if options.reload.lower() == "true":
            self.reload = True
        else:
            self.reload = False
        self.host = options.host
        self.port = int(options.PORT)
        self.run()


    def run(self):
        """
        Runs the program
        """
        if not self.reload:
            try:
                httpd = self.reload()
                httpd.serve_forever()
            except KeyboardInterrupt as e:
                print("Shutting Down...")
        else:
            self.reloadable_run()


    def reloadable_run(self):
        httpd = self.reload(self.host, self.port)
        self.watch_file_structure(httpd)

    def reload(self):
        """
        Reloads the Server
        """
        print("Serving "+self.host+" on port "+str(self.port))
        print("To shut down press Ctrl-c")
        handler = Server_Commands
        return BaseHTTPServer.HTTPServer((self.host, self.port), handler)

    def watch_file_structure(self, httpd):
        path = '.'
        event_handler = MyHandler()
        observer = Observer()
        observer.schedule(event_handler, path, recursive=True)
        observer.start()
        try:
            while not changed:
                httpd.handle_request()
            self.reloadable_run()
        except KeyboardInterrupt:
            observer.stop()
            print("Shutting Down...")
        observer.join()


class Server_Commands(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.response(200)
        s.header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        req_path = s.path
        path = os.listdir
        if req_path=="/" and "index.html" in path:
            file = "index.html"
        elif s.path in path:
            file = s.path
        else:
            s.response(404)
            return
        s.header("content-type", file.)
        s.response(200)
        s.response
        s.wfile("<html><head></head><body><h1> Sean\'s webpage</h1></body></html>")
    def get_type():
        get_Type(


class MyHandler(FileSystemEventHandler, Py_Web):
    def on_any_event(self, event):
        print("detecting "+event.event_type+" "+event.src_path)
        print("Reloading Server...")
        changed = True


if __name__ == "__main__":
    Py_Web()
