# Q 1 :- Write a program to check whether a number is even or odd.
def is_even_odd(num):
    if num % 2 == 0:
        return "Even"
    return "Odd"

print(is_even_odd(12))

# Q 2 :- Write a program to determine if a number is prime.

def is_prime(num):
    count_divisor= 0

    for i in range(1, num+1):
        if num % i == 0:
            count_divisor+= 1
    return "Prime number" if count_divisor <= 2 else "Not a prime number"

        

print(is_prime(12))
print(is_prime(11))
print(is_prime(19))
print(is_prime(249))

# Q 3 :- Write a program to check if a given year is a leap year.
def is_leap_year(year):
    if year % 4 == 0 or year % 400 == 0 and year % 100 !=0:
        return f"{year} is a leap year."
    return f"{year} is not a leap year."

print(is_leap_year(1912))

# Q 4 :- Write a program to check if a number is an Armstrong number.

def is_armstrong_no(num):
    arm_sum = 0
    for i in str(num):
        arm_sum += int(i) ** len(str(num))
    return "Armstrong number" if arm_sum == num else "Not a Armstrong number"

print(is_armstrong_no(153))
print(is_armstrong_no(9))
print(is_armstrong_no(10))


# Q 6 :- Write a program to check if a string or number is a palindrome.

def is_palindrome(value):
    if value == value[::-1] and len(value) == len(value[::-1]):
        return f"{value} is a palindrome"
    return f"{value} is not a palindrome"

print(is_palindrome("rare"))
print(is_palindrome("151"))


# Q 8 :-Write a program to compute the factorial of a given number. 

def compute_factorial(num):
    result = 1
    for i in range(num, 0, -1):
        result *= i
    return result

print(compute_factorial(5))
print(compute_factorial(12))


# Q 9 :-Write a program to calculate the sum of digits of a number.  

def calculate_sum_of_digit(value:str):
    sum_of_num = 0
    for i in value:
        sum_of_num+= int(i)
    return sum_of_num

print(calculate_sum_of_digit('1234'))


# Q 12 :-Write a program to count vowels and consonants in a given string.  

def count_vowels_consonants(string):
    vowels = 0
    consonents = 0
    for i in string:
        if i.lower() in "aeiou":
            vowels += 1
        elif i.isalpha():
            consonents += 1
    return f"Vowels: {vowels}, Consonants: {consonents}"

print(count_vowels_consonants("Programming Street 150"))
print(count_vowels_consonants("Hello World")) 


# Q 13 :- Write a program to reverse a given string. 

def revers_string(strings):
    return strings[::-1]

print(revers_string("hello"))
print(revers_string("programming street 150"))


# Q 14 :- Write a program to find the largest and smallest numbers in an array. 

def find_largest_smallest(arr):
    return f"Largest number is {max(arr)} and Smallest number is {min(arr)}"

print(find_largest_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Q 15 :- Write a program to sort an array of numbers in ascending order.  

def sort_array(arr):
    return sorted(arr)

print(sort_array([1, 5, 3, 2, 4]))

# Q 16 :- Write a program to find the sum of elements in an array. 

def sum_of_elements(arr):
    return sum(arr)

print(sum_of_elements([1, 2, 3, 4, 5]))
print(sum_of_elements([10, 20, 30, 40, 50]))

# Q 17 :- Write a program to find all Armstrong numbers within a given range. 

def find_armstrong_no_in_range(start:int, end:int):
    armstrong_no = []
    for i in range(start, end+1):
        arm_sum = 0
        for j in str(i):
            arm_sum += int(j) ** len(str(i))
        if arm_sum == i:
            armstrong_no.append(i)
    return armstrong_no

print(find_armstrong_no_in_range(1, 500))

# Q 18:- Write a program to generate multiplication tables for a given number.  

def multiplication_table(num:int, start:int, end:int):
    for i in range(start, end+1):
        print(f"{num} * {i} = {num*i}")

multiplication_table(5, 1, 10)

# Q 19 :- Write a program to find all prime numbers within a given range.  

def is_prime(num):
    count_divisor= 0
    if num == 1:
        return "Not a prime number"
    for i in range(1, num+1):
        if num % i == 0:
            count_divisor+= 1
    return "Prime number" if count_divisor <= 2 else "Not a prime number"


def find_prime_in_range(start:int, end:int):
    prime_list= []
    for i in range(start, end+1):
        if is_prime(i) == "Prime number":
            prime_list.append(i)
    return prime_list

print(find_prime_in_range(1, 100))
print(find_prime_in_range(1, 50))


#  Q 20 :- Write a program to determine if a number is a perfect number.  

def is_perfect_no(num):
    divisor_list = []
    sum_divisor = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_list.append(i)
            sum_divisor += i
    return f"Perfect number with divisor list:-{divisor_list} " if sum_divisor == num else "Not a  perfect number"

print(is_perfect_no(6))
print(is_perfect_no(28))
print(is_perfect_no(12))


#  Q 21 ;- Write a program to find the sum of all even numbers within a given range.

def sum_of_even_no_in_range(start:int, end:int):
    sum_even = 0
    for i in range(start, end+1):
        if i %2 == 0:
            sum_even+= i
    return sum_even

print(sum_of_even_no_in_range(1, 10))
print(sum_of_even_no_in_range(1, 20))


#  Q 22 :- Write a program to find the sum of all odd numbers within a given range.

def sum_of_odd_no_in_range(start:int, end:int):
    sum_odd = 0 
    for i in range(start, end+1):
        if i % 2 != 0:
            sum_odd+= i
    return sum_odd

print(sum_of_odd_no_in_range(1, 10))
print(sum_of_odd_no_in_range(1, 20))


#  Q 24 :- Write a program to print all prime numbers less than a given number.

def prime_no_less_than_num(num):
    prime_list = []
    for i in range(1, num):
        count_divisor = 0
        for j in range(1, i+1):
            if i % j == 0:
                count_divisor+= 1
        if count_divisor <= 2:
            prime_list.append(i)
    return prime_list

print(prime_no_less_than_num(10))
print(prime_no_less_than_num(20))


# Q 25 :- Write a program to count the number of digits in a given number.

def count_digit(num):
    return len(str(num))

print(count_digit(12345))
print(count_digit(1234567890))


# Q 28 :- Write a program to find the sum of the digits of the factorial of a given number.  

def sum_of_factorial(num):
    fact= 1
    for i in range(num, 0, -1):
        fact*=i
        sum_fact = 0
        for j in str(fact):
            sum_fact+= int(j)
    return sum_fact

print(sum_of_factorial(4))
print(sum_of_factorial(5))


#  Q 29 :- Write a program to find the largest palindrome in a given string.

def largest_string_palindrome(strings):
    largest_palindrome = ""
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if strings[i:j] == strings[i:j][::-1]:
                if len(strings[i:j]) > len(largest_palindrome):
                    largest_palindrome = strings[i:j]
    return largest_palindrome

print(largest_string_palindrome("babad"))


# Q 30 :- Write a program to find missing numbers in a sequence from 1 to n. 

def find_missing_no(num_list):
    missing_list = []
    for i in range(1, num_list[-1]+1):
        if i not in num_list:
            missing_list.append(i)
    return missing_list

print(find_missing_no([1, 2, 4, 5]))


#  Q 33 :- Write a program to calculate the power of a number. 

def calculate_power(num:int, exp:int):
    return f"{num} raised to the power of {exp} is {num ** exp}"

print(calculate_power(2, 4))


#  Q 34 :- Write a program to check if two strings are anagrams.  

def is_two_string_anagram(str1:str, str2:str):
    if len(str1) != len(str2):
        return f"{str1} and {str2} are not an anagrams of each other."
    else:
        for i in str1:
            if i not in str2:
                return f"{str1} and {str2} are not an anagrams of each other."
        return f"{str1} and {str2} are anagrams of each other."

print(is_two_string_anagram("listen", "silent"))
print(is_two_string_anagram("hello", "world"))



#  Q 35 ;- Write a program to calculate the sum of all prime numbers within a given range.  

def sum_of_all_prime_no_of_range(start:int, end:int):
    prime_list = []
    for i in range(start, end+ 1):
        count_divisor = 0
        if i == 1:
            continue
        for j in range(1, i+1):
            if i % j == 0:
                count_divisor+= 1
        if count_divisor <= 2:
            prime_list.append(i)
    return sum(prime_list)

print(sum_of_all_prime_no_of_range(1, 10))

#  Q 37 : Write a program to determine if a number is a perfect square.

def perfect_square(num):
    return "Perfect square" if num**0.5 == int(num**0.5) else "Not a perfect square"

print(perfect_square(16))
print(perfect_square(25))
print(perfect_square(20))


#  Q 38 :  Write a program to find the sum of the squares of the digits of a number.

def sum_of_squares_of_digits(num):
    sum_squares = 0
    for i in str(num):
        sum_squares+= int(i)**2
    return sum_squares

print(sum_of_squares_of_digits(123))

#  Q 40 : Write a program to keep summing the digits of a number until a single digit is obtained.

def sum_of_digits(num):
    while num > 9:
        num = sum([int(i) for i in str(num)])
    return num

print(sum_of_digits(12345))
print(sum_of_digits(9875))


# Q 41 : Write a program to find the number of occurrences of a specific digit in a number.
def occurance_of_specific_digit(num, digit):
    return str(num).count(str(digit))

print(occurance_of_specific_digit(12345, 5))
print(occurance_of_specific_digit(122333333, 3))
print(occurance_of_specific_digit(123456789, 0))


#  43 :- Write a program to find all divisors of a given number.
def find_all_divisor(num, divisors):
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    return divisors

print(find_all_divisor(6, []))
print(find_all_divisor(28, []))
print(find_all_divisor(12, []))


#  Q 44 : Write a program to calculate the average of numbers in an array.

def average_of_arr(arr):
    return (sum(arr)/len(arr))

print(average_of_arr([1, 2, 3, 4, 5]))


# Q 45:  Write a program to find the mode (most frequent number) in an array.

def mode_of_arr(arr):
    return max(set(arr), key = arr.count)

print(mode_of_arr([1, 2, 3, 4, 5, 5, 5, 5]))

#  Q 46 : Write a program to determine the length of a string without using built-in functions.

def find_length_of_string(string):
    return sum(1 for i in string)

print(find_length_of_string("hello"))
print(find_length_of_string("hello world"))

#  Q 48 : Write a program to find the sum of the prime factors of a given number.

def sum_of_prime_factors(n):
    s = 0  
    for i in range(2, n + 1):  
        if n % i == 0:  # Check if i is a factor
            while n % i == 0:  # Remove all occurrences of i
                n //= i  
            s += i  # Add i to sum once
    return s

# Test cases
print(sum_of_prime_factors(12))  # Output: 5  (2 + 3)
print(sum_of_prime_factors(18))  # Output: 5  (2 + 3)
print(sum_of_prime_factors(15))  # Output: 8  (3 + 5)


#  Q 49 : Write a program to find the second largest number in an array.

def second_largest_num(arr):
    largest_num = 0
    second_largest_num = 0
    if len(arr) < 2:
        return None
    
    for i in arr:
        if i > largest_num:
            second_largest_num = largest_num
            largest_num = i
        elif i > second_largest_num and i != largest_num:
            second_largest_num = i
    return second_largest_num

# Test cases
print(second_largest_num([1, 2, 3, 4, 5]))  # Output: 4
print(second_largest_num([5, 4, 3, 2, 1]))  # Output: 4
print(second_largest_num([1, 2, 3, 16, 12, 19]))  # Output: None

#  Q 50 :  Write a program to find the longest substring without repeating characters in a given string.

def longest_substring(s):
    left = 0
    unique = set()
    max_len = 0
    start_index = 0

    for right in range(len(s)):
        while s[right] in unique:
            unique.remove(s[left])
            left += 1
        
        unique.add(s[right])

        if len(unique)> max_len:
            max_len = len(unique)
            start_index = left
    return s[start_index: start_index + max_len]

print(longest_substring("abcabcbb"))  # Output: abc