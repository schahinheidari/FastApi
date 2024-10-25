import json
import requests


response_numbers = requests.get("http://numbersapi.com/13")
print("api numbers :",response_numbers.text)

response_numbers = requests.get("https://goweather.herokuapp.com/weather/Sarkhon")
print("api weather :",response_numbers.text)

# response_fruit = requests.get("https://www.fruityvice.com/api/fruit/banana")
# print("api fruit :", json.loads(response_fruit.text))

response_Harry_Potte = requests.get("https://hp-api.onrender.com/api/characters")
print("api Harry Potter :",json.loads(response_Harry_Potte.text))
