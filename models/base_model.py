from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.now();

    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now();

    def to_dict(self):
        serialized = dict(self.__dict__)
        serialized["__class__"] = type(self).__name__
        serialized["created_at"] = serialized["created_at"].isoformat()
        serialized["updated_at"] = serialized["updated_at"].isoformat()
        return serialized

if __name__ == "__main__":
    instance_base_model =  BaseModel()
    other_base_model =  BaseModel()

    if type(instance_base_model) is BaseModel:
        print("[OK] it's an instance of BaseModel")
    else:
        print("[FAIL] it's not an instance of BaseModel")

    if instance_base_model.id != other_base_model.id:
        print("[OK] it's not the same id")
    else:
        print("[FAIL] equals id")

    if type(instance_base_model.id) is type(""):
        print("[OK] id string success")
    else:
        print("[FAIL] id isn't a string")

    if type(instance_base_model.created_at) is datetime:
        print("[OK] created_at it is datetime type, the value is", instance_base_model.created_at)
    else:
        print("[FAIL] created_at isn't datetime type")

    if type(instance_base_model.updated_at) is datetime:
        print("[OK] updated_at it is datetime type, the value is", instance_base_model.created_at)
    else:
        print("[FAIL] updated_at isn't datetime type")

    print("[ok]", other_base_model)

    previous_update = instance_base_model.updated_at
    instance_base_model.save();
    if previous_update != instance_base_model.updated_at:
        print("[OK] a new instance as update")
    else:
        print("[FAIL] it's the same instance update")

    if type(instance_base_model.to_dict()) is dict:
        print("[OK] it's a dictionary")
        if type(instance_base_model.to_dict()["updated_at"]) is str:
            print("[OK] updated_at it's a string")
        else:
            print("[FAIL] updated_at isn't a string")
        # TODO validate the formart
    else:
        print("[FAIL] isn't a dictionary")


