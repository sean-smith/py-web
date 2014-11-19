import BaseHTTPServer
from optparse import OptionParser
import os
import time
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


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
        PORT = int(options.PORT)
        if options.reload.lower() == "true":
            reload = True
        else:
            reload = False
        self.run(options.host, PORT, reload)


    def run(self, host, port, reload):
        """
        Runs the program
        """
        if not reload:
            try:
                httpd = self.reload(host, port)
                httpd.serve_forever()
            except KeyboardInterrupt as e:
                print("Shutting Down...")
        else:
            self.reloadable_run(host, port)


    def reloadable_run(self, host, port):
        httpd = self.reload(host, port)
        self.watch_file_structure(httpd)

    def reload(self, host, port):
        """
        Reloads the Server
        """
        print("Serving "+host+" on port "+str(port))
        print("To shut down press Ctrl-c")
        handler = BaseHTTPServer.BaseHTTPRequestHandler
        return BaseHTTPServer.HTTPServer((host, port), handler)

    def watch_file_structure(self, httpd):
        path = '.'
        event_handler = MyHandler()
        observer = Observer()
        observer.schedule(event_handler, path, recursive=True)
        observer.start()
        try:
            while True:
                httpd.handle_request()
        except KeyboardInterrupt:
            observer.stop()
            print("Shutting Down...")
        observer.join()


class MyHandler(FileSystemEventHandler, Py_Web):
    def on_any_event(self, event):
        print("detecting "+event.event_type+" "+event.src_path)
        print("Reloading Server...")
        self.reload("0.0.0.0", 80)


if __name__ == "__main__":
    Py_Web()
