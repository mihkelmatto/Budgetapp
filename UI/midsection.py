from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QScrollArea, QProgressBar
from PyQt5.QtCore import Qt

from UI.widgets import widgets_cardbase

def midsectionUI(self) -> QScrollArea:
    # create a scrollable area and its content widget
    scrollarea = QScrollArea(self)
    scrollarea.setWidgetResizable(True)

    midsection = QWidget()
    layout = QVBoxLayout(midsection)
    layout.setSpacing(12)

    # add items to the scrollable area
    for counter in range(6):
        content_placeholder = expenses()
        layout.addWidget(widgets_cardbase("taun.gif", content_placeholder))

    # set the content widget inside the scroll area
    scrollarea.setWidget(midsection)
    return scrollarea

def expenses() -> QWidget:
    def create_progressbar(current, max) -> QProgressBar:
        progressbar = QProgressBar()
        progressbar.setMaximum(max)
        progressbar.setValue(current)
        progressbar.setFormat(f"{current} / {max} €")
        progressbar.setAlignment(Qt.AlignCenter)

        return progressbar

    expenseswidget = QWidget()
    layout = QVBoxLayout(expenseswidget)

    title = QLabel("Toit")
    subtitle = QLabel("Jooksvad kulud")
    progressbar = create_progressbar(40, 100)
    remaininglabel = QLabel("jääk: 60€")
    account = QLabel("SWED")

    for item in (title, subtitle, progressbar, remaininglabel, account):
        layout.addWidget(item)

    expenseswidget.setObjectName("expenseswidget")
    title.setObjectName("title")
    subtitle.setObjectName("text")
    remaininglabel.setObjectName("text")
    account.setObjectName("text")

    return expenseswidget



def income(self) -> QWidget:
    pass

def accounts(self) -> QWidget:
    pass

def statisticsUI(self) -> QWidget:
    pass