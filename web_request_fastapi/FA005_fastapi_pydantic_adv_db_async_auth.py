import logging
import time
from typing import Optional

from fastapi import FastAPI, HTTPException, BackgroundTasks

# from pydantic import BaseModel
from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator
# EmailStr: Validates that the provided string is a valid email address. needs to be imported from pydantic and installed with 'pydantic[email]' 

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker




logging.basicConfig(
    level=logging.INFO, #DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="%(asctime)s - %(name)s - %(funcName)s - %(levelname)s  - %(message)s",
    #filename=
)

# DB SETUP
DATABASE_URL = "sqlite:///./users.db"  # SQLite database URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Clase de SQLAlchemy para la tabla de usuarios
class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    age = Column(Integer)

Base.metadata.create_all(bind=engine)


# clase de Pydantic para la validacion de datos de entrada
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

def enviar_email(email: str, username: str):
    time.sleep(25)  # Simulate a delay in sending the email
    logger.info(f"Sent email to {email} for user {username}")

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
def create_user(user: User, background_tasks: BackgroundTasks):
    logger.info(f"Creating user: {user.username}, email: {user.email}, age: {user.age}")

    db = SessionLocal()
    # existing_user = db.query(UserDB).filter((UserDB.username == user.username) | (UserDB.email == user.email)).first()
    existing_email = db.query(UserDB).filter(UserDB.email == user.email).first()
    if existing_email:
        db.close()
        return {"message": "User with this email already exists."}

    db_user = UserDB(
        username=user.username,
        email=user.email,
        age=user.age
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    
    logger.info(f"User {user.username} created successfully in the database.")
    logger.info(f"Scheduling email to be sent to {user.email} for user {user.username}.")
    background_tasks.add_task(enviar_email, user.email, user.username)

    return {
        "message": f"User {user.username} created successfully", 
        "user": user
        }