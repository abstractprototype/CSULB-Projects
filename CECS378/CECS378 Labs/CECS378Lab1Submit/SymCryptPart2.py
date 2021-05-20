#Part 2 Encrypting and Decrypting a given phrase

import random

alphabets = "abcdefghijklmnopqrstuvwxyz"
alphaCAP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 

def encrypt(msg, key): #takes in the given phrase and global variable of alphabets
    cipher = ""
    upperAlpha = key.upper() #turns the lowercase in the alphabets into uppercase
    for i in msg:
        if i.isalpha(): #when the phrase is alphabetical and is uppercase 
            if i.isupper():
                cipher += upperAlpha[alphaCAP.find(i)] #finds the letters in the key and encrypts it
            else:
                cipher += key[alphabets.find(i)]        
        else:
            cipher += i 
    return cipher

def decrypt(cipher, key):
    text = ""
    upperAlpha = key.upper()
    for i in cipher:
        if i.isalpha():
            if i.isupper():
                text += alphaCAP[upperAlpha.find(i)]
            else:
                text += alphabets[key.find(i)]
        else:
            text += i
    return text

def makeKey():
    randomList = list(alphabets) #turns the string into a list
    random.shuffle(randomList) #shuffles the list
    newKey = ("".join(randomList)) #turn list back into a string
    return newKey

def part2():
    start = makeKey()
    e = encrypt("Whenever I find  myself  growing  grim  about  the  mouth; whenever  it is a damp , drizzly  November  in my soul; whenever I find  myself involuntarily  pausing  before  coffin  warehouses , and  bringing  up therear of  every  funeral I meet; and  especially  whenever  my  hypos  get such an  upper  hand of me , that it  requires a strong  moral  principle to  prevent  me from  deliberately  stepping  into  the  street , and methodically  knocking  people ’s hats  off - then , I account  it hightime to get to sea as soon as I can", start)
    print("Encryption: ", e)
    d = decrypt(e, start)
    print("Decryption: ", d)

if __name__ == '__main__':
    part2()