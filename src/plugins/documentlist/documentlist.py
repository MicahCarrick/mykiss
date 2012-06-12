from gi.repository import Gtk
from mykiss.plugin import MykissPlugin

class DocumentListPlugin(MykissPlugin):
    icon_name = Gtk.STOCK_FILE
    widget_name = "mykiss.plugins.documentlist"
        
    def activate(self):
        super(DocumentListPlugin, self).activate()

        # add widget to existing windows
        print self.application
        for window in self.application.get_windows():
            window.add_widget(self.widget_name, "Documents", 
                              self._create_widget(), self.icon_name, 
                              Gtk.Orientation.VERTICAL)
        
        # add widget to any windows that get added
        self.connect(self.application, "window-added", self.on_window_added)
    
    def _create_widget(self):
        """ Return a new instance of the dock widget packed in a box. """
        box = Gtk.VBox()  
        box.pack_start(Gtk.Label("Hello!"), True, True, 0)
        box.show_all()

        return box
        
    def deactivate(self):
        super(DocumentListPlugin, self).deactivate()
        
        # remove widget from existing windows
        for window in self.application.get_windows():
            window.remove_widget(self.widget_name)
    
    def on_window_added(self, application, window, data=None):
        
        window.add_widget(self.widget_name, "Documents", 
                           self._create_widget(), self.icon_name, 
                           Gtk.Orientation.VERTICAL)


