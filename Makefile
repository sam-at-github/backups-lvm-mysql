# Simple makefile. All the scripts just go CONFDIR. No macros necessary.

DESTDIR=/
CONFDIR=/etc/backups-lvm-mysql/
.EXPORT_ALL_VARIABLES:

all:
	# ...

clean:

install:
	mkdir -p $(DESTDIR)/$(CONFDIR)
	cp -a backups-lvm-mysql.conf check-config.sh backups-lvm-mysql.sh backups-post backups-pre mysql-flush-snap.py $(DESTDIR)/$(CONFDIR)/
	cp backups-lvm-mysql.cron /etc/cron.d/backups-lvm-mysql

uninstall:
	rm -rf $(DESTDIR)/etc/cron.d/backups-lvm-mysql
	rm -rf $(DESTDIR)/$(CONFDIR)
