from fastapi import APIRouter
from services import funciones as servicio
from model.modelos import EstudianteResponse,EstudiantesRequest,EliminarEstudianteResponse

#Aqui van a ir todas las rutas 
router=APIRouter()

@router.post("/agregar-estudiantes/",response_model=EstudianteResponse)
async def agregar_estudiante(estudiante:EstudiantesRequest):
     
    estudiante_guardado=servicio.agregar_estudiante(estudiante)
    
    return EstudianteResponse(
        estudiante_guardado=estudiante_guardado
    )
@router.get("/mostrar-todos-los-estudiantes/")
async def mostrar_todos_los_estudiantes():
    
    Estudiantes=servicio.mostrar_estudiantes()
    return Estudiantes

@router.get("/mostrar-estudiante/{id_estudiante}/",response_model=EstudiantesRequest)
async def mostrar_estudiante(id_estudiante:int):
    
    estudiante=servicio.mostrar_estudiante(id_estudiante)
    
    
    return EstudiantesRequest(
        id_estudiante=estudiante["id_estudiante"],
        primer_nombre=estudiante["primer_nombre"],
        segundo_nombre=estudiante["segundo_nombre"],
        apellido_paterno=estudiante["apellido_paterno"],
        apellido_materno=estudiante["apellido_materno"],
        edad=estudiante["edad"],
    )
    
@router.put("/actualizar-estudiantes/{id_estudiante}",response_model=EstudiantesRequest)
async def actualizar_estudiante(id_estudiante:int,actualiza:EstudiantesRequest):
    
    estudiante_actualizado=servicio.actualizar_estudiante(actualiza,id_estudiante)
    
    return EstudiantesRequest(
        id_estudiante=estudiante_actualizado["id_estudiante"],
        primer_nombre=estudiante_actualizado["primer_nombre"],
        segundo_nombre=estudiante_actualizado["segundo_nombre"],
        apellido_paterno=estudiante_actualizado["apellido_paterno"],
        apellido_materno=estudiante_actualizado["apellido_materno"],
        edad=estudiante_actualizado["edad"],
    )
    
@router.delete("/eliminar-estudiante/{id_estudiante}",response_model=EliminarEstudianteResponse)
async def eliminar_estudiante(id_estudiante:int):
    
    estudiante_eliminado,mensaje=servicio.eliminar_estudiante(id_estudiante)
    
    return EliminarEstudianteResponse(
        estudiante_eliminado=estudiante_eliminado,
        mensaje=mensaje
    )    


