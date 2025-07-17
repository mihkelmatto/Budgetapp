from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout

from .header import headerUI
from .midsection import expensesUI, incomeUI, accountsUI, statisticsUI
from .footer import footerUI


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1000, 600)
        self.initUI()

    # Create main layout of the app
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setContentsMargins(0, 0, 0, 0)
        central_layout = QVBoxLayout()
        central_layout.setContentsMargins(0, 0, 0, 0)

        # define variables, objects
        header: QWidget = headerUI(self)
        midsection: QWidget = expensesUI(self)
        footer: QWidget = footerUI(self)

        # add to layout, layout settings
        central_layout.addWidget(header, stretch=0)
        central_layout.addWidget(midsection, stretch=1)
        central_layout.addWidget(footer, stretch=0)

        # layout > widget, set stylesheets
        central_widget.setLayout(central_layout)
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