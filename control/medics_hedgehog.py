from database.models import *


class MedicsHedgehog:
    @staticmethod
    def query_all_hedgehog_to_list_medics(ui):
        def query_all_hedgehog_to_list_medics_ui():
            ui.list_query_igel_2.clear()
            m = session.query(Igel).all()
            for i in m:
                ui.list_query_igel_2.addItem(i.name)

        return query_all_hedgehog_to_list_medics_ui

    @staticmethod
    def query_selected_hedgehog_to_list_medics(ui):
        def query_selected_hedgehog_to_list_medics_ui():
            ui.list_query_igel_2.clear()
            name = ui.in_igel_query_filter_2.text()
            try:
                m = session.query(Igel).filter_by(name=name).first()
                ui.list_query_igel_2.addItem(m.name)
            except:
                ui.status_label.setText(f"Igel mit Name {name} wurde nicht in Datenbank gefunden!")

        return query_selected_hedgehog_to_list_medics_ui

    @staticmethod
    def delete_medics_in_medics_page(ui):
        def delete_medics_in_medics_page_ui():
            name = ui.list_medics_new.currentItem().text()
            medic = session.query(Medics).filter_by(name=name).first()

            session.delete(medic)
            session.commit()
            listItems = ui.list_medics_new.selectedItems()
            if not listItems: return
            for item in listItems:
                ui.list_medics_new.takeItem(ui.list_medics_new.row(item))

        return delete_medics_in_medics_page_ui

    @staticmethod

    def add_new_medic_in_medic_page(ui):
        def add_new_medic_in_medic_page_ui():
            list = ui.list_medics_new
            input = ui.in_new_medics_in_medics_page.text()
            list.addItem(input)
            new_medic = Medics(name=input)
            session.add(new_medic)
            session.commit()
            ui.history_list.addItem(f"Medikament: {input} wurde zu Datenbank hinzugefügt")
            ui.list_medics_new.clear()
            ui.init_medics_to_medics_page()
        return add_new_medic_in_medic_page_ui
