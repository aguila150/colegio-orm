from sqlalchemy import or_
from sqlalchemy.orm import Session
from schema import engine, Profesor, Materia, Alumno, Calificacion

with Session(engine) as session:
#1 filtracion
# print("Alumnos de 2 año")

 #alumnos = session.query(Alumno).filter(
  #      Alumno.anio_cursada == 2
   # ).all()

 #for alumno in alumnos:
  #      print(alumno.nombre, alumno.apellido)

#2 filtracion

 #print("Cuantos alumnos aprobaron 7")

 #alumnos = session.query(Calificacion).filter(
  #          Calificacion.nota >7 
   # ).all()

 #for n in alumnos:
  #      print(n.nota)
#3 filtracion

 print("Cuantos alumnos desaprobaron")

resultados = session.query(Alumno, Calificacion).join(
    Calificacion, Alumno.id == Calificacion.alumno_id
).filter(Calificacion.nota < 6).all()

for alumno, calificacion in resultados:
    print(alumno.nombre, alumno.apellido, calificacion.nota)