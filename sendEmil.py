# coding: utf-8
import markdown
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from settings import *
import os, sys,re
from email.mime.image import MIMEImage


# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)
# 构造附件
att = MIMEText(open('h:\\python\\1.jpg', 'rb').read(), 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="1.jpg"'
msg.attach(att)

smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()

def LoginEmil():
    try:
        smtp = smtplib.SMTP()
        smtp.connect('smtp.163.com')
        smtp.login(USERNAME,PASSWORD)
        return smtp
    except Exception as E:
        print E
        sys.exit(1)

def markdown_fromstring(value):  # 表格的支持需要完善
    return markdown.markdown(value,
                             extensions=[
                                 # 'markdown.extensions.tables',
                                 #  'pymdownx.github',
                                 'pymdownx.pymdown',
                                 # 'pymdownx.github',
                                 'pymdownx.extra',
                                 # 'pymdownx.tasklist',
                                 # 'pymdownx.githubemoji',
                                 # 'pymdownx.critic',
                                 # 'pymdownx.inlinehilite',

                                 # 'markdown.extensions.codehilite',
                                 # 'markdown.extensions.footnotes',
                             ],
                             safe_mode=True, enable_attributes=False)
def get_file():
    def new_file(path):
        files = {'file_path':'','ctime':0}
        for dirpath, dirnames, filenames in os.walk('c:\\winnt'):
            file_path = os.path.join(dirpath, filenames)
            if os.path.isfile(path)==False:
                continue
            file_ctime = os.stat(file_path).st_ctime
            if files['ctime']<=file_ctime:
                filenames['file_path'] = file_path
                filenames['ctime']=file_ctime
        return files

    try:
        if os.path.isfile(PATH):
            new_file = PATH
        else:
            new_file = new_file(PATH)['file_path']
    except Exception as E:
        print E
        sys.exit(1)
    return new_file

def Change_html(html):
    res = 'src="(*.?)"'

    for index,src in xrange(re.findall(res,html)):
        imgs_name = 'imgs'

    pass
def sendString():
    strings = open(get_file()).read()
    html = markdown_fromstring(strings)

def sendEmil():
    pass
