
def add_to_list(x):
    list1=[{"name": "Nuraly", "last_name": "Aidarbek", "age": 5},
    {"name": "Askar", "last_name": "Paivich", "age": 10},
    {"name": "Nurs", "last_name": "Zhad", "age": 15}
    ]     
    list1.append(x)
    return list1
print(add_to_list({"name": "jonibek", "last_name": "senimovich", "age":30}))