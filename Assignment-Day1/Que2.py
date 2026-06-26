list = [int(x) for x in input('Enter list elements: ').split()]

def calculate(list, choice = 1):
    if choice == 1:
        return sum(list)
    elif choice == 2:
        product = 1
        for n in list:
            product *= n
        return product
    


print("Default = ", calculate(list))
print("Sum = ", calculate(list, 1))
print("Product = ", calculate(list, 2))