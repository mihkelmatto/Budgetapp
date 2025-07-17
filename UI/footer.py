from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy

def footerUI(self) -> QWidget:
    footer = QWidget()
    layout = QHBoxLayout()

    layout.setContentsMargins(0, 0, 0, 0)
    layout.setSpacing(0)

    height = 60

    # create buttons
    self.menu_kulud = QPushButton("kulud")
    self.menu_tulud = QPushButton("tulud")
    self.menu_kontod = QPushButton("kontod")
    self.menu_statistika = QPushButton("statistika")

    # button settings
    buttons = [self.menu_kulud, self.menu_tulud, self.menu_kontod, self.menu_statistika]

    for button in buttons:
        layout.addWidget(button)
        button.setFixedSize(150, height)

    spacer = QSpacerItem(200, 120, QSizePolicy.Expanding, QSizePolicy.Expanding)
    layout.addItem(spacer)

    # layout settings
    footer.setLayout(layout)
    footer.setFixedHeight(height)

    # used for stylesheets
    footer.setObjectName("footer")

    return footer