import random
from bs4 import BeautifulSoup
import requests
import os

def get_pic(user_gender):
    if user_gender == "男":
        num = random.randint(1, 4)
        if num == 1:
            response = requests.get(f"https://unsplash.com/collections/ahTYAXJvLNU/asian-woman")
        elif num == 2:
            response = requests.get(f"https://unsplash.com/collections/10445225/woman")
        elif num == 3:
            response = requests.get(f"https://unsplash.com/collections/MjdP2GYVPn8/woman")
        elif num == 4:
            response = requests.get(f"https://unsplash.com/collections/4899620/woman")
    else:
        num = random.randint(1, 4)
        if num == 1:
            response = requests.get(f"https://unsplash.com/collections/10587128/male")
        elif num == 2:
            response = requests.get(f"https://unsplash.com/collections/9676885/male")
        elif num == 3:
            response = requests.get(f"https://unsplash.com/collections/27323894/characters-male")
        elif num == 4:
            response = requests.get(f"https://unsplash.com/collections/57716725/boy")
    soup = BeautifulSoup(response.text, "lxml")

    results = soup.find_all("img", {"class": "YVj9w"}, limit=60)


    image_links = [result.get("src") for result in results]
    num = random.randint(0, len(results)-1)
    return image_links[num]
