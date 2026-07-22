import json

from pydantic import BaseModel, Field, field_validator, model_validator,computed_field, ConfigDict, EmailStr, AnyUrl
from typing import Optional, Literal
from datetime import date

class Category(BaseModel):
    name:Literal["starter","main course","beverage","dessert","snacks"]

class Model(BaseModel):
    model_config=ConfigDict(
        extra="allow",
        frozen=True,
        strict=True,
        validate_assignment=True 
    )
    id             : int
    name           : str=Field(..., min_length=3, max_length=100, description="Item name")
    price          : int=Field(...,gt=0,description="Item Price")
    category       : Category = Field(..., description="Item category")
    is_available   : bool=Field(default=True)
    description    : Optional[str]=None
    added_by_email : EmailStr=Field(...,description="Email of the person")
    date_added     : date=Field(...,strict=False,)

    #Field Validator
    @field_validator('category',mode='before')
    @classmethod
    def wrap_category_string(cls,value):
        if isinstance(value,str):
            return {"name":value}
        return value

    @field_validator('name')
    @classmethod
    def title_name(cls,value):
        return value.title()

    @computed_field
    @property
    def price_round(self)->float:
        return round(self.price*1.05,2)


if __name__=='__main__':
    item = Model(
        id=2,
        name="Chole Kulche",
        price=180,
        category="main course",
        added_by_email="chef.manual@spicehouse.com",
        date_added="2025-04-01",
        spicy="Bohot tezz",
    )
print("dictionary model_dump")
print(item.model_dump())
print()
print("JSON format")
print(item.model_dump_json())
import json

from pydantic import BaseModel, Field, field_validator, model_validator,computed_field, ConfigDict, EmailStr, AnyUrl
from typing import Optional, Literal
from datetime import date

class Category(BaseModel):
    name:Literal["starter","main course","beverage","dessert","snacks"]

class Model(BaseModel):
    model_config=ConfigDict(
        extra="allow",
        frozen=True,
        strict=True,
        validate_assignment=True 
    )
    id             : int
    name           : str=Field(..., min_length=3, max_length=100, description="Item name")
    price          : int=Field(...,gt=0,description="Item Price")
    category       : Category = Field(..., description="Item category")
    is_available   : bool=Field(default=True)
    description    : Optional[str]=None
    added_by_email : EmailStr=Field(...,description="Email of the person")
    date_added     : date=Field(...,strict=False,)

    #Field Validator
    @field_validator('category',mode='before')
    @classmethod
    def wrap_category_string(cls,value):
        if isinstance(value,str):
            return {"name":value}
        return value

    @field_validator('name')
    @classmethod
    def title_name(cls,value):
        return value.title()

    @computed_field
    @property
    def price_round(self)->float:
        return round(self.price*1.05,2)


if __name__=='__main__':
    item = Model(
        id=2,
        name="Chole Kulche",
        price=180,
        category="main course",
        added_by_email="chef.manual@spicehouse.com",
        date_added="2025-04-01",
        spicy="Bohot tezz",
    )
print("dictionary model_dump")
print(item.model_dump())
print()
print("JSON format")
print(item.model_dump_json())
