#!/bin/bash -e
cd `dirname $0`
. backups-lvm-mysql.conf
REQUIRE_EXISTS=(VOLUME MYSQLDATADIR)
REQUIRE_SET=(BACKUPROOT VOLUME LVMMOUNT MYSQLDATADIR SNAPSHOTNAME BACKUPLOCKFILE MYUSER MYPASS)

err=0
for v in ${REQUIRE_SET[*]}; do
  [[ -z ${!v} ]] && echo "Required var $v is not set" && err=1
done
for v in ${REQUIRE_EXISTS[*]}; do
  [[ ! -e ${!v} ]] && echo "Required file $v=${!v} does not exist" && err=1
done
[[ $err -gt 0 ]]  && exit 1
return 0
