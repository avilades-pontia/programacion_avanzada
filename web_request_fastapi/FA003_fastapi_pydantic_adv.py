from fastapi import FastAPI
# from pydantic import BaseModel
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator
import logging

# EmailStr: Validates that the provided string is a valid email address. needs to be imported from pydantic and installed with 'pydantic[email]' 

logging.basicConfig(
    level=logging.INFO, #DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="%(asctime)s - %(name)s - %(funcName)s - %(levelname)s  - %(message)s",
    #filename=
)

# class User(BaseModel):
#     username: str
#     email: str
#     age: Optional[int] = None

class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="The username of the user")
    email: EmailStr = Field(..., description="The email address of the user")
    age: Optional[int] = Field(None, ge=0, description="The age of the user")
    #age: Optional[int] = Field(None, ge=0, le=120, description="The age of the user")

    # validacion avanzada de datos con pydantic, para el email, si no contiene @, lanzamos un error
    # @field_validator("email")
    # def validate_email(cls, value):
    #     if "@" not in value:
    #         raise ValueError("Invalid email address")
    #     return value
    
    @model_validator(mode="before")
    def validate_age(cls, values):
        age = values.get("age")
        if age is not None and (age < 0 or age > 120):
            raise ValueError("Age must be an integer between 0 and 120")
        return values

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Fastapi con validacion avanzada de datos con pydantic", 
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