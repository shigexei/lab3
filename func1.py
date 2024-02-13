import sympy
from itertools import permutations
import math
import random
#1
'''def gram_to_ounce(g):
    o = 28.3495231 * g
    print(o, "ounces")
a = int(input())
gram_to_ounce(a)
'''
#2
'''
def faren_to_cent(f):
    c = (5/9) *(f-32)
    print(c, "degrees")
a = int(input())
faren_to_cent(a)
'''
#3
'''
def solve(numheads, numlegs):
    chicken_count=0
    rabbit_count=0    
    rabbit_count=(numlegs-2*numheads)/2
    chicken_count=numheads-rabbit_count
    print(int(chicken_count),int(rabbit_count))

solve(35,94)
'''
#4
'''
def filter_prime(a):
    if(sympy.isprime(a)):
        return a
b = input().split()
listprime = []
for i in range(len(b)):
    c = filter_prime(int(b[i]))
    listprime.append(c)
    if(c == None):
        listprime.remove(c)
print(listprime)
'''
#5
'''
def klkl(s):
    perms = [''.join(p) for p in permutations(s)]
    print(perms)
a = input()
klkl(a)
'''
#6
'''

def lklk(s):
    k = s.split()
    print(' '.join(k[::-1]))

a = input()
lklk(a)
'''
#7
'''
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
list = []
for i in range(3):
    a = int(input())
    list.append(a)

print(has_33(list))
'''
#8
'''
def spy_game(nums):
    pos = 0
    
    for num in nums:
        if pos == 0 and num == 0:
            pos = 1
        elif pos == 1 and num == 0:
            pos = 2
        elif pos == 2 and num == 7:
            return True
    
    return False

arr = [1,2,0,4,7,0,8]
print(spy_game(arr))
'''

#9
'''
def vol_sphere(rad):
    return (4/3)*(math.pi * pow(rad,3))

radius = int(input())

print(vol_sphere(radius))
'''

#10
'''
def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
print(unique_elements([1,2,3,4,5,5,4,5,6,7,1,2]))
'''
#11
'''
def is_palindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]
print(is_palindrome("A man a plan a canal Panama"))
'''
#12
'''
def histogram(numbers):
    for num in numbers:
        return("*" * num)

print(histogram([5,9,7]))
'''
#13
'''
def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    secret_number = random.randint(1, 20)
    num_guesses = 0

    while True:
        print("Take a guess.")
        guess = int(input())

        num_guesses += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {num_guesses} guesses!")
            break
'''

