

def add(a, b):
    """
    Take two numbers as input and return their sum
    """
    return int(a) + int(b)


def multiplication_table(number):
    print(f"Multiplication table for: {number}")
    for count in range(1, 11):
        print(f"{int(number)} x {count} = {int(number)*count}")
    return f'Table created for {number}'


def compute_hcf(x, y):
    global hcf
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if x % i == 0 and y % i == 0:
            hcf = i
    return hcf


def compute_lcm(x, y):
    return (x*y)/compute_hcf(x, y)


def long_sum(*number):
    sum = 0
    for num in number:
        sum += num
    return sum

'''
a = input("Enter a number: ")
b = input("Enter another number: ")
print(f"Sum of {a} and {b} is {add(a, b)}")

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
print(f'HCF of {x} and {y} is: {compute_hcf(x, y)}')
print(f'LCM of {x} and {y} is: {int(compute_lcm(x, y))}')
'''

print(long_sum(10, 20, 30, 40, 50, 60, 70, 80))

print(multiplication_table(input("Enter a number for multiplication table: ")))

