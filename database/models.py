from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Time, DateTime, PickleType, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker, joinedload
from sqlalchemy.sql import func
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

engine = create_engine('mysql://root:@localhost/hgalaxy')
#engine = create_engine('sqlite:///igels.db', echo=True)

Base = declarative_base()

disease_igel = Table(
    "disease_igel",
    Base.metadata,
    Column("igel_id", ForeignKey("igel.id")),
    Column("disease_id", ForeignKey("disease.id")),
)

medics_igel = Table(
    "medics_igel",
    Base.metadata,
    Column("igel_id", ForeignKey("igel.id")),
    Column("medics_id", ForeignKey("medics.id")),
    Column("take_time", DateTime(timezone=True), server_default=func.now())
)


class Igel(Base):
    __tablename__ = 'igel'

    id = Column(Integer, primary_key=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    time_igel_found = Column(DateTime)
    name = Column(String(255))
    sex = Column(String(255))
    age = Column(String(255))
    weight = Column(String(255))
    diseases = relationship("Disease", secondary=disease_igel, back_populates="igel")
    medics = relationship("Medics", secondary=medics_igel, back_populates="igel")
    diet = Column(String(255))
    contacts = Column(String(255))
    description = Column(String(255))



class IgelHistory(Base):
    __tablename__ = 'igel_history'

    id = Column(Integer, primary_key=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_igel_found = Column(DateTime)
    name = Column(String(255))
    sex = Column(String(255))
    age = Column(String(255))
    weight = Column(String(255))
    diseases = Column(PickleType)
    diet = Column(String(255))
    contacts = Column(String(255))
    description = Column(String(255))


class Disease(Base):
    __tablename__ = 'disease'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    igel = relationship("Igel", secondary=disease_igel, back_populates="diseases")

class Medics(Base):
    __tablename__ = 'medics'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))


    igel = relationship("Igel", secondary=medics_igel, back_populates="medics")

class MedicsIgelHistroy(Base):
    __tablename__ = 'medics_igel_history'

    id = Column(Integer, primary_key=True)
    igel_id = Column(Integer)
    medics_id = Column(Integer)
    take_time = Column(DateTime(timezone=True), server_default=func.now())


# Create all tables by issuing CREATE TABLE commands to the DB.
#Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


#session.query(Konten).filter_by(description="Sparkasse Sparkonto").first()

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






"""
igel = session.query(Igel).filter_by(name="Sonic").first()
igel_id = igel.id
take_time = session.query(MedicsIgelHistroy).order_by(MedicsIgelHistroy.igel_id).all()

medic_id_list= []
for k in take_time:
    medic_id_list.append(k.medics_id)



igel_name = session.query(Igel).filter_by(id=igel_id).first()

medic_list = []
for j in medic_id_list:
    medic_name = session.query(Medics).filter_by(id=j).first()
    medic_list.append(medic_name.name)

print(f"{igel.name} hat bis jetzt folgende Medikamenten eingenommen: {medic_list}")


"""

def init_db_diseases():
    Diseases_list = ["Pilz", "Milben", "Abzesse", "Eitrige Stacheln", "Zahnstein", "Schnupfen",
                     "Lungenwürmer", "Lungenhaarwürmer", "Darmwürmer", "Darmsaugwurm", "Kokzidien",
                     "Bandwurm", "Bisse von Hunden", "Bisse von Mader",
                     "Befall von Fliegeneier", "Befall von Maden"]



    for diseases in Diseases_list:
        dis_list = Disease(name=diseases)
        session.add(dis_list)
        session.commit()

def init_db_medics():
    medics_list = ["Schmerzmittel", "Antibiotika", "Entwurmung", "Vitamine", "Aufbaumittel"]



    for medics in medics_list:
        med_list = Medics(name=medics)
        session.add(med_list)
        session.commit()



# init_db_medics()
# init_db_diseases()

# medics_id_query = session.query(Medics).filter_by(id=1).all()
# for y in medics_id_query:
#     print(y.name)

# while True:
#     last_medics(name="Sün1")