import os
import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from UI import nukePipeline_UI


class NukePipelineTool(nukePipeline_UI.Ui_Form, QMainWindow):
    def __init__(self):
        super(NukePipelineTool, self).__init__()
        self.setupUi(self)


def main():
    main.nuke_tool = NukePipelineTool()
    main.nuke_tool.show()


if __name__ == '__main__':
    app = QApplication()
    tool = NukePipelineTool()
    tool.show()
    sys.exit(app.exec_())
