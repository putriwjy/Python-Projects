import random
class Hangman:
    def __init__(self, movieTitle):
        self.userLife = 5
        self.movieTitle = movieTitle
        self.movieTitleList = list(movieTitle)
        self.unknownMovie = [None] * len(self.movieTitleList)
        self.unknownMovie = self.beforeGame()
        self.userGuess = ""

    def beforeGame(self):
        for i in range(len(self.movieTitleList)):
            if self.movieTitleList[i] == " ":
                self.unknownMovie[i] = " "
                
            else:
                self.unknownMovie[i] = "_"
        print(str(self.unknownMovie))
        return self.unknownMovie

    def checkAnswer(self, userGuess):
        self.userGuess = userGuess
        if self.userGuess == self.movieTitle:
            print("You are correct. Congrats!")
            return True
        else:
            self.userLife -=1
            return False

    def checkLetterExists(self, userGuess):
        self.userGuess = userGuess
        if self.userGuess in self.movieTitleList:
            self.matchLetter()
            check = self.checkComplete()
            return check
            
        #else:
        print("hiii")
        self.userLife -=1
        
        return False

    def matchLetter(self):
        for k in range(len(self.movieTitleList)):
            if self.movieTitleList[k] == self.userGuess:
                self.unknownMovie[k] = self.userGuess
        print(self.unknownMovie)
        

    def checkComplete(self):
        if self.unknownMovie == self.movieTitleList:
            return True
        return False



dict = {"romance": ["gone with the wind","breakfast at tiffany's","love actually","dear john", "the princess diaries","17 again",
                    "bridget jones's diary","the proposal", "sleepless in seattle","pride & prejudice"],

        "action":["the avengers","taken","die hard","casino royale","hot fuzz","tomb raider","kick-ass","gladiator","guardians of the galaxy","star wars"],
        "comedy":["white chicks","the hangover","the other guys","grown ups","21 jump street","ted","pitch perfect","bridesmaids","ghostbusters","knocked up"]}


if __name__ == "__main__":
    userGenre = input("Choose genre:" +"\n"+"1.romance" +"\n"+"2.action"+"\n"+"3.comedy")
    userchoice = random.choice(list(dict[userGenre]))
    game = Hangman(userchoice)
    life = game.userLife
    while (life > 0):
        userGuess = input("choose:" +"\n" + "1. type a letter." + "\n" + "2. guess the title: ")
        userGuess = userGuess.lower()
        if len(userGuess) > 1:
            ans = game.checkAnswer(userGuess)
            if ans == True:
                break   
        else:
            ans2 = game.checkLetterExists(userGuess)
            if ans2:
                    print("you guessed the movie right, congrats")
                    break
        life = game.userLife
        if life == 0:
            print("sorry you lost")
    
