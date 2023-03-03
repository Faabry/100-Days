students_grade = {
    "Harry": 87,
    "Ron": 78,
    "Neville": 90,
    "Hermione": 99,
    "Draco": 85
}

for key in students_grade:
    score = students_grade[key]
    if score > 90:
        print(f"{key}: Outstanding")
    elif score > 80:
        print(f"{key}: Exceeds Expectations")
    elif score > 70:
        print(f"{key}: Acceptable")
    else:
        print(f"{key}: Fail")


# Nesting a dictionary inside a list 


