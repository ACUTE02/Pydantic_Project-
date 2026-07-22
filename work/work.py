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
# @field_validator()





item=Model(id=1,name="panner tikka",price=120,category=Category(name='main course'),added_by_email="sdkl@gmail.com",date_added="2005-01-12")
print(item)