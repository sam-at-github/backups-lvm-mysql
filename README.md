# Overview
A simple wrapper script to get a MySQL backup from an LVM snapshot. The script `./backups-lvm-mysql.sh` does the following:

  1. MySQL flush and lock tables
  2. Take LVM snapshot
  3. MySQL unlock tables
  4. cp snapped MySQL database files to some configured location
  5. Remove LVM snapshot

A good alternative to say `mysqldump` if your using LVM. See http://www.lullabot.com/blog/article/mysql-backups-using-lvm-snapshots.

# Installation
Given a valid config you can run from CWD. Optionally you can exec the Makefile which ~just dumps everything in `/etc/backups-lvm-mysql/`.

    sudo make install

# Usage

    ./backups-lvm-mysql.sh

# Dependencies
lvm, python3, bash.
