from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea,QSpacerItem, QSizePolicy,QLineEdit
from PySide6.QtGui import QPixmap
from PySide6.QtCore  import Qt, Signal, Property

class Empresa(QWidget):
    doble_clic = Signal(str)
    def __init__(self, empresa:str, parent=None):
        super().__init__(parent)
        layout=QHBoxLayout(self)
        
        self.__logo=os.path.join(os.path.dirname(__file__), '..', empresa['logo'])
        self.__etiqueta_logo=QLabel()
        self.__etiqueta_logo.setMaximumSize(60,60)
        self.__etiqueta_logo.setScaledContents(True)
        self.__etiqueta_logo.setPixmap(QPixmap(self.__logo))
        
        layout.addWidget(self.__etiqueta_logo)
        
        layout_secundario=QVBoxLayout
        layout.addLayout(layout_secundario)
        self.__nombre=QLabel(empresa['nombre'])
        self.__direccion1