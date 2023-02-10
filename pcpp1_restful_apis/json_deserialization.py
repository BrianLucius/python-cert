import json

jstr = '[1, 2.34, true, "False", null, ["a", 0]]'
my_list = json.loads(jstr)
print(type(my_list))
print(my_list)

json_str = '{"me":"Python","pi":3.141592653589, "data":[1,2,4,8],"friend":"JSON","set": null}'
my_dict = json.loads(json_str)
print(type(my_dict))
print(my_dict)

class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def encode_who(w):
    if isinstance(w, Who):
        return w.__dict__
    else:
        raise TypeError(w.__class__.__name__ + "is not JSON serializable")

def decode_who(w):
    return Who(w['name'], w['age'])

person = Who("Jane Doe", 23)
json_person = json.dumps(person, default=encode_who)
new_person = json.loads(json_person, object_hook=decode_who)
print(type(new_person))
print(new_person.__dict__)

class MyEncoder(json.JSONEncoder):
    def default(self, w):
        if isinstance(w, Who):
            return w.__dict__
        else:
            return super().default(self, z)


class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_who)

    def decode_who(self, d):
        return Who(**d)

another_person = Who("Alex Miller", 50)
json_another_person = json.dumps(another_person, cls=MyEncoder)
new_another_person = json.loads(json_another_person, cls=MyDecoder)
print(type(new_another_person))
print(new_another_person.__dict__)