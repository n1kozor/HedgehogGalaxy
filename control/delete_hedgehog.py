from database.models import *
from database.methods import *
from loguru import logger

class DeleteHedgehog:
    @staticmethod
    def delete_hedgehog(ui, name=str):
        def delete_hedgehog_ui(self):
            name = ui.label_update_igel_name.text()
            igel = session.query(Igel).filter_by(name=name).first()
            session.delete(igel)
            session.commit()
            logger.debug(f"Ige mit Namen: {name} wurde erfolgreich gelöscht")
            ui.manage_pages.setCurrentIndex(1)
            ui.query_all_igel_to_list()

            ui.history_list.addItem(f"Igel: {name} wurde gelöscht")
        return delete_hedgehog_ui