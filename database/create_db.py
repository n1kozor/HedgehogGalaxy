from database.models import *




# Diseases List to DB
def init_db_diseases():
    Diseases_list = ["Pilz", "Milben", "Abzesse", "Eitrige Stacheln", "Zahnstein", "Schnupfen",
                     "Lungenwürmer", "Lungenhaarwürmer", "Darmwürmer", "Darmsaugwurm", "Kokzidien",
                     "Bandwurm", "Bisse von Hunden", "Bisse von Mader",
                     "Befall von Fliegeneier", "Befall von Maden"]



    for diseases in Diseases_list:
        dis_list = Disease(name=diseases)
        session.add(dis_list)
        session.commit()
# Medic List to DB
def init_db_medics():
    medics_list = ["Schmerzmittel", "Antibiotika", "Entwurmung", "Vitamine", "Aufbaumittel"]



    for medics in medics_list:
        med_list = Medics(name=medics)
        session.add(med_list)
        session.commit()

# Create all tables by issuing CREATE TABLE commands to the DB.
Base.metadata.create_all(engine)


# Fill Tables with Medics and Diseases

# init_db_medics()
# init_db_diseases()