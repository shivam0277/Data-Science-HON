#data type

name = "Shivam"
print(type(name))  # Output: <class 'str'>
print(isinstance(name, str))  # Output: True

age = 25
print(type(age))  # Output: <class 'int'>
print(isinstance(age, int))  # Output: True

number = "25"
age = int(number)
print(type(age))  # Output: <class 'int'> 

x = range(10)
#display x:
print(x)
#convert to list to display the content of x:
print(list(x))
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


x = {"name" : "John", "age" : 36}
#display x:
print(x)
#display the data type of x:
print(type(x)) 





#while loop
# Print numbers from 1 to 5 using while loop
num = 1
while num <= 5:
    print(num)
    num += 1
# Output: 1 2 3 4 5


# Stop when number is 3
for i in range(1, 6):
    if i == 3:
        break
    print(i)
# Output: 1 2


# Skip number 3
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
# Output: 1 2 4 5


#basic try and except
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except:
    print("Invalid input! Please enter a valid number.")


try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("That's not a number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")


try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Division successful!")   # runs only if no exception
finally:
    print("Program finished.")      # runs no matter what

# for input 2
# 5.0
# Division successful!
# Program finished.


name = "Beapu"
print(name.lower())    # Output: beapu
print("au" in name) 

name = 'Be\nau'
print(name)
print(name[0])
print(name[-1])
print(name[1:2]) 
print(name[5:0])


done=""
if done:
    print("yes")
else:
    print("no")

num1 = 2+3j
num2 = complex(2,3)
print(num2.real, num2.imag)


print(abs(-5.5)) # Output: 5.5
print(round(5.49)) #Output:5
print(round(5.5)) #Output:6

#Casting
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

print("He is called 'Johnny'")
print('He is called "Johnny"')

#You can assign a multiline string to a variable by using three quotes.
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

txt = "The best things in life are free!"
print("free" in txt)
#True







