from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
import datetime
import shutil
import openpyxl

class Ui(ScreenManager):
    pass

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Orange'
        Builder.load_file('design.kv')

        return Ui()

    def cambiar_fondo(self, checked, value):
        if value:
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'

    def abrir_plantilla_general(self):
            fecha_actual = datetime.datetime.now()
            fecha = fecha_actual.strftime("%d-%m-%Y")
            dir_plantilla_general = "Plantillas/Plantilla_info_general.xlsx"
            dir_archivos_guardados = "Guardados/"
            dir_nuevo_archivo = dir_archivos_guardados + fecha + ".xlsx"
            shutil.copy(dir_plantilla_general, dir_nuevo_archivo)
            #workbook = openpyxl.load_workbook(dir_nuevo_archivo)
            #print('Se abrio el archivo con direccion:', dir_nuevo_archivo)
            #workbook.close()
            #print('Se cerro el archivo con direccion:', dir_nuevo_archivo)

if __name__ == "__main__":
    MainApp().run()
