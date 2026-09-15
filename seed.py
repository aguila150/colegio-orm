from sqlalchemy import DateTime
from sqlalchemy.orm import Session 
from schema import Base, engine, Profesor, Materia, Alumno, Calificacion

#Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

with Session(engine) as session:
    
    profesores = [
        Profesor( nombre="Carlos", apellido="Gómez", email="cgomez@colegio.edu", activo=True),
        Profesor( nombre="Mariana", apellido="López", email="mlopez@colegio.edu", activo=True),
        Profesor( nombre="Roberto", apellido="Sánchez", email="rsanchez@colegio.edu", activo=False),
        Profesor( nombre="Elena", apellido="Fernández", email="efernandez@colegio.edu", activo=True),
        Profesor( nombre="Javier", apellido="Martínez", email="jmartinez@colegio.edu", activo=True),
        Profesor( nombre="Lucía", apellido="Díaz", email="ldiaz@colegio.edu", activo=False),
        Profesor( nombre="Gonzalo", apellido="Pérez", email="gperez@colegio.edu", activo=True),
        Profesor( nombre="Sofia", apellido="Romero", email="sromero@colegio.edu", activo=True),
        Profesor( nombre="Diego", apellido="Torres", email="dtorres@colegio.edu", activo=False),
        Profesor( nombre="Patricia", apellido="Ruiz", email="pruiz@colegio.edu", activo=True),
    ]

    
    materias = [
        Materia( nombre="Matemática I", anio=1, profesor_id=1),
        Materia( nombre="Historia I", anio=1, profesor_id=2),
        Materia( nombre="Física I", anio=2, profesor_id=1),
        Materia( nombre="Biología", anio=2, profesor_id=4),
        Materia( nombre="Lengua y Literatura", anio=1, profesor_id=5),
        Materia( nombre="Química", anio=3, profesor_id=7),
        Materia( nombre="Geografía", anio=2, profesor_id=8),
        Materia( nombre="Inglés Técnico", anio=3, profesor_id=10),
        Materia( nombre="Educación Física", anio=1, profesor_id=3),
        Materia( nombre="Informática", anio=3, profesor_id=5),
    ]

    
    alumnos = [
        Alumno( nombre="Mateo", apellido="Benítez", dni="44111222", anio_cursada=1),
        Alumno( nombre="Valentina", apellido="Alvarez", dni="44222333", anio_cursada=2),
        Alumno( nombre="Joaquín", apellido="Acosta", dni="43333444", anio_cursada=3),
        Alumno( nombre="Camila", apellido="Moreno", dni="43444555", anio_cursada=4),
        Alumno( nombre="Tomás", apellido="Rojas", dni="42555666", anio_cursada=5),
        Alumno( nombre="Mia", apellido="Mendoza", dni="42666777", anio_cursada=1),
        Alumno( nombre="Lucas", apellido="Castro", dni="44777888", anio_cursada=2),
        Alumno( nombre="Martina", apellido="Ortiz", dni="43888999", anio_cursada=3),
        Alumno( nombre="Santiago", apellido="Silva", dni="42999000", anio_cursada=4),
        Alumno( nombre="Delfina", apellido="Molina", dni="44000111", anio_cursada=5),
    ]

    
    calificaciones = [
        Calificacion( nota=8.50, fecha=DateTime, alumno_id=1, materia_id=1),
        Calificacion( nota=6.00, fecha=DateTime, alumno_id=2, materia_id=1),
        Calificacion( nota=9.50, fecha=DateTime, alumno_id=1, materia_id=2),
        Calificacion( nota=4.00, fecha=DateTime, alumno_id=3, materia_id=3),
        Calificacion( nota=7.00, fecha=DateTime, alumno_id=4, materia_id=4),
        Calificacion( nota=10.00, fecha=DateTime, alumno_id=5, materia_id=6),
        Calificacion( nota=5.50, fecha=DateTime, alumno_id=6, materia_id=8),
        Calificacion( nota=8.00, fecha=DateTime, alumno_id=7, materia_id=5),
        Calificacion( nota=3.50, fecha=DateTime, alumno_id=8, materia_id=7),
        Calificacion( nota=9.00, fecha=DateTime, alumno_id=9, materia_id=10),
    ]

    #session.add_all(profesores)


    session.add_all(alumnos)
    #session.flush()
    #session.add_all(alumnos)
    #session.flush()

    #session.add_all(calificaciones)
    session.commit()
    print("Datos insertados correctamente.")