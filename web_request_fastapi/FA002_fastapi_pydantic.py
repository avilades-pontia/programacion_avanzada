from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import logging

logging.basicConfig(
    level=logging.INFO, #DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="%(asctime)s - %(name)s - %(funcName)s - %(levelname)s  - %(message)s",
    #filename=
)

class User(BaseModel):
    username: str
    email: str
    age: Optional[int] = None

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Fastapi con validacion de datos con pydantic", 
    description="API testing",
    version= "1.0.1",
    docs_url="/doc", 
    
)

@app.get("/")
def initial_greeting():
    return {"messge": "FastAPI Hello"}

@app.get("/hello/{name}")
def cutom_greeting(name:str):
    logger.info(f"Greeting request for {name}")
    processed_name = name.capitalize()
    logger.info(f"Capitalize name : {processed_name}")
    if processed_name == "Alvaro":
        #configuramos el logger para que muestre todos los niveles de log, segun lo que tengamos configurado en el basicConfig  pintara
        logger.debug(f"Mister {processed_name} is visiting our web")
        logger.info(f"Mister {processed_name} is visiting our web")
        logger.warning(f"Mister {processed_name} is visiting our web")
        logger.error(f"Mister {processed_name} is visiting our web")
        logger.critical(f"Mister {processed_name} is visiting our web")
        return {"message": f"Mister {processed_name} is visiting our web"}
    return {"message": f"FastAPI Hello {processed_name}"}

@app.post("/users/")
def create_user(user: User):
    logger.info(f"Creating user: {user.username}, email: {user.email}, age: {user.age}")
    return {
        "message": f"User {user.username} created successfully", 
        "user": user
        }