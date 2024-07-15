from fastapi import *
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import weather_data

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(weather_data.router)

@app.get("/county", include_in_schema=False)
async def default_county(request: Request):
	return FileResponse("./static/county.html", media_type="text/html")

@app.get("/county/{locationId}", include_in_schema=False)
async def county(request: Request, locationId: str):
	return FileResponse("./static/county.html", media_type="text/html")