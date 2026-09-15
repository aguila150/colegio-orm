from sqlalchemy import Column, Integer, String, Boolean, create_engine, or_, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Session

# 1. Definimos la clase (una sola vez)
class Base(DeclarativeBase):
    pass

class Profesor(Base):
    __tablename__ = "Profesor"
    id = Column(Integer, primary_key=True)
    nombre    = Column(String)
    apellido = Column(String)
    email  = Column(Integer)
    activo=Column(Boolean)

class Materia(Base):
    __tablename__ = "Materia"
    id = Column(Integer, primary_key=True)
    nombre  = Column(String)
    anio = Column(Integer)
    profesor_id = Column(Integer, ForeignKey("Profesor.id"), nullable=True)

class Alumno(Base):
    __tablename__ = "Alumno"
    id = Column(Integer, primary_key=True)
    nombre  = Column(String)
    apellido = Column(String)
    dni = Column (Integer)
    anio_cursada = Column (DateTime)

class Calificacion(Base):
    __tablename__ = "Calificación"
    id = Column(Integer, primary_key=True)
    nota = Column(Integer)
    fecha = Column(DateTime)
    alumno_id = Column(Integer, ForeignKey("Alumno.id"), nullable=True)
    materia_id = Column(Integer, ForeignKey("Materia.id"), nullable=True)    

# 2. Consultamos como si fueran objetos Python
engine = create_engine("sqlite:///trabajo.db")
Base.metadata.create_all(engine)
