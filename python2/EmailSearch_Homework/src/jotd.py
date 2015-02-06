import email
import settings
import datetime
import time
from database import login_info
import mysql.connector as msc
from email.utils import parsedate_tz, mktime_tz, parseaddr

SENDER = "Chalupa Batman"
SENDER_ADD = "chris@foobar.com"

def generate_message(recipient, rec_address, sender, send_address, date, text, msgid=None):
    """
    Takes arguments and creates an email object.
    """
    msg = email.message_from_string(text)
    msg["Date"] = date.strftime("%a, %d %b %Y %H:%M:%S")
    msg["From"] = '<a href="mailto:{0}">{1}</a>'.format(send_address, sender)
    msg["To"] = '<a href="mailto:{0}">{1}</a>'.format(rec_address, recipient)
    if msgid != None:
        msg["Message-Id"] = msgid
    else:
        msg["Message-Id"] = email.utils.make_msgid()
    return msg

def get_date_list(date, daycount):
    dates = []
    for d in range(0, daycount):
        date += datetime.timedelta(days=1)
        dates.append(date)
    return dates

def generate_messages(recipients, starttime, daycount):
    """
    Creates a list of email message objects for each recipient
    and each day in DAYCOUNT. Messages are dated from STARTTIME.
    """
    messages = []
    dates = get_date_list(starttime, daycount)
    for d in dates:
        for rn, re in recipients:
            msg = generate_message(rn, re, SENDER, SENDER_ADD, d, "spam and eggs")
            messages.append(msg)
    return messages
         
def store(messages):
    """
    Stores a given list of email messages, if necessary, returning its primary id.
    """
    conn = msc.Connect(**login_info)
    curs = conn.cursor()
    for msg in messages:
        message_id = msg['message-id']
        curs.execute("SELECT msgID FROM message WHERE msgMessageID=%s", (message_id, ))
        result = curs.fetchall()
        if result:
            return result[0][0]
        date = msg['date']
        sender, sender_add = parseaddr(msg['from'])
        recipient, recipient_add = parseaddr(msg['to'])
        dt = datetime.datetime.fromtimestamp(mktime_tz(parsedate_tz(date)))
        text = msg.as_string()
        curs.execute("""INSERT INTO message 
                      (msgMessageID, msgDate, msgRecipientName, msgRecipientAddress, msgSenderName, msgSenderAddress, msgText)
                       VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                       (message_id, dt, recipient, recipient_add, sender, sender_add, text))
        conn.commit()
        curs.execute("SELECT msgID FROM message WHERE msgMessageID=%s", (message_id, ))
        result = curs.fetchall()
    conn.close()
    return result

start = time.time()
store(generate_messages(settings.RECIPIENTS, settings.STARTTIME, settings.DAYCOUNT))
end = time.time()
interval = end - start
print("Time to complete was " + str(interval) + " for " + str(settings.DAYCOUNT) + " days")   
    
