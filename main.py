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
            text: "Informacion General Item 1"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "1"

        OneLineListItem:
            text: "Informacion General Item 2"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "2"






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
                                    padding : 50
                                    MDLabel:
                                        halign: "center"
                                        text: "Informacion General"
                                        font_style: "H4"
                                        size: self.size


                                MDLabel:
                                    halign: "left"
                                    text: "Item 1"
                                    font_style: "H5"
                                    size: self.size


                                MDTextField:
                                    id: nombre_proyecto
                                    hint_text: "Nombre Proyecto"
                                    
                                MDTextField:
                                    id: tipologia_vivienda
                                    hint_text: "Tipologia de Vivienda"

                                MDTextField:
                                    id: direccion
                                    hint_text: "Direccion"
                                
                                MDTextField:
                                    id: etapa
                                    hint_text: "Etapa"

                                MDTextField:
                                    id: superficie_vivienda
                                    hint_text: "Superficcie de Vivienda"
                                    
                                MDTextField:
                                    id: numero_pisos
                                    hint_text: "Numero de Pisos"

                                MDTextField:
                                    id: orientacion_fachada
                                    hint_text: "Orientacion Fachada"

                                MDTextField:
                                    id: orientacion_acceso
                                    hint_text: "Orientacion Acceso"
                                
                                MDTextField:
                                    id: clima
                                    hint_text: "Clima"
                                    helper_text: "Opciones: Soleado, Lluvioso, Nublado, Parcialmente nublado"
                                    helper_text_mode: "on_focus"
                                
                                MDTextField:
                                    id: temp_exterior
                                    hint_text: "Temperatura exterior"
                                
                                MDTextField:
                                    id: hum_exterior
                                    hint_text: "Humedad exterior"
                                
                                MDTextField:
                                    id: temp_interior
                                    hint_text: "Temperatura interior"
                                
                                MDTextField:
                                    id: hum_interior
                                    hint_text: "Humedad interior"
                                
                                MDTextField:
                                    id: Recibido_por
                                    hint_text: "Recibido por:"
                                    helper_text: "Opciones: Propietario, Arrendatario, Otro"
                                    helper_text_mode: "on_focus"

                                MDTextField:
                                    id: nombre_recibido_por
                                    hint_text: "Nombre de la persona"

                                MDTextField:
                                    id: años_uso_vivienda
                                    hint_text: "Años de uso vivienda"
                                
                                MDTextField:
                                    id: nom_inspector
                                    hint_text: "Inspector CITEC UBB"
                                
                                MDTextField:
                                    id: ci_inspector
                                    hint_text: "C.I."
                                
                                MDTextField:
                                    id: reparaciones
                                    hint_text: "Reparaciones"
                                    helper_text: "Opciones: Si, No"
                                    helper_text_mode: "on_focus"
                                
                                MDTextField:
                                    id: resp_reparaciones
                                    hint_text: "¿Cuántas y de qué tipo?"
                                
                                MDTextField:
                                    id: apelaciones
                                    hint_text: "Ampliaciones"
                                    helper_text: "Opciones: Si, No"
                                    helper_text_mode: "on_focus"
                                
                                MDTextField:
                                    id: resp_apelaciones
                                    hint_text: "¿Cuántas y de qué tipo?"
                                
                                MDTextField:
                                    id: obs_item_1
                                    multiline: True
                                    hint_text: "Observaciones"
                                
                            


            MDScreen: 
                name: "2"

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
                                    padding : 50
                                    MDLabel:
                                        halign: "center"
                                        text: "Informacion General"
                                        font_style: "H4"
                                        size: self.size

                                MDLabel:
                                    halign: "left"
                                    text: "Item 2"
                                    font_style: "H5"
                                    size: self.size

                                MDTextField:
                                    id: num_residentes
                                    hint_text: "N° de recintos vivienda"
                                
                                MDTextField:
                                    id: total_num_habitantes
                                    hint_text: "Total número de habitantes "
                                
                                MDTextField:
                                    id: num_adultos
                                    hint_text: "Adultos "
                                
                                MDTextField:
                                    id: num_niños
                                    hint_text: "Niños en edad escolar "
                                
                                MDTextField:
                                    id: num_adultos_mayores
                                    hint_text: "Adutlos mayores "
                                
                                MDTextField:
                                    id: num_ocup_dia
                                    hint_text: "Ocupación todo el día "
                                
                                MDTextField:
                                    id: num_ocup_intermitente
                                    hint_text: "Ocupación intermitente "
                                
                                MDTextField:
                                    id: den_ocup_prevista
                                    hint_text: "Densidad ocupacional prevista "
                                
                                MDTextField:
                                    id: den_ocup_total
                                    hint_text: "Densidad ocupacional real "

                                MDTextField:
                                    id: obs_item2
                                    hint_text: "Densidad ocupacional real "

                            
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

    hora_ingreso = datetime.datetime.now().strftime("%H:%M")
   

    def build(self):
        self.theme_cls.primary_palette = "Blue"
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

        #Recuperacion de los datos ingresados para plantilla Informacion General
        nombre_proyecto = self.root.ids.nombre_proyecto.text
        tipología_vivienda = self.root.ids.tipologia_vivienda.text
        direccion = self.root.ids.direccion.text
        etapa = self.root.ids.etapa.text
        superficie_vivienda = self.root.ids.superficie_vivienda.text
        numero_pisos = self.root.ids.numero_pisos.text
        orientacion_fachada = self.root.ids.orientacion_fachada.text
        orientacion_acceso = self.root.ids.orientacion_acceso.text
        clima = self.root.ids.clima.text
        temp_exterior = self.root.ids.temp_exterior.text
        hum_exterior = self.root.ids.hum_exterior.text
        temp_interior= self.root.ids.temp_interior.text
        hum_interior = self.root.ids.hum_interior.text
        Recibido_por = self.root.ids.Recibido_por.text
        nombre_recibido_por=  self.root.ids.nombre_recibido_por.text
        años_uso_vivienda = self.root.ids.años_uso_vivienda.text
        nom_inspector = self.root.ids.nom_inspector.text
        ci_inspector = self.root.ids.ci_inspector.text
        reparaciones= self.root.ids.reparaciones.text
        resp_reparaciones = self.root.ids.resp_reparaciones.text
        apelaciones = self.root.ids.apelaciones.text
        resp_apelaciones = self.root.ids.resp_apelaciones.text
        obs_item_1 = self.root.ids.obs_item_1.text
        num_residentes = self.root.ids.num_residentes.text
        total_num_habitantes = self.root.ids.total_num_habitantes.text
        num_adultos = self.root.ids.num_adultos.text
        num_niños = self.root.ids.num_niños.text
        num_adultos_mayores = self.root.ids.num_adultos_mayores.text
        num_ocup_dia = self.root.ids.num_ocup_dia.text
        num_ocup_intermitente = self.root.ids.num_ocup_intermitente.text
        den_ocup_prevista=  self.root.ids.den_ocup_prevista.text
        den_ocup_total = self.root.ids.den_ocup_total.text
        obs_item2 = self.root.ids.obs_item2.text


        #Dar nombre al archivo creado
        dir_nuevo_archivo = nombre_proyecto + " (" + fecha + ")" + ".xlsx" 
        nombre_archivo = nombre_proyecto
        shutil.copy(dir_plantilla_general, dir_nuevo_archivo)
        hora_salida = datetime.datetime.now().strftime("%H:%M")

        #Carga de la plantilla
        libro = load_workbook(filename=dir_nuevo_archivo)
        print('Se abrio el archivo con direccion:', dir_nuevo_archivo)

        #Datos Automaticos
        informacion_general = libro['Informacion_General']
        informacion_general['F8'] = nombre_archivo
        informacion_general['I10'] = fecha
        informacion_general['M10'] = self.hora_ingreso
        informacion_general['Q10'] = hora_salida
        
        #Guardado datos en plantilla Informacion General
        informacion_general['F9'] = tipología_vivienda
        informacion_general['F11'] = direccion
        informacion_general['P11'] = etapa
        informacion_general['F11'] = superficie_vivienda
        informacion_general['F12'] = numero_pisos
        informacion_general['M12'] = orientacion_fachada
        informacion_general['P12'] = orientacion_acceso
        informacion_general['R12'] = clima
        informacion_general['F14'] = temp_exterior
        informacion_general['N14'] = hum_exterior
        informacion_general['F15'] = temp_interior
        informacion_general['N15'] = hum_interior
        informacion_general['F16'] = Recibido_por
        informacion_general['J17'] = nombre_recibido_por
        informacion_general['M20'] = años_uso_vivienda
        informacion_general['F21'] = nom_inspector
        informacion_general['N21'] = ci_inspector
        informacion_general['F24'] = reparaciones
        informacion_general['H24'] = resp_reparaciones
        informacion_general['F26'] = apelaciones
        informacion_general['H26'] = resp_apelaciones
        informacion_general['C28'] = obs_item_1
        informacion_general['C35'] = num_residentes
        informacion_general['F35'] = total_num_habitantes
        informacion_general['I35'] = num_adultos
        informacion_general['L35'] = num_niños
        informacion_general['O35'] = num_adultos_mayores
        informacion_general['F36'] = num_ocup_dia
        informacion_general['L36'] = num_ocup_intermitente
        informacion_general['F38'] = den_ocup_prevista
        informacion_general['L38'] = den_ocup_total
        informacion_general['P36'] = obs_item2


        #Guardado del archivo
        libro.save(dir_nuevo_archivo)
        print('Se cerro el archivo con direccion:', dir_nuevo_archivo)
        dialog.dismiss()


if __name__ == "__main__":
    MainApp().run()
