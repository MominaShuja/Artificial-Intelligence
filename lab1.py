#-----------------Simple code --------------------------
print("Hello World!")

#--------------------single tab indentation----------------
n = 2
if n>1:
    print("This statement has single tab indentation")
    print("This statement has single tab indentation")

#--------------------double tab indentation----------------
if n>1:
        print("This statement has double tab indentation")
        print("This statement has double tab indentation")

x = 1
# this is the x-COMMENTS
if x>0:
    print("the x is positive")


#-------------- Input -----------------------
no = input("Enter any number : ")
print("The number is " , no)

#-------------Multiple output displaying--------------
print("Statement1") ; print("Statement2")



#--------------Auto Data type assign
l = 20
print(type(l))
m="Hello"
print(type(m))
n=3.5
print(type(n))
o = True
print(type(o))

#------------------Complex Data type--------------
j = complex(2,4)
print(type(j))


#-------------Special String-------------------
print("The text moves to \n to new line")
print("The text moves to \t to new TAB")
print("The text moves to \\ to new backslash")
print("The text moves to \' to new Single Quote")
print("The text moves to \" to new double Quote")


#-------------Character Accessing----------------------
sub = "Human Interaction"
print(sub[0])
print(sub[2])
print(sub[4])
print(sub[-1])
print(sub[-3])
print(sub[-6])


#-------------SLICING---------------
colors = ["red" , "Pink" , "Blue" , "Green" , "Purple"]
print(colors[0:2])
print(colors)
print(colors[1:-3])
