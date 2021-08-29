import sys
import temp #import的时候 __name__ = temp
from PyQt5.QtWidgets import QApplication, QWidget,QToolTip,QLabel,QLineEdit,QPushButton
from PyQt5.QtGui import QIcon, QPixmap
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.move(300,200)
        self.resize(500,800)
        #self.setGeometry(300,200,500,800) 
        self.setWindowTitle("测试程序")
        self.setWindowIcon(QIcon("rocket.jpg"))
        self.setToolTip("Green的测试项目")
        img=QLabel(self)
        img.setPixmap(QPixmap("词云.jpg"))
        img.resize(100,100)
        img.setToolTip("词云")
        userLable=QLabel(self)
        userLable.setText("用户名")
        userLable.move(20,150)
        userEdit=QLineEdit(self)
        userEdit.setPlaceholderText("Green")
        userEdit.move(100,150)

        passWordLable=QLabel(self)
        passWordLable.setText("密码")
        passWordLable.move(20,200)
        passWordEdit=QLineEdit(self)
        passWordEdit.move(100,200)
        
        self.show()

if __name__=="__main__":
    print(__name__)
    app=QApplication(sys.argv)
    ex=Example()
    print(app.exec_())
    sys.exit(app.exec_())
print(__name__)
print(sys.argv)
print(sys.version)