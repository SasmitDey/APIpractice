from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import api



def APOD():
    url = "https://apod.nasa.gov/apod"
    
    params = {
        'api_key': api.secret_nasa_key

    }

    req = requests.get(url, params=params)

    sp = BeautifulSoup(req.content, 'html.parser')
    img_tag = sp.img.get('src')
    img_url = "https://apod.nasa.gov/apod/" + img_tag


    response = requests.get(img_url)
    img = Image.open(BytesIO(response.content))

    img.show()
# APOD()


def cat_facts():
    url = "https://cat-fact.herokuapp.com"
    fact_link = "https://cat-fact.herokuapp.com/facts/random"

    req = requests.get(url)
    sp = BeautifulSoup(req.content, 'html.parser')

    print(sp.prettify())

# cat_facts()

def dog_facts():
    url = "https://dogapi.dog/api/v2"
    fact_link = "https://dogapi.dog/api/v2/facts"
    params={
        "limit" : 1
    }

    req = requests.get(fact_link,params=params)
    response = req.json()

    fact = response["data"][0]["attributes"]["body"]
    print(fact)

# dog_facts()

def duck_img():
    url = "https://random-d.uk/api/v2"
    random_img_link = url + "/random"

    req = requests.get(random_img_link)
    response = req.json()
    img_url = response["url"]
    imgRes = requests.get(img_url)

    img = Image.open(BytesIO(imgRes.content))
    img.show()

# duck_img()

def number_fact():
    url = "http://numbersapi.com/"
    randInt_choice =  input("Do you want a random number: ")
    if randInt_choice.lower() != "yes":
        final_num = input("Enter number: ")

    type = input("Enter the type of fact (trivia/math/date/year): ")
    if randInt_choice.lower() == 'yes':
        match type.lower():
            case 'trivia':
                link = url + "random/trivia"
            case 'date' : 
                link = url + "random/data"
            case 'year' :
                link = url + "random/year"
            case 'math' :
                link = url + "random/math"
            case _:
                print("Invalid input")
    else:
        match type.lower():
            case 'trivia':
                link = url + final_num +"/trivia"
            case 'date' : 
                link = url + final_num +"/data"
            case 'year' :
                link = url + final_num +"/year"
            case 'math' :
                link = url + final_num +"/math"
            case _:
                print("Invalid input")

    
    req = requests.get(link)
    response = req.text
    print(response)


# number_fact()

def YeYe_quote():
    url = "https://api.kanye.rest"
    req = requests.get(url)

    data = req.json()
    print(data["quote"])

# YeYe_quote()


"""
    ADD SWITCH CASE TO LET USER CHOOSE WHAT FUNCTION TO CALL
"""
print("Enter your choice: \n" \
"1. APOD" \
"2. Cat facts" \
"3. Dog facts" \
"4. Number facts" \
"5. YeYe quotes" \
"6. Random duck image" \
"7. Exit")
ch = int(input())
while(True):
    match ch:
        case 1:
            APOD()
        case 2:
            cat_facts()
        case 3:
            dog_facts()
        case 4:
            number_fact()
        case 5:
            YeYe_quote()
        case 6:
            duck_img()
        case 7:
            break
        case _:
            print("Invalid input. Try again")