import os

from gi.repository import GLib
from gi.repository import Gtk
from gi.repository import Vte

from mykiss.plugin import MykissPlugin
from mykiss import icons

class TerminalPlugin(MykissPlugin):
    icon_name = "mykiss-terminal"
    
    def __init__(self):
        super(TerminalPlugin, self).__init__()
        # register icons
        icon_dir = os.path.join(os.path.dirname(__file__), "icons")
        icons.register_stock_icons(icon_dir, (self.icon_name,))
        
    def activate(self):
        super(TerminalPlugin, self).activate()

        # add terminal to existing windows
        for window in self.application.get_windows():
            window.add_widget("Terminal", self._create_widget(), self.icon_name, 
                              Gtk.Orientation.HORIZONTAL)
        
        # add terminal to any windows that get added
        self.connect(self.application, "window-added", self.on_window_added)
    
    def _create_widget(self):
        vte = Terminal()
        scrollbar = Gtk.Scrollbar.new(Gtk.Orientation.VERTICAL, 
            vte.get_vadjustment())
        box = Gtk.HBox(homogeneous=False, spacing=0)  
        box.pack_start(vte, True, True, 0)
        box.pack_start(scrollbar, False, False, 0)
        box.show_all()

        return box
        
    def deactivate(self):
        super(TerminalPlugin, self).deactivate()
        
        # remove terminal from existing windows
        for window in self.application.get_windows():
            window.remove_widget("Terminal")
    
    def on_window_added(self, application, window, data=None):
        window.add_widget("Terminal", self._create_widget(), self.icon_name, 
                           Gtk.Orientation.HORIZONTAL)

class Terminal(Vte.Terminal):
    __gtype_name__ = "MykissTerminal"
    def __init__(self):
        Vte.Terminal.__init__(self)
        self.set_size(self.get_column_count(), 5)
        self.set_size_request(200, 25)
        self.set_font_from_string("monospace 10")
        self.connect("child-exited", lambda x: self.run())
        self.run()
        
    def run(self):
        args = [os.environ["SHELL"]]
        self.fork_command_full(Vte.PtyFlags.DEFAULT, None, args, None,
                               GLib.SpawnFlags.SEARCH_PATH, None, None)

