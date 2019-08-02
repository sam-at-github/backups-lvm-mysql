#!/usr/bin/env python3
'''
This is a simple script to do the following atomically with some error handling:

  1. FLUSH TABLES WITH READ LOCK
  2. Take an LVM snapshot of given volume.
  3. UNLOCK TABLES

After running this you can take a backup of the MySQL db (and anything else) off the snapshot.
'''
import os
import argparse
from subprocess import run, CalledProcessError
from MySQLdb import connect, OperationalError, ProgrammingError


def main():
  parser = argparse.ArgumentParser(description='Atomically flush MySQL db, take an LVM snapshot, unlock MySQL tables')
  parser.add_argument('-H', dest='host', type=str, required=True)
  parser.add_argument('-u', dest='user', type=str, required=True)
  parser.add_argument('-p', dest='passwd', type=str, required=True)
  parser.add_argument('-v', dest='volume', type=str, required=True)
  parser.add_argument('-n', dest='snapshot_name', type=str, required=True)
  args = parser.parse_args()
  print(args)

  cleanup_lvm('{volume_dir}/{snapshot_name}'.format(volume_dir=os.path.dirname(args.volume), snapshot_name=args.snapshot_name))
  try:
    cursor = connect(host=args.host, user=args.user, passwd=args.passwd).cursor()
    cursor.execute('FLUSH TABLES WITH READ LOCK');
    run(['lvcreate', '-l90%FREE', '--snapshot', '--name', args.snapshot_name, args.volume], check=True)
    cursor.execute('UNLOCK TABLES')
    cursor.close()
  except OperationalError as e:
    exit('Could not to connect to MySQL DB [%s]' % (e,))
  except ProgrammingError as e:
    exit('MySQL error [%s]' % (e,))
  except Exception as e:
    exit('Failed creating LVM snapshot [%s]' % (e,))


def cleanup_lvm(snapshot_path):
  ''' Remove the snapshot if exists. It shouldn't exist. If it does we should probably just bork and
  tell use to deal with it. Note the table lock will be released as session dies if script fails.
  '''
  if os.path.exists(snapshot_path):
    print('Warning: snapshot exists! Attempting to remove it')
    subprocess.run('lvremove {snapshot_path} --force'.format(snapshot_path=snapshot_path), check=True);


if __name__ == '__main__':
  main()
