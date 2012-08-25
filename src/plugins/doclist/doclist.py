from gi.repository import GObject, Gtk, GdkPixbuf
from mykiss.plugin import MykissPlugin

class DocumentListPlugin(MykissPlugin):
    icon_name = Gtk.STOCK_FILE
    widget_name = "mykiss.plugins.documentlist"
    def activate(self):
        """ Plugin was activated by the user or at startup. """
        super(DocumentListPlugin, self).activate()

        # add widget to existing windows
        for window in self.application.get_windows():
            self._on_window_added(self.application, window)
        
        # add widget to any windows that get added
        self.connect(self.application, "window-added", self._on_window_added)
    
    def _create_widget(self, window):
        """ Return a new instance of the dock widget. """
        doclist = DocumentList(window.get_documents())
        sw = Gtk.ScrolledWindow()
        sw.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        sw.set_shadow_type(Gtk.ShadowType.ETCHED_IN)
        sw.add(doclist)
        sw.show_all()
        
        self.connect(window.get_editor(), "document-added", 
                     lambda *w: doclist.populate(window.get_documents()))
        self.connect(window.get_editor(), "document-removed", 
                     lambda *w: doclist.populate(window.get_documents()))
                          
        return sw
        
    def deactivate(self):
        """ Plugin was de-activated by the user. """
        super(DocumentListPlugin, self).deactivate()
        
        # remove widget from existing windows
        for window in self.application.get_windows():
            window.remove_widget(self.widget_name)
    
    def _on_window_added(self, application, window, data=None):
        """ A new application window has been created. """
        #print(window.application)
        window.add_widget(self.widget_name, "Documents", 
                           self._create_widget(window), self.icon_name, 
                           Gtk.Orientation.VERTICAL)
        

class DocumentList(Gtk.TreeView):
    """
    A Gtk.TreeView displaying a list of documents for a window.
    """
    def __init__(self, documents):
        self._pixbufs = {}
        self._store = Gtk.ListStore(GdkPixbuf.Pixbuf,       # icon
                                    GObject.TYPE_STRING,    # name            
                                    object)                 # document
        self._store.set_sort_column_id(1, Gtk.SortType.ASCENDING)
        Gtk.TreeView.__init__(self, self._store)

        self.set_headers_visible(False)          
        
        column = Gtk.TreeViewColumn("Document")
        cell = Gtk.CellRendererPixbuf()
        column.pack_start(cell, False)
        column.add_attribute(cell, 'pixbuf', 0)
        cell = Gtk.CellRendererText()
        column.pack_start(cell, True)
        column.add_attribute(cell, 'text', 1)
        self.append_column(column)
        
        if documents:
            self.populate(documents)        
    
    def populate(self, documents):
        self._store.clear()
        for document in documents:
            icon_name = document.get_icon_name()
            if not icon_name in self._pixbufs:
                icon_theme = Gtk.IconTheme.get_default()
                pixbuf = icon_theme.load_icon(icon_name, Gtk.IconSize.MENU, 0)
                self._pixbufs[icon_name] = pixbuf
            self._store.append((self._pixbufs[icon_name], document.name, document))

    
        
