from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt

def headerUI(self) -> QWidget:
    header = QWidget()
    layout = QHBoxLayout()

    layout.setContentsMargins(15, 0, 27, 0)
    layout.setSpacing(0)

    height: int = 80

    # Create items
    main_title = QLabel("Reede 20. Aprill")
    spacer = QSpacerItem(200, 120, QSizePolicy.Expanding, QSizePolicy.Expanding)
    plusbutton = QPushButton("+")

    # item individual settings
    main_title.setFixedHeight(height)
    plusbutton.setFixedSize(int(height * 0.6), int(height * 0.6))

    # Add to layout
    layout.addWidget(main_title)
    layout.addItem(spacer)
    layout.addWidget(plusbutton)

    # Layout > widget
    header.setLayout(layout)
    header.setFixedHeight(height)

    # used for stylesheets
    main_title.setObjectName("main_title")
    header.setObjectName("header")
    plusbutton.setObjectName("plusbutton")

    return header