import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

class Planeta(Base):
    __tablename__ = 'planeta' 
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    diameter=Column(Integer)
    population=Column(Integer)
    climate=Column(String(50))
    relacionpersonaje = relationship("Personaje")
    relacionvehiculo = relationship("Vehiculo")


class Personaje(Base):
    __tablename__ = 'personaje'
    uid = Column(Integer, primary_key=True)
    name = Column(String(50), nullable = False)
    homeworld = Column(String(50), ForeignKey('planeta.name'))
    

class Vehiculo(Base):
    __tablename__ = 'vehiculo' 
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    model= Column(String(50))
    vehicle_class=Column(String(50))
    length=Column(Integer)
    manufactura = Column(String(50), ForeignKey('planeta.name'))
    pilot_uid= Column(Integer,ForeignKey('personaje.uid'))
    relacionpersonaje_vehiculo = relationship("Personaje")
   
 
class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    apellido= Column(String(50), nullable=False)
    email= Column(String(50), nullable=False)
    password=Column(String(12),nullable=False)  

class Lista_favorito(Base):  
   __tablename__ = 'lista_favorito'
   id = Column(Integer, primary_key=True)
   id_usuario=Column(Integer,ForeignKey('usuario.id'))
   favorito_personaje=Column(Integer,ForeignKey('personaje.uid'))
   favorito_planeta=Column(Integer, ForeignKey('planeta.id'))
   favorito_vehiculo=Column(Integer, ForeignKey('vehiculo.id'))
   relacionusuario_listafav = relationship("Usuario")
   relacionpersonaje_listafav = relationship("Personaje")
   relacionplaneta_listafav = relationship("Planeta")
   relacionvehiculo_listafav = relationship("Vehiculo")
   
    
def to_dict(self):
    return {}


    



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')