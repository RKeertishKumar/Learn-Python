students = [
    {"name":"Harry","house":"Gryffindor", "patronus":"stag"},
    {"name":"Hermoine","house":"Gryffindor","patronus":"otter"},
    {"name":"Ron","house":"Gryffindor","patronus":"terrier"},
    {"name":"Draco", "house":"Gryffindor", "patronus":None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")