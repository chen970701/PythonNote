import sys

from requests.sessions import session
import temp #import的时候 __name__ = temp
from PyQt5.QtWidgets import QApplication, QWidget,QToolTip,QLabel,QLineEdit,QPushButton,QCheckBox,QProgressBar,QComboBox,QTextEdit
from PyQt5.QtGui import QFont, QIcon, QPixmap
import requests

#a= requests.get("http://httpbin.org/get?name=green&age=24")
# pa={"name":"green","age":"25"}
# a=requests.get("http://httpbin.org/get",params=pa)
# a.encoding=a.apparent_encoding
# print(a.status_code)
# print(a.text) 

# d="hello green"
# p=requests.post("http://httpbin.org/post",data=d)
# print(p.status_code,p.text)

# form={"name":"green","age":"18"}
# p=requests.post("http://httpbin.org/post",data=form)
# print(p.status_code,p.text)

# f=open("temp.txt","r")
# f2=open("rocket.jpg","rb")
# fs={"file1":f}
# p=requests.post("http://httpbin.org/post",files=fs)
# print(p.status_code,p.text)
# f.close()
# f2.close()

# p=requests.get("http://httpbin.org/cookies/set/name/green")
# print(p.text)
# p2=requests.get("http://httpbin.org/cookies") #如果有会话则cookie会保留
# print(p2.text)
# for key,value in p.cookies:
#     print(key+"="+value)
# print(p.cookies)

s=requests.session()
p=s.get("http://httpbin.org/cookies/set/name/green")
print(p.text)
p2=s.get("http://httpbin.org/cookies") #如果有会话则cookie会保留
print(p2.text)