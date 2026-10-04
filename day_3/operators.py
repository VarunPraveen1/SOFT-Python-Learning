# Day 3: Operators

age = 22
print(age)

height = 5.8
print(height)

complex_number = 3 + 4j
print(complex_number)

base = 20
height = 10

area = 0.5 * base * height

print(area)

side_a = 5
side_b = 4
side_c = 3

perimeter = side_a + side_b + side_c

print(perimeter)

length = 10
width = 20

area = length * width

print(area)

length = 10
width = 20

perimeter = 2 * (length + width)

print(perimeter)

radius = 7

area = 3.14 * radius * radius

print(area)

radius = 7

circumference = 2 * 3.14 * radius

print(circumference)

x1 = 0
y1 = -2
x2 = 1
y2 = 0

slope = (y2 - y1) / (x2 - x1)
x_intercept = 1
y_intercept = -2

print("Slope:", slope)
print("X-intercept:", x_intercept)
print("Y-intercept:", y_intercept)

x1, y1 = 2, 2
x2, y2 = 6, 10

slope = (y2 - y1) / (x2 - x1)

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print("Slope:", slope)
print("Euclidean distance:", distance)

slope_1 = 2
slope_2 = 2

print(slope_1 == slope_2)

x = -3

y = x ** 2 + 6 * x + 9

print(y)

print(7 // 3 == int(2.7))

print(type('10') == type(10))

print(9.8 == '9.8')

number = 10

print(number % 2 == 0)

print(7 // 3 == int(2.7))

print(type('10') == type(10))

print(int(float('9.8')) == 10)

hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))

weekly_earning = hours * rate

print("Your weekly earning is", weekly_earning)

years = int(input("Enter number of years you have lived: "))

seconds = years * 365 * 24 * 60 * 60

print("You have lived for", seconds, "seconds.")

print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)

print(len("python"))
print(len("dragon"))

print(len("python") == len("dragon"))

print("on" in "python" and "on" in "dragon")

sentence = "I hope this course is not full of jargon"

print("jargon" in sentence)

print(not ("on" in "dragon" and "on" in "python"))

length = len("python")

length_float = float(length)
length_string = str(length_float)

print(length)
print(length_float)
print(length_string)