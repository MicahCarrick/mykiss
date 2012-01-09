AC_INIT(
	[Mykiss], 
	[0.1],
	[https://github.com/MicahCarrick/mykiss/issues/new],
	[mykiss],
	[https://github.com/MicahCarrick/mykiss]
)
        
AC_CONFIG_SRCDIR([src/site-packages/mykiss/application.py])
AC_CONFIG_MACRO_DIR([m4])

AM_INIT_AUTOMAKE

dnl --- Check for required Python packages -------------------------------------

AM_PATH_PYTHON([2.5])

AX_PYTHON_MODULE([xdg], [PyXDG])
AX_PYTHON_MODULE([gi.repository], [PyGObject 3])
AX_PYTHON_MODULE([gi.repository.GObject], [GLib 2])
AX_PYTHON_MODULE([gi.repository.Pango], [Pango])
AX_PYTHON_MODULE([gi.repository.Gtk], [GTK+ 3])
AX_PYTHON_MODULE([gi.repository.Gdl], [GNOME Docking Library])
AX_PYTHON_MODULE([gi.repository.Peas], [Peas Plugin Engine])
AX_PYTHON_MODULE([gi.repository.GtkSource], [GtkSourceView 3])

dnl --- GSettings --------------------------------------------------------------

dnl GLIB_GSETTINGS requires glib headers
PKG_CHECK_MODULES([glib], [glib-2.0 >= 2.28])
GLIB_GSETTINGS

dnl --- Output files (at configure time) ---------------------------------------

AC_CONFIG_FILES([
	Makefile 
	data/Makefile
	data/mykiss.desktop
	data/icons/Makefile
	data/icons/hicolor/Makefile
	data/icons/hicolor/48x48/Makefile
	data/icons/hicolor/48x48/apps/Makefile
	data/icons/hicolor/scalable/Makefile
	data/icons/hicolor/scalable/apps/Makefile
	data/ui/Makefile
	src/Makefile 
	src/plugins/Makefile
	src/site-packages/Makefile
	src/site-packages/mykiss/Makefile
])

AC_OUTPUT


