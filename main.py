from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os
from PIL import Image
from io import BytesIO
import json   #simplify response 

load_dotenv()



def APOD():
    nasa_api = os.getenv("secret_nasa_key")
    url = "https://apod.nasa.gov/apod"
    
    params = {
        'api_key': nasa_api

    }

    req = requests.get(url, params=params)

    sp = BeautifulSoup(req.content, 'html.parser')
    img_tag = sp.img.get('src')
    img_url = "https://apod.nasa.gov/apod/" + img_tag


    response = requests.get(img_url)
    img = Image.open(BytesIO(response.content))

    img.show() 
    return
# APOD()

#CatFacts API deprecated 
def cat_facts():
    url = "https://cat-fact.herokuapp.com"
    fact_link = "https://cat-fact.herokuapp.com/facts/random"

    req = requests.get(url)
    sp = BeautifulSoup(req.content, 'html.parser')

    print(sp.prettify())
    return

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
    print("\n"+fact)
    return

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
    return

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
    return


# number_fact()

def YeYe_quote():
    url = "https://api.kanye.rest"
    req = requests.get(url)

    data = req.json()
    print("\n"+data["quote"])
    print(" "*len(data["quote"])+"-YeYe")
    return

# YeYe_quote()


def poem_api():
    url = "https://poetrydb.org/"
    finLink = ""

    print("What would you like to do?\n" \
    "1. Check list of poets\n" \
    "2. Get poems by poets\n" \
    "3. Get particular poem by poet\n" \
    "4. Get poem by poem title")


    checkList = int(input())
    match checkList:
        case 1:
            finLink = url + "author"
            req = requests.get(finLink)
            response = req.json()

            firstLetter = input("List by first letter? (yes/no): ")
            if firstLetter.lower() == 'no':
                print()
                print("--------------------List of poets--------------------")
                for author in response["authors"]:
                    print(author)
            else:
                firstLetterInput = input("Enter first letter: ")
                print()
                print(f"--------------------List of poets beginning with {firstLetterInput}--------------------")
                for author in response["authors"]:
                    if author[0].lower() == firstLetterInput.lower():
                        print(author)

        case 2:
            poetName = input("Enter poet name: ")
            finLink = url + f"author/{poetName}/title"
            req = requests.get(finLink)
            response = req.json()
           
            try:
                if response['status']==404:
                    print("Poet does not exist in database. Recommend checking out poet list first.")
            except TypeError:
                print()
                print(f"--------------------List of poems by {poetName}--------------------")
                for item in response:
                    print(item["title"])
        
        case 3:
            poetName = input("Enter name of poet: ")
            poemName = input("Enter name of poem: ")
            finLink = url + f"author,title/{poetName};{poemName}"
            req = requests.get(finLink)
            response = req.json()

            try:
                if response['status']==404:
                    print("Error. Either poet or poem is not in database. Recommend checking poet(1) or poem(2) list from database.")
            except TypeError:
                print()
                print(f"--------------------{poemName.title()}--------------------\n\n")
                for lines in response[0]['lines']:
                    print(lines)

        case 4:
            poemName = input("Enter poem name: ")   
            finLink = url + f"title/{poemName}"
            req = requests.get(finLink)
            response = req.json()

            try:
                if response['status']==404:
                    print("Poem not found in database. Recommend looking at poems in database first.")
            except TypeError:
                print()
                print(f"--------------------{poemName.title()}--------------------\n\n")
                for lines in response[0]['lines']:
                    print(lines)
        case _:
            print("Enter valid input (yes/no)")
    return

# poem_api()

def ip_tracker():
    api_key = os.getenv('ip_api_key')
    url = "https://iplocate.io/api/lookup/"
    params={
        'apikey':api_key
    }
    opChoice = int(input("\n" \
    "1. Lookup from ip address\n" \
    "2. Lookup own ip address\n"))
    match opChoice:
        case 1:
            ip = input("Enter ip address: ")
            finLink = url + f"{ip}"
            req = requests.get(finLink,params=params)
            response = req.json()
            
            # print(json.dumps(response,indent=4))

            print(f"\nIP address: {response['ip']}")
            print(f"\nCountry: {response['country']}")
            print(f"\nCity: {response['city']}")
            print(f"\nLatitude: {response['latitude']}")
            print(f"\nLongitude: {response['longitude']}")
            print(f"\nISP: {response['asn']['name']}")
            print()
            for key, value in response['privacy'].items():
                print(f"{key}: {value}")
        case 2:
            req = requests.get(url,params=params)
            response = req.json()
            print("Your public IP: "+response['ip'])
        case _:
            print("Invalid input. Try again...")

    return



"""
    ADD SWITCH CASE TO LET USER CHOOSE WHAT FUNCTION TO CALL
"""


while(True):
    input("\nEnter any key to continue....")
    print("\n\nEnter your choice: \n" \
    " 1. APOD\n" \
    " 2. Cat facts (not working rn)\n" \
    " 3. Dog facts\n" \
    " 4. Number facts\n" \
    " 5. YeYe quotes\n" \
    " 6. Random duck image\n" \
    " 7. PoetryDB\n" \
    " 8. IP location tracker\n" \
    " 0. Exit")
    print()
    try:
        ch = int(input())
    except ValueError:
        print("Invalid input. Enter a number...")
    match ch:
        case 1:
            APOD()
        case 2:
            print("API Endpoint not working")
            # cat_facts()
        case 3:
            dog_facts()
        case 4:
            number_fact()
        case 5:
            YeYe_quote()
        case 6:
            duck_img()
        case 7:
            poem_api()
        case 8:
            ip_tracker()
        case 0:
            break
        case _:
            print("Invalid input. Try again")