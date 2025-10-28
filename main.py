
from fastapi  import FastAPI
from core.database import  Base,engine
from api import user_routes,room_routes


Base.metadata.create_all(engine)

app = FastAPI(title="Appixo")

app.include_router(user_routes.router)
app.include_router(room_routes.router)