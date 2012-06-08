#!/usr/bin/env python

import sys
import os
import logging
import argparse



# add our local site-packages which would normally be installed to system
sys.path.insert(1, os.path.join(os.path.dirname(__file__),'src/site-packages'))

from mykiss.application import Application

if __name__ == "__main__":
    # parse command line options
    parser = argparse.ArgumentParser(description="A programmer's text editor.")
    parser.add_argument('-l', '--loglevel', default='WARNING',
                        help='Set the logging level: CRITICAL, ERROR, WARNING, INFO, DEBUG')
    args = parser.parse_args()
    
    # setup logging
    loglevel = getattr(logging,args.loglevel)
    #logging.basicConfig(level=loglevel)
    logging.basicConfig(level=logging.DEBUG) # for run_local.py only!
    
    try:
        app = Application(package="mykiss", 
                          package_name="Mykiss",
                          version="0.1-dev",
                          data_dir=os.path.join(os.path.abspath(os.path.dirname(__file__)),'data'),
                          plugin_dir=os.path.join(os.path.abspath(os.path.dirname(__file__)), 'src', 'plugins'))
    except Exception, e:
        sys.exit("Could not initialize application: %s" % str(e))
    app.run(sys.argv)
