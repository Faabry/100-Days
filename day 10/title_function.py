def title_function(f_name, l_name):
    name1 = f_name.title()
    name2 = l_name.title()
    complete_name = f"{name1} {name2}"
    return complete_name


name = str(input("First name: \n>>>"))
last_name = str(input("Last name: \n>>>"))

output = title_function(name, last_name)
print(output)