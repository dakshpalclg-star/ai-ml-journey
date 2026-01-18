# 1 --> Check even or odd

def is_even(n1):
    if n1%2==0:
        print(f"{n1} is an even number")
    else:
        print(f"{n1} is not an even number")
# n = int(input("enter the number to check if it is even or odd: "))
# is_even(n)

# --> max of three numbers (there are many methods to do it)
# --> i will do with both of them (i will do with max function and if elif statements. again there are many methods to it)

def max_of_three(a,b,c):
    if a>=b and a>=c:
        print(f"{a} is the greatest of the three")
    elif b>=a and b>=c:
        print(f"{b} is the greatest of the three")
    elif c>=a and c>=b:
        print(f"{c} is the greatest of the three")
# a=int(input("enter the first number"))
# b=int(input("enter the second number"))
# c=int(input("enter the third number"))
# max_of_three(a,b,c)

# Reverse of string

def rev_str(s1):
    print("the reversed string is'", s1[::-1],"'")

# s=input("enter a string to be reversed")
# rev_str(s)

def count_vowels(s2):
    ct = 0
    vowels = "aeiouAEIOU"
    for i in s2:
        if i in vowels:
            ct+=1
    print("number of vowels in the string are:",ct)
# s2 = input("enter the string to find out the number of vowels in it: ")
# count_vowels(s2)