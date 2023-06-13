from typing import Optional,List
from pydantic import BaseModel,Field
from uuid import uuid4

class object(BaseModel):
    id: str = str(uuid4())
    codigo: str
    nombre: str
    descripcion: Optional[str]
    url_foto: Optional[str]
    path: Optional[str]

class texture(BaseModel):
    id: str = str(uuid4())
    codigo: str
    nombre: str
    descripcion: Optional[str]
    url_foto: Optional[str]