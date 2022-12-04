import time

from control.new_hedgehog import NewHedgehog
import sys
from PyQt5 import QtWidgets, uic
from pprint import pprint
from database.models import *
from PyQt5.QtWidgets import *
from loguru import logger
from database.methods import *
from database.create_db import *
from control.new_hedgehog import NewHedgehog
from control.init_methods import InitMethods
from control.update_hedgehog import UpdateHedgehog
from control.delete_hedgehog import DeleteHedgehog
from control.medics_hedgehog import MedicsHedgehog
from control.diseases import Diseases

class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('libary\hgalaxy.ui', self)
        self.manage_pages.setCurrentIndex(2)
        """
                        Init Methods ( Insert to lists etc.... )
        """
        self.init_disease = InitMethods.query_all_diseases(self)
        self.init_disease()  # Init all diseases to lists

        self.init_medics = InitMethods.query_all_medics(self)
        self.init_medics()  # Init all medics to lists

        self.init_hedgehog_list = InitMethods.query_all_hedgehog_to_list(self)
        self.init_hedgehog_list()  # Init all hedgehog to list

        self.init_hedgehog_list_to_medic_list = MedicsHedgehog.query_all_hedgehog_to_list_medics(self)
        self.init_hedgehog_list_to_medic_list()  # Init all hedgehog to list in medics page

        self.init_diseases_to_list = Diseases.query_all_diseases(self)
        self.init_diseases_to_list()
        self.init_list = self.findChild(QtWidgets.QListWidget, "init_list")
        self.btn_new_igel = self.findChild(QtWidgets.QPushButton, 'btn_new_igel')
        self.btn_new_igel.clicked.connect(InitMethods.show_new_hedgehog_page(self))
        self.btn_query_igel = self.findChild(QtWidgets.QPushButton, 'btn_query_igel')
        self.btn_query_igel.clicked.connect(InitMethods.show_query_hedgehog_page(self))
        self.btn_medics_igel = self.findChild(QtWidgets.QPushButton, 'btn_medics_igel')
        self.btn_medics_igel.clicked.connect(InitMethods.show_medics_hedgehog_page(self))
        self.manage_pages = self.findChild(QtWidgets.QStackedWidget, "manage_pages")
        self.btn_new_save_igel = self.findChild(QtWidgets.QPushButton, 'btn_new_save_igel')
        self.btn_new_save_igel.clicked.connect(NewHedgehog.save_new_igel_ui(self))
        """
                            Add New Igel
        """
        self.in_new_igel_time = self.findChild(QtWidgets.QDateEdit, "in_new_igel_time")
        self.in_new_igel_contact = self.findChild(QtWidgets.QLineEdit, "in_new_igel_contact")
        self.in_new_igel_local = self.findChild(QtWidgets.QLineEdit, "in_new_igel_local")
        self.in_new_igel_sex = self.findChild(QtWidgets.QComboBox, "in_new_igel_sex")
        self.in_new_igel_name = self.findChild(QtWidgets.QLineEdit, "in_new_igel_name")
        self.in_new_igel_age = self.findChild(QtWidgets.QLineEdit, "in_new_igel_age")
        self.in_new_igel_disease = self.findChild(QtWidgets.QLineEdit, "in_new_igel_disease")
        self.in_new_igel_weight = self.findChild(QtWidgets.QLineEdit, "in_new_igel_weight")
        self.in_new_igel_description = self.findChild(QtWidgets.QLineEdit, "in_new_igel_description")
        self.btn_add_new_disease = self.findChild(QtWidgets.QPushButton, "btn_add_new_disease")
        self.btn_add_new_disease.clicked.connect(NewHedgehog.add_new_igel_disease(self))
        self.list_new_disease = self.findChild(QtWidgets.QListWidget, "list_new_disease")
        self.list_new_disease.itemDoubleClicked.connect(InitMethods.take_diseases_to_igel_diseases(self))
        self.list_new_disease_to_igel = self.findChild(QtWidgets.QListWidget, "list_new_disease_to_igel")
        self.list_new_disease_to_igel.itemDoubleClicked.connect(InitMethods.take_diseases_from_igel_to_diseases(self))
        self.btn_disease_to_igel = self.findChild(QtWidgets.QPushButton, "btn_disease_to_igel")
        self.btn_disease_to_igel.clicked.connect(InitMethods.take_diseases_to_igel_diseases(self))
        self.btn_igel_to_disease = self.findChild(QtWidgets.QPushButton, "btn_igel_to_disease")
        self.btn_igel_to_disease.clicked.connect(InitMethods.take_diseases_from_igel_to_diseases(self))
        self.in_new_igel_status = self.findChild(QtWidgets.QComboBox, "in_new_igel_status")

        """
                            Status ( right side, main Window ) itemDoubleClicked.connect
        """
        self.status_label = self.findChild(QtWidgets.QLabel, "label_status")
        """
                                    Igel Query Page
        """
        self.list_query_igel = self.findChild(QtWidgets.QListWidget, "list_query_igel")
        self.list_query_igel.clicked.connect(UpdateHedgehog.show_hedgehog_profil(self))
        self.btn_query_all_igel = self.findChild(QtWidgets.QPushButton, "btn_query_all_igel")
        self.btn_query_all_igel.clicked.connect(InitMethods.query_all_hedgehog_to_list(self))
        self.in_igel_query_filter = self.findChild(QtWidgets.QLineEdit, "in_igel_query_filter")
        self.label_query_profil_name = self.findChild(QtWidgets.QLabel, "profil_name")
        self.label_query_profil_sex = self.findChild(QtWidgets.QLabel, "profil_sex")
        self.label_query_profil_age = self.findChild(QtWidgets.QLabel, "profil_age")
        self.label_query_profil_weight = self.findChild(QtWidgets.QLabel, "profil_weight")
        self.list_query_profil_disease = self.findChild(QtWidgets.QListWidget, "profil_disease")
        self.label_query_profil_local = self.findChild(QtWidgets.QLabel, "profil_local")
        self.label_query_profil_contacts = self.findChild(QtWidgets.QLabel, "profil_contact")
        self.label_query_profil_description = self.findChild(QtWidgets.QLabel, "profil_description")
        self.btn_update_igel = self.findChild(QtWidgets.QPushButton, "btn_update_igel")
        self.btn_update_igel.clicked.connect(InitMethods.show_update_hedgehog_page(self))
        self.label_igel_status = self.findChild(QtWidgets.QLabel, "label_igel_status")

        """
                                    Igel Update Page
        """
        self.in_update_igel_weight = self.findChild(QtWidgets.QLineEdit, "in_update_igel_weight")
        self.in_update_igel_age = self.findChild(QtWidgets.QLineEdit, "in_update_igel_age")
        self.in_update_igel_sex = self.findChild(QtWidgets.QLineEdit, "in_update_igel_sex")
        self.in_update_igel_local = self.findChild(QtWidgets.QLineEdit, "in_update_igel_local")
        self.in_update_igel_description = self.findChild(QtWidgets.QLineEdit, "in_update_igel_description")
        self.in_update_igel_contact = self.findChild(QtWidgets.QLineEdit, "in_update_igel_contact")
        self.label_update_igel_name = self.findChild(QtWidgets.QLabel, "label_update_igel_name")
        self.btn_save_update_igel = self.findChild(QtWidgets.QPushButton, "btn_save_update_igel")
        self.btn_save_update_igel.clicked.connect(UpdateHedgehog.update_hedgehog_profil(self))
        self.btn_delete_igel = self.findChild(QtWidgets.QPushButton, "btn_delete_igel")
        self.btn_delete_igel.clicked.connect(DeleteHedgehog.delete_hedgehog(self))
        self.list_update_diseases = self.findChild(QtWidgets.QListWidget, "list_update_diseases")
        self.in_update_igel_status = self.findChild(QtWidgets.QComboBox, "in_update_igel_status")
        """
                                    Igel Medics Page
        """
        self.list_query_igel_2 = self.findChild(QtWidgets.QListWidget, "list_query_igel_2")
        self.list_query_igel_2.clicked.connect(self.query_selected_igel_take_medics)
        self.btn_query_all_igel_2 = self.findChild(QtWidgets.QPushButton, "btn_query_all_igel_2")
        self.btn_query_all_igel_2.clicked.connect(MedicsHedgehog.query_all_hedgehog_to_list_medics(self))
        self.in_igel_query_filter_2 = self.findChild(QtWidgets.QLineEdit, "in_igel_query_filter_2")
        self.btn_query_selected_igel_2 = self.findChild(QtWidgets.QPushButton, "btn_query_selected_igel_2")
        self.btn_query_selected_igel_2.clicked.connect(MedicsHedgehog.query_selected_hedgehog_to_list_medics(self))
        self.btn_query_medics_igel = self.findChild(QtWidgets.QPushButton, "btn_query_medics_igel")
        self.table_medics_history = self.findChild(QtWidgets.QTableWidget, "table_medics_history")
        self.list_add_medic_to_igel = self.findChild(QtWidgets.QListWidget, "list_add_medic_to_igel")
        self.btn_add_medic_to_selected_igel = self.findChild(QtWidgets.QPushButton, "btn_add_medic_to_selected_igel")
        self.btn_add_medic_to_selected_igel.clicked.connect(UpdateHedgehog.add_medic_to_hedgehog(self))

        """
                                    Status / History List LENT
        """

        self.history_list = self.findChild(QtWidgets.QListWidget, "history_list")
        self.history_list.setSelectionRectVisible(True)
        """
                                            Diseases
        """
        self.btn_diseases_igel = self.findChild(QtWidgets.QPushButton, "btn_diseases_igel")
        self.btn_diseases_igel.clicked.connect(InitMethods.show_diseases_hedgehog_page(self))
        self.btn_delete_disease = self.findChild(QtWidgets.QPushButton, "btn_delete_disease")
        self.btn_delete_disease.clicked.connect(Diseases.delete_disease(self))
        self.list_diseases = self.findChild(QtWidgets.QListWidget, "list_dieseases")
        self.list_diseases.clicked.connect(Diseases.take_disease_name_to_label(self))
        self.in_new_disease_in_disease_page = self.findChild(QtWidgets.QLineEdit, "in_new_disease_in_disease_page")
        self.btn_add_new_disease_in_disease_page = self.findChild(QtWidgets.QPushButton, "btn_add_new_disease_in_disease_page")
        self.btn_add_new_disease_in_disease_page.clicked.connect(Diseases.add_new_disease(self))
        self.label_disease_name = self.findChild(QtWidgets.QLabel, "label_28")




        """
                                        Administrator
        """

        self.btn_admin_create_db = self.findChild(QtWidgets.QPushButton, "btn_admin_create_db")
        self.btn_admin_create_db.clicked.connect(admin_db_init)
        self.show()
        self.setFixedSize(1379, 765)
        logger.debug("Programm wurde erfolgreich initialisiert.")
        self.init_list.addItem("Datenbank wird kontrolliert....")
        self.init_list.addItem("Anwendung wird initalisiert....")
        self.init_list.addItem("Keine Fehler gefunden!")



    def query_selected_igel_take_medics(self):
        self.list_add_medic_to_igel.setEnabled(True)
        self.table_medics_history.setEnabled(True)
        self.btn_add_medic_to_selected_igel.setEnabled(True)
        try:
            table = self.table_medics_history

            label = self.findChild(QtWidgets.QLabel, "label_24")
            name = self.list_query_igel_2.currentItem().text()
            igel = session.query(Igel).filter_by(name=name).first()
            medics_ids = session.query(MedicsIgelHistroy).filter_by(igel_id=igel.id).all()
            medic_take_time_list = []
            medic_list = []
            for c in medics_ids:
                medic_list.append(c.medics_id)
                medic_take_time_list.append(str(c.take_time))
            medic_name_list = []
            for j in medic_list:
                medics_id_query = session.query(Medics).filter_by(id=int(j)).all()
                for y in medics_id_query:
                    medic_name_list.append(y.name)

            table.setRowCount(len(medic_name_list))
            table.setColumnCount(2)
            table.setHorizontalHeaderLabels(["Medikamente", "Datum"])
            medic_take_time_list.reverse()
            medic_name_list.reverse()
            i = 0
            for name in medic_name_list:
                item_name = QTableWidgetItem(name)
                table.setItem(i, 0, item_name)

                i += 1
            d = 0
            for date in medic_take_time_list:
                item_date = QTableWidgetItem(str(date))
                table.setItem(d, 1, item_date)

                d += 1

            label.setText(igel.name)

        except:
            print("fehler")


    def save_new_disease(self):
        var = None

    def none(self):

        return None






logger.add("hedgehoggalaxy.log", retention="10 days")
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()

