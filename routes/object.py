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
        
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"object with code {code} not found")
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"object with code {code} not found")

'''CREATE object'''
@routerobject.post("/", response_description="Create a new object", status_code=status.HTTP_201_CREATED, response_model=object)
def create_object(request: Request,object = Body(...)):
    object = jsonable_encoder(object)

    new_object = db[collection].insert_one(object)
    created_object = db[collection].find_one(
        {"_id": new_object.inserted_id}
    )

    return created_object

'''DELETE object'''
@routerobject.delete("/{codigo}", response_description="Delete a object")
def delete_object(codigo:str, request: Request, response: Response):

    try:
        object_deleted = db[collection].delete_one({"codigo": codigo})
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"object with ID {codigo} not found")

    if object_deleted.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"object with ID {codigo} not found")


'''UPDATE object'''
@routerobject.put("/{codigo}", response_description="Update a object", response_model=object)
def update_object(codigo:str, request: Request, data: object = Body(...)):

    object = {k: v for k, v in data.dict().items() if v is not None}
    
    if len(object) >= 1:
        update_result = db[collection].update_one(
            {"codigo": codigo}, {"$set": object}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"object with ID {codigo} not modified")

    if (
        existing_object := db[collection].find_one({"codigo":codigo})
    ) is not None:
        return existing_object

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"object with ID {codigo} not found")