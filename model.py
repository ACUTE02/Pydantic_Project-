from pydantic import BaseModel, Field, field_validator, model_validator,computed_field, ConfigDict, EmailStr, AnyUrl
from typing import Optional, Literal
from datetime import date

class Category(BaseModel): #Pydantic Model # small class ko hum pydantic model bolte 
    name: Literal['starter','main course', 'desert', 'beverage']


class Model(BaseModel):
    #type conversion
    model_config=ConfigDict(
        #allow ,forbid,ignore
        extra="allow",
        frozen=True, #frozen model like tuple not chnage after create
        strict=True, # sometimes pydantic chang ethe data types like id->string then chnages to id->interger
        validate_assignment=True # "Whenever someone changes a field after the model has been created, validate the new value too."
        #email : EmailStr-> valid email
        #url   : AnyUrl  -> valid URL
        #date  : date    -> Valid date format  folllow

    )


    id            : int
    name          : str = Field(..., min_length=3, max_length=50, description="Item name")
    price         : float = Field(..., gt=0, description="Item price")
    category      : Category = Field(..., description="Item category")
    is_available  : bool = Field(default=True)
    description   : Optional[str] = None

#filed vaidator: one filed is required to give 

    @field_validator('name')
    @classmethod
    def title_name(cls,value): #value: Panner TIKKA ->Panner Tikka
        return value.title()

    @model_validator(mode="after")
    def check_avaivable(self):
        if self.is_available and self.price <=0:
            raise("avaiable item must have price greater than 0")
        return self
#COMPUTE FIELD
    @computed_field
    @property
    def price_tax(self)->float:
        return round(self.price*1.05,2)


'''Easy way to remember
field_validator → "Check one field."
model_validator(before) → "Clean the incoming data before Pydantic touches it."
model_validator(after) → "Check the finished model."
model_validator(wrap) → "Surround the entire validation process with custom logic."

For most applications, you'll use:

@field_validator for individual field validation.
@model_validator(mode="after") when validation depends on multiple fields.'''









item=Model(id=2,name="PANNER TIKKA",price=24,category=Category(name='main course'),spicy="boht spicyy hai ree")
# item = Model(
#     id=1,
#     name='Espresso',
#     price=20.98,
#     category=Category(name='main course')
# )
#1. model_dump() -> object ko convert kar dega dictionary
#This will only work inside Python

print('Dictionary model_dump()')
print(item.model_dump())


#2. model_dump_json() -> Object over the internet or the website, Out of Python

print('JSON model_dump_json()')
print(item.model_dump_json())


# print(item)
