py-web
======

Simple python based webserver. It's easy to use, yet powerful.

Usage
-----

Simply type <code>webserver</code> into shell:

    $ webserver
    Serving 127.0.0.1 on port 5000
    To shut down press Ctrl-c


This will automatically start a server on localhost (127.0.0.1) with port 5000. This server serves your current directory.

To specify the port add a <code>-p</code> and the port number. For example:

    $ webserver -p 800
    Serving 127.0.0.1 on port 800
    To shut down press Ctrl-c

To specify the host (ip) address add a <code>-i</code> and the ip address.

    $ webserver -i 0.0.0.0 -p 80
    Serving 0.0.0.0 on port 80
    To shut down press Ctrl-c

The above line will make your site live at your ip address.



To install:
-----------

    $ git clone https://github.com/sean-smith/py-web.git

    $ cd py-web

    $ sudo pip install -r requirements.txt

    $ brew install libyaml
