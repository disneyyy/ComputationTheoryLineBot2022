import random
from bs4 import BeautifulSoup
import requests
import os

file_name = "crawl_result_malepic.txt"
def get_pic(user_gender):

    if user_gender == "男":
        file_name = "crawl_result_malepic.txt"
        num = random.randint(1, 4)
        if num == 1:
            response = requests.get(f"https://unsplash.com/collections/AX3FuWre3TU/asian")
        elif num == 2:
            response = requests.get(f"https://unsplash.com/collections/10445225/woman")
        elif num == 3:
            response = requests.get(f"https://unsplash.com/collections/MjdP2GYVPn8/woman")
        elif num == 4:
            response = requests.get(f"https://unsplash.com/collections/4899620/woman")

    else:
        file_name = "crawl_result_femalepic.txt"
        num = random.randint(2, 4)
        if num == 2:
            response = requests.get(f"https://unsplash.com/collections/9676885/male")
        elif num == 3:
            response = requests.get(f"https://unsplash.com/collections/27323894/characters-male")
        elif num == 4:
            response = requests.get(f"https://unsplash.com/collections/57716725/boy")

    soup = BeautifulSoup(response.text, "lxml")

    results = soup.find_all("img", {"class": "tB6UZ a5VGX"}, limit=60)

    image_links = [result.get("src") for result in results]
    print(len(image_links))
    if len(image_links) > 50:
        with open(file_name, 'w') as f:
            for i in image_links:
                f.write(i)
                f.write('\n')
        num = random.randint(0, len(results) - 1)
        f.close()
    with open(file_name, 'r') as f:
        image_links = f.readlines()
    for i in image_links:
        i = i.replace('\n', '')
    f.close()
    # print(response.text)
    num = random.randint(0, len(image_links) - 1)
    return image_links[num].replace('\n', '')
