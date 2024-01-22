from PySide6.QtWidgets import QApplication, QLineEdit, QLabel, QWidget
from PySide6.QtGui import QIcon, QAction


class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo de uso de slot predefinido")
        self.setFixedSize(300, 30)
        self.mostrar = QIcon("C:/Users/Edu/Desktop/Si.png")

        self.line_edit1 = QLineEdit(self)

        self.line_edit1.setFixedSize(150, 30)
        self.line_edit1.setMaxLength(25)

        self.accion_cambiar_visibilidad = QAction(self.mostrar, "¡Ejemplo!", self)
        self.accion_cambiar_visibilidad.triggered.connect(self.cambiar_visibilidad)

        self.line_edit1.addAction(self.accion_cambiar_visibilidad, QLineEdit.TrailingPosition)
        self.etiqueta1 = QLabel("Self")
        self.etiqueta1.setFixedSize(150, 30)
        self.etiqueta1.move(150, 0)

        self.line_edit1.textChanged.connect(self.etiqueta1.setText)

    def cambiar_visibilidad(self):
        print("¡Ejemplo!")


if __name__== "__main__":
    app = QApplication()
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()