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

# results = {}

# from requests import get

# websites = (
#   "google.com",
#   "https://airbnb.com",
#   "facebook.com",
#   "naver.com",
#   "nexon.com"
# )

# for website in websites:
#   if not website.startswith("https://"):
#     website = f"https://{website}"
#   response = get(website)
#   if response.status_code == 200 :
#     results[website] = "OK"
#   else :
#     results[website] = "NOT OK"

# print(results)



# import requests

# movie_ids = [
#     238,
#     680,
#     550,
#     185,
#     641,
#     515042,
#     152532,
#     120467,
#     872585,
#     906126,
#     840430
# ]

# x = 0


# for movie_address in movie_ids:

#   movie = f"https://nomad-movies.nomadcoders.workers.dev/movies/{movie_ids[x]}"
#   response = requests.get(movie)
#   data = response.json()
#   print("title : ", data.get("original_title"),"\n")
#   print("status : ", data.get("status"),"\n")
#   print("release_date : ", data.get("release_date"),"\n")
#   print("overview : ", data.get("overview"),"\n")
#   print("original_language : ", data.get("original_language"),"\n")
#   print("vote_average : ", data.get("vote_average"),"\n")
#   print("-----------------------------------------------------------------------\n")

#   x = x+1


# Jioh = {
#   "name" : " Jioh",
#   "XP" : 1000,
#   "team" : "tean X"
# }
# def create_player_for_team(name, xp team:)

# def create_player(name, xp, team):
#   return {
#     "name" : name,
#     "XP" : xp,
#     "team" : team
#   }
# def introduce_player(player):
#   name = player["name"]
#   team = player["team"]
#   print(f"Hello! my name is {name} and I play for {team}.")

# Jioh = creat_player("Jioh", 1000, "tean X")
# class dog:
  
#   def __init__(self, name, breed, age):
#     self.name = name
#     self.breed = breed
#     self.age = age

#   def sleep(self):
#     print("zzzzz....")

# class GuardDog(dog):
#   # def __init__(self, name, breed):
#   #   self.name = name
#   #   self.age = 5
#   #   self.breed = breed

#   def __init__(self, name, breed):
#     super().__init__(name, breed, 5)

#     self.aggresive = True
  
#   def rrrrr(self):
#     print("stay away!")

# class puppy(dog): 
  
#   def __init__(self, name, breed):
#     super().__init__(name, breed, 0.1)

#     self.spoiled = True
#   #   self.name = name
#   #   self.age = 0.1 
#   #   self.breed = breed

#   # def __str__(self):
#   #   return f"{self.breed} puppy named {self.name}."

#   def woof_woof(self):
#     print("woof woof!")

#   # def introduce(self):
#   #   self.woof_woof()
#   #   print(f"My name is {self.name} and I am a baby {self.breed}")
#   #   self.woof_woof()

# ruffus = puppy(name = "ruffus", breed = "beagle",)
# bibi = GuardDog(name = "bibi", breed = "dalmathian",)

# ruffus.sleep()

# bibi.sleep()

# class player:

#   def __init__(self, name, team):
#     self.name = name
#     self.xp = 1500
#     self.team = team

#   def introduce(self):
#     print(f"Hello I am {self.name} and I play for {self.team}.")

# class team:

#   def __init__(self, team_name):
#     self.teamname = team_name
#     self.players = []

#   def show_players(self):
#     for player in self.players:
#       player.introduce()
  
#   def add_player(self, name):
#     new_player = player(name, self.teamname)
#     self.players.append(new_player)


# team_X = team("team X")

# team_X.add_player("Jioh")

# team_blue = team("team blue")

# team_blue.add_player("Yeon")

# team_blue.show_players()

# import requests
# from bs4 import BeautifulSoup


# all_jobs = []




def scrape_page(url):
  print(f"Scrapping{url}...")
  response = requests.get(url)

  soup = BeautifulSoup(response.content, "html.parser",)

  jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

  for job in jobs:
    title = job.find("span", class_="title").text
    company, position, region = job.find_all("span", class_="company")

    url = job.find("div", class_="tooltip").next_sibling["href"]

    job_data = {
      "title" : title,
      "company" : company.text,
      "position" : position.text,
      "region" : region.text,
      "url" : f"https://weworkremotely.com{url}",
    }
    all_jobs.append(job_data)

def get_pages(url):
  response = requests.get(url)

  soup = BeautifulSoup(response.content, "html.parser")

  return len(soup.find("div", class_="pagination").find_all("span",class_="page"))

total_pages = get_pages("https://weworkremotely.com/remote-full-time-jobs?page=1")

for x in range(total_pages):
  url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
  scrape_page(url)

print(len(all_jobs))


keywords = ["flutter", "python", "golang"]

r = requests.get(
    "https://remoteok.com/remote-flutter-jobs",
    headers={
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Whale/3.24.223.21 Safari/537.36"
    })

print(r.status_code)


from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from file import save_to_file

keyword = input("What do you want to search for?")

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
jobs = indeed + wwr

save_to_file(keyword, jobs)