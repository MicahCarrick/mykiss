from gi.repository import GObject, Gtk, GdkPixbuf
from mykiss.plugin import MykissPlugin

class DocumentListPlugin(MykissPlugin):
    icon_name = Gtk.STOCK_FILE
    widget_name = "mykiss.plugins.documentlist"
    def activate(self):
        """ Plugin was activated by the user or at startup. """
        super(DocumentListPlugin, self).activate()

        # add widget to existing windows
        print self.application
        for window in self.application.get_windows():
            self._on_window_added(self.application, window)
        
        # add widget to any windows that get added
        self.connect(self.application, "window-added", self._on_window_added)
    
    def _create_widget(self, window):
        """ Return a new instance of the dock widget. """
        self._list = DocumentList(window.get_documents())
        sw = Gtk.ScrolledWindow()
        sw.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        sw.set_shadow_type(Gtk.ShadowType.ETCHED_IN)
        sw.add(self._list)
        sw.show_all()

        return sw
        
    def deactivate(self):
        """ Plugin was de-activated by the user. """
        super(DocumentListPlugin, self).deactivate()
        
        # remove widget from existing windows
        for window in self.application.get_windows():
            window.remove_widget(self.widget_name)
    
    def _on_window_added(self, application, window, data=None):
        """ A new application window has been created. """
        window.add_widget(self.widget_name, "Documents", 
                           self._create_widget(window), self.icon_name, 
                           Gtk.Orientation.VERTICAL)
        self.connect(window.get_editor(), "document-added", 
                     self._on_document_added_or_removed, window)
        self.connect(window.get_editor(), "document-removed", 
                     self._on_document_added_or_removed, window)
    
    def _on_document_added_or_removed(self, editor, document, window):
        self._list.populate(window.get_documents())
        

class DocumentList(Gtk.TreeView):
    """
    A Gtk.TreeView displaying a list of documents.
    """
    def __init__(self, documents=None):
        self._store = Gtk.ListStore(GdkPixbuf.Pixbuf,       # icon
                                    GObject.TYPE_STRING,    # name            
                                    object)                 # document
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
            # TODO: get pixbuf from document.get_icon_pixbuf()
            pixbuf = self.render_icon_pixbuf(Gtk.STOCK_FILE, Gtk.IconSize.MENU)
            self._store.append((pixbuf, document.name, document))

    
        
