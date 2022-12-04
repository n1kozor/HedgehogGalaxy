from database.models import *
from database.methods import *
from loguru import logger



class DeleteHedgehog:
    @staticmethod
    def delete_hedgehog(ui):
        def delete_hedgehog_ui():

            name = ui.label_update_igel_name.text()

            igel = session.query(Igel).filter_by(name=name).first()

            session.delete(igel)
            session.commit()

            logger.debug(f"Ige mit Namen: {name} wurde erfolgreich gelöscht")
            ui.label_query_profil_description.clear()
            ui.label_query_profil_name.clear()
            ui.label_query_profil_age.clear()
            ui.label_query_profil_local.clear()
            ui.label_query_profil_sex.clear()
            ui.label_query_profil_weight.clear()
            ui.list_query_profil_disease.clear()
            ui.list_query_igel.clear()
            ui.list_query_igel.clear()
            m = session.query(Igel).all()
            for i in m:
                ui.list_query_igel.addItem(i.name)
            ui.manage_pages.setCurrentIndex(1)


            ui.history_list.addItem(f"Igel: {name} wurde gelöscht")

        return delete_hedgehog_ui



