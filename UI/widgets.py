from PyQt5.QtWidgets import QLabel, QWidget, QHBoxLayout, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from utils.filepath import root_directory

def widgets_cardbase(icon_filename: str, content: QWidget) -> QWidget:
    # Creates a card with icon and settings button - empty content section

    def get_icon(filename: str, height: int) -> QLabel:
        filepath = root_directory("Resources", "Icons", filename)

        label = QLabel()
        pixmap = QPixmap(filepath)

        label.setFixedSize(height, height)
        label.setPixmap(pixmap)
        label.setScaledContents(True)

        return label

    def get_settingswidget(height: int) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout()

        button = QPushButton("⋮")
        button.setFixedSize(30, 30)
        button.setStyleSheet("font-size: 30px; font-weight: bold;")

        layout.addWidget(button, alignment=Qt.AlignTop)
        widget.setLayout(layout)
        widget.setFixedSize(50, height)

        return widget

    card_widget = QWidget()
    card_layout = QHBoxLayout()

    # Card size formatting
    cardheight: int = 150
    card_margin: int = 5
    itemheight: int = int(cardheight - 2 * card_margin)

    card_widget.setContentsMargins(card_margin, card_margin, card_margin, card_margin)
    card_layout.setContentsMargins(0, 0, 0, 0)
    card_layout.setSpacing(5)

    # create items
    icon: QLabel = get_icon(icon_filename, itemheight)
    settingswidget: QWidget = get_settingswidget(itemheight)

    # add to main layout
    card_layout.addWidget(icon)
    card_layout.addWidget(content)
    card_layout.addWidget(settingswidget, alignment=Qt.AlignTop)

    # main widget settings, add layout, set objectname for stylesheets
    card_widget.setLayout(card_layout)
    card_widget.setFixedHeight(cardheight)

    # card_widget.setStyleSheet("border: 3px solid;")
    card_widget.setObjectName("card")

    return card_widget