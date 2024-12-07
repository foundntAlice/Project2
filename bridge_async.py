import os

import gevent.monkey

os.environ.setdefault('SETTINGS_MODULE', 'settings')
gevent.monkey.patch_all()

import install_pymysql

import django
django.setup()

from judge.bridge.daemon import judge_daemon

if __name__ == '__main__':
    judge_daemon()
