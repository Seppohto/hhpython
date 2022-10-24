
# # from decimal import Decimal
# # isTrue=True

# # x=Decimal(input('Enter first number: '))

# # sum=0
# # counter=0
# # while(x!=0) :
# #     sum+=x
# #     counter+=1
# #     x=Decimal(input('Enter next number: '))
# # if sum==0:
# #     print('Nothing to be calculated')
# # else:
# #     print(f"The average is {sum/counter:.2f}")
# # x = input('Enter a weekday number: ')
# # try:    
# #     x= int(x)
# #     print('OK')
# # except:
# #     print(f"\'{x}\' is not an integer")
# # try:
# #     x = int(input('Enter a weekday number: '))
# #     if 1 <= x <=7 :
# #         print('OK')
# #     else:
# #         print("Please enter an integer between 1 and 7")
# # except:
# #     print("Please enter an integer between 1 and 7")
# # while(True):
# #     try:
# #         x=input('Enter a month number: ')
# #         x=int(x)
# #         if 1 <= x <= 12:
# #             print('OK')
# #             break
# #         else:
# #             print(f"{x} is not a valid month number\n")
# #     except:
# #         print(f"\'{x}\' is not a valid month number\n")

# n = int(input('Enter a non-negative integer: '))
# while True:
#     if n < 0 :
#         n = int(input('Please enter a non-negative integer: '))
#     else:
#         break
# def doublefactorial(n):
#     res = 1;
#     for i in range(n, -1, -2):
#         if(i == 0 or i == 1):
#             return res
#         else:
#             res *= i
    
# print(f"{n}!! = {doublefactorial(n)}")
import calendar
import datetime
import math


def print_powers():
    for i in range(20):
        print(2**i, end=' ')
    return
def print_rectangle(width, height):
    for i in range(height):
        print('*'*width)
    return
def compute_discount(price, discount):
    return (price * discount)
def compute_earnings(hourlywage, hoursworked):
    if hoursworked <= 40:
        return hourlywage * hoursworked
    else:
        return hourlywage * 40 + (hourlywage * 1.5) * (hoursworked - 40)
def add(a, b):
    if (a + b) % 1 >= 0.5:
        return math.ceil(a + b)
    else:
        return math.floor(a + b)
def print_pyramid(height):
    for i in range(height):
        print(' '*(height-i-1), end='')
        print('*'*(i*2+1))
    return
def double_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * double_factorial(n-2)
def printdoublefactorialsfrom0to9():
    for i in range(10):
        print(f"{i}!! = {double_factorial(i)}")
    return
def print_month_calendar(month, year):
    print('')
    print(f" > {calendar.month_name[month]} {year} <")
    print(" Mon Tue Wed Thu Fri Sat Sun")
    for i in range(1, calendar.monthrange(year, month)[1]+1):
        if i == 1:
            print(' '*(calendar.weekday(year, month, i)*4), end='')
        if i < 10:
            print(f" {i} ", end='')
        else:
            print(f"{i} ", end='')
        if calendar.weekday(year, month, i) == 6:
            print('')
    return
def main():
    year = int(input('Enter year: '))
    month = int(input('Enter month: '))
    print_month_calendar(month, year)
    
    print ("\033[A                             \033[A                             \033[A")
    # printdoublefactorialsfrom0to9()
    # height = int(input('Enter pyramid height: '))
    # print_pyramid(height)
    # float_a = float(input('Enter a float: '))
    # float_b = float(input('Enter a float: '))
    # print(add(float_a, float_b))
    # wage = float(input('Enter wage: '))
    # hours = float(input('Enter hours: '))
    # print(f'The earnings are {compute_earnings(wage, hours):.2f}')
    # price = float(input('Enter price: '))
    # discount = (float(input('Enter discount percentage: '))/100)
    # print(f"The discount is {compute_discount(price, discount):.2f} euros")
    # # height = int(input('Enter height: '))
    # width = int(input('Enter width: '))
    # print_rectangle(width, height)
    return
if __name__ == "__main__":
    main()