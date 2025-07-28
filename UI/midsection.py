from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QScrollArea

from UI.widgets import widgets_cardbase


def expensesUI(self) -> QScrollArea:
    # create a scrollable area and its content widget
    scrollarea = QScrollArea(self)
    scrollarea.setWidgetResizable(True)

    expenseswidget = QWidget()
    layout = QVBoxLayout(expenseswidget)

    # add items to the scrollable area
    for counter in range(6):
        content_placeholder = QLabel("content")
        layout.addWidget(widgets_cardbase("taun.gif", content_placeholder))

    # set the content widget inside the scroll area
    scrollarea.setWidget(expenseswidget)
    return scrollarea

def incomeUI(self) -> QWidget:
    pass

def accountsUI(self) -> QWidget:
    pass

def statisticsUI(self) -> QWidget:
    pass