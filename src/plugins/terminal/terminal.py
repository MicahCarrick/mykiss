import os

from gi.repository import GLib
from gi.repository import Gtk
from gi.repository import Vte

from mykiss.plugin import MykissPlugin
from mykiss import icons

STOCK_TERMINAL = "mykiss-terminal"

class TerminalPlugin(MykissPlugin):

    def __init__(self):
        super(TerminalPlugin, self).__init__()
        
    def activate(self):
        super(TerminalPlugin, self).activate()
        
        # register icons
        icon_dir = os.path.join(os.path.dirname(__file__), "icons")
        icons.register_stock_icons(icon_dir, (STOCK_TERMINAL,))
        
        # add terminal to existing windows
        for window in self.application.get_windows():
            self.add_dock_item_to_window(window)
        
        # add terminal to any windows that get added
        self.connect(self.application, "window-added", self.on_window_added)
    
    def add_dock_item_to_window(self, window):
        """
        Install a new terminal dock item in the window.
        
        Args:
            window -- A `mykiss.window.Window()` instance.
        
        """
        vte = Terminal()
        
        #self._vte.connect("child-exited", self.on_child_exited)
        scrollbar = Gtk.Scrollbar.new(Gtk.Orientation.VERTICAL, 
            vte.get_vadjustment())
        box = Gtk.HBox(homogeneous=False, spacing=0)  
        box.pack_start(vte, True, True, 0)
        box.pack_start(scrollbar, False, False, 0)
        box.show_all()
        window.add_dock_item("Terminal", box, STOCK_TERMINAL, 
            Gtk.Orientation.HORIZONTAL)
        
    def deactivate(self):
        super(TerminalPlugin, self).deactivate()
    
    def on_window_added(self, application, window, data=None):
        self.add_dock_item_to_window(window)

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

