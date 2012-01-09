from gi.repository import GObject
from gi.repository import Gtk
from mykiss.window import Window
from mykiss.plugin import WindowPlugin

class TerminalPlugin(WindowPlugin):
    __gtype_name__ = 'TerminalPlugin'
    window = GObject.property(type=Window)
    
    def do_activate(self):
        print("terminal.do_activate", repr(self.window))


    def do_deactivate(self):
        print("ExamplePlugin.do_activate", repr(self.window))

