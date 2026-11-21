from fastapi import FastAPI
import logging

logging.basicConfig(
    level=logging.INFO, #DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
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
        logger.warning(f"Mister {processed_name} is visiting our web")
    return {f"FastAPI Hello {processed_name}"}

@app.get("/data")
def devolvemos_datos():
    return{
        "teclados": 5,
        "ratones": 6,
    }

