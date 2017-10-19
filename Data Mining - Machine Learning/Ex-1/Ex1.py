# Ex #1
# Miki Manor - 310962212
# Peter Zubkov - 310658984

import random

class Roulette(object):
    def __init__(self):
        self.amountOfLosing = 0
        self.amountOfWinning = 0
        self.amountOfBet = 0

    def Red(self):
        self.Check_Winning(2, 1, 1)

    def Black(self):
        self.Check_Winning(2, 1, 2)

    def Number(self):
        roulleteNumbers = list(range(0,36))
        selectedNumber = int(input("Please choose number between 0-36 :"))
        if selectedNumber in roulleteNumbers:
            self.Check_Winning(37, 0, selectedNumber)
        else:
            print("Error!")
            exit(1)

    def Check_Winning(self, i_NumOfOptions, i_startPosition, i_BetSelection):
        # 1 - Red | 2 - Black | if numbers so numbers :)
        roulleteCurrentState = random.randint(i_startPosition, i_NumOfOptions)
        if roulleteCurrentState is i_BetSelection:
            print("You Won " + str(self.amountOfBet) + "$ !!!" )
            self.amountOfWinning += self.amountOfBet
        else:
            print("You Lost " + str(self.amountOfBet) + "$ !!!" )
            self.amountOfLosing += self.amountOfBet

    def play(self):
        betOptions = ["1", "2", "3"]
        self.amountOfBet = int(input("Enter amount of bet : "))
        betSelection = input("Bet for what? Red Color (1), Black Color(2) or else, a Number(3) ?")
        while betSelection not in betOptions:
            betSelection = input("Wrong Selection, please choose between " + ", ".join([str(option) for option in betOptions]) + " : ")
        if betSelection is "1":
            self.Red()
        elif betSelection is "2":
            self.Black()
        elif betSelection is "3":
            self.Number()
        print("Summary : \nAmount Of Winning until now: " + str(self.amountOfWinning) + "\nAmount Of Losing until now : " + str(self.amountOfLosing) + "\nCurrent State : " + str(self.amountOfWinning - self.amountOfLosing))

class Casino(object):

    def __init__(self):
        self.sumOfWinningsToday = 0
        self.sumOfLosingsToday = 0
        self.numOfRoulettes = input("How many Roulettes to create? ")

    def InistializeRoulettes(self):
        self.listOfRouletes = [Roulette() for i in range(int(self.numOfRoulettes))]

    def PlayOnRoulettes(self, i_RouletteToPlayWith):
        continuePlaying = True
        roullete = Roulette()
        YES_VALUES = {'y', 'yes', 'ok'}
        while continuePlaying:
            self.listOfRouletes[i_RouletteToPlayWith].play()
            userResponse = input("+++++++++++++++++++++++++\n\nContinue Playing on this Roulette (Y)? ")
            if userResponse.lower() in YES_VALUES:
                continuePlaying = True
            else:
                continuePlaying = False
                print("Bye Bye")

    def GetTotalWinningLosing(self):
        for roulette in self.listOfRouletes:
            self.sumOfWinningsToday += roulette.amountOfWinning
            self.sumOfLosingsToday += roulette.amountOfLosing

if __name__ == "__main__":
    myCasino  = Casino()
    myCasino.InistializeRoulettes()
    YES_VALUES = {'y', 'yes', 'ok'}
    continuePlaying = True
    while continuePlaying:
        userResponse = input("+++++++++++++++++++++++++\n\nChoose Roulette to play with (Y) or Exit (E) ? ")
        if userResponse.lower() in YES_VALUES:
            RouletteToPlayWith = int(input("Choose Roulette to play with - the options are : 1 - " +
                                       str(myCasino.numOfRoulettes) + " "))
            if ((RouletteToPlayWith < int(myCasino.numOfRoulettes)) and (RouletteToPlayWith > 0)):
                myCasino.PlayOnRoulettes(RouletteToPlayWith - 1)
                myCasino.GetTotalWinningLosing()
                print("\nCasino Summary : \nTotal Won : " + str(myCasino.sumOfWinningsToday) +  "\nTotal Lost : " + str(myCasino.sumOfLosingsToday) )
        else:
            continuePlaying = False
            print("Bye Bye From Casino")
            exit()
