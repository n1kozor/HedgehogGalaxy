import sys
from PyQt5 import QtWidgets, uic
from pprint import pprint
from database.models import *
from PyQt5.QtWidgets import *
from loguru import logger
def none():

    return None


class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('libary\hgalaxy.ui', self)
        """
                        Init Methoden ( Insert to lists etc.... )
        """
        self.query_all_krankheiten()
        self.query_all_medics()
        self.query_all_igel_to_list()
        self.query_all_igel_to_list_medics()
        self.btn_new_igel = self.findChild(QtWidgets.QPushButton, 'btn_new_igel')
        self.btn_new_igel.clicked.connect(self.show_new_igel_page)
        self.btn_query_igel = self.findChild(QtWidgets.QPushButton, 'btn_query_igel')
        self.btn_query_igel.clicked.connect(self.show_query_igel_page)
        self.btn_medics_igel = self.findChild(QtWidgets.QPushButton, 'btn_medics_igel')
        self.btn_medics_igel.clicked.connect(self.show_medics_igel_page)
        self.manage_pages = self.findChild(QtWidgets.QStackedWidget, "manage_pages")
        self.btn_new_save_igel = self.findChild(QtWidgets.QPushButton, 'btn_new_save_igel')
        self.btn_new_save_igel.clicked.connect(self.save_new_igel)
        """
                            Add New Igel
        """
        self.in_new_igel_time = self.findChild(QtWidgets.QDateEdit, "in_new_igel_time")
        self.in_new_igel_sex = self.findChild(QtWidgets.QComboBox, "in_new_igel_sex")
        self.in_new_igel_local = self.findChild(QtWidgets.QLineEdit, "in_new_igel_local")
        self.in_new_igel_name = self.findChild(QtWidgets.QLineEdit, "in_new_igel_name")
        self.in_new_igel_age = self.findChild(QtWidgets.QLineEdit, "in_new_igel_age")
        self.in_new_igel_disease = self.findChild(QtWidgets.QLineEdit, "in_new_igel_disease")
        self.in_new_igel_weight = self.findChild(QtWidgets.QLineEdit, "in_new_igel_weight")
        self.in_new_igel_description = self.findChild(QtWidgets.QLineEdit, "in_new_igel_description")
        self.btn_add_new_disease = self.findChild(QtWidgets.QPushButton, "btn_add_new_disease")
        self.btn_add_new_disease.clicked.connect(self.add_new_igel_disease)
        self.list_new_disease = self.findChild(QtWidgets.QListWidget, "list_new_disease")
        self.list_new_disease.itemDoubleClicked.connect(self.take_diseases_to_igel_diseases)
        self.list_new_disease_to_igel = self.findChild(QtWidgets.QListWidget, "list_new_disease_to_igel")
        self.list_new_disease_to_igel.itemDoubleClicked.connect(self.take_diseases_from_igel_to_diseases)
        self.btn_disease_to_igel = self.findChild(QtWidgets.QPushButton, "btn_disease_to_igel")
        self.btn_disease_to_igel.clicked.connect(self.take_diseases_to_igel_diseases)
        self.btn_igel_to_disease = self.findChild(QtWidgets.QPushButton, "btn_igel_to_disease")
        self.btn_igel_to_disease.clicked.connect(self.take_diseases_from_igel_to_diseases)
        """
                            Status ( right side, main Window ) itemDoubleClicked.connect
        """
        self.status_label = self.findChild(QtWidgets.QLabel, "label_status")
        """
                                    Igel Query Page
        """
        self.list_query_igel = self.findChild(QtWidgets.QListWidget, "list_query_igel")
        self.btn_query_all_igel = self.findChild(QtWidgets.QPushButton, "btn_query_all_igel")
        self.btn_query_all_igel.clicked.connect(self.query_all_igel_to_list)
        self.in_igel_query_filter = self.findChild(QtWidgets.QLineEdit, "in_igel_query_filter")
        self.btn_query_selected_igel = self.findChild(QtWidgets.QPushButton, "btn_query_selected_igel")
        self.btn_query_selected_igel.clicked.connect(self.query_selected_igel_to_list)
        self.label_query_profil_name = self.findChild(QtWidgets.QLabel, "profil_name")
        self.label_query_profil_sex = self.findChild(QtWidgets.QLabel, "profil_sex")
        self.label_query_profil_age = self.findChild(QtWidgets.QLabel, "profil_age")
        self.label_query_profil_weight = self.findChild(QtWidgets.QLabel, "profil_weight")
        self.list_query_profil_disease = self.findChild(QtWidgets.QListWidget, "profil_disease")
        self.label_query_profil_local = self.findChild(QtWidgets.QLabel, "profil_local")
        self.label_query_profil_description = self.findChild(QtWidgets.QLabel, "profil_description")
        self.btn_update_igel = self.findChild(QtWidgets.QPushButton, "btn_update_igel")
        self.btn_update_igel.clicked.connect(self.show_update_igel_page)

        """
                                    Igel Update Page
        """
        self.in_update_igel_weight = self.findChild(QtWidgets.QLineEdit, "in_update_igel_weight")
        self.in_update_igel_age = self.findChild(QtWidgets.QLineEdit, "in_update_igel_age")
        self.in_update_igel_sex = self.findChild(QtWidgets.QLineEdit, "in_update_igel_sex")
        self.in_update_igel_local = self.findChild(QtWidgets.QLineEdit, "in_update_igel_local")
        self.in_update_igel_description = self.findChild(QtWidgets.QLineEdit, "in_update_igel_description")
        self.label_update_igel_name = self.findChild(QtWidgets.QLabel, "label_update_igel_name")
        self.btn_save_update_igel = self.findChild(QtWidgets.QPushButton, "btn_save_update_igel")
        self.btn_save_update_igel.clicked.connect(self.update_igel_profil)

        self.btn_show_igel_profil = self.findChild(QtWidgets.QPushButton, "btn_show_igel_profil")
        self.btn_show_igel_profil.clicked.connect(self.show_igel_profil)
        self.btn_delete_igel = self.findChild(QtWidgets.QPushButton, "btn_delete_igel")
        self.btn_delete_igel.clicked.connect(self.delete_igel)

        """
                                    Igel Medics Page
        """
        self.list_query_igel_2 = self.findChild(QtWidgets.QListWidget, "list_query_igel_2")
        self.btn_query_all_igel_2 = self.findChild(QtWidgets.QPushButton, "btn_query_all_igel_2")
        self.btn_query_all_igel_2.clicked.connect(self.query_all_igel_to_list_medics)
        self.in_igel_query_filter_2 = self.findChild(QtWidgets.QLineEdit, "in_igel_query_filter_2")
        self.btn_query_selected_igel_2 = self.findChild(QtWidgets.QPushButton, "btn_query_selected_igel_2")
        self.btn_query_selected_igel_2.clicked.connect(self.query_selected_igel_to_list_medics)
        self.btn_query_medics_igel = self.findChild(QtWidgets.QPushButton, "btn_query_medics_igel")
        self.btn_query_medics_igel.clicked.connect(self.query_selected_igel_take_medics)
        self.table_medics_history = self.findChild(QtWidgets.QTableWidget, "table_medics_history")
        self.list_add_medic_to_igel = self.findChild(QtWidgets.QListWidget, "list_add_medic_to_igel")
        self.btn_add_medic_to_selected_igel = self.findChild(QtWidgets.QPushButton, "btn_add_medic_to_selected_igel")
        self.btn_add_medic_to_selected_igel.clicked.connect(self.add_medic_to_igel)

        self.show()
        logger.debug("Programm wurde erfolgreich initialisiert.")

    def add_new_igel_disease(self):
        list = self.list_new_disease
        input = self.in_new_igel_disease.text()
        list.addItem(input)

    def update_igel_profil(self):
        """
        Update the Hedgehog
        """
        diseases = []
        name = self.list_query_igel.currentItem().text()
        igel = session.query(Igel).filter_by(name=name).first()

        """
        Krankheiten to History Hedgehog
        """
        for i in igel.diseases:
            diseases.append(i.name)
        print(diseases)

        add_new_igel_to_history(name=igel.name, sex=igel.sex, age=igel.age,
                                weight=igel.weight, description=igel.description, diseases=diseases)

        igel.sex = self.in_update_igel_sex.text()
        igel.age = self.in_update_igel_age.text()
        igel.description = self.in_update_igel_description.text()
        igel.weight = self.in_update_igel_weight.text()
        session.commit()

        """
        Take Hedgehog To History Table ( Version )
        """

        print(igel.name)

    def take_igel_profil_to_update_page(self):
        name = self.list_query_igel.currentItem().text()
        igel = session.query(Igel).filter_by(name=name).first()
        self.label_update_igel_name.setText(igel.name)
        self.in_update_igel_weight.setText(igel.weight)
        self.in_update_igel_age.setText(igel.age)
        self.in_update_igel_sex.setText(igel.sex)
        self.in_update_igel_description.setText(igel.description)
        print(igel.weight)

    def show_igel_profil(self):
        disease_list = []
        selected_igel = self.list_query_igel.currentItem().text()
        s = session.query(Igel).filter_by(name=selected_igel).first()
        self.label_query_profil_name.setText(s.name)
        self.label_query_profil_sex.setText(s.sex)
        self.label_query_profil_age.setText(s.age)
        self.label_query_profil_weight.setText(s.weight)
        for i in s.diseases:
            disease_list.append(i.name)
        for x in disease_list:
            self.list_query_profil_disease.addItem(x)
        self.label_query_profil_description.setText(s.description)

    def query_all_igel_to_list_medics(self):
        self.list_query_igel_2.clear()
        m = session.query(Igel).all()
        for i in m:
            self.list_query_igel_2.addItem(i.name)

    def query_all_igel_to_list(self):
        self.list_query_igel.clear()
        m = session.query(Igel).all()
        for i in m:
            self.list_query_igel.addItem(i.name)

    def query_selected_igel_to_list(self):
        self.list_query_igel.clear()
        name = self.in_igel_query_filter.text()
        try:
            m = session.query(Igel).filter_by(name=name).first()
            self.list_query_igel.addItem(m.name)
        except:
            self.status_label.setText(f"Igel mit Name {name} wurde nicht in Datenbank gefunden!")

    def query_selected_igel_take_medics(self):
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
        except: print("fehler")

        # i = 0
        # for(k, v) in enumerate(res):
        #     med = QTableWidgetItem(k)
        #     date = QTableWidgetItem(str(v))
        #     table.setItem(i, 0, med)
        #     table.setItem(i, 1, date)
        #     #i += 1

        #pprint(res)

    def delete_igel(self):
        name = self.label_update_igel_name.text()
        print(name)
        igel = session.query(Igel).filter_by(name=name).first()
        session.delete(igel)
        session.commit()
        logger.debug(f"Ige mit Namen: {name} wurde erfolgreich gelöscht")
        self.manage_pages.setCurrentIndex(1)
        self.query_all_igel_to_list()

    def query_selected_igel_to_list_medics(self):
        self.list_query_igel_2.clear()
        name = self.in_igel_query_filter_2.text()
        try:
            m = session.query(Igel).filter_by(name=name).first()
            self.list_query_igel_2.addItem(m.name)
        except:
            self.status_label.setText(f"Igel mit Name {name} wurde nicht in Datenbank gefunden!")

    def show_query_igel_page(self):
        self.manage_pages.setCurrentIndex(1)
        self.query_all_igel_to_list()

    def show_update_igel_page(self):
        self.manage_pages.setCurrentIndex(2)
        self.take_igel_profil_to_update_page()
        self.query_all_igel_to_list()

    def show_medics_igel_page(self):
        self.manage_pages.setCurrentIndex(3)
        self.query_all_igel_to_list()

    def show_new_igel_page(self):
        self.manage_pages.setCurrentIndex(0)
        self.query_all_igel_to_list()

    def save_new_igel(self):
        name = self.in_new_igel_name.text()
        sex = self.in_new_igel_sex.currentText()
        age = self.in_new_igel_age.text()
        weight = self.in_new_igel_weight.text()
        description = self.in_new_igel_description.text()
        disease = self.list_new_disease_to_igel
        s = bool(session.query(Igel).filter_by(name=name).first())
        if s is True:
            self.label_status.setText(f"Igel mit Namen {name} ist bereits in Datenbank")

        else:
            new_igel = Igel(name=name, sex=sex, age=age, weight=weight, description=description)
            itemsTextList = [str(disease.item(i).text()) for i in range(disease.count())]
            for u in itemsTextList:
                krankhnt = session.query(Disease).filter_by(name=u).first()
                new_igel.diseases.append(krankhnt)

            session.add(new_igel)
            session.commit()
            self.label_status.setText(f"Igel mit Namen {name} wurde in Datenbank aufgenommen")

    def query_all_krankheiten(self):
        disease_list = []
        m = session.query(Disease).all()
        for i in m:
            disease_list.append(i.name)
        for x in disease_list:
            self.list_new_disease.addItem(x)

    def query_all_medics(self):
        medics_list = []
        m = session.query(Medics).all()
        for i in m:
            medics_list.append(i.name)
        for x in medics_list:
            self.list_add_medic_to_igel.addItem(x)

    def save_new_disease(self):
        var = None

    def take_diseases_to_igel_diseases(self):
        index = self.list_new_disease.currentRow()
        disease_list = self.list_new_disease.currentItem()
        try:
            self.list_new_disease.takeItem(index)
            self.list_new_disease_to_igel.addItem(disease_list.text())
        except:
            pass

    def take_diseases_from_igel_to_diseases(self):
        index = self.list_new_disease_to_igel.currentRow()
        disease_list = self.list_new_disease_to_igel.currentItem()
        try:
            self.list_new_disease_to_igel.takeItem(index)
            self.list_new_disease.addItem(disease_list.text())
        except:
            pass

    def add_medic_to_igel(self):
        try:
            name = self.label_24.text()
            selected = self.list_add_medic_to_igel.currentItem().text()
            medic = session.query(Medics).filter_by(name=selected).first()

            take_medics(name=name, medicid=medic.id)
            self.query_selected_igel_take_medics()
        except: print("fehler")

logger.add("hedgehoggalaxy.log", retention="10 days")
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
