from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.scrollview import ScrollView
import datetime
import shutil
from openpyxl import load_workbook



class CitecUbbApp(MDApp):

    hora_ingreso = datetime.datetime.now().strftime("%H:%M")

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'LightBlue'
        return Builder.load_file('main.kv')


    def cancelar_proceso_d(self):
        dialog = MDDialog(
            text="¿Seguro que deseas cancelar el proceso?",
            buttons=[
                MDFlatButton(
                    text="Si",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=lambda x: self.redirigir_pantalla_dialogo("inicio", dialog) 
                ),
                MDFlatButton(
                    text="No",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=lambda *args: dialog.dismiss()
                ),
            ],
        )
        dialog.open()


    def guardar_archivo(self, dialog, textfield):
        # Obtener el valor ingresado en el textfield
        nombre_ingresado = textfield.text
        
        self.guardar(nombre_ingresado)
        
        #self.root.clear_widgets()
        #self.root = Builder.load_file('main.kv')
        #self.stop()
        #CitecUbbApp().run()
        dialog.dismiss()



    #Eliminar Habitacion con sus hojas
    def eliminar_habitacion_d(self, habitacion):
        if habitacion == "Habitacion 1":
            dialog_h = MDDialog(
                text="¿Seguro que deseas eliminar la " + habitacion + " ?",
                buttons=[
                    MDFlatButton(
                        text="Si",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x: self.eliminar_habitacion(habitacion, dialog_h)
                    ),
                    MDFlatButton(
                        text="No",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda *args: dialog_h.dismiss()
                    ),
                ],
            )
            dialog_h.open()



    def eliminar_habitacion(self, habitacion, dialog_h):
        
        if habitacion == "Habitación 1":
            self.h1_mea=0
            self.h1_me2=0
            self.h1_me3=0
            self.h1_pi_cie=0
            
        self.redirigir_pantalla_dialogo("info_general", dialog_h) 






    #Dialogos eliminar hojas
    def eliminar_hoja_d(self, hoja):
        dialogo_h = MDDialog(
            text="¿Seguro que deseas eliminar " + hoja + " ?",
            buttons=[
                MDFlatButton(
                    text="Si",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=lambda x: self.eliminar_hoja(hoja, dialogo_h)
                ),
                MDFlatButton(
                    text="No",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=lambda *args: dialogo_h.dismiss()
                ),
            ],
        )
        dialogo_h.open()

    

    #Eliminar Hojas
    def eliminar_hoja(self, hoja, dialogo_h):
        
        if hoja == "H1 Hoja 2":
            self.h1_me2=0
            self.redirigir_pantalla_dialogo("info_general", dialogo_h) 

        if hoja == "H1 Hoja 3":
            self.h1_me3=0
            self.redirigir_pantalla_dialogo("info_general", dialogo_h) 

        if hoja == "H1 Piso-Cielo":
            self.h1_pi_cie=0
            self.redirigir_pantalla_dialogo("info_general", dialogo_h) 



    #Redirigir pantallas
    def redirigir_pantalla_dialogo(self, pantalla, dialog):

        if pantalla == "inicio":
            self.root.clear_widgets()
            self.root = Builder.load_file('main.kv')
            self.stop()
            CitecUbbApp().run()
        else:
            self.root.ids.sm_global.current = pantalla
        dialog.dismiss()



    #Dialogo Guardar
    def mostrar_dialogo_guardar(self):
        textfield = MDTextField(
            hint_text="Nombre del Archivo:",
            required=True,
            helper_text="Requerido",
            helper_text_mode="on_error",
        )
        
        dialog = MDDialog(
            title="Guardar y terminar el proceso",
            type="custom",
            content_cls=textfield,
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
                    on_release=lambda *args: self.guardar_archivo(dialog, textfield)  
                ),
            ],
        )
        dialog.open()


        




    


    clima=""
    recibido_por=""
    ampliaciones=""
    reparaciones=""
    def guardar_checkbox(self, seleccion):
        if seleccion == "Soleado":
            self.clima = seleccion
            
        if seleccion == "Nublado":
            self.clima = seleccion

        if seleccion == "Lluvioso":
            self.clima = seleccion

        if seleccion == "Parcialmente Nublado":
            self.clima = seleccion

        if seleccion == "Propietario":
            self.recibido_por = seleccion

        if seleccion == "Arrendatario":
            self.recibido_por = seleccion

        if seleccion == "Otro":
            self.recibido_por = seleccion
        
        if seleccion == "Ampliaciones: Si":
            self.ampliaciones = "Si"

        if seleccion == "Ampliaciones: No":
            self.ampliaciones = "No"

        if seleccion == "Reparaciones: Si":
            self.reparaciones = "Si"

        if seleccion == "Reparaciones: No":
            self.reparaciones = "No"


    pat_vis=""
    olor=""
    manif=""
    modif=""
    en_esq_muro=""
    en_cie_muro=""
    en_pis_muro=""
    ras_ven=""
    baj_ven=""
    ar_cen=""
    pun_loc=""
    d_en_esq_muro=""
    d_en_cie_muro=""
    d_en_pis_muro=""
    d_ras_ven=""
    d_baj_ven=""
    d_ar_cen=""
    d_pun_loc=""
    aireador=""
    extractor=""
    campana=""
    cel_pu=""
    reb_pu=""
    otra_vent=""
    afectacion=""
    calefaccion=""
    def guardar_checkbox_h1_mea(self, seleccion):
        if seleccion == "Patologias: Si":
            self.pat_vis = "Si"

        if seleccion == "Patologias: No":
            self.pat_vis = "No"
        
        if seleccion == "Olor: Si":
            self.olor = "Si"
        
        if seleccion == "Olor: No":
            self.olor = "No"

        if seleccion == "Manifestaciones: Si":
            self.manif = "Si"

        if seleccion == "Manifestaciones: No":
            self.manif = "No"
        
        if seleccion == "Modificaciones: Si":
            self.modif = "Si"
        
        if seleccion == "Modificaciones: No":
            self.modif = "No"



        if seleccion == "Encuentro esquina muro mancha: Si":
            self.en_esq_muro = "Si"

        if seleccion == "Encuentro esquina muro mancha: No":
            self.en_esq_muro = "No"

        if seleccion == "Encuentro cielo muro mancha: Si":
            self.en_cie_muro = "Si"
        
        if seleccion == "Encuentro cielo muro mancha: No":
            self.en_cie_muro = "No"

        if seleccion == "Encuentro piso muro mancha: Si":
            self.en_pis_muro = "Si"
        
        if seleccion == "Encuentro piso muro mancha: No":
            self.en_pis_muro = "No"

        if seleccion == "Rasgo de ventana mancha: Si":
            self.ras_ven = "Si"

        if seleccion == "Rasgo de ventana mancha: No":
            self.ras_ven = "No"

        if seleccion == "Bajo ventana (antepecho) mancha: Si":
            self.baj_ven = "Si"

        if seleccion == "Bajo ventana (antepecho) mancha: No":
            self.baj_ven = "No"

        if seleccion == "Área central mancha: Si":
            self.ar_cen = "Si"

        if seleccion == "Área central mancha: No":
            self.ar_cen = "No"

        if seleccion == "Puntual localizada y/o extendida mancha: Si":
            self.pun_loc = "Si"

        if seleccion == "Puntual localizada y/o extendida mancha: No":
            self.pun_loc = "No"

        

        if seleccion == "Encuentro esquina muro daño: Si":
            self.d_en_esq_muro = "Si"

        if seleccion == "Encuentro esquina muro daño: No":
            self.d_en_esq_muro = "No"

        if seleccion == "Encuentro cielo muro daño: Si":
            self.d_en_cie_muro = "Si"
        
        if seleccion == "Encuentro cielo muro daño: No":
            self.d_en_cie_muro = "No"

        if seleccion == "Encuentro piso muro daño: Si":
            self.d_en_pis_muro = "Si"
        
        if seleccion == "Encuentro piso muro daño: No":
            self.d_en_pis_muro = "No"

        if seleccion == "Rasgo de ventana daño: Si":
            self.d_ras_ven = "Si"

        if seleccion == "Rasgo de ventana daño: No":
            self.d_ras_ven = "No"

        if seleccion == "Bajo ventana (antepecho) daño: Si":
            self.d_baj_ven = "Si"

        if seleccion == "Bajo ventana (antepecho) daño: No":
            self.d_baj_ven = "No"

        if seleccion == "Área central daño: Si":
            self.d_ar_cen = "Si"

        if seleccion == "Área central daño: No":
            self.d_ar_cen = "No"

        if seleccion == "Puntual localizada y/o extendida daño: Si":
            self.d_pun_loc = "Si"

        if seleccion == "Puntual localizada y/o extendida daño: No":
            self.d_pun_loc = "No"



        if seleccion == "Aireador: Operativo":
            self.aireador = "Operativo"

        if seleccion == "Aireador: No Operativo":
            self.aireador = "No Operativo"

        if seleccion == "Extractor: Operativo":
            self.extractor = "Operativo"

        if seleccion == "Extractor: No Operativo":
            self.extractor = "No Operativo"

        if seleccion == "Campana: Operativo":
            self.campana = "Operativo"

        if seleccion == "Campana: No Operativo":
            self.campana = "No Operativo"

        if seleccion == "Celosía puerta: Operativo":
            self.cel_pu = "Operativo"

        if seleccion == "Celosía puerta: No Operativo":
            self.cel_pu = "No Operativo"

        if seleccion == "Rebaje puerta: Operativo":
            self.reb_pu = "Operativo"

        if seleccion == "Rebaje puerta: No Operativo":
            self.reb_pu = "No Operativo"

        if seleccion == "Otro vent: Operativo":
            self.otra_vent = "Operativo"

        if seleccion == "Otro vent: No Operativo":
            self.otra_vent = "No Operativo"

        if seleccion == "Nulo":
            self.afectacion = seleccion

        if seleccion == "Bajo":
            self.afectacion = seleccion

        if seleccion == "Medio":
            self.afectacion = seleccion
        
        if seleccion == "Alto":
            self.afectacion = seleccion

        if seleccion == "Calefacción: Eléctrico":
            self.calefaccion = "Eléctrico"

        if seleccion == "Calefacción: Gas / parafina con evacuacipon exterior (seca)":
            self.calefaccion = "Gas / parafina con evacuacipon exterior (seca)"

        if seleccion == "Calefacción: Biomasa con evacuación exterior (seca)":
            self.calefaccion = "Biomasa con evacuación exterior (seca)"
        
        if seleccion == "Calefacción: Parafina/gas móvil (húmeda)":
            self.calefaccion = "Parafina/gas móvil (húmeda)"
        




    h1_afectacion_h2=""
    en_esq_muro_h2=""
    en_cie_muro_h2=""
    en_pis_muro_h2=""
    ras_ven_h2=""
    baj_ven_h2=""
    ar_cen_h2=""
    pun_loc_h2=""
    d_en_esq_muro_h2=""
    d_en_cie_muro_h2=""
    d_en_pis_muro_h2=""
    d_ras_ven_h2=""
    d_baj_ven_h2=""
    d_ar_cen_h2=""
    d_pun_loc_h2=""
    def guardar_checkbox_h1_me2(self, seleccion):
        
        if seleccion == "Nulo":
            self.h1_afectacion_h2 = seleccion

        if seleccion == "Bajo":
            self.h1_afectacion_h2 = seleccion

        if seleccion == "Medio":
            self.h1_afectacion_h2 = seleccion
        
        if seleccion == "Alto":
            self.h1_afectacion_h2 = seleccion
        
        if seleccion == "Encuentro esquina muro mancha: Si":
            self.en_esq_muro_h2 = "Si"

        if seleccion == "Encuentro esquina muro mancha: No":
            self.en_esq_muro_h2 = "No"

        if seleccion == "Encuentro cielo muro mancha: Si":
            self.en_cie_muro_h2 = "Si"
        
        if seleccion == "Encuentro cielo muro mancha: No":
            self.en_cie_muro_h2 = "No"

        if seleccion == "Encuentro piso muro mancha: Si":
            self.en_pis_muro_h2 = "Si"
        
        if seleccion == "Encuentro piso muro mancha: No":
            self.en_pis_muro_h2 = "No"

        if seleccion == "Rasgo de ventana mancha: Si":
            self.ras_ven_h2 = "Si"

        if seleccion == "Rasgo de ventana mancha: No":
            self.ras_ven_h2 = "No"

        if seleccion == "Bajo ventana (antepecho) mancha: Si":
            self.baj_ven_h2 = "Si"

        if seleccion == "Bajo ventana (antepecho) mancha: No":
            self.baj_ven_h2 = "No"

        if seleccion == "Área central mancha: Si":
            self.ar_cen_h2 = "Si"

        if seleccion == "Área central mancha: No":
            self.ar_cen_h2 = "No"

        if seleccion == "Puntual localizada y/o extendida mancha: Si":
            self.pun_loc_h2 = "Si"

        if seleccion == "Puntual localizada y/o extendida mancha: No":
            self.pun_loc_h2 = "No"

        if seleccion == "Encuentro esquina muro daño: Si":
            self.d_en_esq_muro_h2 = "Si"

        if seleccion == "Encuentro esquina muro daño: No":
            self.d_en_esq_muro_h2 = "No"

        if seleccion == "Encuentro cielo muro daño: Si":
            self.d_en_cie_muro_h2 = "Si"
        
        if seleccion == "Encuentro cielo muro daño: No":
            self.d_en_cie_muro_h2 = "No"

        if seleccion == "Encuentro piso muro daño: Si":
            self.d_en_pis_muro_h2 = "Si"
        
        if seleccion == "Encuentro piso muro daño: No":
            self.d_en_pis_muro_h2 = "No"

        if seleccion == "Rasgo de ventana daño: Si":
            self.d_ras_ven_h2 = "Si"

        if seleccion == "Rasgo de ventana daño: No":
            self.d_ras_ven_h2 = "No"

        if seleccion == "Bajo ventana (antepecho) daño: Si":
            self.d_baj_ven_h2 = "Si"

        if seleccion == "Bajo ventana (antepecho) daño: No":
            self.d_baj_ven_h2 = "No"

        if seleccion == "Área central daño: Si":
            self.d_ar_cen_h2 = "Si"

        if seleccion == "Área central daño: No":
            self.d_ar_cen_h2 = "No"

        if seleccion == "Puntual localizada y/o extendida daño: Si":
            self.d_pun_loc_h2 = "Si"

        if seleccion == "Puntual localizada y/o extendida daño: No":
            self.d_pun_loc_h2 = "No"





    h1_afectacion_h3=""
    en_esq_muro_h3=""
    en_cie_muro_h3=""
    en_pis_muro_h3=""
    ras_ven_h3=""
    baj_ven_h3=""
    ar_cen_h3=""
    pun_loc_h3=""
    d_en_esq_muro_h3=""
    d_en_cie_muro_h3=""
    d_en_pis_muro_h3=""
    d_ras_ven_h3=""
    d_baj_ven_h3=""
    d_ar_cen_h3=""
    d_pun_loc_h3=""
    def guardar_checkbox_h1_me3(self, seleccion):
        
        if seleccion == "Nulo":
            self.h1_afectacion_h3 = seleccion

        if seleccion == "Bajo":
            self.h1_afectacion_h3 = seleccion

        if seleccion == "Medio":
            self.h1_afectacion_h3 = seleccion
        
        if seleccion == "Alto":
            self.h1_afectacion_h3 = seleccion
        
        if seleccion == "Encuentro esquina muro mancha: Si":
            self.en_esq_muro_h3 = "Si"

        if seleccion == "Encuentro esquina muro mancha: No":
            self.en_esq_muro_h3 = "No"

        if seleccion == "Encuentro cielo muro mancha: Si":
            self.en_cie_muro_h3 = "Si"
        
        if seleccion == "Encuentro cielo muro mancha: No":
            self.en_cie_muro_h3 = "No"

        if seleccion == "Encuentro piso muro mancha: Si":
            self.en_pis_muro_h3 = "Si"
        
        if seleccion == "Encuentro piso muro mancha: No":
            self.en_pis_muro_h3 = "No"

        if seleccion == "Rasgo de ventana mancha: Si":
            self.ras_ven_h3 = "Si"

        if seleccion == "Rasgo de ventana mancha: No":
            self.ras_ven_h3 = "No"

        if seleccion == "Bajo ventana (antepecho) mancha: Si":
            self.baj_ven_h3 = "Si"

        if seleccion == "Bajo ventana (antepecho) mancha: No":
            self.baj_ven_h3 = "No"

        if seleccion == "Área central mancha: Si":
            self.ar_cen_h3 = "Si"

        if seleccion == "Área central mancha: No":
            self.ar_cen_h3 = "No"

        if seleccion == "Puntual localizada y/o extendida mancha: Si":
            self.pun_loc_h3 = "Si"

        if seleccion == "Puntual localizada y/o extendida mancha: No":
            self.pun_loc_h3 = "No"


        if seleccion == "Encuentro esquina muro daño: Si":
            self.d_en_esq_muro_h3 = "Si"

        if seleccion == "Encuentro esquina muro daño: No":
            self.d_en_esq_muro_h3 = "No"

        if seleccion == "Encuentro cielo muro daño: Si":
            self.d_en_cie_muro_h3 = "Si"
        
        if seleccion == "Encuentro cielo muro daño: No":
            self.d_en_cie_muro_h3 = "No"

        if seleccion == "Encuentro piso muro daño: Si":
            self.d_en_pis_muro_h3 = "Si"
        
        if seleccion == "Encuentro piso muro daño: No":
            self.d_en_pis_muro_h3 = "No"

        if seleccion == "Rasgo de ventana daño: Si":
            self.d_ras_ven_h3 = "Si"

        if seleccion == "Rasgo de ventana daño: No":
            self.d_ras_ven_h3 = "No"

        if seleccion == "Bajo ventana (antepecho) daño: Si":
            self.d_baj_ven_h3 = "Si"

        if seleccion == "Bajo ventana (antepecho) daño: No":
            self.d_baj_ven_h3 = "No"

        if seleccion == "Área central daño: Si":
            self.d_ar_cen_h3 = "Si"

        if seleccion == "Área central daño: No":
            self.d_ar_cen_h3 = "No"

        if seleccion == "Puntual localizada y/o extendida daño: Si":
            self.d_pun_loc_h3 = "Si"

        if seleccion == "Puntual localizada y/o extendida daño: No":
            self.d_pun_loc_h3 = "No"
        
    


    h1_piso_niv_afe=""
    h1_cielo_niv_afe=""
    h1_per_piso_m=""
    h1_ar_cen_piso_m=""
    h1_pun_loc_piso_m=""
    h1_per_piso_d=""
    h1_ar_cen_piso_d=""
    h1_pun_loc_piso_d=""
    h1_per_cielo_m=""
    h1_ar_cen_cielo_m=""
    h1_pun_loc_cielo_m=""
    h1_per_cielo_d=""
    h1_ar_cen_cielo_d=""
    h1_pun_loc_cielo_d=""
    def guardar_checkbox_h1_pi_cie(self, seleccion):

        if seleccion == "Piso Nulo":
            self.h1_piso_niv_afe = "Nulo"

        if seleccion == "Piso Bajo":
            self.h1_piso_niv_afe = "Bajo"

        if seleccion == "Piso Medio":
            self.h1_piso_niv_afe = "Medio"

        
        if seleccion == "Piso Alto":
            self.h1_piso_niv_afe = "Alto"

        #Afectacion Cielo
        if seleccion == "Cielo Nulo":
            self.h1_cielo_niv_afe = seleccion

        if seleccion == "Cielo Bajo":
            self.h1_cielo_niv_afe = seleccion
            
        if seleccion == "Cielo Medio":
            self.h1_cielo_niv_afe = seleccion
           
        if seleccion == "Cielo Alto":
            self.h1_cielo_niv_afe = seleccion

        #piso
        if seleccion == "Perímetro piso mancha: Si":
            self.h1_per_piso_m = "Si"

        if seleccion == "Perímetro piso mancha: No":
            self.h1_per_piso_m = "No"

        if seleccion == "Área central piso mancha: Si":
            self.h1_ar_cen_piso_m = "Si"
        
        if seleccion == "Área central piso mancha: No":
            self.h1_ar_cen_piso_m = "No"

        if seleccion == "Puntual localizada y/o extendida piso mancha: Si":
            self.h1_pun_loc_piso_m = "Si"
        
        if seleccion == "Puntual localizada y/o extendida piso mancha: No":
            self.h1_pun_loc_piso_m = "No"

        if seleccion == "Perímetro piso daño: Si":
            self.h1_per_piso_d = "Si"

        if seleccion == "Perímetro piso daño: No":
            self.h1_per_piso_d = "No"

        if seleccion == "Área central piso daño: Si":
            self.h1_ar_cen_piso_d = "Si"
        
        if seleccion == "Área central piso daño: No":
            self.h1_ar_cen_piso_d = "No"

        if seleccion == "Puntual localizada y/o extendida piso daño: Si":
            self.h1_pun_loc_piso_d = "Si"
        
        if seleccion == "Puntual localizada y/o extendida piso daño: No":
            self.h1_pun_loc_piso_d = "No"

        #Cielo
        if seleccion == "Perímetro cielo mancha: Si":
            self.h1_per_cielo_m = "Si"

        if seleccion == "Perímetro cielo mancha: No":
            self.h1_per_cielo_m = "No"

        if seleccion == "Área central cielo mancha: Si":
            self.h1_ar_cen_cielo_m = "Si"
        
        if seleccion == "Área central cielo mancha: No":
            self.h1_ar_cen_cielo_m = "No"

        if seleccion == "Puntual localizada y/o extendida cielo mancha: Si":
            self.h1_pun_loc_cielo_m = "Si"
        
        if seleccion == "Puntual localizada y/o extendida cielo mancha: No":
            self.h1_pun_loc_cielo_m = "No"

        if seleccion == "Perímetro cielo daño: Si":
            self.h1_per_cielo_d = "Si"

        if seleccion == "Perímetro cielo daño: No":
            self.h1_per_cielo_d = "No"

        if seleccion == "Área central cielo daño: Si":
            self.h1_ar_cen_cielo_d = "Si"
        
        if seleccion == "Área central cielo daño: No":
            self.h1_ar_cen_cielo_d = "No"

        if seleccion == "Puntual localizada y/o extendida cielo daño: Si":
            self.h1_pun_loc_cielo_d = "Si"
        
        if seleccion == "Puntual localizada y/o extendida cielo daño: No":
            self.h1_pun_loc_cielo_d = "No"











    def guardar(self, nombre_archivo):

        fecha_actual = datetime.datetime.now()
        fecha = fecha_actual.strftime("%d-%m-%Y")
        hora_salida = datetime.datetime.now().strftime("%H:%M")


        #Dar nombre al archivo creado
        dir_plantilla_general = "Plantilla_info_general.xlsx"
        dir_nuevo_archivo = nombre_archivo + " (" + fecha + ")" + ".xlsx" 
        shutil.copy(dir_plantilla_general, dir_nuevo_archivo)

        #Carga de la plantilla
        libro = load_workbook(filename=dir_nuevo_archivo)

        #Datos Automaticos
        informacion_general = libro['Informacion_General']
        informacion_general['F8'] = self.root.ids.nombre_proyecto.text
        informacion_general['I10'] = fecha
        informacion_general['M10'] = self.hora_ingreso
        informacion_general['Q10'] = hora_salida
        
        #Guardado datos en plantilla Informacion General
        informacion_general['F9'] = self.root.ids.tipologia_vivienda.text
        informacion_general['F11'] = self.root.ids.direccion.text
        informacion_general['P11'] = self.root.ids.etapa.text
        informacion_general['F11'] = self.root.ids.superficie_vivienda.text
        informacion_general['J12'] = self.root.ids.numero_pisos.text
        informacion_general['M12'] = self.root.ids.orientacion_fachada.text
        informacion_general['P12'] = self.root.ids.orientacion_acceso.text
        informacion_general['R12'] = self.clima
        informacion_general['F14'] = self.root.ids.temp_exterior.text
        informacion_general['N14'] = self.root.ids.hum_exterior.text
        informacion_general['F15'] = self.root.ids.temp_interior.text
        informacion_general['N15'] = self.root.ids.hum_interior.text
        informacion_general['F16'] = self.recibido_por
        informacion_general['J17'] = self.root.ids.nombre_recibido_por.text
        informacion_general['M20'] = self.root.ids.años_uso_vivienda.text
        informacion_general['F21'] = self.root.ids.nom_inspector.text
        informacion_general['N21'] = self.root.ids.ci_inspector.text
        informacion_general['F24'] = self.reparaciones
        informacion_general['H24'] = self.root.ids.d_rep.text
        informacion_general['F26'] = self.ampliaciones
        informacion_general['H26'] = self.root.ids.d_amp.text
        informacion_general['C28'] = self.root.ids.obs_item_1.text
        informacion_general['C35'] = self.root.ids.num_recintos.text
        informacion_general['F35'] = self.root.ids.num_habitantes.text
        informacion_general['I35'] = self.root.ids.num_adultos.text
        informacion_general['L35'] = self.root.ids.num_niños.text
        informacion_general['O35'] = self.root.ids.num_adultos_may.text
        informacion_general['F36'] = self.root.ids.ocup_dia.text
        informacion_general['L36'] = self.root.ids.ocup_intermitente.text
        informacion_general['F38'] = self.root.ids.dens_ocup_prev.text
        informacion_general['L38'] = self.root.ids.dens_ocup_real.text
        informacion_general['P36'] = self.root.ids.obs_item_2.text




        #Guardar pantallas ocupadas

        
        #Guardar H1 Muro Eje A
        if self.h1_mea==1:
            
            H1_Muro_Eje_A = libro['H1_Muro_Eje_A']
            H1_Muro_Eje_A['C8'] = self.root.ids.nombre_habitacion1.text

            H1_Muro_Eje_A['F33'] = self.root.ids.h1_meA_perimetral.text
            H1_Muro_Eje_A['F34'] = self.root.ids.h1_meA_interior.text
            H1_Muro_Eje_A['J32'] = self.root.ids.h1_meA_sup_muro.text
            H1_Muro_Eje_A['P32'] = self.root.ids.h1_meA_sup_ven.text
            H1_Muro_Eje_A['G27'] = self.root.ids.h1_meA_tie_calef.text
            H1_Muro_Eje_A['G46'] = self.root.ids.total_sup_afec.text
            H1_Muro_Eje_A['O22'] = self.root.ids.manifestaciones.text
            H1_Muro_Eje_A['O24'] = self.root.ids.mod.text
            

            H1_Muro_Eje_A['K39'] = self.root.ids.sup_afe_esq_muro.text
            H1_Muro_Eje_A['K40'] = self.root.ids.sup_afe_cie_muro.text
            H1_Muro_Eje_A['K41'] = self.root.ids.sup_afe_pis_muro.text
            H1_Muro_Eje_A['K42'] = self.root.ids.sup_afe_ras_ven.text
            H1_Muro_Eje_A['K43'] = self.root.ids.sup_afe_baj_ven.text
            H1_Muro_Eje_A['K44'] = self.root.ids.sup_afe_ar_cen.text
            H1_Muro_Eje_A['K45'] = self.root.ids.sup_afe_pun_loc.text


            H1_Muro_Eje_A['Q39'] = self.root.ids.d_sup_afe_esq_muro.text
            H1_Muro_Eje_A['Q40'] = self.root.ids.d_sup_afe_cie_muro.text
            H1_Muro_Eje_A['Q41'] = self.root.ids.d_sup_afe_pis_muro.text
            H1_Muro_Eje_A['Q42'] = self.root.ids.d_sup_afe_ras_ven.text
            H1_Muro_Eje_A['Q43'] = self.root.ids.d_sup_afe_baj_ven.text
            H1_Muro_Eje_A['Q44'] = self.root.ids.d_sup_afe_ar_cen.text
            H1_Muro_Eje_A['Q45'] = self.root.ids.d_sup_afe_pun_loc.text

            

            H1_Muro_Eje_A['G22']=self.pat_vis
            H1_Muro_Eje_A['G24']=self.olor
            H1_Muro_Eje_A['M22']=self.manif
            H1_Muro_Eje_A['M24']=self.modif

            H1_Muro_Eje_A['G39']=self.en_esq_muro
            H1_Muro_Eje_A['G40']=self.en_cie_muro
            H1_Muro_Eje_A['G41']=self.en_pis_muro
            H1_Muro_Eje_A['G42']=self.ras_ven
            H1_Muro_Eje_A['G43']=self.baj_ven
            H1_Muro_Eje_A['G44']=self.ar_cen
            H1_Muro_Eje_A['G45']=self.pun_loc
            H1_Muro_Eje_A['M39']=self.d_en_esq_muro
            H1_Muro_Eje_A['M40']=self.d_en_cie_muro
            H1_Muro_Eje_A['M41']=self.d_en_pis_muro
            H1_Muro_Eje_A['M42']=self.d_ras_ven
            H1_Muro_Eje_A['M43']=self.d_baj_ven
            H1_Muro_Eje_A['M44']=self.d_ar_cen
            H1_Muro_Eje_A['M45']=self.d_pun_loc

            H1_Muro_Eje_A['G30']=self.aireador
            H1_Muro_Eje_A['I30']=self.extractor
            H1_Muro_Eje_A['K30']=self.campana
            H1_Muro_Eje_A['M30']=self.cel_pu
            H1_Muro_Eje_A['O30']=self.reb_pu
            H1_Muro_Eje_A['Q30']=self.otra_vent
            H1_Muro_Eje_A['G26']=self.calefaccion

            otro_cal_mea=self.root.ids.otro_cal.text
            H1_Muro_Eje_A['O26'] = otro_cal_mea

            if self.afectacion == "Nulo":
                H1_Muro_Eje_A['J34'] = "X"
            if self.afectacion == "Bajo":
                H1_Muro_Eje_A['L34'] = "X"
            if self.afectacion == "Medio":
                H1_Muro_Eje_A['N34'] = "X"
            if self.afectacion == "Alto":
                H1_Muro_Eje_A['P34'] = "X"
        

        if self.h1_mea==0:
            hoja_a_eliminar = libro["H1_Muro_Eje_A"]
            libro.remove(hoja_a_eliminar)
        




        #Guardar H1 Muro Eje 2
        if self.h1_me2==1:
            H1_Muro_Eje_2 = libro['H1_Muro_Eje_2']
            H1_Muro_Eje_2['C7'] = self.root.ids.nombre_habitacion1.text
            H1_Muro_Eje_2['F22'] = self.root.ids.h1_me2_m_perimetral.text
            H1_Muro_Eje_2['F23'] = self.root.ids.h1_me2_m_interior.text
            H1_Muro_Eje_2['J21'] = self.root.ids.h1_me2_sup_mur.text
            H1_Muro_Eje_2['P21'] = self.root.ids.h1_me2_sup_ven.text
            H1_Muro_Eje_2['G35'] = self.root.ids.total_sup_afec_h2.text

            #Superficie afectada
            H1_Muro_Eje_2['K28'] = self.root.ids.sup_afe_esq_muro_h2.text
            H1_Muro_Eje_2['K29'] = self.root.ids.sup_afe_cie_muro_h2.text
            H1_Muro_Eje_2['K30'] = self.root.ids.sup_afe_pis_muro_h2.text
            H1_Muro_Eje_2['K31'] = self.root.ids.sup_afe_ras_ven_h2.text
            H1_Muro_Eje_2['K32'] = self.root.ids.sup_afe_baj_ven_h2.text
            H1_Muro_Eje_2['K33'] = self.root.ids.sup_afe_ar_cen_h2.text
            H1_Muro_Eje_2['K34'] = self.root.ids.sup_afe_pun_loc_h2.text

            H1_Muro_Eje_2['Q28'] = self.root.ids.d_sup_afe_esq_muro_h2.text
            H1_Muro_Eje_2['Q29'] = self.root.ids.d_sup_afe_cie_muro_h2.text
            H1_Muro_Eje_2['Q30'] = self.root.ids.d_sup_afe_pis_muro_h2.text
            H1_Muro_Eje_2['Q31'] = self.root.ids.d_sup_afe_ras_ven_h2.text
            H1_Muro_Eje_2['Q32'] = self.root.ids.d_sup_afe_baj_ven_h2.text
            H1_Muro_Eje_2['Q33'] = self.root.ids.d_sup_afe_ar_cen_h2.text
            H1_Muro_Eje_2['Q34'] = self.root.ids.d_sup_afe_pun_loc_h2.text

            #Si o No
            H1_Muro_Eje_2['G28']=self.en_esq_muro_h2
            H1_Muro_Eje_2['G29']=self.en_cie_muro_h2
            H1_Muro_Eje_2['G30']=self.en_pis_muro_h2
            H1_Muro_Eje_2['G31']=self.ras_ven_h2
            H1_Muro_Eje_2['G32']=self.baj_ven_h2
            H1_Muro_Eje_2['G33']=self.ar_cen_h2
            H1_Muro_Eje_2['G34']=self.pun_loc_h2

            H1_Muro_Eje_2['M28']=self.d_en_esq_muro_h2
            H1_Muro_Eje_2['M29']=self.d_en_cie_muro_h2
            H1_Muro_Eje_2['M30']=self.d_en_pis_muro_h2
            H1_Muro_Eje_2['M31']=self.d_ras_ven_h2
            H1_Muro_Eje_2['M32']=self.d_baj_ven_h2
            H1_Muro_Eje_2['M33']=self.d_ar_cen_h2
            H1_Muro_Eje_2['M34']=self.d_pun_loc_h2

            #nivel de afectacion
            if self.h1_afectacion_h2 == "Nulo":
                H1_Muro_Eje_2['J23'] = "X"
            if self.h1_afectacion_h2 == "Bajo":
                H1_Muro_Eje_2['L23'] = "X"
            if self.h1_afectacion_h2 == "Medio":
                H1_Muro_Eje_2['N23'] = "X"
            if self.h1_afectacion_h2 == "Alto":
                H1_Muro_Eje_2['P23'] = "X"

        #Eliminar H1 Hoja2
        if self.h1_me2==0:
            hoja_a_eliminar = libro["H1_Muro_Eje_2"]
            libro.remove(hoja_a_eliminar)




        #Guardar H1 Muro Eje 3
        if self.h1_me3==1:
            H1_Muro_Eje_3 = libro['H1_Muro_Eje_3']
            H1_Muro_Eje_3['C7'] = self.root.ids.nombre_habitacion1.text
            H1_Muro_Eje_3['F22'] = self.root.ids.h1_me3_m_perimetral.text
            H1_Muro_Eje_3['F23'] = self.root.ids.h1_me3_m_interior.text
            H1_Muro_Eje_3['J21'] = self.root.ids.h1_me3_sup_mur.text
            H1_Muro_Eje_3['P21'] = self.root.ids.h1_me3_sup_ven.text
            H1_Muro_Eje_3['G35'] = self.root.ids.total_sup_afec_h3.text

            #Superficie afectada
            H1_Muro_Eje_3['K28'] = self.root.ids.sup_afe_esq_muro_h3.text
            H1_Muro_Eje_3['K29'] = self.root.ids.sup_afe_cie_muro_h3.text
            H1_Muro_Eje_3['K30'] = self.root.ids.sup_afe_pis_muro_h3.text
            H1_Muro_Eje_3['K31'] = self.root.ids.sup_afe_ras_ven_h3.text
            H1_Muro_Eje_3['K32'] = self.root.ids.sup_afe_baj_ven_h3.text
            H1_Muro_Eje_3['K33'] = self.root.ids.sup_afe_ar_cen_h3.text
            H1_Muro_Eje_3['K34'] = self.root.ids.sup_afe_pun_loc_h3.text

            H1_Muro_Eje_3['Q28'] = self.root.ids.d_sup_afe_esq_muro_h3.text
            H1_Muro_Eje_3['Q29'] = self.root.ids.d_sup_afe_cie_muro_h3.text
            H1_Muro_Eje_3['Q30'] = self.root.ids.d_sup_afe_pis_muro_h3.text
            H1_Muro_Eje_3['Q31'] = self.root.ids.d_sup_afe_ras_ven_h3.text
            H1_Muro_Eje_3['Q32'] = self.root.ids.d_sup_afe_baj_ven_h3.text
            H1_Muro_Eje_3['Q33'] = self.root.ids.d_sup_afe_ar_cen_h3.text
            H1_Muro_Eje_3['Q34'] = self.root.ids.d_sup_afe_pun_loc_h3.text

            #Si o No
            H1_Muro_Eje_3['G28']=self.en_esq_muro_h3
            H1_Muro_Eje_3['G29']=self.en_cie_muro_h3
            H1_Muro_Eje_3['G30']=self.en_pis_muro_h3
            H1_Muro_Eje_3['G31']=self.ras_ven_h3
            H1_Muro_Eje_3['G32']=self.baj_ven_h3
            H1_Muro_Eje_3['G33']=self.ar_cen_h3
            H1_Muro_Eje_3['G34']=self.pun_loc_h3

            H1_Muro_Eje_3['M28']=self.d_en_esq_muro_h3
            H1_Muro_Eje_3['M29']=self.d_en_cie_muro_h3
            H1_Muro_Eje_3['M30']=self.d_en_pis_muro_h3
            H1_Muro_Eje_3['M31']=self.d_ras_ven_h3
            H1_Muro_Eje_3['M32']=self.d_baj_ven_h3
            H1_Muro_Eje_3['M33']=self.d_ar_cen_h3
            H1_Muro_Eje_3['M34']=self.d_pun_loc_h3

            #nivel de afectacion
            if self.h1_afectacion_h3 == "Nulo":
                H1_Muro_Eje_3['J23'] = "X"
            if self.h1_afectacion_h3 == "Bajo":
                H1_Muro_Eje_3['L23'] = "X"
            if self.h1_afectacion_h3 == "Medio":
                H1_Muro_Eje_3['N23'] = "X"
            if self.h1_afectacion_h3 == "Alto":
                H1_Muro_Eje_3['P23'] = "X"



        #Eliminar H1 Hoja3
        if self.h1_me3==0:
            hoja_a_eliminar = libro["H1_Muro_Eje_3"]
            libro.remove(hoja_a_eliminar)




        #Guardar H1 Piso -Cielo
        if self.h1_pi_cie==1:
            H1_Piso_Cielo = libro['H1_Piso_Cielo']
            H1_Piso_Cielo['C7'] = self.root.ids.nombre_habitacion1.text
            H1_Piso_Cielo['J21'] = self.root.ids.H1_Sup_piso.text
            H1_Piso_Cielo['G31'] = self.root.ids.H1_total_sup_piso_afec.text
            H1_Piso_Cielo['J51'] = self.root.ids.H1_Sup_cielo.text
            H1_Piso_Cielo['G61'] = self.root.ids.H1_total_sup_cielo_afec.text

            H1_Piso_Cielo['G28'] = self.h1_per_piso_m
            H1_Piso_Cielo['G29'] = self.h1_ar_cen_piso_m
            H1_Piso_Cielo['G30'] = self.h1_pun_loc_piso_m
            H1_Piso_Cielo['M28'] = self.h1_per_piso_d
            H1_Piso_Cielo['M29'] = self.h1_ar_cen_piso_d
            H1_Piso_Cielo['M30'] = self.h1_pun_loc_piso_d
            H1_Piso_Cielo['K28'] = self.root.ids.h1_per_piso_sup_afe.text
            H1_Piso_Cielo['K29'] = self.root.ids.h1_ar_cen_piso_sup_afe.text
            H1_Piso_Cielo['K30'] = self.root.ids.h1_pun_loc_piso_sup_afe.text
            H1_Piso_Cielo['Q28'] = self.root.ids.h1_d_per_piso_sup_afe.text
            H1_Piso_Cielo['Q29'] = self.root.ids.h1_d_ar_cen_piso_sup_afe.text
            H1_Piso_Cielo['Q30'] = self.root.ids.h1_d_pun_loc_piso_sup_afe.text

            H1_Piso_Cielo['G58'] = self.h1_per_cielo_m
            H1_Piso_Cielo['G59'] = self.h1_ar_cen_cielo_m
            H1_Piso_Cielo['G60'] = self.h1_pun_loc_cielo_m
            H1_Piso_Cielo['M58'] = self.h1_per_cielo_d
            H1_Piso_Cielo['M59'] = self.h1_ar_cen_cielo_d
            H1_Piso_Cielo['M60'] = self.h1_pun_loc_cielo_d
            H1_Piso_Cielo['K58'] = self.root.ids.h1_per_cielo_sup_afe.text
            H1_Piso_Cielo['K59'] = self.root.ids.h1_ar_cen_cielo_sup_afe.text
            H1_Piso_Cielo['K60'] = self.root.ids.h1_pun_loc_cielo_sup_afe.text
            H1_Piso_Cielo['Q58'] = self.root.ids.h1_d_per_cielo_sup_afe.text
            H1_Piso_Cielo['Q59'] = self.root.ids.h1_d_ar_cen_cielo_sup_afe.text
            H1_Piso_Cielo['Q60'] = self.root.ids.h1_d_pun_loc_cielo_sup_afe.text

            if self.h1_piso_niv_afe == "Nulo":
                H1_Piso_Cielo['J23'] = "X"
            if self.h1_piso_niv_afe == "Bajo":
                H1_Piso_Cielo['L23'] = "X"
            if self.h1_piso_niv_afe == "Medio":
                H1_Piso_Cielo['N23'] = "X"
            if self.h1_piso_niv_afe == "Alto":
                H1_Piso_Cielo['P23'] = "X"

            if self.h1_cielo_niv_afe == "Nulo":
                H1_Piso_Cielo['J53'] = "X"
            if self.h1_cielo_niv_afe == "Bajo":
                H1_Piso_Cielo['L53'] = "X"
            if self.h1_cielo_niv_afe == "Medio":
                H1_Piso_Cielo['N53'] = "X"
            if self.h1_cielo_niv_afe == "Alto":
                H1_Piso_Cielo['P53'] = "X"

        if self.h1_pi_cie==0:
            hoja_a_eliminar = libro["H1_Piso_Cielo"]
            libro.remove(hoja_a_eliminar)
        
        libro.save(dir_nuevo_archivo)
















    


  #Flags
    h1_mea=0
    def asig_h1_mea(self):
        self.h1_mea=1

    h1_me2=0
    def asig_h1_me2(self):
        self.h1_me2=1

    h1_me3=0
    def asig_h1_me3(self):
        self.h1_me3=1

    h1_pi_cie=0
    def asig_h1_pi_cie(self):
        self.h1_pi_cie=1







    
if __name__ == '__main__':
    CitecUbbApp().run()