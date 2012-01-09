#!/usr/bin/env python

import sys
import os
import logging

logging.basicConfig()
sys.path.insert(1, os.path.join(os.path.dirname(__file__),'src/site-packages'))

from mykiss.application import Application

if __name__ == "__main__":
    try:
        app = Application(package="mykiss", 
                          package_name="Mykiss",
                          version="0",
                          data_dir=os.path.join(os.path.abspath(os.path.dirname(__file__)),'data'),
                          log_level=logging.DEBUG,
                          plugin_dir=os.path.join(os.path.abspath(os.path.dirname(__file__)), 'src', 'plugins'))
    except Exception, e:
        sys.exit("Could not initialize application: %s" % str(e))
    app.run(sys.argv)
