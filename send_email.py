'''
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 2/29/16
'''

import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import email.encoders as encoders
# >Need to install dnspython package.
import dns.resolver


def send_mail(mail_from, mail_to, subject, msg_txt, files=None):
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = mail_from
    msg['To'] = mail_to

    # Create the body of the message (a plain-text and an HTML version).
    html = msg_txt

    # Record the MIME types of both parts - text/plain and text/html.
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part2)

    # attachment
    if files:
        for f in files:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(open(f, 'rb').read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
            msg.attach(part)

    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    mailto_list = mail_to.strip().split(",")
    # if len(mailto_list) > 1:
    for mailtoi in mailto_list:
        domain_name = mailtoi[mailtoi.find('@')+1:]
        answers = dns.resolver.query(domain_name, 'MX')
        s = smtplib.SMTP(str(answers[0].exchange), 25)
        s.sendmail(mail_from, mailtoi.strip(), msg.as_string())
        s.quit()
    # else:
    #     s.sendmail(mail_from, mail_to, msg.as_string())

    return True


if __name__ == "__main__":
    send_mail('fromSomeOne@TESTING.com', 'cuyu@splunk.com', 'Test send_email.py', 'Hello World!')
    # send_mail('GuessMe', 'icyarm@qq.com,cuyu@splunk.com', 'Test send_email.py', 'Hello World!')
