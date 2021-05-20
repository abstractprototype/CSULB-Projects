#Global variables for dictionary characters and items
characterList = {1: "SirVinky", 2: "SHAMINO", 3: "IOLO", #Dictionary for character names
                 4: "MARIAH", 5: "GEOFFREY", 6: "JAANA",
                 7: "JULIA", 8: "DUPRE", 9: "KATRINA",
                 10: "SENTRI", 11: "GWENNO",  12: "JOHNE",
                 13: "GORN", 14: "MAXWELL", 15: "TOSHI",
                 16: "SADUJ"}

characterOffsets = {"SirVinky": int('0x02', 16), "SHAMINO": int('0x22', 16), "IOLO": int('0x42', 16), #Dictionary for character offsets 
            "MARIAH": int('0x62', 16), "GEOFFREY": int('0x82', 16), "JAANA": int('0xA2', 16),
            "JULIA": int('0xC2', 16), "DUPRE": int('0xE2', 16), "KATRINA": int('0x102', 16),
            "SENTRI": int('0x122', 16), "GWENNO": int('0x142', 16), "JOHNE": int('0x162', 16),
            "GORN": int('0x182', 16), "MAXWELL": int('0x1A2', 16), "TOSHI": int('0x1C2', 16),
            "SADUJ": int('0x1E2', 16)}

attributes = {1: "STRENGTH", 2: "INTELLIGENCE", 3: "DEXTERITY", #Dictionary for attribute names
              4: "HP", 5: "MAXHP", 6: "EXPERIENCE"}

attributeOffsets = {"STRENGTH": int('0x0C', 16), "INTELLIGENCE": int('0x0E', 16), "DEXTERITY": int('0x0D', 16), #Dictionary for attribute offsets
            "HP": int('0x10', 16), "MAXHP": int('0x12', 16), "EXPERIENCE": int('0x14', 16),
            "MAGIC": int('0x0F', 16)}

itemList = {1: "GOLD", 2: "KEYS", 3: "SKULL KEYS", #Dictionary for item names
         4: "GEMS", 5: "BLACK BADGE", 6: "MAGIC CARPET",
         7: "MAGIC AXE"}

itemOffsets = {"GOLD": int('0x204', 16), "KEYS": int('0x206', 16), "SKULL KEYS": int('0x20B', 16), #Dictionary for item offsets
            "GEMS": int('0x207', 16), "BLACK BADGE": int('0x218', 16), "MAGIC CARPET": int('0x20A', 16),
            "MAGIC AXE": int('0x240', 16)}
#End of global variables

#Begin editing file
def readFile():
    file = open('SAVED.GAM', 'rb')
    byte = list(bytearray(file.read()))
    file.close()
    return byte

def pickCharacter(data): #Allows user to pick which character's attributes to edit then passes: the choice of the character AND the file into pickCharacter()
    print("Choose your Character.")
    for c, name in characterList.items(): #Iterates through character list then prints them all
        print(c, name)
    choice = int(input())
    editAttributes(choice, data) #Passes the choice and data to change attributes
    print("Would you like to edit another Character? Press y for yes or n for no\n")
    ynChoice = input()
    if(ynChoice.lower() == "y"):
        pickCharacter(data)
    if(ynChoice.lower() == "n"):
        menu(data)

def editAttributes(character, data): #Edits the selected characters attributes with bytearray then prompts if user wants to edit another character
    print("Pick an attribute to change for {}.\n".format(characterList[character]))
    for a, att in attributes.items(): #Prints all the attributes
        print(a, att)
    choice = int(input())
    attributeName = attributes[choice] #The chosen attribute store into attributeName #Str
    characterName = characterList[character] #The chosen character store into characterName #Player
    attOffset = attributeOffsets[attributeName] # 12
    charOffset = characterOffsets[characterList[character]] #2
    index = attOffset + charOffset # 2 + 12 Strength = E - 14

    #Makes sure user enters the right value for the proper attribute
    #print("Current Value For {}'s {} is {}. You may enter a value to change a characters stat.\n".format(characterList[character], attributeName, data[index]))
    while(True):
        if(choice > 0 and choice < 4):
            #Changes the str, dex, or int from 0 to 99
            print("Enter a number between 0 and 99 to change {}'s {}\n".format(characterName, attributeName))
            a = int(input())
            break
        elif(choice == 4 or choice == 5):
            #Changes the hp or max hp from 0 to 999
            print("Enter a number between 0 and 999 to change {}'s {}\n".format(characterName, attributeName)) 
            a = int(input())
            break
        else: #Choice is 6
            #Changes the exp from 0 to 9999
            print("Enter a number between 0 and 9999 to change {}'s {}\n".format(characterName, attributeName)) 
            a = int(input())
            break
    
    increment = 0 #increment to move the value right by 1
    bitty = list(bytearray((a).to_bytes(2, byteorder="little"))) #1 byte = 8 bits
    #newBitty = [i for i in bitty if i != 0] #If there is a 0 in the list detected then it will generate a new list so that it does not reset the next offset to 0
    print("Bitty", bitty) #ex. Entering 9999 = 0010 0111 0000 1111 = [15, 39]. 0010 0111 is 39 and 0000 1111 is 15. Little Endian switches them into [15, 39]. However, we changed this to print only one offset
    if(0 in bitty): #checks for extra 0's in offsets then removes if there is. We do this because the extra 0 will overwrite the next offset
        bitty.remove(0)
        print("New Bitty after removing 0:", bitty)
    for i in bitty:
        data[index + increment] = i
        increment += 1 #moves offset to the right by 1 [15,39]
    print("New Bitty", bitty)
    print("{} {} changed to {}".format(characterList[character], attributeName, a)) #Displays updated value
    repeat = input("Do you wish to change another stat? Press y for YES or n for NO\n")
    while((repeat != "y" and repeat != "n")):
        repeat = input("Do you wish to change another stat? Press y for YES or n for NO\n")
    if(repeat == "y"):
        editAttributes(character, data)

def pickItem(data): #Picks the item the user wants to edit then passes: the choice of the item AND the file into editItem()
    print("Which Item would you like to edit?")
    for i, name in itemList.items(): #Iterates through items and prints them all
        print(i, name)
    choice = int(input())
    editItem(choice, data)

def editItem(item, data): #Edits the value of the selected item with bytearray where it counts the binary and changes it
    index = itemOffsets[itemList[item]]
    #print("Current Value For {} is {}. You may enter a value to change the item number.\n".format(itemList[item], data[index]))
    while(True):
        print("Enter a value to change for {}.\n".format(itemList[item]))
        choice = int(input()) #69
        if(choice < 0 and choice > 100):
            continue
        else:
            break

    increment = 0 #Counter to keep track of offset
    bitty = list(bytearray((choice).to_bytes(2, byteorder="little"))) #Gets little endian 2 bytes
    #newBitty = [i for i in bitty if i != 0] #If there is a 0 in the list detected then it will generate a new list so that it does not reset the next offset to 0
    print("Bitty", bitty) #Original offsets
    if(0 in bitty):#checks for extra 0's in offsets then removes if there is. We do this because the extra 0 will overwrite the next offset
        bitty.remove(0)
        print("New Bitty after removing 0:", bitty)
    print("New Bitty:", bitty) #Prints new offset
    for i in bitty:
        data[index + increment] = i
        increment += 1 #Moves counter by 1 to the right offset
    print("{} changed to {}".format(itemList[item], choice)) #ex. Entering 9999 = 0010 0111 0000 1111 = [15, 39]. 0010 0111 is 39 and 0000 1111 is 15. Little Endian switches them into [15, 39]
    repeat = input("Do you wish to change another item? Press y for YES or n for NO\n")
    while((repeat != "y" and repeat != "n")):
        repeat = input("Do you wish to change another item? Press y for YES or n for NO\n")
    if(repeat == "y"):
        pickItem(data)
    if(repeat == "n"):
        menu(data)

def writeFile(data): #Writes the new changes to the file then saves it
    file = open('SAVED.GAM', 'wb')
    file.write(bytearray(data))
    file.close()

def menu(data): #The main menu prompting user to edit the character attributes or item values
    #Main Menu
    print("Welcome to the Ultima 5 Cheat Engine. Please choose which cheat to edit.\n")
    print("1. Character Attributes")
    print("2. Inventory")
    print("3. Save and Exit")
    choice = input()
    if(choice == "1"):
        pickCharacter(data)
    elif(choice == "2"):
        pickItem(data)
    else:
        print("Saving...")
        writeFile(data)
        print("Cheats have been saved!")

if __name__ == '__main__':
    #Reads in the hex file then passes it to the main menu
    #print(characterOffsets.get("KATRINA")) #prints out 258 because turns hex into decimal form
    menu(readFile())
    