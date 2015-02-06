import email
import os
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def generateMessage(address, content, attachments=None):
    msg = email.message_from_string(content)
    msg['To'] = address
    if attachments != None:
        msg = MIMEMultipart()
        for f in attachments:
            typ = mimetypes.guess_type(f)[0]
            if typ == "text/plain" or typ == "text/html":
                t = ""
                if typ == "text/plain":
                    t = "plain"
                elif typ == "text/html":
                    t = "html"
                with open(f, "r") as fh:
                    new_msg = MIMEText(fh.read(), t)
            elif typ == "image/png":
                with open(f, "rb") as fh:
                    new_msg = MIMEImage(fh.read())
            else:
                with open(f, "rb") as fh:
                    new_msg = MIMEApplication(fh.read())
            new_msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(f))
            msg.attach(new_msg)
    return msg
