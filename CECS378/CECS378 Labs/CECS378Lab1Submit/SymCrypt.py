#@author: Sam Chen
#Lab 1

#Part 1 Bruteforcing
#whats in a name a rose by any other name would smell as sweet
#there are two things to a imatin life first to get  what you want and a
import random
import enchant
import re
import ngram_score

dictionary = enchant.Dict("en_US") #makes dictionary for english
alphabets = "abcdefghijklmnopqrstuvwxyz"
alphaCAP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
transAlphabet = {}
key = "qwertyuiopasdfghjklzxcvbnm"

#make a dictionary for our alphabets for our encrypt and decrypt 
def createDict(shift):
    for i in range(0, 26):
        letter = alphabets[i]
        transAlphabet[letter] = alphabets[(i+shift) % 26]
     
#decrypts the passed in message with message parameter
#makes an empty string for the ciphertext to go into
#passes all the possibilities to detect function to find english words
def decrypt(message):
    ciphertext = ''
    for letter in message:
        if letter in transAlphabet:
            letter = transAlphabet[letter]
            ciphertext = ciphertext + letter
        else:
            ciphertext = ciphertext + ' '
    #print ("\nPrint possibilities: ", ciphertext)
    detect(ciphertext)

#detects first english word from an imported english dictionary and prints out the phrase
def detect(decrypted):
    word = decrypted.split(" ")
    check = dictionary.check(word[0])
    if check:
        print("\nDecrypted bruteforce phrases: ", decrypted)
        return

#Attempt to encrypt part 1 for phrases 3 and 4
def encrypt(msg, key, alphabet): #takes in the given phrase and global variable of alphabets
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

#Part 2 Encrypting and Decrypting a given phrase
#Encrypts the 3 given messages with a simple substitution cipher
def encrypt2(msg, key): #takes in the given phrase and global variable of alphabets
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

#Decrypts the 3 given phrases with the passed in encryption and a randomly generated key
def decryptPart2(cipher, key):
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

#Generates a random key to use for part 2 to accomplish the task of encrypting and decrypting the 3 phrases
def makeKey():
    randomList = list(alphabets) #turns the string into a list
    random.shuffle(randomList) #shuffles the list
    newKey = ("".join(randomList)) #turn list back into a string
    return newKey

#Executes the substitution cipher for part 2
#Starts by generating a random key then passed the 3 phrases to our Encrypt and Decrypt functions
#Prints out the results of encryption and decryption
def part2():
    start = makeKey()
    e = encrypt2("He who fights with monsters should look to it that he himself does not become a monster And if you  gaze long into an abyss the  abyssal so gazes into you", start)
    e1 = encrypt2("There is a theory which states that if ever anybody discovers exactly what the Universe is for and why it is here it will instantly disappear and be replaced  by  something  even  more  bizarre and  inexplicable There  is  another  theory  which  states  that  this has  already happened", start)
    e2 = encrypt2("Whenever I find  myself  growing  grim  about  the  mouth whenever  it isa damp drizzly  November  in my soul whenever I find  myself involuntarily  pausing  before  coffin  warehouses and  bringing  up therear of  every  funeral I meet and  especially  whenever  my  hypos  get such an  upper  hand of me that it  requires a strong  moral  princip leto  prevent  me from  deliberately  stepping  into  the  street and methodically  knocking  peoples hats  off  then I account it hightime to get to sea as soon as I can", start)
    print("\nEncryption1: ", e)
    print("\nEncryption2: ", e1)
    print("\nEncryption3: ", e2)
    d = decryptPart2(e, start)
    d1 = decryptPart2(e1, start)
    d2 = decryptPart2(e2, start)
    print("\nDecryption1: ", d)
    print("\nDecryption2: ", d1)
    print("\nDecryption3: ", d2)

#Begin program
if __name__ == '__main__':
  
    #activates part 1 bruteforce style
    #creates and starts the dictionary 
    #loops throughout the alphabet
    for i in range(0,26):
        createDict(i)
        decrypt("fqjcb  rwjwj  vnjax  bnkhj  whxcq  nawjv  nfxdu  mbvnu  ujbbf  nn")
        decrypt("oczmz  vmzor  jocdi  bnojv  dhvod  igdaz  admno  ojbzo  rcvot  jprvi  oviyvaozmo  cvooj  ziejt  dojig  toczr  dnzno  jahvi  fdiyv  xcdzq  zoczn  zxjiy")

    #activates part 2 for simple substition cipher encryption and decryption
    part2()  

    #Part 1: Attempts to decrypts phrases 3 and 4
    graham = ngram_score.ngram_score('C:/Users/SamTopSSD/CECS378 Labs/quadgrams.txt') # load our quadgram statistics

    mystery='ejitp  spawa  qleji  taiul  rtwll  rflrl  laoat  wsqqj  atgac  kthls  iraoatwlpl  qjatw  jufrh  lhuts  qataq  itats  aittk  stqfj  cae'
    mystery1='iyhqz  ewqin  azqej  shayz  niqbe  aheum  hnmnj  jaqii  yuexq  ayqkn  jbeuqiihed  yzhni  ifnun  sayiz  yudhe  sqshu  qesqa  iluym  qkque  aqaqm  oejjshqzyu  jdzqa  diesh  niznj  jayzy  uiqhq  vayzq  shsnj  jejjz  nshna  hnmytisnae  sqfun  dqzew  qiead  zevqi  zhnjq  shqze  udqai  jrmtq  uishq  ifnunsiiqa  suoij  qqfni  syyle  iszhn  bhmei  squih  nimnx  hsead  shqmr  udququaqeu  iisqe  jshnj  oihyy  snaxs  hqihe  lsilu  ymhni  tyz'
   
    masterkey = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    masterscore = -99999
    bigscore,bigkey = masterscore,masterkey[:] #big score copy of master score, big key copy of alphabet
    

    i = 0
    while 1:
        i = i+1
        random.shuffle(bigkey)
        deciphered = encrypt(mystery, key, bigkey)
        bigscore = graham.score(deciphered)
        count = 0


        while count < 999 and count <= 690:
            a = random.randint(0,25)
            b = random.randint(0,25)
            child = bigkey[:]
            # swap two characters in the child
            child[a],child[b] = child[b],child[a]
            str1 = " ".join(child)
            deciphered = encrypt(mystery, str1, bigkey)
            score = graham.score(deciphered)
            # if the child was better, replace the parent with it
            if score > bigscore:
                bigscore = score
                bigkey = child[:]
                count = 0
            count = count+1


        # keep track of best score seen so far
        if bigscore > masterscore:
            masterscore,masterkey = bigscore,bigkey[:]
            print('\nbest score so far:',masterscore,'on iteration', i)
            print('best key: '+''.join(masterkey))
            print('plaintext: '+ deciphered)
        

