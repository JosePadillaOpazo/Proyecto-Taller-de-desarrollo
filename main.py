from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.scrollview import MDScrollView
from kivy.properties import ObjectProperty
import datetime
import shutil
from openpyxl import load_workbook
from kivy.lang.builder import Builder

KV = '''
#: import RiseInTransition kivy.uix.screenmanager.RiseInTransition
#: import SlideTransition kivy.uix.screenmanager.SlideTransition

<ContentNavigationDrawer>

    MDList:

        OneLineListItem:
            text: "Screen 1"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "1"

        OneLineListItem:
            text: "Screen 2"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "2"

        OneLineListItem:
            text: "Screen 3"

        OneLineListItem:
            text: "Screen 4"
                        
        OneLineListItem:
            text: "Screen 5"
            
        OneLineListItem:
            text: "Screen 6"
            
        OneLineListItem:
            text: "Screen 7"
            
        OneLineListItem:
            text: "Screen 8"
            
        OneLineListItem:
            text: "Screen 9"
            
        OneLineListItem:
            text: "Screen 10"
            
        OneLineListItem:
            text: "Screen 11"
            
        OneLineListItem:
            text: "Screen 12"
            
        OneLineListItem:
            text: "Screen 13"
            
        OneLineListItem:
            text: "Screen 14"
            
        OneLineListItem:
            text: "Screen 15"
            
        OneLineListItem:
            text: "Screen 16"





MDScreen:

    MDNavigationLayout:

        MDScreenManager:
            id: screen_manager
    
            MDScreen: 
                name: "1"

                MDBoxLayout:
                    orientation: 'vertical'

                    MDTopAppBar:
                        use_overflow: True
                        pos_hint: {"top": 1}
                        elevation: 4
                        title: "Navegación"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        right_action_items: [["content-save", lambda x: app.mostrar_dialogo_guardar()]]

                    MDBoxLayout:
                        orientation: 'vertical'

                        ScrollView:

                            MDBoxLayout:
                                orientation: 'vertical'
                                size_hint_y: None
                                height: self.minimum_height
                                padding : 100
                                
                                MDBoxLayout:    
                                    orientation: 'vertical'    
                                    padding : 30
                                    MDLabel:
                                        halign: "center"
                                        text: "Informacion General"
                                        font_style: "H4"
                                        size: self.size

                                MDTextField:
                                    id: nombre_proyecto
                                    hint_text: "Nombre Proyecto"
                                    
                                   

                                MDTextField:
                                    hint_text: "Tipologia de Vivienda"
                                
                                MDTextField:
                                    hint_text: "Numero de Ficha"

                                MDTextField:
                                    hint_text: "Direccion"
                                
                                MDTextField:
                                    hint_text: "Etapa"

                                MDTextField:
                                    hint_text: "Superficcie de Vivienda"

                                MDTextField:
                                    hint_text: "Orientacion Fachada"

                                MDTextField:
                                    hint_text: "Orientacion Acceso"

                                MDTextField:
                                    hint_text: "info 1"

                                MDTextField:
                                    hint_text: "info 2"

                                MDTextField:
                                    hint_text: "info 3"

                                MDTextField:
                                    hint_text: "info 4"


            MDScreen: 
                name: "2"

                MDBoxLayout:
                    orientation: 'vertical'

                    MDTopAppBar:
                        pos_hint: {"top": 1}
                        elevation: 4
                        title: "Navegación"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

                    MDBoxLayout:
                        orientation: 'vertical'
                        ScrollView:
                            MDBoxLayout:
                                orientation: 'vertical'
                                size_hint_y: None
                                height: self.minimum_height
                                padding: dp(100)

                                MDTextField:
                                    hint_text: "info 1"

                                MDTextField:
                                    hint_text: "info 2"

                                MDTextField:
                                    hint_text: "info 3"

                                MDTextField:
                                    hint_text: "info 4"

                            
        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer



'''


class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)
    
    def mostrar_dialogo_guardar(self):
        dialog = MDDialog(
            text="¿Deseas guardar el archivo?",
            buttons=[
                MDFlatButton(
                    text="Cancelar",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=lambda *args: dialog.dismiss()
                ),
                MDFlatButton(
                    text="Guardar",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=lambda *args: self.guardar_archivo(dialog)
                ),
            ],
        )
        dialog.open()

    def guardar_archivo(self, dialog):
        fecha_actual = datetime.datetime.now()
        fecha = fecha_actual.strftime("%d-%m-%Y")
        dir_plantilla_general = "Plantillas/Plantilla_info_general.xlsx"
        dir_archivos_guardados = "Guardados/"
        nombre_proyecto = self.root.ids.nombre_proyecto.text
        dir_nuevo_archivo = dir_archivos_guardados + nombre_proyecto + " (" + fecha + ")" + ".xlsx" 
        nombre_archivo = nombre_proyecto
        shutil.copy(dir_plantilla_general, dir_nuevo_archivo)

        libro = load_workbook(filename=dir_nuevo_archivo)
        print('Se abrio el archivo con direccion:', dir_nuevo_archivo)
        hoja1 = libro['Hoja 1']
        hoja1['F8'] = nombre_archivo
        libro.save(dir_nuevo_archivo)
        print('Se cerro el archivo con direccion:', dir_nuevo_archivo)
        dialog.dismiss()


if __name__ == "__main__":
    MainApp().run()
