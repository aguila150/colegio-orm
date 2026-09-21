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

 #print("Cuantos alumnos desaprobaron")

#resultados = session.query(Alumno, Calificacion).join(
 #   Calificacion, Alumno.id == Calificacion.alumno_id
#).filter(Calificacion.nota < 6).all()

#for alumno, calificacion in resultados:
 #   print(alumno.nombre, alumno.apellido, calificacion.nota)


#consulta con or_
#busqueda = session.query(Profesor) \
 #                 .filter((Profesor.activo == True) or
  #                        (Profesor.nombre =="Carlos")) \
        #         .all()
#print("\nProfesores Activos con nombre Carlos:")

#for n in busqueda:
 
 #   print(
  #         n.nombre,
   #      n.activo
    #)


#consulta con contains_
#nose = session.query(Alumno) \
 #                 .filter(Alumno.nombre.startswith("m")) \
  #               .all()

#print("\nAlumnos cuyo nombre contiene la letra 'm':")

#for z in nose:
#   print(z.nombre)


 
#.order_by() && .first_()
 choclo = session.query(Alumno, Calificacion).join(
    Calificacion, Alumno.id == Calificacion.alumno_id
).order_by(Calificacion.nota.desc()).first()

print("\n:nota mas alta")
alumno, calificacion = choclo
print(alumno.nombre,alumno.apellido, calificacion.nota)


#UPDATE
alumno = session.get(Alumno, 1)
alumno.anio_cursada = 2
session.commit()
print("Alumno actualizado correctamente")

#UPDATE con filter
profesor = session.query(Profesor).filter(
    Profesor.apellido == "Gomez"
).first()
profesor.activo = False
session.commit()
print("Profesor actualizado correctamente")

#DELETE
alumno = session.get(Alumno, 10)
session.delete(alumno)
session.commit()
print("Alumno eliminado correctamente")

#UPDATE masivo
session.query(Alumno).filter(
    Alumno.anio_cursada == 1
).update({
    Alumno.anio_cursada: 2
})
session.commit()
print("Actualización masiva realizada")

