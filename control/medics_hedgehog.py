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
