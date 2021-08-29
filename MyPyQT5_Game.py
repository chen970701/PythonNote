import sys
import temp #import的时候 __name__ = temp
from PyQt5.QtWidgets import QApplication, QWidget,QToolTip,QLabel,QLineEdit,QPushButton,QCheckBox,QProgressBar,QComboBox,QTextEdit
from PyQt5.QtGui import QFont, QIcon, QPixmap
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.waiguaName=""
        self.move(300,200)
        self.resize(600,500)
        #self.setGeometry(300,200,500,800) 
        self.setWindowTitle("测试程序")
        self.setWindowIcon(QIcon("rocket.jpg"))

        self.ms=QLabel("消息提示框",self)
        self.ms.move(0,160)
        self.ms.resize(500,100)
        ff=QFont()
        ff.setPointSize(20)
        self.ms.setFont(ff)
           
        self.cb=QCheckBox("是否开挂",self)
        # self.cb.setChecked(True)
        self.cb.stateChanged.connect(self.checkBoxChange)
        btn1=QPushButton("检测是否开挂",self)
        btn1.move(0,100)
        btn1.clicked.connect(self.CheckCheat)

        self.cbb=QComboBox(self)
        self.cbb.addItems(["透视","锁血","隐身"])
        self.cbb.move(100,0)
        self.cbb.activated[str].connect(self.changeSelect)
        self.waiguaName=self.cbb.currentText()

        self.te=QTextEdit(self)
        self.te.setPlaceholderText("输入举报内容")
        self.te.resize(200,200)
        self.te.move(0,300)
        self.te.textChanged.connect(self.editText)

        self.sub=QPushButton("提交举报",self)
        self.sub.move(220,300)
        self.sub.clicked.connect(self.submit)
        
        

        self.show()
    def checkBoxChange(self):
        if(self.cb.isChecked()):
            self.ms.setText("我开挂了"+self.waiguaName)
        else:
            self.ms.setText("我没有开挂")
    def CheckCheat(self):
        print(self.sender().text())
        if(self.cb.isChecked()):
            self.ms.setText("他开了"+self.waiguaName+" 逮捕他")
        else:
            self.ms.setText("他没有开挂 放过他")
    def timerEvent(self, e):
        print(11)
    def changeSelect(self,text):
        self.waiguaName=text
    def editText(self):
        self.ms.setText("编辑中")
    def submit(self):
        print("举报内容："+self.te.toPlainText())


if __name__=="__main__":
    print(__name__)
    app=QApplication(sys.argv)
    ex=Example()
    print(app.exec_())
    sys.exit(app.exec_())
print(__name__)
print(sys.argv)
print(sys.version)