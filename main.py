from fastapi import FastAPI, Request,Response,Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from config.database import Session, engine, Base
from models.user import User as UserModel
from pydantic import BaseModel, Field
from typing import Optional
from passlib_pass import encry, verify_encry

app = FastAPI()

Base.metadata.create_all(bind = engine)

template = Jinja2Templates(directory="./view")



@app.get("/", response_class=HTMLResponse)
def root(req:Request):
    return template.TemplateResponse("index.html", {"request":req})

@app.post("/user", response_class=HTMLResponse)
def session(req:Request, username: str = Form(),password_user: str = Form()):
    db = Session()
    result = db.query(UserModel).filter(UserModel.username == username).first()
    print(password_user)
    print(result.password)
    verify = verify_encry(password_user,result.password)
    if verify == True:
        return ("bienvenido")
    else:("usuario o cable incorrectos")

@app.get("/signup", response_class=HTMLResponse)
def signup(req: Request):
    return template.TemplateResponse("signup.html", {"request": req})


#se crea metodo para obtener los datos y enviarlos a la base de datos
@app.post("/signup")
def registro(req:Request):
    return template.TemplateResponse("signup.html", {"request": req})

 

@app.get("/user", response_class=HTMLResponse)
def user(req:Request):
    return template.TemplateResponse("user.html", {"request": req})




@app.post("/data-processing", response_class=HTMLResponse)
def data_processing(firstname:str = Form(), lastname: str = Form(), username: str = Form(), country:str = Form(),password_user: str = Form()):
    password = encry(password_user)
    print(password)
    new_user_data = {
        "firstname": firstname,
        "lastname": lastname,
        "username": username,
        "country": country,
        "password": password
    }
    new_user = UserModel(**new_user_data)
    db = Session()
    db.add(new_user)
    db.commit()
    print(new_user)
    return "save date"
