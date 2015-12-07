SUBDIRS = btc_channel

bin_SCRIPTS = btc-channel
CLEANFILES = $(bin_SCRIPTS)
EXTRA_DIST = btc-channel.in

do_substitution = sed -e 's,[@]pythondir[@],$(pythondir),g' \
	-e 's,[@]PACKAGE[@],$(PACKAGE),g' \
	-e 's,[@]VERSION[@],$(VERSION),g' 

btc-channel: btc-channel.in Makefile
	$(do_substitution) < $(srcdir)/btc-channel.in > btc-channel
	chmod +x btc-channel