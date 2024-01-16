import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog
from PySide6.QtGui import QAction, QIcon


class CasoPractico5(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Caso practico 5")
        
        
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)
        self.crear_menu()
        self.crear_herramientas()

    
    def crear_menu(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("Archivo")
        open_action = QAction(QIcon("C:/Users/Edu/Desktop/abrir_archivo.png"), "Abrir archivo", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.abrir)
        file_menu.addAction(open_action)

        save_action = QAction(QIcon("C:/Users/Edu/Desktop/guardar_imagen.png"), "Guardar archivo", self)
        save_action.setShortcut("Ctrl+G")
        save_action.triggered.connect(self.Guardar)
        file_menu.addAction(save_action)

        close_action = file_menu.addAction("Cerrar archivo")
        close_action.setShortcut("Ctrl+ñ")
        close_action.triggered.connect(self.close_file)

        exit_action = file_menu.addAction("Salir")
        exit_action.setShortcut("Ctrl+b")
        exit_action.triggered.connect(self.close)

    def crear_herramientas(self):
        toolbar = self.addToolBar("Herramientas")
        open_action = QAction(QIcon("C:/Users/Edu/Desktop/abrir_archivo.png"), "Abrir archivo", self)
        open_action.triggered.connect(self.abrir)
        open_action.setText("Abrir archivo")
        toolbar.addAction(open_action)

        save_action = QAction(QIcon("C:/Users/Edu/Desktop/guardar_imagen.png"), "Guardar archivo", self)
        save_action.triggered.connect(self.Guardar)
        save_action.setText("Guardar archivo")
        toolbar.addAction(save_action)

    def abrir(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Archivos de texto (*.txt)")
        if file_name:
            with open(file_name, "r") as file:
                self.text_edit.setText(file.read())
            self.current_file = file_name

    def Guardar(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "" , "Archivos de texto (*.txt)")
        if file_name:
            with open(file_name, "w") as file:
                file.write(self.text_edit.toPlainText())

    def close_file(self):
        self.text_edit.clear()
        self.current_file = None


if __name__ == "__main__":
    app = QApplication([])
    ventana1 = CasoPractico5()
    ventana1.show()
    app.exec()