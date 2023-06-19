# Learn Python

## link tham khảo:

-   https://docs.python.org/3/tutorial/datastructures.html
-   https://docs.python.org/3/library/functions.html

## Day 1 - Beginner - Working with Variables in Python to Manage Data

1. String:

```c
print("Nguyễn Tuấn Anh" + " " + "đẹp trai")
```

-   output: Nguyễn Tuấn Anh đẹp trai

2. Input function: hiện câu hỏi và cho phép người dùng nhập tên vào

```c
input("What's your name?")
```

-   output: What's your name?(enter your name)

3. Kết hợp cả 2

```c
print("Hello " + input("What's your name?"))
```

-   output: What's your name?(enter your name)
-   output: Hello (your name)

4. Function len(): in ra size của chuỗi

```c
print(len("SauBanh"))
```

-   output: 7

5. làm cách nào để đặt biến trong python

```c
name = input("What's your name?")
print(name)
```

6. Ví dụ 1 bài về switch giá trị a sang b và b sang a

```c
a = input("a: ")
b = input("b: ")
c = a
a = b
b = c
print("a = " + a)
print("b = " + b)
```

7. tạo một cái câu hỏi cho người dùng nhập sử dụng các kiên thức đã học ở day 1

```c
print("Welcome to the Band Name Generator.")
city = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + city + " " + pet)
```

## Day 2 - Beginner - Understanding Data Types and How to Manipulate Strings

### Datatype

1. String
   print("Hello"[0]) output: H
2. Integer
   print(123 + 456) output: 579
3. Float
   3.123
4. Boolean
   True
   False
5. Lưu ý
   Ta có thể viết như thế này 300*250.5 khi chạy in lên màn hình máy sẽ tự động bỏ qua dấu "*" vào sẽ hiểu đó là con số 300250.5

### Type Eror

-   Trong trường hợp chúng ta sử dụng đoạn code như thế này sẽ bị gặp lỗi vì chúng ta chỉ có thể nối chuỗi với chuỗi chứ không thể nối với số

```c
num_char = len(input("What's your name?"))
print("Your name has" + num_char + " characters")
```

-   Để xem được kiểu dữ liệu của một biến nào đó hãy dùng

```c
print(type(num_char))
```

-   Để khắc phục điều này hãy sử như sau

```c
num_char = len(input("What's your name?"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters")
```

### Ví dụ

```c
a = input("a: ")
b = input("b: ")
print(int(a) + int(b))
```

### Toán tử

1. Cộng: +
2. Trừ: -
3. Nhân: \*
4. Chia: /
5. chia lấy dư: %
6. Mũ: ** (2 mũ 3: 2**3=8)
7. Thứ tự ưu tiên sẽ là (), \*_, _, /, +, -.

### Ví dụ BMI

```c
height = input("Enter your height in m:  ")
weight = input("Enter your weight in kg:  ")

bmi = int(weight)/float(height)**2
print(int(bmi))
```

### Hàm round làm tròn đến số xác định ví dụ: than số thứ 2 sẽ là số làm tròn như ví dụ bên dưới sẽ làm tròn 3 số ngoài

```c
print(round(8/3,3))
```

### Một cách viết khác nhanh hơn khi in ra màn hình

```c
score = 0
height = 1.73
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")
```

```c
age = input("age?")

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left"
print(message)
```

## Day 3 - Beginner - Control Flow and Logical Operators

### Conditional (if else)

```c
height = int(input("height: "))

if height > 170:
    print("You are taller")
else:
    print("You aren't taller")
```

### Ví dụ nhập 1 số là số chẵn hay là số lẻ

```c
a = input("Nhập 1 số bất kỳ:  ")
if int(a)%2 == 0:
    print("Số chẵn")
else:
    print("Số lẻ")
```

### Tạo một bài toán BMI và hiển thị về tình hình sức khỏe

```c
weight = float(input("weight: "))
height = float(input("height: "))
bmi = round(weight/height ** 2)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have a normal weight")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese")
else:
    print(f"Your bmi is {bmi}, you are clinically obese.")
```

### Tạo một bài toán về tính tiền pizza

```c
print("Welcome to Python Pizza:")
size = input("What size pizza do you want? S, M, or L  ")
add_pepperoni = input("Do you want pepperoni? Y or N  ")
extra_cheese = input("Do you want extra cheese? Y or N  ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}")
```

## Day 4 - Beginner - Randomisation and Python Lists

### Cách import một file trong python

1. Tạo một file mới (vd: file.py) và trong file file.py chứa pi

```c
pi = 3.14159246
```

2. tại file cần import gõ import với tên file

```c
import file
print(file.pi)
```

3. output sẽ l hiển thị giá trị của pi

### Thêm hàm random từ thư viện

```c
import random
# randint sẽ random số nguyên từ 1 đến 10
random_integer = random.randint(1, 10)
print(random_integer)
# random sẽ random ra số float từ 0.000000 đến 0.9999999...
random_float = random.random()
print(random_float)
# random sẽ random ra số float từ 0.000000 đến 4.9999999...
random_float = random.random() * 5
print(random_float)
```

### Các tạo mảng trong python

```c
fruits = ["cherry", "Apple", "Pear"]
```

-   Để thêm một thành phần vào mảng cụ thể sử dụng hàm append() vd:

```c
fruits = ["cherry", "Apple", "Pear"]

fruits.append("Banana")

print(fruits)
```

-   để thêm nhiều thành phần vào mảng có thể sử dụng hàm extend() vd:

```c
fruits = ["Cherry", "Apple", "Pear"]

fruits.extend(["Banana", "Watermelon"])

print(fruits)
```

### Hàm split() dùng để cách chuỗi thêm vào mảng

```c
print("Gợi ý món hoa quả ăn hôm nay!")
str = input("Nhập các hoa quả mà hôm nay bạn muốn ăn tôi sẽ giúp bạn chọn 1 món: \n")
str_to_array = str.split(",")
str_length = len(str_to_array)
index_random = random.randint(0, str_length - 1)
print(str_to_array[index_random])
```

### Ví dụ về mảng lồng

```c
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
print(dirty_dozen[1][1])
```

### Đặt bánh kem vào 1 ô bất kỳ

```c
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?")

horizontal = position[0]
vertical = position[1]

map[int(horizontal) - 1][int(vertical) - 1] = "🎂"
print(f"{row1}\n{row2}\n{row3}")
```

## Day 5 - Beginner - Python Loops

### Vòng lặp trong python

```c
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
```

### Hàm range - Python (hàm này cho phép trả về một chuỗi số bắt đầu từ 0 và tăng dần lên 1 cho đến khi đạt được một số cụ thể)

```c
student_heights = input("Input a list of students heights").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
```

-   hàm trên sau khi nhập các giá trị và cách nhau bằng khảng cách thì sẽ tạo ra một mảng vơi các giá trị nhập vừa rồi
-   input: 5 4 6 4 5 5 5 .Thì output sẽ là: [5, 4, 6, 4, 5, 5, 5]

#### Tính chiều cao trung bình ( không sử dụng các hàm sum len chỉ được sử dụng vòng lặp for)

```c
student_heights = input("Input a list of students heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
for height in student_heights:
    total_height += height
print(total_height)

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(number_of_students)

average_height = round(total_height / number_of_students)
print(average_height)
```

#### Hiển thị ra số bé nhất trong và số lớn nhất trong mảng và không sử dụng min max chỉ được sử dụng vòng lặp for

```c
student_scores = input("Input a list of students scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

min_score = 1
max_score = 0
for score in student_scores:
    if score < min_score:
        min_score = score
    if score > max_score:
        max_score = score
print(min_score)
print(max_score)
```

### Tìm hiểu vòng lặp với range

```c
# For Loop with Range
for number in range(1,11,3):
    print(number)
total = 0
for number in range(1,101):
    total += number
print(total)
```

-   Tính tông các số lẻ từ 1 đến 100

```c
total = 0
for number in range(2,101,2):
    total += number
print(total)
# hoặc
total = 0
for number in range(1,101):
    if number % 2 == 0:
        total += number
print(total)
```

## Day 6 - Beginner - Python Functions & Karel

### Hàm trong python

```c
def my_function():
    print("my_function")
my_function()
```

```c
def my_function(n):
    print(f"my_function {n}")
my_function("123")
```

## Day 7 - Beginner - Hangman

## Day 8 - Beginner - Function Parameters & Caesar Cipher

## Day 9 - Beginner - Dictionaries, Nesting and the Secret Auction

## Day 10 - Beginner - Functions with Outputs

## Day 11 - Beginner - The Blackjack Capstone Project

## Day 12 - Beginner - Scope & Number Guessing Game

## Day 13 - Beginner - Debugging: How to Find and Fix Errors in your Code

## Day 14 - Beginner - Higher Lower Game Project

## Day 15 - Intermediate - Local Development Environment Setup & the Coffee Machine

## Day 16 - Intermediate - Object Oriented Programming (OOP)

## Day 17 - Intermediate - The Quiz Project & the Benefits of OOP

## Day 18 - Intermediate - Turtle & the Graphical User Interface (GUI)

## Day 19 - Intermediate - Instances, State and Higher Order Functions

## Day 20 - Intermediate - Build the Snake Game Part 1: Animation & Coordinates

## Day 21 - Intermediate - Build the Snake Game Part 2: Inheritance & List Slicing

## Day 22 - Intermediate - Build Pong: The Famous Arcade Game

## Day 23 - Intermediate - The Turtle Crossing Capstone Project

## Day 24 - Intermediate - Files, Directories and Paths

## Day 25 - Intermediate - Working with CSV Data and the Pandas Library

## Day 26 - Intermediate - List Comprehension and the NATO Alphabet

## Day 27 - Intermediate - Tkinter, \*args, \*\*kwargs and Creating GUI Programs

## Day 28 - Intermediate - Tkinter, Dynamic Typing and the Pomodoro GUI Application

## Day 29 - Intermediate - Building a Password Manager GUI App with Tkinter

## Day 30 - Intermediate - Errors, Exceptions and JSON Data: Improving the Password

## Day 31 - Intermediate - Flash Card App Capstone Project

## Day 32 - Intermediate+ Send Email (smtplib) & Manage Dates (datetime)

## Day 33 - Intermediate+ API Endpoints & API Parameters - ISS Overhead Notifier

## Day 34 - Intermediate+ API Practice - Creating a GUI Quiz App

## Day 35 - Intermediate+ Keys, Authentication & Environment Variables: Send SMS

## Day 36 - Intermediate+ Stock Trading News Alert Project

## Day 37 - Intermediate+ Habit Tracking Project: API Post Requests & Headers

## Day 38 - Intermediate+ Workout Tracking Using Google Sheets

## Day 39 - Intermediate+ Capstone Part 1: Flight Deal Finder

## Day 40 - Intermediate+ Capstone Part 2: Flight Club

## Day 41 - Web Foundation - Introduction to HTML

## Day 42 - Web Foundation - Intermediate HTML

## Day 43 - Web Foundation - Introduction to CSS

## Day 44 - Web Foundation - Intermediate CSS

## Day 45 - Intermediate+ Web Scraping with Beautiful Soup

## Day 46 - Intermediate+ Create a Spotify Playlist using the Musical Time Machine

## Day 47 - Intermediate+ Create an Automated Amazon Price Tracker

## Day 48 - Intermediate+ Selenium Webdriver Browser and Game Playing Bot

## Day 49 - Intermediate+ Automating Job Applications on LinkedIn

## Day 50 - Intermediate+ Auto Tinder Swiping Bot

## Day 51 - Intermediate+ Internet Speed Twitter Complaint Bot

## Day 52 - Intermediate+ Instagram Follower Bot

## Day 53 - Intermediate+ Web Scraping Capstone - Data Entry Job Automation

## Day 54 - Intermediate+ Introduction to Web Development with Flask

## Day 55 - Intermediate+ HTML & URL Parsing in Flask and the Higher Lower Game

## Day 56 - Intermediate+ Rendering HTML/Static files and Using Website Templates

## Day 57 - Intermediate+ Templating with Jinja in Flask Applications

## Day 58 - Web Foundation Bootstrap

## Day 59 - Advanced - Blog Capstone Project Part 2 - Adding Styling

## Day 60 - Advanced - Make POST Requests with Flask and HTML Forms

## Day 61 - Advanced - Building Advanced Forms with Flask-WTForms

## Day 62 - Advanced - Flask, WTForms, Bootstrap and CSV - Coffee & Wifi Project

## Day 63 - Advanced - Databases and with SQLite and SQLAlchemy

## Day 64 - Advanced -My Top 10 Movies Website

## Day 65 - Web Design School - How to Create a Website that People will Love

## Day 66 - Advanced - Building Your Own API with RESTful Routing

## Day 67 - Advanced - Blog Capstone Project Part 3 - RESTful Routing

## Day 68 - Advanced - Authentication with Flask

## Day 69 - Advanced - Blog Capstone Project Part 4 - Adding Users

## Day 70 - Advanced - Deploying Your Web Application with Heroku

## Day 71 - Advanced - Data Exploration with Pandas: College Major v.s. Your Salary

## Day 72 - Advanced - Data Visualisation with Matplotlib: Programming Languages

## Day 73 - Advanced - Aggregate & Merge Data with Pandas: Analyse the LEGO Dataset

## Day 74 - Advanced - Google Trends Data: Resampling and Visualising Time Series

## Day 75 - Advanced - Beautiful Plotly Charts & Analysing the Android App Store

## Day 76 - Advanced - Computation with NumPy and N-Dimensional Arrays

## Day 77 - Advanced - Linear Regression and Data Visualisation with Seaborn

## Day 78 - Advanced - Analysing the Nobel Prize with Plotly, Matplotlib & Seaborn

## Day 79 - Advanced - The Tragic Discovery of Handwashing: t-Tests & Distributions

## Day 80 - Advanced - Capstone Project - Predict House Prices

## Day 81 - Professional Portfolio Project - [Python Scripting]

## Day 82 - Professional Portfolio Project - [Python Web Development]

## Day 83 - Professional Portfolio Project - [Python Scripting]

## Day 84 - Professional Portfolio Project - [GUI]

## Day 85 - Professional Portfolio Project - [GUI]

## Day 85 - Professional Portfolio Project - [GUI]

## Day 87 - Professional Portfolio Project - [Web Development]

## Day 88 - Professional Portfolio Project - [Web Development]

## Day 89 - Professional Portfolio Project - [GUI Desktop App]

## Day 90 - Professional Portfolio Project - [HTTP Requests & APIs]

## Day 91 - Professional Portfolio Project - [Image Processing & Data Science]

## Day 92 - Professional Portfolio Project - [Web Scraping]

## Day 93 - Professional Portfolio Project - [GUI Automation]

## Day 94 - Professional Portfolio Project - [Game]

## Day 95 - Professional Portfolio Project - [HTTP Requests & APIs]

## Day 96 - Professional Portfolio Project - [Web Development]

## Day 97 - Professional Portfolio Project - [Python Automation]

## Day 98 - Professional Portfolio Project - [Data Science]

## Day 99 - Professional Portfolio Project - [Data Science]

## Day 100 - Professional Portfolio Project - [Data Science]

## Final Stretch
