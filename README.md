# Overview
A simple wrapper script to do a MySQL flush, lock, LVM snapshot, unlock, then backup of a MySQL database.
Good alternative to say `mysqldump`. See http://www.lullabot.com/blog/article/mysql-backups-using-lvm-snapshots.

# Installation
The trivial script `install.sh` copies ~everything from the source directory to /etc/backups-lvm-mysql/
and installs a crontab. You'll want to change the configuration options. Main conf is `backups-conf`.
May also want to change cron times - or just not use the cron at all. If deps are met everything will work.

# Usage

    /etc/backups-lvm-mysql/backups.sh

# Dependencies

 * cron
 * lvm
 * php5

# Notes
This setup simply keeps one local snapshot. A remote backup that syncs and rotates that snapshot is a good idea.
