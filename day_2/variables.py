challenge = "30 Days Of Python"
print(challenge)
print(len(challenge))

company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.title())
print(company[:6])
print(company.replace("Coding", "Python"))
print("Coding" in company)
print("Python for Everyone".replace("Everyone", "All"))
print(company.split())
print(company[0])
print(company[-1])
print(company[10])
words = "Python For Everyone".split()
print(words[0][0] + words[1][0] + words[2][0])
words = company.split()
print(words[0][0] + words[1][0] + words[2][0])
print(company.index("C"))
print(company.index("F"))
print("Coding For All People".rfind("l"))
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.index("because"))
print(sentence.rindex("because"))
print(company.startswith("Coding"))
print(company.endswith("coding"))
text = "   Coding For All      "
print(text.strip())
print(type(challenge))

# Day 2: 30 Days of python programming

first_name = "Varun"
last_name = "Praveen"
full_name = "Varun Praveen"
country = "India"
city = "Kochi"
age = 18
year = 2026
is_married = False
is_true = True
is_light_on = True

first_name, last_name, country, age = "Varun", "Praveen", "India", 18

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(first_name))
print(len(first_name) > len(last_name))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)

radius = 30
area_of_circle = 3.14 * radius ** 2

print(area_of_circle)
circum_of_circle = 2 * 3.14 * radius

print(circum_of_circle)

radius = float(input("Enter the radius of the circle: "))
area = 3.14 * radius ** 2

print("Area of the circle:", area)

base = 20
height = 10

area_of_triangle = 0.5 * base * height

print("Area of the triangle:", area_of_triangle)

a = 5
b = 4
c = 3

perimeter_of_triangle = a + b + c

print("Perimeter of the triangle:", perimeter_of_triangle)

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")

print(first_name)
print(last_name)
print(country)
print(age)

help("keywords")

# Level 3

# Equation: y = 2x - 2
slope = 2
y_intercept = -2
x_intercept = 1

print("Slope:", slope)
print("Y-intercept:", y_intercept)
print("X-intercept:", x_intercept)

x1, y1 = 2, 2
x2, y2 = 6, 10

slope = (y2 - y1) / (x2 - x1)

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print("Slope:", slope)
print("Euclidean distance:", distance)

x = -3
y = x ** 2 + 6 * x + 9

print("y =", y)

sentence = "I hope this course is not full of jargon"

words = sentence.split()

print("Number of words:", len(words))