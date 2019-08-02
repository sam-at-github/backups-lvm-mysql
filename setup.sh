#!/bin/bash -e
cd `dirname $0`
. backups-lvm-mysql.conf
[[ -d "${BACKUPROOT}" ]] || mkdir -p "${BACKUPROOT}"
[[ -d "${LVMMOUNT}" ]] || mkdir "${LVMMOUNT}"
chown -R root:root /etc/backups-lvm-mysql
