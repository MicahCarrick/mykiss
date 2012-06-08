import os

from gi.repository import Gtk

from mykiss.plugin import MykissPlugin
from mykiss import icons

class FileBrowserPlugin(MykissPlugin):
    icon_name = Gtk.STOCK_DIRECTORY
    def activate(self):
        super(FileBrowserPlugin, self).activate()

        # add dock item to existing windows
        #for window in self.application.get_windows():
            #self.add_dock_item_to_window(window)
        
        # add dock item to existing windows
        self.connect(self.application, "window-added", self.on_window_added)
    
    def add_dock_item_to_window(self, window):
        """
        Install a new terminal dock item in the window.
        
        Args:
            window -- A `mykiss.window.Window()` instance.
        
        """
        widget = Gtk.TreeView()
        widget.show_all()
        window.add_dock_item("File Browser", widget, self.icon_name, 
            Gtk.Orientation.VERTICAL)
        
    def deactivate(self):
        super(FileBrowserPlugin, self).deactivate()
    
    def on_window_added(self, application, window, data=None):
        #self.add_dock_item_to_window(window)
        pass



