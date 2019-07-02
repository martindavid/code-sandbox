import random
import string
import json


def randomStringDigits(stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

users = ["Anuradha","Kevin","Gudrun","Nicholas","Dmitry","Andriy","Lani","Eloi","Aseel","Jody","Tanya","Julianna","Josh","Rod","David","Jacqui","Michael","Myra","Jennifer","James","Michael Bylstra","Liliana","Rongzuo","Segolene","Dave","Steve","Jeen","Will","Josh Berman"]

users2 = ["Amelia","Sahra","Joanne","Deborah","Letian","Chloe","Paul","Brad","Peter","Stephanie"]

users3 = ["James Lovell","Nicholas Godenzi", "Brenton", "Sushma", "Doug", "Jeanne", "Alicia", "Nicole"]

data = [{
  "username": username, "unique_hash": randomStringDigits(25)
} for username in users3]

print(json.dumps(data))

for i in data:
    print(i["unique_hash"])
