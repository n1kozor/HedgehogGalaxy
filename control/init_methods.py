from database.models import *
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
            InitMethods.query_all_hedgehog_to_list(ui)

        return show_new_hedgehog_page_ui

    @staticmethod
    def show_medics_hedgehog_page(ui):
        def show_medics_hedgehog_page():
            ui.manage_pages.setCurrentIndex(3)
            InitMethods.query_all_hedgehog_to_list(ui)

        return show_medics_hedgehog_page

    @staticmethod
    def show_update_hedgehog_page(ui):
        def show_update_hedgehog_page_ui():
            ui.manage_pages.setCurrentIndex(2)
            take = UpdateHedgehog.take_hedgehog_profil_to_update_page(ui)
            take()
            query = InitMethods.query_all_hedgehog_to_list(ui)
            query()
        return show_update_hedgehog_page_ui
