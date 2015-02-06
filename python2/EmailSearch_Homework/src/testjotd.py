"""
Tests the jotd.py program.

NOTE: This test creates the message table, dropping any
previous version and should leave it empty. DANGER: this
test will delete any existing message table.
"""

import unittest
import mysql.connector as msc
from database import login_info
import jotd
import settings
import datetime

conn = msc.Connect(**login_info)
curs = conn.cursor()

TBLDEF = """\
CREATE TABLE message (
     msgID INTEGER AUTO_INCREMENT PRIMARY KEY,
     msgMessageID VARCHAR(128),
     msgDate DATETIME,
     msgRecipientName VARCHAR(128),
     msgRecipientAddress VARCHAR(128),
     msgSenderName VARCHAR(128),
     msgSenderAddress VARCHAR(128),
     msgText LONGTEXT
)"""

EMAIL_TXT = """Date: Tue, 01 Jun 2010 00:00:00
From: <a href="mailto:website@example.com">website@example.com</a>
To: <a href="mailto:foo@bar.com">foo@bar.com</a>
Message-Id: <NNNNNN>

This is a test message."""

class TestJokes(unittest.TestCase):
    
    def setUp(self):
        """
        Establishes resources for the tests (obvsiously) including
        creating a empty message table for populating.  
        
        DANGER: Any exisiting message table WILL be lost.
        """
        
        # resources for testing generate message
        self.ex_email_text = EMAIL_TXT # exemplar message text
        self.email_date = datetime.date(2010, 6, 1) # Tue, 01 Jun 2010 00:00:00 +0000
        self.recipient = "foo@bar.com"
        self.sender = "website@example.com"
        self.text = "This is a test message."
        self.msgid = "<NNNNNN>"
        
        # resources to testing that the correct dates for sending messages is generated
        self.ex_date_list = [datetime.date(2010,6,2), datetime.date(2010,6,3), datetime.date(2010,6,4)] # this is our exemplar list for start time self.email_date
        self.test_daycount = 3
        
        # set up test generating a list of messages
        self.test_rec = [("Gandalf Grey", "foo@me.net"),
                         ("Bilbo Baggins", "bilbo@me.net"),
                        ]
        self.ex_num_gen_messages = len(self.test_rec)*self.test_daycount
        # need the database set up
        curs.execute("DROP TABLE IF EXISTS message")
        conn.commit()
        curs.execute(TBLDEF)
        conn.commit()
        self.ex_num_stored_messages = len(settings.RECIPIENTS)*settings.DAYCOUNT
        
    def test_generate_message(self):
        """
        Verify that jotd generates a message with the expected text format.
        """
        obs_email = jotd.generate_message(self.recipient, self.recipient,self.sender,self.sender, self.email_date, self.text, msgid=self.msgid)
        self.assertEqual(self.ex_email_text, obs_email.as_string())
    
    def test_date_list(self):
        """
        Verify that the list of dates for sending messages is correct.
        """
        obs_dates = jotd.get_date_list(self.email_date, self.test_daycount)
        self.assertEqual(self.ex_date_list, obs_dates)
        
    def test_generate_message_list(self):
        """
        Verifies that generate messages function produces the expected number of emails for the given starttime and daycount
        """
        messages = jotd.generate_messages(self.test_rec, self.email_date, self.test_daycount)
        self.assertEqual(self.ex_num_gen_messages, len(messages))
    
    def test_number_messages(self):
        """
        Verify that the expected number of messages are entered into
        the database table.
        """
        jotd.store(jotd.generate_messages(settings.RECIPIENTS, settings.STARTTIME, settings.DAYCOUNT))
        curs.execute("SELECT COUNT(*) FROM message")
        results = curs.fetchall()
        self.assertEqual(self.ex_num_stored_messages, results[0][0], "Number of messages in db not equal to number of recipients times number of days")


if __name__ == "__main__":
    unittest.main()
    conn.close()