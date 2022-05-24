from model.modelos import Estudiantes
from fastapi import HTTPException
from loguru import logger

#Estudiantes=[]


def agregar_estudiante(estudiante):
    if estudiante.id_estudiante == 0:
        raise HTTPException(status_code=422,detail="No se puede almacenar un id_vacio")
    else:
        Estudiantes.append(estudiante.dict())

    return True


def mostrar_estudiante(id_estudiante:int):
    for estudiante in Estudiantes:
        if estudiante["id_estudiante"]== id_estudiante:
            logger.info("Estudiante: {}".format(estudiante))
            return estudiante


def mostrar_estudiantes():
    return Estudiantes

def actualizar_estudiante(actualiza,id_estudiante:int):
    for estudiante in Estudiantes:
        if estudiante["id_estudiante"]== id_estudiante:
            estudiante["primer_nombre"] = actualiza.primer_nombre
            estudiante["segundo_nombre"]= actualiza.segundo_nombre
            estudiante["apellido_paterno"]= actualiza.apellido_paterno
            estudiante["apellido_materno"]= actualiza.apellido_materno
            estudiante["edad"]= actualiza.edad
            logger.info("Estudiante Actualizadp")
            return estudiante
        else:
            raise HTTPException(status_code=422,detail="No se encontro un estudiante con ese ID")
        
def eliminar_estudiante(id_estudiante:int):
    for estudiante in Estudiantes:
        if estudiante["id_estudiante"] == id_estudiante:
            Estudiantes.remove(estudiante)
            mensaje="El estudiante {} fue eliminado correctamente".format(estudiante["primer_nombre"])
            return True,mensaje