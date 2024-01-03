

'''import builtins

# Get the names of all built-in functions
functions = [obj for obj in dir(builtins) if isinstance(getattr(builtins, obj), type(print))]

# Print the names of all built-in functions
for function in functions:
    print(function)


x = 5
y = "Hello"
z = [1, 2, 3]

print(isinstance(x, int))    # True, x is an instance of the int class
print(isinstance(y, str))    # True, y is an instance of the str class
print(isinstance(z, list))   # True, z is an instance of the list class
print(isinstance(x, str)) 


print("First\tSecond\tThird")

import tkinter as tk

def on_label_click():
    # Perform some action when the label is clicked
    print("sorry!")

root = tk.Tk()

my_variable = "sorry!"
label = tk.Label(root, text=my_variable, fg="blue", cursor="hand2")
label.pack()

label.bind("<Button-1>", lambda event: on_label_click())

root.mainloop()'''



'''marks = ('12','343','54','6656','56')
index = 0
for index,mark in enumerate(marks):
    print(mark)
    if(index ==0):
        print('harry')
    index+=1'''

'''import string
import random
a = string.ascii_letters
n = int(input())
for i in range(n):
    L = []
    for j in range(n):
        L.append(random.choice(a))

    for element in L:
        print(element,end=('\t'))

    print()'''


'''import random
L = []
for i in range(10):
    L.append(random.randint(0,10))

L.sort()
L.reverse()
print(L)
'''
'''#prime number :
for i in range(2,101):
    flag = 0
    for j in range(2,i):
        if(i%j == 0):
            flag = 1
            break
    if(flag == 0):
            print(i)'''

'''def find_vowels(input_string):
    vowels = "aeiouAEIOU"  # List of lowercase and uppercase vowels
    vowel_list = []  # To store the vowels found in the string

    for char in input_string:
        if char in vowels:
            vowel_list.append(char)

    return vowel_list

# Example usage
input_str = "Hello, World!"
result = find_vowels(input_str)
print("Vowels found:", result)'''


def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = s.lower()  # Convert the input string to lowercase
    for char in alphabet:
        if char not in s:
            return False
    return True
s = "The quick brown fox jumps over the lazy dog"
print(s)
print(is_pangram(s))

'''def is_pangram(s):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    s = s.lower()  # Convert the input string to lowercase
    s_chars = set(s)
    return alphabet.issubset(s_chars)
input_string = "The quick brown fox jumps over the lazy dog"
print(is_pangram(input_string))'''

