# comments

# variable

print('hello world')
print('sainaveen')

name ='Hare krishna'
age = 25
print(name)
print(age)
full_name = 'Harekrishna'
print(full_name)

width, height = 400, 500
print(width)
print(height)

your_name = input('please enter your name: ')
print(your_name)
print('hi' + your_name)

num1 =  input('enter a number: ')
num2 =  input('enter a number: ')

print(num1 + num2)
print(int(num1) + int(num2))


# DATA TYPES
# strings
# int(1,2,3,4), float/decimal (0.2) (number)

# string 'hello', "cookie" => "hellocookie"
# string '10', "20" =>  "1020"
# math operators (+,-,*,**,/,//,%)
# tip calculater
food_amount = float(input('Enter food amount $: '))
tip_percentage = float(input('Enter your tip percentage %: '))/100
tip_amount = food_amount * tip_percentage
print(tip_amount)
# total  food_amount + tip_amount
total = food_amount + tip_amount
print('-----------------------------------')
print(f'🥗 Food Amount: ${food_amount}')
print(f'⚖ Tip Amount:  ${tip_amount}')
print('\n')
print(f'💰 Total Amount: ${total}')
print('------------------------------------')
print('$'+ str(total))


# string formating

print("-------------------")

# BOOLEAN (True, False)
# IF THEN ELSE

# if withdrawal amount > balance:
#    don't allow withdraw
# else:
#     allow withdrawl

# Baby wather app
weather = 'rain'

if weather == 'rain':
    print("☔")
else:
    print('😃')

weather1 = input("How is the weather?")

if weather1 == 'rain':
  print("it's raining ☔")
elif weather1 == 'coudy':
  print("it's cloudy  ⛈")
elif weather1 == 'sunny':
  print("it's sunny  ☀")
elif weather1 == 'tunderstome':
  print("it's tunderstome ⛈")
else:
  print('😎')


# comparison operators (==, <, >, <=, >=)

# comparison operators (==, <, >, <=, >=)

score = float(input("Enter your score: "))

if score >=90:

  print("You are in A grade")

elif score >=80:
  print("you are in B grade")

elif score >=70:
  print("you are in c grade")

elif score >=60:
  print("you are in D grade")

elif score < 60:
  print("You are in F grade")

else:
  print(" you scored very low to give you a grade")

print("---------------------------------------")


# eiter a SUPER PASS  passing grade or a failing grade
# SUPER PASS > 100

score = 80
if score >=60 and score <= 100: # this is the regular way of writing the pythonic code
  print("passing grade")


#  we can write the python code in a simple manner
# Example for a simple code by not using the "and" boolean  key word
if 60 <= score <= 100: # pythonic way o fwriting the code
  print("passing grade")


## Function ##
# function with no Arguments
def say_my_name():
  print("Naveen")
  print("john")
  print("Sam")

say_my_name()

# function with one Argument
def say_my_name2(name):
  print(name)

say_my_name2("sainaveen")

# function with Multipule Arguments
# Default Arguments
def greeting(name, greet='aloha'):
    print(f'Hey!🤞 {greet} {name}!')
    '''
     greeting takes in 2 arguments, greet & name
     and it greets the user

     >>>greeting('aloha', 'naveen')
     Hey!🤞 aloha Naveen
     '''
# postional Arguments
greeting('naveen', 'hello')

# named Arguments

greeting(name = "naveen", greet = 'hi')










