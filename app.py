from fastapi import *
from fastapi.staticfiles import StaticFiles
import weather_data

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(weather_data.router)
