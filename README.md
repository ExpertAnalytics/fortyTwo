fortyTwo
========

The XAL Application Framework, known as XAF or just fortyTwo. 


To get started, simply type the following commands in you bash shell:

::

    $ curl -O http://python-distribute.org/distribute_setup.py
    $ python distribute_setup.py
    $ sudo easy_install pip
    $ sudo pip install virtualenv
    $ cd fortyTwo
    $ virtualenv fortyTwo-env
    $ source fortyTwo-env/bin/activate

Additionally, iPython is of great help:

::
    $ cd fortyTwo-env
    $ pip install ipython

Use your local package manager to install nginx, e.g.

::
    $ brew install nginx
Locate your nginx configuration file and possibly change the port it listens for and start it. With homebrew on a Mac, this works:

::
    $ vim /usr/local/etc/nginx/nginx.conf
    $ sudo nginx

Then get uwsgi

::
    $ pip install uwsgi

webapp2:
::
    $ pip install WebOb
    $ pip install webapp2

Databases:
::
    $ pip install pymongo
    $ pip install elasticsearch

*Warning:* If you have installed python with homebrew on mac, the setup seems to not work.
