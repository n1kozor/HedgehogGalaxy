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


Session = sessionmaker(bind=engine)
session = Session()
