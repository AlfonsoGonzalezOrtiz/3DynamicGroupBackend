from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
from config.db import db
from models.model import texture
routertexture = APIRouter()

collection = "Texture"

'''LIST textures'''
@routertexture.get("/",response_description="List all textures", response_model=List[texture])
def list_textures(request: Request):
    textures = list(db[collection].find(limit=100))
    return textures
    
'''GET texture'''
@routertexture.get("/{code}", response_description="Get a single texture", response_model=texture)
def get_texture(code:str, request: Request):
    try:
        if(texture := db[collection].find_one({"codigo": code})) is not None:
            return texture
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"texture with code {code} not found")
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"texture with code {code} not found")

'''CREATE texture'''
@routertexture.post("/", response_description="Create a new texture", status_code=status.HTTP_201_CREATED, response_model=texture)
def create_texture(request: Request,texture = Body(...)):
    texture = jsonable_encoder(texture)

    new_texture = db[collection].insert_one(texture)
    created_texture = db[collection].find_one(
        {"_id": new_texture.inserted_id}
    )

    return created_texture

'''DELETE texture'''
@routertexture.delete("/{codigo}", response_description="Delete a texture")
def delete_texture(codigo:str, request: Request, response: Response):

    try:
        texture_deleted = db[collection].delete_one({"codigo": codigo})
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"texture with ID {codigo} not found")

    if texture_deleted.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"texture with ID {codigo} not found")


'''UPDATE texture'''
@routertexture.put("/{codigo}", response_description="Update a texture", response_model=texture)
def update_texture(codigo:str, request: Request, data: texture = Body(...)):

    texture = {k: v for k, v in data.dict().items() if v is not None}
    
    if len(texture) >= 1:
        update_result = db[collection].update_one(
            {"codigo": codigo}, {"$set": texture}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"texture with ID {codigo} not modified")

    if (
        existing_texture := db[collection].find_one({"codigo":codigo})
    ) is not None:
        return existing_texture

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"texture with ID {codigo} not found")