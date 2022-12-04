from database.models import *
from loguru import logger

class Diseases:
    @staticmethod
    def query_all_diseases(ui):
        def query_all_diseases_ui():
            disease_list = []
            m = session.query(Disease).all()
            for i in m:
                disease_list.append(i.name)
            for x in disease_list:
                ui.list_dieseases.addItem(x)

        return query_all_diseases_ui

    @staticmethod
    def delete_disease(ui):
        def delete_disease_ui():
            name = ui.list_diseases.currentItem().text()

            disease = session.query(Disease).filter_by(name=name).first()

            session.delete(disease)
            session.commit()

            logger.debug(f"Krankheit mit Namen: {name} wurde erfolgreich gelöscht")
            ui.history_list.addItem(f"Krankheit: {name} wurde gelöscht")
            ui.list_diseases.clear()
            ui.init_diseases_to_list()
            ui.label_disease_name.clear()
        return delete_disease_ui

    @staticmethod

    def add_new_disease(ui):
        def add_new_disease_ui():
            list = ui.list_diseases
            input = ui.in_new_disease_in_disease_page.text()
            list.addItem(input)
            new_disease = Disease(name=input)
            session.add(new_disease)
            session.commit()
            ui.history_list.addItem(f"Krankheit: {input} wurde zu Datenbank hinzugefügt")
            ui.list_diseases.clear()
            ui.init_diseases_to_list()
            ui.in_new_disease_in_disease_page.clear()
        return add_new_disease_ui

    @staticmethod
    def take_disease_name_to_label(ui):
        def take_disease_name_to_label_ui():
            disease_name = ui.list_dieseases.currentItem().text()
            ui.label_disease_name.setText(disease_name)
        return take_disease_name_to_label_ui

