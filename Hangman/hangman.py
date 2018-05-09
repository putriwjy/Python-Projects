import random

dict = {"romance": ["gone with the wind","breakfast at tiffany's","love actually","dear john", "the princess diaries","17 again",
                    "bridget jones's diary","the proposal", "sleepless in seattle","pride & prejudice"],

        "action":["the avengers","taken","die hard","casino royale","hot fuzz","tomb raider","kick-ass","gladiator","guardians of the galaxy","star wars"],
        "comedy":["white chicks","the hangover","the other guys","grown ups","21 jump street","ted","pitch perfect","bridesmaids","ghostbusters","knocked up"]}


def beforeGame(userchoicelist):
    biglist=[]
    emptycount = 0
    guessword = []
    guessword.extend(userchoicelist)
    for i in range(len(userchoicelist)):
        if userchoicelist[i] == ' ':
            guessword[i] = ' '

            emptycount +=1
            
        else:
            guessword[i] = "_"
    print(userchoicelist)
    biglist.append(guessword)
    biglist.append(emptycount)
    return biglist

def checkAnswer(userguess, userchoice):
    if userguess == userchoice:
        return True
    else:
        return False

def checkLetterExists(userchoicelist, userGuess):
    if userGuess in userchoicelist:
        return True
    return False

def matchLetter(oriList, guessList, letter):
    for k in range(len(oriList)):
        if oriList[k] == letter:
            guessList[k] = letter
            print(guessList)
    if guessList == oriList:
        return True
    return False
    
userGenre = input("Choose genre: ")
userchoice = random.choice(list(dict[userGenre]))
#userchoice = "die hard"
userchoicelist = list(userchoice)
newlist = beforeGame(userchoicelist)
#print(unknownmovie)
unknownmovie = newlist[0]
emptylettercount = newlist[1]


userlife = 5
while (True):
    userGuess = input("guess a letter or type answer to guess the moviez: ")
    userGuess = userGuess.lower()
    if len(userGuess) > 1:
        ans = checkAnswer(userGuess, userchoice)
        if ans:
            print("You are correct. Congrats!")
            break
        else:
            print("sorry, wrong")
            userlife -=1
    else:
        ans2 = checkLetterExists(userchoicelist, userGuess)
        if ans2:
            ans3 = matchLetter(userchoicelist, unknownmovie, userGuess)
            if ans3:
                print("you guessed the movie right, congrats")
                break
            continue
        
        else:
            userlife -=1
            if userlife == 0:
                print("u lost")
                break
            
            
            
    
            
                
            















            
            






