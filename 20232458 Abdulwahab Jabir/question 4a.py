cubes_for_loop = []
for i in range(1, 11):
    cube = i ** 3
    print(f"The cube of {i} is: {cube}")
    cubes_for_loop.append(cube)

cubes_list_comprehension = [i ** 3 for i in range(1, 11)]

print("\nList of the first 10 cubes using list comprehension:")
print(cubes_list_comprehension)
