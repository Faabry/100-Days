print("Welcome to the sum of a hundred")

total = 0
for n in range(0, 101):
    total += n

print(f"The sum of the numbers between 1 and 100 is {total}")
print()
print("The even numbers between 1 and 100 are:")
for n in range(2, 101, 2):
    print(f"{n}, ", end='')


