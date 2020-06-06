zoo = ("tiger", "elephant", "beaver", "giraffe", "penguin",
       "monkey", "lion", "gorilla", "polar bear", "sloth")
zoo.index("penguin")

animal_to_find = "lion"
if animal_to_find in zoo:
    print(animal_to_find)

(first_child, second_child, third_child, fourth_child, fifth_child,
 sixth_child, seventh_child, eighth_child, ninth_child, tenth_child) = zoo
print(first_child)
print(second_child)
print(third_child)
print(fourth_child)
print(fifth_child)
print(sixth_child)
print(seventh_child)
print(eighth_child)
print(ninth_child)
print(tenth_child)

zooList = list(zoo)

moreAnimals = ["koala", "otter", "leopard"]

zooList.extend(moreAnimals)

extendedZoo = tuple(zooList)

print(extendedZoo)
