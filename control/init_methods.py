from PyQt5.QtWidgets import QMessageBox

from control.medics_hedgehog import *
from control.update_hedgehog import UpdateHedgehog


class InitMethods:
    @staticmethod
    def query_all_diseases(ui):
        def query_all_diseases_ui():
            disease_list = []
            m = session.query(Disease).all()
            for i in m:
                disease_list.append(i.name)
            for x in disease_list:
                ui.list_new_disease.addItem(x)

        return query_all_diseases_ui

    @staticmethod
    def query_all_medics(ui):
        def query_all_medics_ui():
            medics_list = []
            m = session.query(Medics).all()
            for i in m:
                medics_list.append(i.name)
            for x in medics_list:
                ui.list_add_medic_to_igel.addItem(x)

        return query_all_medics_ui

    @staticmethod
    def query_all_medics_to_medics_page(ui):
        def query_all_medics_to_medics_page_ui():
            medics_list = []
            m = session.query(Medics).all()
            for i in m:
                medics_list.append(i.name)
                print(i)
            for x in medics_list:
                ui.list_medics_new.addItem(x)
                print(x)

        return query_all_medics_to_medics_page_ui

    @staticmethod
    def query_all_hedgehog_to_list(ui):
        def query_all_hedgehog_to_list_ui():
            ui.list_query_igel.clear()
            m = session.query(Igel).all()
            for i in m:
                ui.list_query_igel.addItem(i.name)

        return query_all_hedgehog_to_list_ui

    @staticmethod
    def show_new_hedgehog_page(ui):
        def show_new_hedgehog_page_ui():
            ui.manage_pages.setCurrentIndex(0)
            ui.init_hedgehog_list()
            ui.list_new_disease.clear()
            ui.init_disease()

        return show_new_hedgehog_page_ui

    @staticmethod
    def show_medics_hedgehog_page(ui):
        def show_medics_hedgehog_page():
            ui.manage_pages.setCurrentIndex(4)
            ui.init_hedgehog_list_to_medic_list()
            ui.list_add_medic_to_igel.setDisabled(True)
            ui.table_medics_history.setDisabled(True)
            ui.btn_add_medic_to_selected_igel.setDisabled(True)
            ui.list_add_medic_to_igel.clear()
            ui.init_medics()

        return show_medics_hedgehog_page

    @staticmethod
    def show_update_hedgehog_page(ui):
        def show_update_hedgehog_page_ui():
            try:
                ui.list_update_diseases.clear()
                take = UpdateHedgehog.take_hedgehog_profil_to_update_page(ui)
                take()
                query = InitMethods.query_all_hedgehog_to_list(ui)
                query()
                ui.manage_pages.setCurrentIndex(3)

            except:
                QMessageBox.about(ui, "Warnung", "Kein Igel ausgewählt. Sie müssen ein Igel auswählen, um sein Profil "
                                                 "anzuzeigen!")

        return show_update_hedgehog_page_ui

    @staticmethod
    def show_query_hedgehog_page(ui):
        def show_query_hedgehog_page_ui():
            ui.manage_pages.setCurrentIndex(1)
            ui.label_query_profil_description.clear()
            ui.label_query_profil_name.clear()
            ui.label_query_profil_age.clear()
            ui.label_query_profil_local.clear()
            ui.label_igel_status.clear()
            ui.label_igel_status.setStyleSheet("color: white; background-color: transparent")
            ui.label_query_profil_sex.clear()
            ui.label_query_profil_weight.clear()
            ui.list_query_profil_disease.clear()
            ui.list_query_igel.clear()
            ui.label_query_profil_contacts.clear()
            m = session.query(Igel).all()
            for i in m:
                ui.list_query_igel.addItem(i.name)

        return show_query_hedgehog_page_ui

    @staticmethod
    def show_diseases_hedgehog_page(ui):
        def show_diseases_hedgehog_page_ui():
            ui.list_diseases.clear()
            ui.manage_pages.setCurrentIndex(5)
            ui.init_diseases_to_list()

        return show_diseases_hedgehog_page_ui

    @staticmethod
    def show_medics_hedgehog_page_add_new(ui):
        def show_medics_hedgehog_page_add_new_ui():
            ui.list_medics_new.clear()
            ui.manage_pages.setCurrentIndex(6)
            ui.init_medics_to_medics_page()

        return show_medics_hedgehog_page_add_new_ui

    @staticmethod
    def take_diseases_to_igel_diseases(ui):
        def take_diseases_to_igel_diseases_ui():
            index = ui.list_new_disease.currentRow()
            disease_list = ui.list_new_disease.currentItem()
            try:
                ui.list_new_disease.takeItem(index)
                ui.list_new_disease_to_igel.addItem(disease_list.text())
            except:
                pass

        return take_diseases_to_igel_diseases_ui

    @staticmethod
    def take_diseases_from_igel_to_diseases(ui):
        def take_diseases_from_igel_to_diseases_ui():
            index = ui.list_new_disease_to_igel.currentRow()
            disease_list = ui.list_new_disease_to_igel.currentItem()
            try:
                ui.list_new_disease_to_igel.takeItem(index)
                ui.list_new_disease.addItem(disease_list.text())
            except:
                pass

        return take_diseases_from_igel_to_diseases_ui
