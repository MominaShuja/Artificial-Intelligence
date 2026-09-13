# ============================================================
# Page 1 - Basic Python Syntax
# ============================================================
print("Hello, World!")


# ============================================================
# Page 2 - Comments and Input / Output
# ============================================================

x = 1
# The initial value of x is 1.
if x > 0:
    print("These are two comments")  # Print a string.

txt = input("Enter a number: ")
print(txt)


# ============================================================
# Page 3 - Multiple Statements on a Single Line
# ============================================================

print("Statement1")
print("Statement2")

# You can write the above two statements in the following way:
print("Statement1"); print("Statement2")


# ============================================================
# Page 4 - Indentation
# ============================================================
x = 1
if x > 0:
 print("This statement has a single space Indentation")
 print("This statement has a single space Indentation")


# ============================================================
# Page 5 - Tab / Mixed Indentation Examples
# ============================================================
x = 1
if x > 0:
	print("This statement has a single tab Indentation")
	print("This statement has a single tab Indentation")



# ============================================================
# Page 8 - Numeric Data Types
# ============================================================

a = 1452
type(a)

b = (-4587)
type(b)

c = 0
type(c)

g = 1.03
type(g)

h = -11.23
type(g)

i = .34
type(i)

j = 2.12e-10
type(j)

k = 5E220
type(k)


# ============================================================
# Page 9 - Complex Numbers
# ============================================================

x = complex(i, 2)
type(x)
print(x)

z = 1 + 2j
type(z)

z = 1 + 2j
type(z)


# ============================================================
# Page 9 - Boolean (bool)
# ============================================================

x = True
type(x)

y = False
type(y)


# ============================================================
# Page 10 - Strings
# ============================================================

str1 = "String"  # Strings start and end with double quotes
print(str1)

str2 = "String"  # Strings start and end with single quotes
print(str2)


str2 = "Day's"  # Single quote within double quotes
print(str2)

str2 = 'Day"s'  # Double quote within single quotes
print(str2)


# ============================================================
# Page 11 - Special Characters in Strings
# ============================================================

print("The is a backslash (\\) mark.")
print("This is tab \t key")
print("These are \'single quotes\'")
print("These are \"double quotes\"")
print("This is a new line\nNew line")


# ============================================================
# Page 11-12 - String Indices and Accessing String Elements
# ============================================================

string1 = "PYTHON TUTORIAL"

print(string1[0])    # Print first character
print(string1[-15])  # Print first character
print(string1[14])   # Print last character
print(string1[-1])   # Print last character
print(string1[4])    # Print 4th character
print(string1[-11])  # Print 4th character

# Original PDF example produces an IndexError:
# print(string1[16])  # Out of index range


# ============================================================
# Page 13 - Creating Lists
# ============================================================

my_list1 = [5, 12, 13, 14]  # the list contains all integer values
print(my_list1)

my_list2 = ['red', 'blue', 'black', 'white']  # the list contains all string values
print(my_list2)

my_list3 = ['red', 12, 112.12]  # the list contains a string, an integer and a float values
print(my_list3)

my_list = []
print(my_list)

color_list = ["RED", "Blue", "Green", "Black"]


# ============================================================
# Page 14 - List Indices
# ============================================================

color_list = ["RED", "Blue", "Green", "Black"]  # The List have four elements indices start at 0 and end at 3

color_list[0]  # Return the First Element
print(color_list[0], color_list[3])  # Print First and Last Elements
color_list[-1]  # Return Last Element


# ============================================================
# Page 15 - List Slicing
# ============================================================

color_list = ["RED", "Blue", "Green", "Black"]  # The List have four elements indices start at 0 and end at 3

print(color_list[0:2])  # cut first two items
print(color_list[1:2])  # Cut second item
print(color_list[1:-2])  # Cut second item
print(color_list[:3])  # Cut first three items
print(color_list[:])  # Creates copy of original List


# ============================================================
# Page 15 - Conditional Statements
# ============================================================

if b > a:
    print("b is greater than a")
