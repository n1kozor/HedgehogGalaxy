from PyQt5.QtWidgets import QMessageBox

from database.models import *


class NewHedgehog:
    @staticmethod
    def save_new_igel_ui(ui):
        def save_new_igel():
            name = ui.in_new_igel_name.text()
            sex = ui.in_new_igel_sex.currentText()
            age = ui.in_new_igel_age.text()
            weight = ui.in_new_igel_weight.text()
            description = ui.in_new_igel_description.text()
            disease = ui.list_new_disease_to_igel
            local = ui.in_new_igel_local.text()
            contacts = ui.in_new_igel_contact.text()
            status = ui.in_new_igel_status.currentText()
            s = bool(session.query(Igel).filter_by(name=name).first())
            if name == "":
                QMessageBox.about(ui, "Information", f"Name darf nicht leer bleiben")
            elif s is True:
                QMessageBox.about(ui, "Information", f"Igel mit Namen: {name} ist bereits im Datenbank!")

            else:
                new_igel = Igel(name=name, sex=sex, age=age, weight=weight, description=description, local=local,
                                contacts=contacts, status=status)

                itemsTextList = [str(disease.item(i).text()) for i in range(disease.count())]
                for u in itemsTextList:
                    krankhnt = session.query(Disease).filter_by(name=u).first()
                    new_igel.diseases.append(krankhnt)

                session.add(new_igel)
                session.commit()

                QMessageBox.about(ui, "Information", f"Igel mit Namen {name} wurde in Datenbank aufgenommen")

                # CLEAR ALL

                ui.in_new_igel_name.clear()
                ui.in_new_igel_sex.currentText()
                ui.in_new_igel_age.clear()
                ui.in_new_igel_weight.clear()
                ui.in_new_igel_description.clear()
                ui.list_new_disease_to_igel.clear()
                ui.in_new_igel_local.clear()
                ui.in_new_igel_contact.clear()
                ui.list_new_disease.clear()
                ui.init_disease()

        return save_new_igel

    @staticmethod
    def add_new_igel_disease(ui):
        def add_new_igel_disease_ui():
            lists = ui.list_new_disease
            inputs = ui.in_new_igel_disease.text()
            lists.addItem(inputs)
            new_disease = Disease(name=inputs)
            session.add(new_disease)
            session.commit()
            ui.history_list.addItem(f"Krankheit: {inputs} wurde zu Datenbank hinzugefügt")

        return add_new_igel_disease_ui
