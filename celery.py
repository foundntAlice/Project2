import os

try:
    import MySQLdb
except ImportError:
    import install_pymysql

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'algo_lib.settings')

from algo_lib.celery import app
