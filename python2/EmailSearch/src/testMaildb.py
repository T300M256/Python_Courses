"""
Read in and parse email message to verify readability.

NOTE: This test creates the message table, dropping any
previous version and should leave it empty. DANGER: this
test will delete any existing message table.
"""

from glob import glob
from email import message_from_string
import mysql.connector as msc
from database import login_info
import maildb
import unittest
import datetime
from email.utils import parsedate_tz, mktime_tz

conn = msc.Connect(**login_info)
curs = conn.cursor()

TBLDEF = """\
CREATE TABLE message (
     msgID INTEGER AUTO_INCREMENT PRIMARY KEY,
     msgMessageID VARCHAR(128),
     msgDate DATETIME,
     msgSenderName VARCHAR(128),
     msgSenderAddress VARCHAR(128),
     msgText LONGTEXT
)"""
FILESPEC = "C:/PythonData/*.eml"

class testRealEmail_traffic(unittest.TestCase):
    def setUp(self):
        """
        Reads an arbitrary number of mail message and
        stores them in a brand new message table.
        
        DANGER: Any exisitng message table WILL be lost.
        """
        curs.execute("DROP TABLE IF EXISTS message")
        conn.commit()
        curs.execute(TBLDEF)
        conn.commit()
        files = glob(FILESPEC)
        self.msgids = {}
        self.message_ids = {}
        self.msgdates = []
        self.rowcount = 0
        for f in files:
            ff = open(f)
            text = ff.read()
            msg = message_from_string(text)
            id = self.msgids[msg['message-id']] = maildb.store(msg)
            self.message_ids[id] = msg['message-id']
            date = msg['date']
            self.msgdates.append(datetime.datetime.fromtimestamp(mktime_tz(parsedate_tz(date))))
            self.rowcount += 1 # assuming no duplicated Message-IDs
            ff.close()
            
    def test_not_empty(self):
        """
        Verify that the setUp method actually created some messages.
        If it finds no files there will be no messages in the table,
        the loop bodies in the other tests will never run, and potential
        errors will never be discovered.
        """
        curs.execute("SELECT COUNT(*) FROM message")
        messagect = curs.fetchone()[0]
        self.assertGreater(messagect, 0, "Database message tabel is empty")
        
    def test_message_ids(self):
        """
        verify that items retrieved by id have the correct Message-ID
        """
        for message_id in self.msgids.keys():
            pk, msg = maildb.msg_by_id(self.msgids[message_id])
            self.assertEqual(msg['message-id'], message_id)
            
    def test_ids(self):
        """
        Verfiy that items retrieved by message_id have the correct Message-iD.
        """
        for i in self.message_ids.keys():
            pk, msg = maildb.msg_by_message_id(self.message_ids[i])
            self.assertEqual(msg['message-id'], self.message_ids[i])
            
    def test_dates(self):
        """
        Verify that retrieveing records between the mini and max dates
        returns an appropriate number of records.
        """
        mind = min(self.msgdates)
        mindate = datetime.date(mind.year, mind.month, mind.day)
        maxd = max(self.msgdates)
        maxdate = datetime.date(maxd.year, maxd.month, maxd.day)
        self.assertEqual(self.rowcount, len(maildb.msgs(mindate=mindate, maxdate=maxdate)))
            
if __name__ == "__main__":
    unittest.main()