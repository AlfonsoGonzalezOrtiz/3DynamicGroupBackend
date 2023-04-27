from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
from config.db import db
from models.model import object
routerobject = APIRouter()

collection = "Object"

'''LIST objects'''
@routerobject.get("/",response_description="List all objects", response_model=List[object])
def list_objects(request: Request):
    objects = list(db[collection].find(limit=100))
    return objects
    
'''GET object'''
@routerobject.get("/{code}", response_description="Get a single object", response_model=object)
def get_object(code:str, request: Request):
    try:
        if(object := db[collection].find_one({"codigo": code})) is not None:
            return object
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"object with code {code} not found")

