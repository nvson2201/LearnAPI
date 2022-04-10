# Import FastAPI
from fastapi import FastAPI
import api
import models
from database import SessionLocal, db_engine
# Initialize the app

models.Base.metadata.create_all(bind=db_engine)

app = FastAPI()

app.include_router(api.router)


# GET operation at route '/'


@app.get('/')
def root_api():
    return {"message": "Welcome to Balasundar's Technical Blog"}
