from pg_queue import PgQueue
import time


DB_NAME = 'sandbox'
DB_USER = 'postgres'
DB_PASSWORD = ''
CHANNEL = 'test_channel'


if __name__ == '__main__':
    q = PgQueue(CHANNEL, dbname=DB_NAME, dbuser=DB_USER, dbpass=DB_PASSWORD)
    message = {}
    message['test'] = "value"
    q.send(message)