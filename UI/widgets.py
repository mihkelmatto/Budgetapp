from PyQt5.QtWidgets import QLabel, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from utils.filepath import root_directory



def widgets_cardbase(icon_filename: str, content: QWidget) -> QWidget: # Creates a card with icon and settings button - empty content section
    def get_icon(filename: str, size: int) -> QLabel:
        filepath = root_directory("Resources", "Icons", filename)

        label = QLabel()
        pixmap = QPixmap(filepath)

        label.setFixedSize(size, size)
        label.setPixmap(pixmap)
        label.setScaledContents(True)

        return label

    def get_settingsbutton() -> QPushButton:
        button = QPushButton("⋮")
        button.setFixedSize(30, 30)
        button.setStyleSheet("font-size: 30px; font-weight: bold;")

        return button

    card_widget = QWidget()
    card_layout = QHBoxLayout()

    # Card size formatting
    cardheight = 150
    card_widget.setContentsMargins(0, 0, 0, 0)
    card_layout.setContentsMargins(0, 0, 0, 0)
    card_layout.setSpacing(0)

    # create items
    icon: QLabel = get_icon(icon_filename, cardheight)
    settingsbutton: QPushButton = get_settingsbutton()

    # add to main layout
    card_layout.addWidget(icon)
    card_layout.addWidget(content)
    card_layout.addWidget(settingsbutton, alignment=Qt.AlignTop)

    # main widget settings, add layout, set objectname for stylesheets
    card_widget.setLayout(card_layout)
    card_widget.setFixedHeight(cardheight)

    card_widget.setStyleSheet("border: 3px solid")

    return card_widget