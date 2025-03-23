#!/usr/bin/python3
from models.base_model import BaseModel

# Create a new instance of BaseModel
my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
print(my_model.to_dict())

# Save the instance
my_model.save()

# Reload objects from storage
from models import storage
all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id, obj in all_objs.items():
    print(obj)#!/usr/bin/python3
from models.base_model import BaseModel

# Create a new instance of BaseModel
my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
print(my_model.to_dict())

# Save the instance
my_model.save()

# Reload objects from storage
from models import storage
all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id, obj in all_objs.items():
    print(obj)