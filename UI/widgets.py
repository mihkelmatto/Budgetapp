from PyQt5.QtWidgets import QLabel, QWidget, QHBoxLayout, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from utils.filepath import root_directory

def widgets_cardbase(icon_filename: str, content: QWidget) -> QWidget:
    """
    Reusable function that creates a card layout with an icon and settings button
    Content section has to be passed as an argument (QWidget)
    Height
    """

    def create_icon(filename: str, height: int) -> QLabel:
        """Create an icon label with provided height and filename (without path)"""
        filepath = root_directory("Resources", "Icons", filename)

        # create items
        label = QLabel()
        pixmap = QPixmap(filepath)
        label.setPixmap(pixmap)

        # size formatting
        label.setFixedSize(height - 15, height - 15)
        label.setScaledContents(True)

        return label

    def create_settingswidget(height: int) -> QWidget:
        """Create a settings button widget with vertical layout"""
        # create widget
        widget = QWidget()
        widget.setContentsMargins(0, 0, 5, 0)
        layout = QVBoxLayout(widget)

        # create items
        button = QPushButton("⋮")
        button.setFixedSize(20, 30)
        button.setStyleSheet("font-size: 30px; font-weight: bold;")

        # add to layout, size formatting
        layout.addWidget(button, alignment=Qt.AlignTop | Qt.AlignRight)
        widget.setFixedSize(50, height)
        button.setObjectName("settingsbutton")

        return widget
    # Main widget setup (size variables > formatting)
    cardheight, cardmargin = 170, 5
    itemheight: int = cardheight - 2 * cardmargin
    card_widget = QWidget()
    card_layout = QHBoxLayout(card_widget)

    card_widget.setFixedHeight(cardheight)
    card_widget.setContentsMargins(cardmargin, cardmargin, cardmargin, cardmargin)
    card_layout.setContentsMargins(0, 0, 0, 0)
    card_layout.setSpacing(5)

    # add items to main layout
    card_layout.addWidget(create_icon(icon_filename, itemheight))
    card_layout.addWidget(content)
    card_layout.addWidget(create_settingswidget(itemheight), alignment=Qt.AlignTop)

    # Set object names for stylesheets
    card_widget.setObjectName("card")
    # card_widget.setStyleSheet("border: 3px solid;")

    return card_widget