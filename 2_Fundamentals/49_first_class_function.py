operations = {
    "average": lambda seq: sum(seq)  / len(seq),
    "total": sum,
    "top": max
}

students = [
    {"name": "John", "grade": (67, 34, 45, 21)},
    {"name": "Jane", "grade": (67, 34, 94, 55)},
    {"name": "Mary", "grade": (67, 34, 84,22)},
    {"name": "Mike", "grade": (67, 34, 53, 43)},
]

for student in students:
    name = student["name"]
    grades = student["grade"]
    
    print(f"Student: {name}")
    operation = input("Enter 'average', 'total', 'top' : ")
    
    operation_function = operations[operation]
    print(operation_function(grades))