SUBDIRS = site-packages plugins

bin_SCRIPTS = mykiss
CLEANFILES = $(bin_SCRIPTS)
EXTRA_DIST = mykiss.in

do_substitution = sed -e 's,[@]pythondir[@],$(pythondir),g' \
	-e 's,[@]pkgdatadir[@],$(pkgdatadir),g' \
	-e 's,[@]PACKAGE[@],$(PACKAGE),g' \
	-e 's,[@]PACKAGE_NAME[@],$(PACKAGE_NAME),g' \
	-e 's,[@]VERSION[@],$(VERSION),g' 

mykiss: mykiss.in Makefile
	$(do_substitution) < $(srcdir)/mykiss.in > mykiss
	chmod +x mykiss
