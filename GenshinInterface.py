# Grace Bero

import boto3

TABLE_NAME = "Genshin-Characters"

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

def print_character(character_dict):
    print("Name: ", character_dict["Name"])
    print("Element: ", character_dict.get("Element"))
    print("Region: ", character_dict.get("Region"))
    print("Weapon: ", character_dict.get("Weapon"))
    print("LifeStatus: ", character_dict.get("LifeStatus"))
    print()

# Create
def create_character():
    name = input("Enter their name: ")
    element = input("Enter their element: ")
    region = input("Enter their region: ")
    weapon = input("Enter their weapon type: ")
    alive = input("Alive or Dead?: ")
    print("-------------ฅ^•ﻌ•^ฅ---------------")
    table.put_item(
        Item = {
            'Name' : name,
            'Element' : element,
            'Region' : region,
            'Weapon' : weapon,
            'LifeStatus' : alive,
        })
    print("Character Created Successfully... ദ്ദി ˉ꒳ˉ )✧ ")
    
def print_all_characters():
    response = table.scan() #get all of the movies
    for character in response["Items"]:
        print_character(character)

def update_character():
    name = input("Who has died/been revived?: ")
    invalid = True
    while invalid:
        question = input("Type 'a' for alive, type 'b' for dead: ")
        print("-------------ฅ^•ﻌ•^ฅ---------------")
        if question == "a":
            status = "Alive"
            invalid = False
        elif question == "b":
            status = "Dead"
            invalid = False
        else:
            print(" ")
            print("<(ꐦㅍ _ㅍ)> A and B are the only choices")
    
    try:
        table.update_item(
        Key = { 'Name' : name },
        UpdateExpression = "SET LifeStatus = :value",
        ExpressionAttributeValues = { ':value' : status}
        )
        print("Character Updated Successfully... ദ്ദി ˉ꒳ˉ )✧ ")
    
    except:
        print("This character might not be in the database (╥﹏╥)")
        print("Check your spelling or try a different character")
        update_character()
            
    

def delete_character():
    name = input("Name of character: ")
    print("-------------ฅ^•ﻌ•^ฅ---------------")
    try:
        table.delete_item(
            Key={
                'Name' : name,
            })
        print("Character Deleted Successful... ʕ •ɷ•ʔฅ ")
    except:
        print("This character might not be in the database (╥﹏╥)")
        print("Check your spelling or try a different character")


def query_character():    
    name = input("Which character: ")
    invalid = True
    trait = ""
    while invalid:
        question = input("Which trait would you like \n 'a' Element\n 'b' Life Status\n 'c' Region\n 'd' Weapon Type\n")
        print("-------------ฅ^•ﻌ•^ฅ---------------")
        if question == "a":
            trait = 'Element'
            invalid = False
        elif question == 'b':
            trait = 'LifeStatus'
            invalid = False
        elif question == "c":
            trait = 'Region'
            invalid = False
        elif question == "d":
            trait = 'Weapon'
            invalid = False
        else:
            print("<(ꐦㅍ _ㅍ)> a, b, c, or d are the only choices")
    try:
        response = table.get_item(
            Key={ 'Name' : name })
        item = response['Item'].get(trait)
        print(item)
    except:
        print("This character might not be in the database (╥﹏╥)")
        print("Check your spelling or try a different character/trait")
        query_character()
    
def print_menu():
    print("-------------ฅ^•ﻌ•^ฅ---------------")
    print("Press C: to CREATE a character")
    print("Press R: to READ all characters")
    print("Press U: to UPDATE alive status")
    print("Press D: to DELETE a character")
    print("Press Q: to Query a chosen character trait")
    print("Press X: to EXIT application")
    print("-------------ฅ^•ﻌ•^ฅ---------------")


def main():
    input_char = ""
    while input_char.upper() != "X":
        print_menu()
        input_char = input("Choice: ")
        if input_char.upper() == "C":
            create_character()
        elif input_char.upper() == "R":
            print_all_characters()
        elif input_char.upper() == "U":
            update_character()
        elif input_char.upper() == "D":
            delete_character()
        elif input_char.upper() == "Q":
            query_character()
        elif input_char.upper() == "X":
            print("Good Bye! Hope to see you soon! (´^ω^)ノ ")
        else:
            print('Not a valid option. Try again.')
main()

