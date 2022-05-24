from pydantic import BaseModel,Field
from typing import List

Estudiantes=[]


# Request -> Clases que se requieren
class EstudiantesRequest(BaseModel):
    id_estudiante:int=Field(title="Identificador del estudiante")
    primer_nombre:str=Field(title="Primer nombre del estudiante")
    segundo_nombre:str=Field(title="Segundo nombre del estudiante")
    apellido_paterno:str=Field(title="Primer apellido del estudiante")
    apellido_materno:str=Field(title="Segundo apellido del estudiante")
    edad:int=Field(title="Edad del estudiante")
    
# Response -> Clases que se muestra 
class EstudianteResponse(BaseModel):
    estudiante_guardado:bool

class EliminarEstudianteResponse(BaseModel):
    estudiante_eliminado:bool
    mensaje:str
    
    
    