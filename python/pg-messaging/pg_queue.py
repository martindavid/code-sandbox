import select
import psycopg2
import psycopg2.extensions
from psycopg2.extensions import QuotedString
import json
import time


class PgQueue:
    dbuser = None
    dbpass = None
    dbname = None

    conn = None
    curs = None
    channel = None

    continue_recv = True

    def __init__(self, channel, dbname=None, dbuser=None, dbpass=None):
        """
        Connect to the database.
        If one of dbname, dbuser or dbpassword are not provided,
        the responsibility of providing (and setting a connection on
        this object) will fall on the calling code. 

        Otherwise, this will create a connection to the database.
        """
        self.dbname = dbname
        self.dbuser = dbuser
        self.dbpass = dbpass
        self.channel = channel

        if not channel:
            raise Exception("No channel provided")

        self.conn = psycopg2.connect(
            f'dbname={dbname} user={dbuser} password={dbpass} host=localhost')
        self.conn.set_isolation_level(
            psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    def recvLoop(self):
        """
        Loop that's concerned with receiving notifications
        """
        print(self.conn)
        self.curs = self.conn.cursor()
        self.curs.execute("LISTEN {0};".format(self.channel))

        while self.continue_recv:
            if select.select([self.conn], [], [], 60) == ([], [], []):
                print("consumer: timeout")
            else:
                self.conn.poll()
                print("consumer: received messages")
                while self.conn.notifies:
                    notif = self.conn.notifies.pop(0)
                    # print "Got NOTIFY:", notif.pid, notif.channel, notif.payload
                    self.recvCallback(notif)

    def recvCallback(self, notification):
        """
        Needs to be implemented with notification handling logic
        """
        pass

    def send(self, data):
        """
        Send a notification
        """
        curs = self.conn.cursor()

        message = {}
        print("producer: sending..")
        # equip the message object with a timestamp
        message['time'] = time.time()
        message['data'] = data
        messageJson = json.dumps(message)
        # messagePg = QuotedString(messageJson).getquoted()
        print("JSON String", str(messageJson))
        query = f"NOTIFY {self.channel}, '{messageJson}';"
        print(query)
        curs.execute(query)
