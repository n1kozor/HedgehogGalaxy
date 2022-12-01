from database.models import *



def add_new_igel(name=str, sex=str, age=str, weight=str, description=str):
    new_igel = Igel(name=name, sex=sex, age=age, weight=weight, description=description)
    s = bool(session.query(Igel).filter_by(name=name).first())
    if s is not True:
        session.add(new_igel)
        session.commit()

        return False
    else:

        return True

def add_new_igel_to_history(name=str, sex=str, age=str, weight=str, description=str, diseases=str):
    new_igel = IgelHistory(name=name, sex=sex, age=age, weight=weight, description=description, diseases=diseases)
    session.add(new_igel)
    session.commit()


def add_new_disease(name=str):
    new_disease = Disease(name=name)
    s = bool(session.query(Disease).filter_by(name=name).first())
    if s is not True:
        session.add(new_disease)
        session.commit()

        return False
    else:

        return True

#
def take_medics(name=str, medicid=int):
    try:
        igel = session.query(Igel).filter_by(name=name).first()
        medics = session.query(Medics).filter_by(id=medicid).first()
        session.commit()
        new_medics_take = MedicsIgelHistroy(igel_id=igel.id, medics_id=medics.id)
        session.add(new_medics_take)
        session.commit()

    except: print("Fehler in Parameter")


