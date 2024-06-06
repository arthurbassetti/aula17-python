from pydantic import BaseModel, PositiveFloat, EmailStr, field_validator, Field
from enum import Enum
from datetime import datetime
from typing import Optional


class CategoriaBase(Enum):
    categoria1 = "Eletrônico"
    categoria2 = "Eletrodoméstico"
    categoria3 = "Móveis"
    categoria4 = "Roupas"
    categoria5 = "Calçados"


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: PositiveFloat
    categoria: str
    email_fornecedor: EmailStr

class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[PositiveFloat] = None
    categoria: Optional[str] = None
    email_fornecedor: Optional[EmailStr] = None
