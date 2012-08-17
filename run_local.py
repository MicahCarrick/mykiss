#!/usr/bin/env python
"""
Run Local

Run Mykiss from the current folder, setting up local paths for plugins and 
application data. This script is primarily used for development. 
"""
import sys
import os
import logging
from gi.repository import Gtk

# local data paths
data_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)),'data')
plugin_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'src', 'plugins')

# add our local site-packages which would normally be installed to system
sys.path.insert(1, os.path.join(os.path.dirname(__file__),'src/site-packages'))

# append local named icons to theme search path for named icons
theme = Gtk.IconTheme.get_default()
theme.append_search_path(os.path.join(data_dir, 'icons'))

from mykiss.application import Application

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG) # for run_local.py only!
    
    try:
        app = Application(package="mykiss", 
                          package_name="Mykiss",
                          version="0.3",
                          data_dir=data_dir,
                          plugin_dir=plugin_dir)
    except Exception as e:
        sys.exit("Could not initialize application: %s" % str(e))
    app.run(sys.argv)
