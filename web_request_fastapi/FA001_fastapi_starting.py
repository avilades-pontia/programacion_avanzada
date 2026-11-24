from fastapi import FastAPI
import logging

logging.basicConfig(
    level=logging.WARNING, #DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="%(asctime)s - %(name)s - %(funcName)s - %(levelname)s  - %(message)s",
    #filename=
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Hello world con fastapi", 
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

@app.get("/data")
def devolvemos_datos():
    return{
        "teclados": 5,
        "ratones": 6,
    }

