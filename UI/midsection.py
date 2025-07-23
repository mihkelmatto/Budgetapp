from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout

from UI.widgets import widgets_cardbase


def expensesUI(self) -> QWidget:
    expenseswidget = QWidget()
    layout = QVBoxLayout()

    for counter in range(3):
        content_placeholder = QLabel("content")
        layout.addWidget(widgets_cardbase("taun.gif", content_placeholder))

    expenseswidget.setLayout(layout)
    return expenseswidget

def incomeUI(self) -> QWidget:
    pass

def accountsUI(self) -> QWidget:
    pass

def statisticsUI(self) -> QWidget:
    pass