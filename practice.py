x = 3.14
y = -0.001
z = 1e3   # 1 × 10^3 = 1000.0

type(x)   # <class 'float'>
type(z)   # <class 'float'>
print("x:", x)
print("y:", y)
print("z:", z)
print("Type of x:", type(x))
print("Type of z:", type(z))
print("Type of y:", type(y))
#-------------------------------------
is_adult = True
logged_in = False
print("is_adult:", is_adult)
print("logged_in:", logged_in) 
print("Type of is_adult:", type(is_adult))
print("Type of logged_in:", type(logged_in))
#------------------------------------- 
10 > 3      # True
5 == 7      # False
print("10 > 3:", 10 > 3)
print("5 == 7:", 5 == 7)
#-------------------------------------
name = "Balaji"
greet = 'Hello'
line = "I'm learning Python"
print("name:", name)
print("greet:", greet)  
print("line:", line)
print("Type of name:", type(name))  
print("Type of greet:", type(greet))
print("Type of line:", type(line))
#-------------------------------------
"Hi" + " " + "there"    # 'Hi there'
"ha" * 3                # 'hahaha'
print('"Hi" + " " + "there":', "Hi" + " " + "there")
print('"ha" * 3:', "ha" * 3) 
#-------------------------------------
nums = [10, 20, 30]
stuff = [1, "two", 3.0, True]

nums[0]      # 10
nums.append(40)
print("nums:", nums)            # Output: [10, 20, 30, 40]
print("stuff:", stuff)
#-------------------------------------
point = (10, 20)
print("point:", point)           # Output: (10, 20)
print("Type of point:", type(point))  # <class 'tuple'>
#-------------------------------------   
person = {
    "name": "Balaji",
    "role": "Developer",
    "experience": 5
}

person["name"]       # 'Balaji'
person["experience"] # 5
print("person:", person)    
print("Type of person:", type(person))  # <class 'dict'>
print("Experience:", person["experience"])
print("type of experience:", type(person["experience"]))
#-------------------------------------
s = {1, 2, 2, 3}
# s is {1, 2, 3}
print("s:", s)                  # Output: {1, 2, 3}
print("Type of s:", type(s))    # <class 'set'>
#-------------------------------------
x = 25

y = 3.0

name = "Python"

flag = 5 > 3

items = [1, 2, 3]

coords = (1, 2)

student = {"name": "Ram", "age": 20}

unique = {1, 1, 2, 3}

nothing = None
print("Type of x:", type(x))               # <class 'int'>
print("Type of y:", type(y))               # <class 'float'>    
print("Type of name:", type(name))         # <class 'str'>
print("Type of flag:", type(flag))         # <class 'bool'>
print("Type of items:", type(items))       # <class 'list'>
print("Type of coords:", type(coords))     # <class 'tuple'>
print("Type of student:", type(student))   # <class 'dict'>
print("Type of unique:", type(unique))     # <class 'set'>
print("Type of nothing:", type(nothing))   # <class 'NoneType'>
#-------------------------------------
x = 10
x = 20        # now x is 20
x = "hello"   # now x is a string
print("x:", x)
#-------------------------------------
a, b = 10, 20
x = y = z = 0
print("a:", a)
print("b:", b)
print("x:", x)
print("y:", y)
print("z:", z)
a, b = b, a
print("After swapping - a:", a)
print("After swapping - b:", b)
#-------------------------------------
a = 10
b = 3
addition = a + b          # 13
print("Addition:", addition)
subtraction = a - b       # 7
print("Subtraction:", subtraction)
multiplication = a * b    # 30
print("Multiplication:", multiplication)
division = a / b         # 3.3333...
print("Division:", division)
floor_div = a // b      # 3
print("Floor Division:", floor_div)
modulus = a % b         # 1
print("Modulus:", modulus)
exponent = a ** b      # 1000
print("Exponentiation:", exponent)
#-------------------------------------
print(7/2)
print(7//2)
print(-7/2)
print(-7//2)
#-------------------------------------
print(2**3)
print(9**0.5)
print(27**(1/3))
#-------------------------------------
abs(-10)          # 10
round(3.14159, 2) # 3.14
max(1, 5, 2)      # 5
min(1, 5, 2)      # 1
print("Absolute value of -10:", abs(-10))
print("3.14159 rounded to 2 decimal places:", round(3.14159, 2))
print("Maximum of (1, 5, 2):", max(1, 5, 2))
print("Minimum of (1, 5, 2):", min(1, 5, 2))
#-------------------------------------
int(3.9)        # 3       (truncates)
float(5)        # 5.0
str(123)        # '123'
int("10")       # 10
float("3.14")   # 3.14
print("int(3.9):", int(3.9))
print("float(5):", float(5))
print("str(123):", str(123))
print('int("10"):', int("10"))
print('float("3.14"):', float("3.14"))
#-------------------------------------
x = 10
y += 5   # x = x + 5 → 15
z -= 2   # 13
a *= 3   # 39
b /= 3   # 13.0
c=10
c **= 2  # 169.0
print("Final value of x:", x)
print("Final value of y:", y)
print("Final value of z:", z)
print("Final value of a:", a)
print("Final value of b:", b)
print("Final value of c:", c)
#-------------------------------------
result = 2 + 3 * 4      # 2 + 12 = 14
result = (2 + 3) * 4    # 5 * 4 = 20
print("2 + 3 * 4 =", 2 + 3 * 4)
print("(2 + 3) * 4 =", (2 + 3) * 4)