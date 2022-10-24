# Create a program called lists_second. The program should first input words from the user until the user decides to quit by entering "quit". Then the program should print the words in alphabetical order.
from itertools import count


def  lists_second():
    words = []
    while True:
        word = input('Enter a word (quit ends): ')
        if word == 'quit':
            break
        words.append(word)
    words.sort()
    print(*words, sep='\n')
    return

# Create a program called lists_reverse. The program should first ask the user how many integers the user will enter. Then the program should input the integers from the user. Finally, the program should print the integers in reverse order on a single line as shown in the example output.
def  lists_reverse():
    n = int(input('How many integers? '))
    nums = []
    for i in range(n):
        nums.append(int(input(f'Enter an integer: ')))
    nums.reverse()
    print()
    print(*nums, sep=' ')
    return

# Create a program called lists_integers that first inputs five integers from the user and saves them to a list. Then the program should print the integers in descending order on a single line.
def  lists_integers():
    nums = []
    for i in range(5):
        nums.append(int(input(f'Enter an integer: ')))
    nums.sort(reverse=True)
    print()
    print(*nums, sep=' ', end='')
    print(' ',end='')
    return

# Create a program called lists_info that inputs five integers from the user and saves them in a list. The program should print the following: the count of the values in the list, the smallest value, the largest value, and the sum of the values in the list.

# Hint: Please notice that you can compute the required results by using Python's built-in functions.

def  lists_info():
    nums = []
    for i in range(5):
        nums.append(int(input(f'Enter an integer: ')))
    print(f'count: {len(nums)}')
    print(f'min:   {min(nums)}')
    print(f'max:   {max(nums)}')
    print(f'sum:   {sum(nums)}')
    return

# Create a program called lists_grades that first inputs a grade letter from user. Then the program should compute and show the percentage of the grade letter found in a list that contains the following values:  "A", "A", "B", "A", "C", "B", "C", "F", "B", "B", "A", "A", "C", "C", "C"
def  lists_grades():
    grades = ["A", "A", "B", "A", "C", "B", "C", "F", "B", "B", "A", "A", "C", "C", "C"]
    grade = input('Enter grade letter: ')
    #print percentage of grade
    print(f'{grades.count(grade)/len(grades)*100:.1f} %')
    return

# Create a program called lists_surnames. The program should input surnames until the user enters "ok". Then the program should print distinct surnames in alphabetical order as shown in the example output. Please notice that we can use a set to remove duplicates.
def  lists_surnames():
    surnames = []
    while True:
        surname = input('Enter a surname (ok ends): ')
        if surname == 'ok':
            break
        surnames.append(surname)
    surnames = set(surnames)
    surnames = list(surnames)
    surnames.sort()
    print()
    print(*surnames, sep=', ')
    return

# Create a program called lists_positive_sum. The program should have a function named positive_sum that takes a list as argument. The function should return the sum of positive values in the list. If there are no positive values in the list, the function should return zero. NB! The function should not modify the original list. The main function should first input five integers from the user and save them to a list. Then the main function should call the positive_sum function and finally print the return value of the positive_sum function.
def lists_positive_sum():
    nums = []
    for i in range(5):
        nums.append(int(input(f'Enter an integer: ')))
    print(f'Sum of positive values: {positive_sum(nums)}')
    return
def  positive_sum(nums):
    sum = 0
    for num in nums:
        if num > 0:
            sum += num
    return sum

#Create a program called lists_positive_sum. The program should have a function named positive_sum that takes a list as argument. The function should return the sum of positive values in the list. If there are no positive values in the list, the function should return zero.

#NB! The function should not modify the original list.

#The main function should first input five integers from the user and save them to a list. Then the main function should call the positive_sum function and finally print the return value of the positive_sum function.
def  lists_positive_sum():
    nums = []
    for i in range(5):
        nums.append(int(input(f'Enter an integer: ')))
    print()
    print(f'{positive_sum(nums)}')
    return
def  positive_sum(nums):
    sum = 0
    for num in nums:
        if num > 0:
            sum += num
    return sum


# Create a program called lists_words_from_url. The program should first fetch a word list from the
# given URL and save the words to a list. This we can do with the code below1
# .
# from urllib.request import urlopen
# url = "https://www.mit.edu/~ecprice/wordlist.10000"
# word_list = urlopen(url).read().splitlines()
# Then the program should determine and display the count of the words in the list, the average word
# length (float, no decimal-part formatting), and how many words there are of each length (the count
# of one-letter words, the count of two-letter words etc) as shown in the example output.
# You can suppose that the longest word contains 22 letters. We can use the len function to get the
# length of a word. To create counters for words of different lengths, we can create another list and
# initialise it with 23 zeros as below.
# counters = [0] * 23
# The word lengths are between 1 and 22. You can use the word length as the index and leave the first
# element in the counters list untouched.
# Your PC should be connected to the Internet when you are running this program on your own PC.

def  lists_words_from_url():
    from urllib.request import urlopen
    url = "https://www.mit.edu/~ecprice/wordlist.10000"
    word_list = urlopen(url).read().splitlines()
    print(f'{len(word_list)} words')
    sum = 0
    for word in word_list:
        sum += len(word)
    print(f'The average word length is {sum/len(word_list):.3f}')
    counters = [0] * 23
    for word in word_list:
        counters[len(word)] += 1
    print(f'{"Length":>5}{"Count":>5}')
    for i in range(1, len(counters)):
        print(f'{i:>5}{counters[i]:>5}')
    return

# Lists Sum Every Other
# Create a program called lists_sum_every_other. The program should have a function named
# sum_every_other that takes a list as argument. The function should return the sum of every other
# value starting from the first value in the list. If the list is empty, the function should return None.
# In Python, None is a keyword that represents null (no value at all)2
# .
# NB! The function should not modify the original list.

def sum_every_other(list):
    sum = 0
    for i in range(0, len(list), 2):
        sum += list[i]
    #return None if list is empty
    if len(list) == 0:
        return None
    return sum

# Lists Common Members
# Create a program called lists_common_members. The program should have a function named
# common_membersthat takes two lists as arguments. The function should return True if the lists have
# at least one common member. Otherwise, the function should return False.
# NB! The function should not modify the original lists.
# Hint: In this exercise, you can solve the problem by writing a loop.
# An alternative, advanced way to solve the problem is to use a set operation. Please see the
# Python documentation for more features of the set type:
# https://docs.python.org/3/library/index.html

def common_members(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

# Create a program called strings_start that first inputs a string from the user. Then the program should print the following: the string in all small letters, the string in all capital letters, and the length of the string.


# Example output:
# Enter a string: First String Exercise

# first string exercise
# FIRST STRING EXERCISE
# 21 characters
def strings_start():
    string = input('Enter a string: ')
    print()
    print(string.lower())
    print(string.upper())
    print(f'{len(string)} characters')
    return

# Create a program called strings_of_pearls that first inputs strings from the user until he/she decides to quit by entering the text "quit". Then the program should count how many times the user enters the string "pearl". The program should test the entered sting in case-insensitive way.

# If the user does not enter anything else but "quit", the program should not print anything else but "Bye!".


# Example output:
# Enter first string: Orange
# Enter next string: Pearl
# Enter next string: Pear
# Enter next string: PEARL
# Enter next string: pearl
# Enter next string: quit

# 3 pearls
# Bye!
def strings_of_pearls():
    pearls = 0
    count = 0
    while True:
        if count == 0:
            string = input('Enter first string: ')
            count += 1
        else:
            string = input('Enter next string: ')
            count += 1
        if string.lower() == 'pearl':
            pearls += 1
        if string.lower() == 'quit':
            break
    print()
    if count > 1:
        print(f'{pearls} pearls')
    print('Bye!')
    return


# Create a program called strings_digit_sum that first inputs a string from the user. Then the program should print the sum of all digits that are included in the inputted string. If there are no digits in the string, the program should print 0.


# Example output:
# Enter a string: abc1234

# The sum of digits is 10 
def strings_digit_sum():
    string = input('Enter a string: ')
    sum = 0
    for char in string:
        if char.isdigit():
            sum += int(char)
    print()
    print(f'The sum of digits is {sum}')
    return

# Create a program called strings_surnames. The program should first ask the user how many surnames the user will enter. Then the program should input the surnames from the user. Finally, the program should print distinct surnames as shown in the example output.


# Example output:
# How many surnames? 6
# Enter a surname: sheeRAN
# Enter a surname: Eilish
# Enter a surname: Niinistö
# Enter a surname: marin
# Enter a surname: Mars
# Enter a surname: niinistÖ

# Eilish Marin Mars Niinistö Sheeran
def strings_surnames():
    surnames = []
    count = int(input('How many surnames? '))
    for i in range(count):
        surname = input('Enter a surname: ')
        surnames.append(surname.lower())
    surnames = set(surnames)
    surnames = list(surnames)
    surnames.sort()
    for i in range(len(surnames)):
        surnames[i] = surnames[i].capitalize()
    print()
    print(' '.join(surnames))
    return

# Create a program called strings_subset that first inputs two strings from the user. The program should check if all the characters in the second string are included in the first string.

# The program should print "Subset" if this is true. Otherwise, the program should print "Not subset". If the second string is empty, the program should print "Nothing to be checked".

# Hint:  A boolean variable (initalised to True) and a loop is useful in this exercise.


# Example output:
# Enter first string: document
# Enter second string: code
# Subset
def strings_subset():
    string1 = input('Enter first string: ')
    string2 = input('Enter second string: ')
    if len(string2) == 0:
        print('Nothing to be checked')
        return
    for char in string2:
        if char not in string1:
            print('Not subset')
            return
    print('Subset')
    return

# Create a program called strings_box that first inputs a string. Then the program should print the inputted string in a in a "box" as shown in the example output.

# NB! You should not write a loop in your program.


# Example output:
# Enter a string: Hello
# ---------
# | Hello |
# ---------
def strings_box():
    string = input('Enter a string: ')
    print('-' * (len(string) + 4))
    print(f'| {string} |')
    print('-' * (len(string) + 4))
    return

# Create a program called strings_slicing_1 that first inputs a string. Then the program should print the following: first two characters in the string and every other character in the string.

# NB! You should use slicing in this exercise.


# Example output:
# Enter a string: heavy
# he
# hay

def strings_slicing_1():
    string = input('Enter a string: ')
    print(string[:2])
    print(string[::2])
    return

# Create a program called strings_slicing_2 that first inputs a string. Then the program should print the next to last character in the string. If the string has less than two characters, the program should print "Too short string".

# NB! You should use slicing in this exercise.


# Example output:
# Enter a string: exercise
# s
def strings_slicing_2():
    string = input('Enter a string: ')
    if len(string) < 2:
        print('Too short string')
        return
    print(string[-2])
    return

# Create a program called strings_slicing_3 that first inputs a string. Then the program should print all substrings of the string, which start from the first position in the string. The substrings should be printed as shown in the example output.

# NB!  You should use slicing in this exercise.  

# Hint: A loop is useful here.


# Example output:
# Enter a string: Python
# P
# Py
# Pyt
# Pyth
# Pytho
# Python
def strings_slicing_3():
    string = input('Enter a string: ')
    for i in range(len(string)):
        print(string[:i+1])
    return

# (This is an optional grade level 5+ exercise)

# Create a program called strings_circular_prime that has the following three functions: main, is_prime, and is_circular_prime.

# The is_prime function takes an integer as argument and returns True if the integer is a prime number. Otherwise, the function should return False. The function should not input anything from the user or print anything.

# The is_circular_prime function takes an integer as argument and returns True if the integer is a circular prime number. Otherwise, the function should return False. The function should not input anything from the user or print anything.

# A prime number (prime) is an integer greater than 1 whose only factors are 1 and itself.

# A circular prime number is a prime number that remains prime on any cyclic rotation of its digits in base 10. For example,

# 113 is a circular prime because 113, 131, and 311 are primes.

# 41 is a prime but is not a circular prime because its circular rotation 14 is not a prime.

# The main function should first ask the user to enter a positive integer. Then the main function should print the integer and either the text "is a circular prime" or "is not a circular prime". The main function should call the is_circular_prime function to determine if a number is a circular prime or not.


# Example output:
# Enter a positive integer: 19937
# 19937 is a circular prime
def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def is_circular_prime(number):
    number = str(number)
    for i in range(len(number)):
        if not is_prime(int(number[i:] + number[:i])):
            return False
    return True

def main():
    number = int(input('Enter a positive integer: '))
    if number <= 1:
        print(f'{number} is not a circular prime')
        return
    if is_circular_prime(number):
        print(f'{number} is a circular prime')
    else:
        print(f'{number} is not a circular prime')
    return

# Create a program called strings_duplicate_characters that first inputs a string from the user. The program should check if any character occurs more than once in the string. If there are no duplicate characters in the string, the program should print "No duplicates". Otherwise, the program should print "Contains duplicate(s)".

# NB! You should not write a loop is here. We can solve this problem using a set.


# Example output:
# Enter a string: benchmark
# No duplicates
def strings_duplicate_characters():
    string = input('Enter a string: ')
    if len(set(string)) == len(string):
        print('No duplicates')
    else:
        print('Contains duplicate(s)')
    return

# Create a program called matrix_count_occurrences. The program should have a function named count_occurrences, which takes a matrix (two-dimensional array) and an integer as its arguments. The function should return the count of occurrences of the integer in the matrix.


# Example output:
# 7
# 4
# 0
def count_occurrences(matrix, number):
    count = 0
    for row in matrix:
        for element in row:
            if element == number:
                count += 1
    return count

def main():
 m = [[1, 2, 3], [1, 2, 2], [1, 1, 1], [1, 2, 1]]
 print(count_occurrences(m, 1))
 print(count_occurrences(m, 2))
 print(count_occurrences(m, 5))


# if __name__ == "__main__":
#     main()
    # strings_box()
    # strings_subset()
    # strings_surnames()
    # strings_digit_sum()
    # strings_of_pearls()
    # strings_start()

# Matrix Sum
# Two matrices must have an equal number of rows and columns to be added. The example below
# shows an entry-wise addition of two matrices.
# Create a program called matrix_sum. First, copy/paste the main function below to your program.
# Then write the print_matrix_sum function. The print_matrix_sum function should take two matrices
# as arguments and print the sum of the matrices. You can suppose that the two matrices are always of
# the same size.
# def main():
#  m1 = [[1, 2, 0], [2, 3, 4]]
#  m2 = [[3, 2, 5], [6, 4, 3]]
#  m3 = [[1, 1, 1, 1], [3, 3, 2, 1], [2, 2, 2, 2]]
#  m4 = [[2, 2, 2, 3], [2, 3, 1, 0], [1, 2, 3, 4]]
#  print_matrix_sum(m1, m2)
#  print()
#  print_matrix_sum(m3, m4)

#  Example output:
# 4 4 5 
# 8 7 7 

# 3 3 3 4 
# 5 6 3 1 
# 3 4 5 6 
def print_matrix_sum(matrix1, matrix2):
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            print(matrix1[i][j] + matrix2[i][j], end=' ')
        print()
    return

def main():
 m1 = [[1, 2, 0], [2, 3, 4]]
 m2 = [[3, 2, 5], [6, 4, 3]]
 m3 = [[1, 1, 1, 1], [3, 3, 2, 1], [2, 2, 2, 2]]
 m4 = [[2, 2, 2, 3], [2, 3, 1, 0], [1, 2, 3, 4]]
 print_matrix_sum(m1, m2)
 print()
 print_matrix_sum(m3, m4)

# Sudoku Check Row
# Create a program called sudoku_check_row. The program should have a function named row_ok
# that takes sudoku grid (matrix) and row index (int) as arguments.
# You can suppose that each item on a row in the matrix is a digit between 0 and 9. Zero represents an
# empty square in a sudoku grid. That is, there can be several zeros on a row until the sudoku is solved.
# The row_ok function should return True if the row is ok. Otherwise, it should return False. NB! The
# function should not modify the sudoku grid.
# A row is ok if each of the digits between 1 and 9 appears zero or one times on the row. The row is
# not ok if any of the digits between 1 and 9 appears more than once on the row.
# In the sudoku grid below, the second row is not ok because the digit 2 appears twice on the row. All
# the other rows are ok.
# NB! Please copy/paste the code of the main function below to your program.
# def main():
# sudoku = [
# [9, 0, 0, 0, 8, 0, 3, 0, 0],
# [2, 0, 0, 2, 5, 0, 7, 0, 0],
# [0, 2, 0, 3, 0, 0, 0, 0, 4],
# [2, 9, 4, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 7, 3, 0, 5, 6, 0],
# [7, 0, 5, 0, 6, 0, 4, 0, 0],
# [0, 0, 7, 8, 0, 3, 9, 0, 0],
# [0, 0, 1, 0, 0, 0, 0, 0, 3],
# [3, 0, 0, 0, 0, 0, 0, 0, 2]
# ]
# print(row_ok(sudoku, row_index=0)) # True
# print(row_ok(sudoku, row_index=1)) # False
# print(row_ok(sudoku, row_index=8)) # True
# if __name__ == "__main__":
# main()
def row_ok(sudoku, row_index):
    row = sudoku[row_index]
    for i in range(1, 10):
        if row.count(i) > 1:
            return False
    return True

def main():
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    print(row_ok(sudoku, row_index=0)) # True
    print(row_ok(sudoku, row_index=1)) # False
    print(row_ok(sudoku, row_index=8)) # True

# Sudoku Check Column
# Create a program called sudoku_check_column. The program should have a function named
# column_ok that takes sudoku grid (matrix) and column index (int) as arguments.
# The column_ok function should return True if the row is ok. Otherwise, it should return False.
# NB! The function should not modify the sudoku grid.
# A column is ok if each of the digits between 1 and 9 appears zero or one times in the column. The
# column is not ok if any of the digits between 1 and 9 appears more than once in the column.
# In the sudoku grid below, the first column is not ok because the digit 2 appears twice in the column.
# All the other columns are ok.
# NB! Please copy/paste the code of the main function below to your program.
# def main():
# sudoku = [
# [9, 0, 0, 0, 8, 0, 3, 0, 0],
# [2, 0, 0, 2, 5, 0, 7, 0, 0],
# [0, 2, 0, 3, 0, 0, 0, 0, 4],
# [2, 9, 4, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 7, 3, 0, 5, 6, 0],
# [7, 0, 5, 0, 6, 0, 4, 0, 0],
# [0, 0, 7, 8, 0, 3, 9, 0, 0],
# [0, 0, 1, 0, 0, 0, 0, 0, 3],
# [3, 0, 0, 0, 0, 0, 0, 0, 2]
# ]
# print(column_ok(sudoku, column_index=0)) # False
# print(column_ok(sudoku, column_index=1)) # True
# print(column_ok(sudoku, column_index=8)) # True

def column_ok(sudoku, column_index):
    column = []
    for row in sudoku:
        column.append(row[column_index])
    for i in range(1, 10):
        if column.count(i) > 1:
            return False
    return True

def main():
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    print(column_ok(sudoku, column_index=0)) # False
    print(column_ok(sudoku, column_index=1)) # True
    print(column_ok(sudoku, column_index=8)) # True

# Sudoku Check Block
# Create a program called sudoku_check_block. The program should have a function named block_ok
# that takes sudoku grid (matrix), row index (int), and column index (int) as arguments.
# The block_ok function should return True if the 3x3 block is ok. Otherwise, it should return False.
# NB! The function should not modify the sudoku grid.
# A 3x3 block is ok if each of the digits between 1 and 9 appears zero or one times in the block. The
# block is not ok if any of the digits between 1 and 9 appears more than once in the block.
# In a sudoku grid, the 3x3 blocks begin at the indexes (row_index, column_index)
# (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)
# NB! If the block_ok function is called with any other combination of row and column, it should
# return False.
# NB! Please copy/paste the code of the main function below to your program.
# def main():
#  sudoku = [
#  [9, 0, 0, 0, 8, 0, 3, 0, 0],
#  [2, 0, 0, 2, 5, 0, 7, 0, 0],
#  [0, 2, 0, 3, 0, 0, 0, 0, 4],
#  [2, 9, 4, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 7, 3, 0, 5, 6, 0],
#  [7, 0, 5, 0, 6, 0, 4, 0, 6],
#  [0, 0, 7, 8, 0, 3, 9, 0, 0],
#  [0, 0, 1, 0, 0, 0, 0, 0, 3],
#  [3, 0, 0, 0, 0, 0, 0, 0, 2]
#  ]
#  print(block_ok(sudoku, row_index=0, column_index=0)) # False
#  print(block_ok(sudoku, row_index=3, column_index=6)) # False
#  print(block_ok(sudoku, row_index=6, column_index=3)) # True

def block_ok(sudoku, row_index, column_index):
    if row_index not in [0, 3, 6] or column_index not in [0, 3, 6]:
        return False
    block = []
    for row in sudoku[row_index:row_index+3]:
        block.extend(row[column_index:column_index+3])
    for i in range(1, 10):
        if block.count(i) > 1:
            return False
    return True

def main():
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 6],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    print(block_ok(sudoku, row_index=0, column_index=0)) # False
    print(block_ok(sudoku, row_index=3, column_index=6)) # False
    print(block_ok(sudoku, row_index=6, column_index=3)) # True

# Sudoku Check Grid
# Create a program called sudoku_check_grid. The program should have a function named grid_ok
# that takes sudoku grid (matrix) as argument. The function should use the functions from the three
# previous sudoku exercises to determine whether the complete sudoku grid is ok.
# The grid_ok function should check each of the nine rows, nine columns, and nine 3x3 blocks in the
# sudoku grid. If all of them are ok, the function should return True. Otherwise, the function should
# return False.
# NB! First, copy/paste the functions (row_ok, column_ok, and block_ok) from your previous exercise
# solutions to this program. Then copy/paste the code of the main function below to your program.
# Finally, write the grid_ok function.
# def main():
# sudoku_1 = [
# [9, 0, 0, 0, 8, 0, 3, 0, 0],
# [2, 0, 0, 2, 5, 0, 7, 0, 0],
# [0, 2, 0, 3, 0, 0, 0, 0, 4],
# [2, 9, 4, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 7, 3, 0, 5, 6, 0],
# [7, 0, 5, 0, 6, 0, 4, 0, 0],
# [0, 0, 7, 8, 0, 3, 9, 0, 0],
# [0, 0, 1, 0, 0, 0, 0, 0, 3],
# [3, 0, 0, 0, 0, 0, 0, 0, 2]
# ]
# sudoku_2 = [
# [2, 6, 7, 8, 3, 9, 5, 0, 4],
# [9, 0, 3, 5, 1, 0, 6, 0, 0],
# [0, 5, 1, 6, 0, 0, 8, 3, 9],
# [5, 1, 9, 0, 4, 6, 3, 2, 8],
# [8, 0, 2, 1, 0, 5, 7, 0, 6],
# [6, 7, 4, 3, 2, 0, 0, 0, 5],
# [0, 0, 0, 4, 5, 7, 2, 6, 3],
# [3, 2, 0, 0, 8, 0, 0, 5, 7],
# [7, 4, 5, 0, 0, 3, 9, 0, 1]
# ]
# print(grid_ok(sudoku_1)) # False
# print(grid_ok(sudoku_2)) # True

def grid_ok(sudoku):
    for row in sudoku:
        if not row_ok(row):
            return False
    for i in range(9):
        if not column_ok(sudoku, i):
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not block_ok(sudoku, i, j):
                return False
    return True

def main():
    sudoku_1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    sudoku_2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]
    print(grid_ok(sudoku_1)) # False
    print(grid_ok(sudoku_2)) # True

# References Multiply by Two
# Create a program called references_multiply_by_two. The program should have a function named
# multiply_by_two that takes a list of numbers as argument.
# The multiply_by_two function should multiply each number in the list by two.
# First, copy/paste the main function below to your program. Then write the multiply_by_two function.
# def main():
#  numbers = [1, 2, 3, 4, 5, 6]
#  more_numbers = [10, 20, 30]
#  print(numbers)
#  multiply_by_two(numbers)
#  print(numbers)
#  print(more_numbers)
#  multiply_by_two(more_numbers)
#  print(more_numbers)

# Example output:
# [1, 2, 3, 4, 5, 6]
# [2, 4, 6, 8, 10, 12]
# [10, 20, 30]
# [20, 40, 60]

def multiply_by_two(numbers):
    for i in range(len(numbers)):
        numbers[i] *= 2

def main():
    numbers = [1, 2, 3, 4, 5, 6]
    more_numbers = [10, 20, 30]
    print(numbers)
    multiply_by_two(numbers)
    print(numbers)
    print(more_numbers)
    multiply_by_two(more_numbers)
    print(more_numbers)

# References Fix an Error
# Create a program called references_fix_an_error.
# First, copy/paste the code below to your program.
# playlist_1 = ["Levitating", "Hold me closer", "As it was"]
# playlist_2 = playlist_1
# playlist_2.append("Bad Habit")
# playlist_2.append("Shivers")
# print("Playlist 1: ", end="")
# print(*playlist_1, sep=", ")
# print("Playlist 2: ", end="")
# print(*playlist_2, sep=", ")
# The program should print two lists of songs. The second song list should contain the same songs as
# the first song list plus two other songs. The songs are already added to the lists in the code above.
# Unfortunately, the program above does not print the song lists as expected. Please fix the error
# without adding more code lines to the program.
# Hint: You can visualise the code in the Python Tutor tool: https://pythontutor.com/visualize.html

# Example output:
# Playlist 1: Levitating, Hold me closer, As it was
# Playlist 2: Levitating, Hold me closer, As it was, Bad Habit, Shivers

def main():
    playlist_1 = ["Levitating", "Hold me closer", "As it was"]
    playlist_2 = playlist_1.copy()
    playlist_2.append("Bad Habit")
    playlist_2.append("Shivers")
    print("Playlist 1: ", end="")
    print(*playlist_1, sep=", ")
    print("Playlist 2: ", end="")
    print(*playlist_2, sep=", ")

# References New Doubled List
# Create a program called references_new_doubled_list. The program should have a function named
# new_doubled_list that takes a list of numbers as argument. The new_doubled_list function should
# return a copy of the list where each number in the original list are multiplied by two.
# First, copy/paste the main function below to your program. Then write the new_doubled_list
# function.
# def main():
#  first_list = [1, 2, 3, 4, 5, 6]
#  second_list = new_doubled_list(first_list)
#  print(first_list)
#  print(second_list)

# Example output:
# [1, 2, 3, 4, 5, 6]
# [2, 4, 6, 8, 10, 12]

def new_doubled_list(numbers):
    new_list = []
    for number in numbers:
        new_list.append(number * 2)
    return new_list

def main():
    first_list = [1, 2, 3, 4, 5, 6]
    second_list = new_doubled_list(first_list)
    print(first_list)
    print(second_list)

# References New Doubled Matrix
# Create a program called references_new_doubled_matrix. The program should have a function
# named new_doubled_matrix that takes a matrix as argument. The matrix contains numbers. The
# new_doubled_matrix function should return a copy of the matrix where each number in the original
# matrix are multiplied by two.
# First, copy/paste the main function below to your program. Then write the new_doubled_matrix
# function.
# def main():
#  m1 = [[1, 2, 3], [4, 5, 6]]
#  m2 = new_doubled_matrix(m1)
#  print(m1)
#  print(m2)

# Example output:
# [[1, 2, 3], [4, 5, 6]]
# [[2, 4, 6], [8, 10, 12]]

def new_doubled_matrix(matrix):
    new_matrix = []
    for row in matrix:
        new_row = []
        for number in row:
            new_row.append(number * 2)
        new_matrix.append(new_row)
    return new_matrix

def main():
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = new_doubled_matrix(m1)
    print(m1)
    print(m2)

# References Weekdays
# Create a program called references_weekdays.
# First, copy/paste the code below to your program.
# from copy import copy
# weekdays_1 = ["Branch 1", ["Monday", "Wednesday", "Friday"]]
# weekdays_2 = copy(weekdays_1) # duplicate the first list
# weekdays_2[0] = "Branch 2" # change the branch name in the second list
# weekdays_2[1].insert(1, "Tuesday") # insert one more weekday name
# print(*weekdays_1)
# print(*weekdays_2)
# The program should print the names of the weekdays when two company branches are open. The
# second company branch is open on the same weekdays as the first company branch plus on one more
# weekday. The weekday names are already added to the lists in the code above.
# Unfortunately, the program above does not print the weekday names as expected. Please fix the error
# without adding more code lines to the program. 

# Example output:
# Branch 1 ['Monday', 'Wednesday', 'Friday']
# Branch 2 ['Monday', 'Tuesday', 'Wednesday', 'Friday']
from copy import deepcopy

def refrences_weekdays():
    weekdays_1 = ["Branch 1", ["Monday", "Wednesday", "Friday"]]
    weekdays_2 = deepcopy(weekdays_1) # duplicate the first list
    weekdays_2[0] = "Branch 2" # change the branch name in the second list
    weekdays_2[1].insert(1, "Tuesday") # insert one more weekday name
    print(*weekdays_1)
    print(*weekdays_2)

def main():
    refrences_weekdays()

# Tuples First
# Create a program called tuples_first. The program should first input an integer and a float from the
# user. Then the program should create a tuple that holds the inputted two values. Finally, the
# program should print the tuple.

# Example output:
# Enter an int: 5
# Enter a float: 0.29
# (5, 0.29)

def tuples_first():
    integernumber = int(input("Enter an int: "))
    floatnumber = float(input("Enter a float: "))
    tuple = (integernumber, floatnumber)
    print(tuple)

def main():
    tuples_first()

# Tuples Argument
# Create a program called tuples_argument. The program should have a function named print_player
# that takes a tuple as argument. The tuple should contain a team name, player name and the number
# of the goals the player has scored. Finally, the print_player function should print these values.
# First, copy/paste the main function below to your program. Then write the print_player function.
# def main():
# p = ("Hawks", "Jennifer", 10)
# print_player(p)

# Example output:
# Jennifer (Hawks), 10 goals

def print_player(tuple):
    print(tuple[1], "(" + tuple[0] + "),", tuple[2], "goals")

def main():
    p = ("Hawks", "Jennifer", 10)
    print_player(p)

# Tuples Return
# Create a program called tuples_return. The program should have a function named pow_2_3 that
# takes an integer as argument. The function should compute the second power and the third power
# of the integer and return them in a tuple.
# First, copy/paste the main function below to your program. Then write the pow_2_3 function.
# def main():
# x = int(input("Enter an integer: "))
# p2, p3 = pow_2_3(x)
# print(p2)
# print(p3)

def pow_2_3(integer):
    p2 = integer ** 2
    p3 = integer ** 3
    return p2, p3

def main():
    x = int(input("Enter an integer: "))
    p2, p3 = pow_2_3(x)
    print(p2)
    print(p3)

if __name__ == "__main__":
    main()

# Lists Remove Min Max
# Create a program called lists_remove_min_max. The program should have a function named
# remove_min_max that takes a list as argument. The function should remove the smallest and the
# largest value in the list. Note: The function should be able to handle an empty list and a list that has
# only one element.
# First, copy/paste the main function below to your program. Then write the remove_min_max
# function.
# def main():
# a = [3, 1, 4, 1, 5]
# remove_min_max(a)
# print(a)
# if __name__ == "__main__":
# main()

def remove_min_max(list):
    if len(list) > 1:
        list.remove(min(list))
        if len(list) > 1:
            list.remove(max(list))

def main():
    a = [3, 1, 4, 1, 5]
    remove_min_max(a)
    print(a)

# Tuples Entry Exam
# Create a program called tuples_entry_exam. The program should have a function named
# grade_exam that takes a list of applicants and the exam passing score as arguments. In the list,
# applicant names and exam scores are contained in tuples.
# The grade_exam function should return a new list of tuples that contains only those applicants'
# names and scores who have passed the entry exam.
# First, copy/paste the main function below to your program. Then write the grade_exam function.
# def main():
# applicants = [("Ann", 30), ("Jack", 25), ("Jill", 40)]
# passed_applicants = grade_exam(applicants, 30)
# print("Entry exam passed")
# for name, points in passed_applicants:
# print(f"{name}, {points} points")
# if __name__ == "__main__":
# main()

def grade_exam(applicants, score):
    passed_applicants = []
    for applicant in applicants:
        if applicant[1] >= score:
            passed_applicants.append(applicant)
    return passed_applicants

def main():
    applicants = [("Ann", 30), ("Jack", 25), ("Jill", 40)]
    passed_applicants = grade_exam(applicants, 30)
    print("Entry exam passed")
    for name, points in passed_applicants:
        print(f"{name}, {points} points")

# Tuples Swap
# Create a program called tuples_swap. The program should first input seven integers from the user
# and save them in a list. Then the program should swap each successive pair of elements in the list.
# Finally, the program should print the list as shown
# Please see the example output for more details.
# NB! You should use slicing when you swap a pair of elements.


# Example output:
# Enter an integer: 1
# Enter an integer: 2
# Enter an integer: 3
# Enter an integer: 4
# Enter an integer: 5
# Enter an integer: 6
# Enter an integer: 7
# [2, 1, 4, 3, 6, 5, 7]

def tuples_swap():
    list = []
    for i in range(7):
        list.append(int(input("Enter an integer: ")))
    for i in range(0, len(list-1), 2):
        list[i], list[i + 1] = list[i + 1], list[i]
    print(list)

def main():
    tuples_swap()

if __name__ == "__main__":
    main()

# Tuples Clock
# Create a program called tuples_clock. The program should have a function named roll_forward. The
# function should take the following as arguments:
# • clock time as a tuple that contains hours (int) and minutes (int)
# • the number of hours to be added to the clock time
# • the number of minutes to be added to the clock time.
# The roll_forward function should roll the clock time forward and return a new clock time as a tuple.
# In the new clock time, hours should be between 0 and 23, and minutes should be between 0 and 59.
# The clock time should start from 00:00. The main function should
# • input hours and minutes to be added to the clock time
# • call the roll_forward function to roll the time forward
# • print the new clock time.
# The program should terminate when the user enters negative hours.

# Example output:
# The current time is 00:00
# Enter hours to add: 12
# Enter minutes to add: 30
# 12:30
# Enter hours to add: 5
# Enter minutes to add: 35
# 18:05
# Enter hours to add: 0
# Enter minutes to add: 1439
# 18:04
# Enter hours to add: -1

def roll_forward(clock, hours, minutes):
    clock = clock[0] + hours, clock[1] + minutes
    if clock[1] >= 60:
        clock = clock[0] + clock[1] // 60, clock[1] % 60
    if clock[0] >= 24:
        clock = clock[0] % 24, clock[1]
    return clock

def main():
    clock = (0, 0)
    print(f"The current time is {clock[0]:02}:{clock[1]:02}")
    while True:
        hours = int(input("Enter hours to add: "))
        if hours < 0:
            break
        minutes = int(input("Enter minutes to add: "))
        clock = roll_forward(clock, hours, minutes)
        print(f"{clock[0]:02}:{clock[1]:02}")

# Dictionaries Team 1
# Create a program called dictionaries_team_1. The program should first create a dictionary that holds
# each team member's name (as the key) and role in the team (as the value). Then the program should
# print the dictionary as shown in the example output.
# The team members are the following:
# John software developer
# Ann project manager
# Susan software developer
# Jill lead developer
# Example output:
# {'John': 'software developer', 'Ann': 'project manager', 'Susan': 'software developer', 'Jill': 'lead developer'}

def main():
    team = {"John": "software developer", "Ann": "project manager", "Susan": "software developer", "Jill": "lead developer"}
    print(team)

# Dictionaries Team 2
# Create a program called dictionaries_team_2. Copy/paste the dictionary from the Dictionaries Team
# 1 exercise to this program. The program should print the team members as shown in the example
# output.

# Example output:
# John Ann Susan Jill 
# Ann Jill John Susan 

def main():
    team = {"John": "software developer", "Ann": "project manager", "Susan": "software developer", "Jill": "lead developer"}
    for member in team:
        print(member, end=" ")
    print()
    for member in sorted(team):
        print(member, end=" ")

# Dictionaries Team 3
# Create a program called dictionaries_team_3. Copy/paste the dictionary from the Dictionaries Team
# 1 exercise to this program. The program should ask the user to enter a team member's name and
# print the team member's role in the team. If the name is not in the dictionary, the program should
# print the name and "is not in the team". The program should be repeating these steps until the user
# enters "quit" when the program asks the user to enter a name.
# Example output:
# Enter name (quit ends): Frank
# Frank is not in the team

# Enter name (quit ends): Ann
# Ann is a project manager

# Enter name (quit ends): Susan
# Susan is a software developer

# Enter name (quit ends): quit

def main():
    team = {"John": "software developer", "Ann": "project manager", "Susan": "software developer", "Jill": "lead developer"}
    while True:
        name = input("Enter name (quit ends): ")
        if name == "quit":
            break
        if name in team:
            print(f"{name} is a {team[name]}")
            print()
        else:
            print(f"{name} is not in the team")
            print()

# Dictionaries Translator
# Create a program called dictionaries_translator. The program should first input Finnish and English
# words from the user until the user enters "quit". The program should save the inputted words to a
# dictionary. The words should be saved in lowercase.
# Next, the program should input an English word from the user and print the corresponding Finnish
# word. If the English word does not exist in the dictionary, the program should print "Unknown word".
# The program should keep repeating these steps until the user enters "quit" when the program asks
# the user to enter an English word.
# Example output:
# === Creating a dictionary ===
# Enter english word (quit ends): CAT
# Enter finnish word: kisSA
# Enter english word (quit ends): dog
# Enter finnish word: koira
# Enter english word (quit ends): quit

# === Using a dictionary ===
# Enter english word (quit ends): caT
# kissa

# Enter english word (quit ends): python
# Unknown word

# Enter english word (quit ends): Dog
# koira

# Enter english word (quit ends): quit

def main():
    dictionary = {}
    print("=== Creating a dictionary ===")
    while True:
        english = input("Enter english word (quit ends): ").lower()
        if english == "quit":
            break
        finnish = input("Enter finnish word: ").lower()
        dictionary[english] = finnish
    print()
    print("=== Using a dictionary ===")
    while True:
        english = input("Enter english word (quit ends): ").lower()
        if english == "quit":
            break
        if english in dictionary:
            print(dictionary[english])
            print()
        else:
            print("Unknown word")
            print()

# Dictionaries Team 4
# Create a program called dictionaries_team_4 Copy/paste the dictionary from the Dictionaries Team
# 1 exercise to this program.
# The program should ask the user to enter name and role. If the name is not in the dictionary, the
# program should add the inputted data to the dictionary. If the name is already in the dictionary, the
# program should update the team member's role with the inputted role. The program should keep
# repeating these steps until the user enters "quit" when the program asks the user to enter a name.
# Finally, the program should print the team members' names and roles as shown in the example
# output.
# Please set the output width to 8 when you print team members' names.
# Example output:
# Enter name (quit ends): Mike
# Enter role: software developer

# Enter name (quit ends): Rosanna
# Enter role: ux designer

# Enter name (quit ends): quit

# Ann     project manager
# Jill    lead developer
# John    software developer
# Mike    software developer
# Rosanna ux designer
# Susan   software developer

def main():
    team = {"John": "software developer", "Ann": "project manager", "Susan": "software developer", "Jill": "lead developer"}
    while True:
        name = input("Enter name (quit ends): ")
        if name == "quit":
            break
        role = input("Enter role: ")
        print()
        team[name] = role
    print()
    for member in sorted(team):
        print(f"{member:<8}{team[member]}")

# Dictionaries Team 5
# Create a program called dictionaries_team_5 Copy/paste the dictionary from the Dictionaries Team
# 1 exercise to this program.
# The program should print team members' roles as shown in the example output. Please notice that
# each role is printed only once.
# Example output:
# lead developer
# project manager
# software developer

def main():
    team = {"John": "software developer", "Ann": "project manager", "Susan": "software developer", "Jill": "lead developer"}
    roles = set()
    for member in team:
        roles.add(team[member])
    for role in roles:
        print(role)


# Dictionaries Count Letters
# Create a program called dictionaries_count_letters. The program should first fetch the content of a
# text from the given URL and save it as single a string. This we can do with the code below.
# from urllib.request import urlopen
# url = "https://www.mit.edu/~ecprice/wordlist.10000"
# content = urlopen(url).read().decode("UTF-8")
# Then the program should count the letters in the string and display the result as shown in the example
# output below.
# In this exercise,
# • you should use a dictionary to hold the count of occurrences of each distinct letter in the string
# • you should count letters in a case-insensitive way
# • you should not display a letter if it does not appear in the string
# Example output:
# a: 5378
# b: 1141
# c: 3025
# d: 2507
# e: 7601
# f: 927
# g: 1717
# h: 1429
# i: 5461
# j: 183
# k: 592
# l: 3231
# m: 1912
# n: 4822
# o: 4252
# p: 2027
# q: 123
# r: 4860
# s: 5085
# t: 4760
# u: 1939
# v: 849
# w: 632
# x: 264
# y: 1027
# z: 136

def main():
    from urllib.request import urlopen
    url = "https://www.mit.edu/~ecprice/wordlist.10000"
    content = urlopen(url).read().decode("UTF-8")
    letters = {}
    for letter in content.lower():
        if letter.isalpha():
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    for letter in sorted(letters):
        print(f"{letter}: {letters[letter]}")

if __name__ == "__main__":
    main()