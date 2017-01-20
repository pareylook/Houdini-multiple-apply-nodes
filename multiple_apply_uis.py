from PySide import QtCore, QtGui
import hou, random

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(256, 71)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ln_name = QtGui.QLineEdit(Form)
        self.ln_name.setObjectName("ln_name")
        self.horizontalLayout_2.addWidget(self.ln_name)
        self.btn_go = QtGui.QPushButton(Form)
        self.btn_go.setObjectName("btn_go")
        self.horizontalLayout_2.addWidget(self.btn_go)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chbox_colorize = QtGui.QCheckBox(Form)
        self.chbox_colorize.setObjectName("chbox_colorize")
        self.horizontalLayout.addWidget(self.chbox_colorize)
        self.chbox_apply = QtGui.QCheckBox(Form)
        self.chbox_apply.setObjectName("chbox_apply")
        self.horizontalLayout.addWidget(self.chbox_apply)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Multiple Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_go.setText(QtGui.QApplication.translate("Form", "Enter", None, QtGui.QApplication.UnicodeUTF8))
        self.chbox_colorize.setText(QtGui.QApplication.translate("Form", "Colorize", None, QtGui.QApplication.UnicodeUTF8))
        self.chbox_apply.setText(QtGui.QApplication.translate("Form", "Apply", None, QtGui.QApplication.UnicodeUTF8))



class exampleWindow(QtGui.QWidget, Ui_Form):
    def __init__(self):
        super(exampleWindow, self).__init__()
        self.setupUi(self)
        self.btn_go.clicked.connect(self.multiple_apply)
        self.update_ui()

    def update_ui(self):
        self.chbox_apply.setChecked(True) 



    def multiple_apply (self):
        nodes = hou.selectedNodes()
        text = self.ln_name.text()

        for n in nodes:
            new = "none"
            color = (random.random(), random.random(), random.random())
            clr = hou.Color(color)
            if self.chbox_apply.isChecked() == True:
                new = n.createOutputNode(text, str(n))
            if self.chbox_colorize.isChecked() == True:
                if new != "none":
                    new.setColor(clr)
                else:
                    n.setColor(clr)
            
 


w = exampleWindow()
w.show()
