# print("Hello world!")

# a = 2
# b = 3
# c = a + b
# print(c)

# my_name = "Jioh"
# age = 28
# dead = False
# print("hello my name is", my_name)
# print("and I'm ", age, " years old")

# print("asdf")
# print(True)
# print("hello")
# print(12)

# def say_hello(name, age= 28):
#   print("hello", name)
#   print("You are", age , "years old")

# say_hello("jioh", 28)
# # say_hello(input("what your name?"))

# def say_bye():
#   print("bye bye")


# def tax_calculator(pay):
#   return pay * 0.35

# def pay_tax(tax):
#   print("thank you for paying", tax)

# to_pay = tax_calculator(1500000)
# pay_tax(to_pay)

# tax_calculator(input("How much money did you make this year? $ "))

# # 1/24
# def say_hello(name = "anonymous"):
#   print("Hello", name)

# say_hello("Jioh")
# say_hello()

# def plus(a,b):
#   print(a + b)


# def pay_tax(tax):
#   print("thank you for paying", tax)

# to_pay = tax_calculator(1500000)
# pay_tax(to_pay)

# my_name = "Jioh"
# my_age = 28
# my_color_eyes = "brown"

# print(f"Hello i'm {my_name}, I have {my_age} years old, {my_color_eyes} is my eye color.")

# def make_juice(fruit):
#   return f"{fruit} + J"

# def add_ice(juice):
#   return f"{juice} + I"

# def add_sugar(ice_juice):
#   return f"{ice_juice} + S"

# juice = make_juice("사과")
# cold_juice = add_ice(juice)
# perfect_juice = add_sugar(cold_juice)

# print(perfect_juice)


# from random import randint

# print("welcome to Python Casino")
# pc_choice = randint(1,50)

# playing = True

# while playing:
#   user_choice = int(input("Choose number:"))
  
#   if user_choice == pc_choice:
#     print("You win!")
#     playing = False
#   elif user_choice > pc_choice:
#     print("Lower! Computer chose" , pc_choice)
  
#   elif user_choice < pc_choice:
#     print("Higher! Computer chose" , pc_choice)

# 1/26

# days_of_week = ["mon","tue","wed","thur","fri"] #리스트는 ㅈ대로 만들 수 있다. 불리언 스트링 인티저 리스트안리스트..
# print(days_of_week)


# days_of_week.append("sat")
# print(days_of_week)
# days_of_week.append("sun")
# print(days_of_week)

# days_of_week.remove("fri")
# print(days_of_week)

# print(days_of_week[4]) 

# name = "jioh"
# print(name.endswith("h"))


# days = ("mon", "tue","wed")    #변경불가능한 리스트 튜플.
# print(days[0])

# player = {# 여러 형식의 키워드를 저장할 수 있음 , 딕셔너리는 많은 속성들을 가지고 있는 데이터를 만들 때 쓰인다.
#   'name': 'jioh',
#   'age': 28,
#   'alive': True,
#   'fav_food': ["BUR" , "HAM"]
# }
# player['fav_food'].append("NOO")
# print(player.get('fav_food')[0])
# print(player['fav_food'])


# print(player.get('age'))
# print(player.get('fav_food')[0])

# print(player)
# player.pop('age')
# print(player)

# print(player)
# player["xp"] = 1500
# print(player)

# numbers = [5,3,1,5,"true",True]
# numbers.append(["A","B"])
# print(numbers[-1][0])


# player = {
#   "name": "jioh",
#   "age": 28,
#   "alive": True,
#   "fav_food": ("BUR" , "HAM"),
#   "friend": {
#     "name": "Yeon",
#     "fav_food": ["APP"]
#   }
# }
# player["fav_food"] = "APP"
# player.pop("alive")
# player["friend"]["fav_food"].append("BUR")


# print(player["fav_food"])
# print(player["friend"]["fav_food"])


websites = (
  "goole.com",
  "https://airbnb.com",
  "facebook.com"
)

for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"
  print(website)