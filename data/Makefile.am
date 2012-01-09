SUBDIRS = icons ui

desktopdir = $(datadir)/applications
desktop_DATA = mykiss.desktop
UPDATE_DESKTOP = update-desktop-database $(datadir)/applications || :

gsettings_SCHEMAS = apps.mykiss.gschema.xml
@GSETTINGS_RULES@

EXTRA_DIST = \
	$(desktop_in_files) \
	apps.mykiss.gschema.xml

CLEANFILES = \
	$(desktop_DATA)	

DISTCLEANFILES = \
	$(desktop_DATA) 

install-data-hook: 
	$(UPDATE_DESKTOP)
uninstall-hook: 
	$(UPDATE_DESKTOP)
