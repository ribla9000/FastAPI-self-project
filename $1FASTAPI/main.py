from fastapi import FastAPI
from db.base import *
from endpoints import users, auth, models, statuses
import uvicorn


app = FastAPI(title='Kolya')
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(models.router, prefix="/models", tags=["models"])
app.include_router(statuses.router, prefix="/statuses", tags=["statuses"])

@app.on_event('startup')
async def startup():
	await database.connect()


@app.on_event('shutdown')
async def shutdown():
	await database.disconnect()

if __name__ == "__main__":
	uvicorn.run("main:app", port=8001, host='0.0.0.0', reload=True)
