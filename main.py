from fastapi import FastAPI
from app.api.posts.routes import router as RouterPost
from app.api.users.routes import router as RouterUser
from app.api.gtrack.routes import router as RouterGtrack
from app.core.database import connect_database, disconnect_database

# Función para crear la aplicación FastAPI
def create_app():
    app = FastAPI(
        title="CLR Fast Api",
        description="This is a simple CRUD API with FastAPI",
        version="1.0",
        docs_url="/docs",
        # redoc_url=None,
        # openapi_url=None
    )
    
    # Registrando los routers
    app.include_router(router=RouterPost, prefix="/api")
    app.include_router(router=RouterUser, prefix="/api")
    app.include_router(router=RouterGtrack, prefix="/api")
    
    return app

# Crear la aplicación FastAPI
app = create_app()

# # Configuración de eventos de ciclo de vida de la aplicación
# @app.on_event("startup")
# def startup_event():
#     connect_database()  # Configurar conexión a la base de datos

# @app.on_event("shutdown")
# def shutdown_event(database_connection):
#     disconnect_database(db=database_connection)  # Cerrar conexión a la base de datos

# Punto de entrada para ejecutar la aplicación con Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app=app, host="0.0.0.0", port=8000, reload=True)
