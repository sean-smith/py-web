import BaseHTTPServer
from optparse import OptionParser
import os, time, sys
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

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
        try:
            handler = BaseHTTPServer.BaseHTTPRequestHandler
            httpd = BaseHTTPServer.HTTPServer((host, port), handler)

            if not reload:
                print("serving "+host+" on port "+str(port))
                print("To shut down press Ctrl-c")
                httpd.serve_forever()
            else:
                while reload_not_true():
                    httpd.handle_request()

        except KeyboardInterrupt as e:
            print("Shutting Down...")

    def reload_not_true(self):
        current = os.listdir()
        


if __name__ == "__main__":
    Py_Web()
