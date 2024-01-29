from PySide6.QtGui import QIcon, QKeySequence
from PySide6.QtWidgets import QLineEdit

import DI_U04_A02_CP_03

class Editor_contraseña(QLineEdit):
   
    def _init_(self, parent=None):
        self.parent = parent
        super()._init_(parent)
        self.mostrar = QIcon()
        self.ocultar = QIcon()
        self.label=self.setEchoMode(QLineEdit.Password) #
        self.setPlaceholderText("introduce tu contraseña")
        self.accion_cambiar_visibilidad=self.addAction(self.mostrar,QLineEdit.TrailingPosition)
        self.accion_cambiar_visibilidad.setShortcut(QKeySequence("Ctrl+M"))
        self.accion_cambiar_visibilidad.triggered.connect(self.cambiar_visibilidad)
        self.contraseña_visible = False
        self.setWindowIcon(QIcon(self.mostrar))
    def cambiar_visibilidad(self):
        if not self.contraseña_visible:
            self.echoMode(QLineEdit.Normal)
            self.contraseña_visible = True
            self.accion_cambiar_visibilidad.setIcon(self.ocultar)
            self.setWindowIcon(QIcon(self.ocultar))
        else:
            self.echoMode(QLineEdit.Password)
            self.contraseña_visible = False
            self.accion_cambiar_visibilidad.setIcon((self.mostrar))
            self.setWindowIcon(QIcon(self.mostrar))
import C