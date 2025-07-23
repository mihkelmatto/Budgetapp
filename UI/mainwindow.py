from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout

from utils.filepath import root_directory

from UI.header import headerUI
from UI.midsection import expensesUI, incomeUI, accountsUI, statisticsUI
from UI.footer import footerUI


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1000, 600)
        self.setWindowTitle("Budget app")
        self.setWindowIcon(QIcon(root_directory("Resources", "Icons", "windowicon.png")))
        self.initUI()

    # Create main layout of the app
    def initUI(self):
        widget = QWidget()
        self.setCentralWidget(widget)
        layout = QVBoxLayout()

        widget.setContentsMargins(0, 0, 0, 0)
        layout.setContentsMargins(0, 0, 0, 0)

        # define variables, objects
        header: QWidget = headerUI(self)
        midsection: QWidget = expensesUI(self)
        footer: QWidget = footerUI(self)

        # add to layout, layout settings
        layout.addWidget(header, stretch=0)
        layout.addWidget(midsection, stretch=1)
        layout.addWidget(footer, stretch=0)

        # layout > widget, set stylesheets
        widget.setLayout(layout)
        self.set_stylesheets()

    def set_stylesheets(self) -> None:
        self.setStyleSheet("""
            /* "Global" settings */
            QMainWindow, QPushButton, QLabel{
                background-color: hsl(0, 0%, 15%);
                font-family: Bahnschrift, Arial;
                color: hsl(34, 98%, 40%);
            }            

            /* top settings */     
            #header, #header QLabel, #header QPushButton{
            background-color: hsl(0, 0%, 12%);
            }            
            #header #main_title, #header QPushButton{
                font-size: 40px;
                padding-left: 5px;
                font-weight: bold;
            }

            /* mid settings */

            /* bot settings */
            #footer, #footer QLabel, #footer QPushButton{
            background-color: hsl(0, 0%, 12%);
            }
            #footer QPushButton{
                font-size: 30px;
            }
                """)