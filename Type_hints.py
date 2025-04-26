
def get_fullname(firstname:str, lastname:str):
    full_name = firstname.title() + " " + lastname.title()
    return full_name

print(get_fullname("enes", "mulolli"))




def get_item(item1:str, item2:int, item3:float, item4:bool):
    return item1, item2, item3, item4
print(get_item("Item1", 2, 3.0, False))