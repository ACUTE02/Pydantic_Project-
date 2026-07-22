from pydantic import BaseModel, Field, field_validator, model_validator,computed_field, ConfigDict, EmailStr, AnyUrl
from typing import Optional, Literal
from datetime import date

class Category(BaseModel):
    name:Literal["starter","main course","beverage","dessert","snacks"]

class Category(BaseModel):
    model_config=ConfigDict(
        extra='allow'
        frozen=True
        strict==True
        validate_assignment=True 
    )
    id             : int
    name           : str=Field(..., min_length=3, max_length=100, description="Item name")
    price          : int=Field(...,gt=0,description="Item Price")
    category       : str=Field(...,description="Item Category")
    is_available   : bool=Field(...,default=True)
    description    : Optional[str]=None
    added_by_email : EmailStr=Field(...,description="Email of the person")
    date_added     : date=Field(...,strict=False,)




item=work(id=1,name="panner tikka",price=120,category=Category(name='main course'),added_by_email=sdkl@gmail.com,date_added=12/1/2005)
print(item)