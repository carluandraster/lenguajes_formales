import openpyxl
from openpyxl.worksheet.worksheet import Worksheet

class PruebaDeEscritorio:
    __wb: openpyxl.Workbook
    __ws: Worksheet
    __fila: int = 1
    __cabeceras: list[str]
    
    def __init__(self, nombre_archivo: str, cabeceras: list[str]):
        self.__wb = openpyxl.load_workbook(nombre_archivo)
        self.__ws = Worksheet(self.__wb)
        self.__cabeceras = cabeceras
        for cabecera in cabeceras:
            self.__ws.cell(row=self.__fila, column=cabeceras.index(cabecera) + 1, value=cabecera)
        self.__fila += 1
    
    def modificar_variable(self, nombre_variable: str, valor: str):
        self.__ws.cell(row=self.__fila, column=self.__cabeceras.index(nombre_variable) + 1, value=valor)
        self.__fila += 1