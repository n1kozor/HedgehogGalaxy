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
            s = bool(session.query(Igel).filter_by(name=name).first())
            if s is True:
                ui.label_status.setText(f"Igel mit Namen {name} ist bereits in Datenbank")

            else:
                new_igel = Igel(name=name, sex=sex, age=age, weight=weight, description=description)
                itemsTextList = [str(disease.item(i).text()) for i in range(disease.count())]
                for u in itemsTextList:
                    krankhnt = session.query(Disease).filter_by(name=u).first()
                    new_igel.diseases.append(krankhnt)

                session.add(new_igel)
                session.commit()
                ui.label_status.setText(f"Igel mit Namen {name} wurde in Datenbank aufgenommen")
        return save_new_igel
    @staticmethod
    def add_new_igel_disease(ui, list=list, input=str):
        def add_new_igel_disease_ui():
            list = ui.list_new_disease
            input = ui.in_new_igel_disease.text()
            list.addItem(input)
        return add_new_igel_disease_ui
