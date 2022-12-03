from database.methods import *
from loguru import logger


class UpdateHedgehog:
    @staticmethod
    def update_hedgehog_profil(ui, name=str):
        def update_hedgehog_profil():
            try:
                """
                Update the Hedgehog
                """
                diseases = []
                name = ui.label_update_igel_name.text()
                igel = session.query(Igel).filter_by(name=name).first()
                """
                Krankheiten to History Hedgehog
                """
                for i in igel.diseases:
                    diseases.append(i.name)
                igel.sex = ui.in_update_igel_sex.text()
                igel.age = ui.in_update_igel_age.text()
                igel.description = ui.in_update_igel_description.text()
                igel.weight = ui.in_update_igel_weight.text()
                add_new_igel_to_history(name=igel.name, sex=igel.sex, age=igel.age,
                                        weight=igel.weight, description=igel.description, diseases=diseases)
                session.commit()
                ui.history_list.addItem(f"Igel: {name} wurde aktualisiert!")
            except:
                ui.history_list.addItem("Systemfehler!")

        return update_hedgehog_profil

    @staticmethod
    def add_medic_to_hedgehog(ui):
        def add_medic_to_hedgehog_ui():
            try:
                name = ui.label_24.text()
                selected = ui.list_add_medic_to_igel.currentItem().text()
                medic = session.query(Medics).filter_by(name=selected).first()

                take_medics(name=name, medicid=medic.id)
                ui.query_selected_igel_take_medics()
                ui.history_list.addItem(f"Igel: {name} hat {medic.name} genommen!")
                logger.debug(f"Igel: {name} hat {medic.name} genommen!")
            except:
                ui.history_list.addItem("Systemfehler!")

        return add_medic_to_hedgehog_ui

    @staticmethod
    def take_hedgehog_profil_to_update_page(ui):
        def take_hedgehog_profil_to_update_page_ui():
            name = ui.list_query_igel.currentItem().text()
            igel = session.query(Igel).filter_by(name=name).first()
            ui.label_update_igel_name.setText(igel.name)
            ui.in_update_igel_weight.setText(igel.weight)
            ui.in_update_igel_age.setText(igel.age)
            ui.in_update_igel_sex.setText(igel.sex)
            ui.in_update_igel_description.setText(igel.description)

        return take_hedgehog_profil_to_update_page_ui

    @staticmethod
    def show_hedgehog_profil(ui):
        def show_hedgehog_profil_ui():
            disease_list = []
            selected_igel = ui.list_query_igel.currentItem().text()
            s = session.query(Igel).filter_by(name=selected_igel).first()
            ui.label_query_profil_name.setText(s.name)
            ui.label_query_profil_sex.setText(s.sex)
            ui.label_query_profil_age.setText(s.age)
            ui.label_query_profil_weight.setText(s.weight)
            for i in s.diseases:
                disease_list.append(i.name)
            for x in disease_list:
                ui.list_query_profil_disease.addItem(x)
            ui.label_query_profil_description.setText(s.description)
        return show_hedgehog_profil_ui

    @staticmethod
    def query_selected_igel_to_list(ui):
        def query_selected_igel_to_list_ui():
            ui.list_query_igel.clear()
            name = ui.in_igel_query_filter.text()
            try:
                m = session.query(Igel).filter_by(name=name).first()
                ui.list_query_igel.addItem(m.name)
            except:
                ui.status_label.setText(f"Igel mit Name {name} wurde nicht in Datenbank gefunden!")

        return query_selected_igel_to_list_ui

