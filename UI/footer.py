from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy

def footerUI(self) -> QWidget:
    footer = QWidget()
    layout = QHBoxLayout()

    layout.setContentsMargins(0, 0, 0, 0)
    layout.setSpacing(0)

    height = 60

    # create buttons
    self.kulud_button = QPushButton("kulud")
    self.tulud_button = QPushButton("tulud")
    self.kontod_button = QPushButton("kontod")
    self.statistika_button = QPushButton("statistika")

    # button settings
    buttons = [self.kulud_button, self.tulud_button, self.kontod_button, self.statistika_button]

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