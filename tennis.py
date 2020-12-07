import random
class Player:
    """
    Player class that'll be used to create a user's player
    The class has private instance properties, so it must have methods to change a Player instance
    """
    def __init__(self, givenname = 'Charles Dalisay', foreh = 1 , backh = 1, vol = 1, serv = 1, mentalstr = 1, stam = 100):
        """
        Constructor that gives a player its name and stats (such as forehand, bachand, volley, serve, mental strength, and stamina)
        These stats will be used throughout the match (in the class Match) that will determine who wins a point which will lead into games and the entire match.
        """
        if type(givenname) != str:
            raise TypeError('Name must be a string')
        if type(foreh) != int or type(backh) != int or type(vol) != int or type(serv) != int or type(mentalstr) != int or type(stam) != int:
            raise TypeError('Value must be an integer')
        if foreh < 1 or foreh > 10:
            raise Exception('Value must be a valid value')
        if backh < 1 or backh > 10:
            raise Exception('Value must be a valid value')
        if vol < 1 or vol > 10:
            raise Exception('Value must be a valid value')
        if serv < 1 or serv > 10:
            raise Exception('Value must be a valid value')
        if mentalstr < 1 or mentalstr > 10:
            raise Exception('Value must be a valid value')
        if stam < 1 or stam > 100:
            raise Exception('Value must be a valid value')

        #private player properties of its skillset
        self.__name = givenname
        self.__forehand = foreh
        self.__backhand = backh
        self.__volley = vol
        self.__serve = serv
        self.__mentalstrength = mentalstr
        self.__stamina = stam

        #private player properties which keeps track of how many points, games, and sets a player won
        self.__points = 0
        self.__gameswon = 0
        self.__setwon = 0

    def setname(self, givenname):
        """
        Method to set the player's name
        """
        if type(givenname) != str:
            raise TypeError('Value must be an integer')
        self.__name = givenname

    def setforehand(self, val):
        """
        Method to set the player's forehand value
        """
        if type(val) != int:
            raise TypeError('Value must be an integer')
        if val < 1 or val > 10:
            raise Exception('Value must be a valid value')
        self.__forehand = val

    def setbackhand(self, val):
        """
        Method to set the player's backhand value
        """
        if type(givenname) != str:
            raise TypeError('Value must be an integer')
        if val < 1 or val > 10:
            raise Exception('Value must be a valid value')
        self.__backhand = val

    def setvolley(self, val):
        """
        Method to set the player's volley value
        """
        if type(givenname) != str:
            raise TypeError('Value must be an integer')
        if val < 1 or val > 10:
            raise Exception('Value must be a valid value')
        self.__volley = val

    def setserve(self, val):
        """
        Method to set the player's serve value
        """
        if type(givenname) != str:
            raise TypeError('Value must be an integer')
        if val < 1 or val > 10:
            raise Exception('Value must be a valid value')
        self.__serve = val

    def setmentalstrength(self, val):
        """
        Method to set the player's mental strength value
        """
        if type(givenname) != str:
            raise TypeError('Value must be an integer')
        if val < 1 or val > 10:
            raise Exception('Value must be a valid value')
        self.__mentalstrength = val

    def setstamina(self, val):
        """
        Method to set the player's serve stamina
        """
        if type(givenname) != str:
            raise TypeError('Value must be an integer')
        if val < 1 or val > 100:
            raise Exception('Value must be a valid value')
        self.__stamina = val

    def getname(self):
        """
        Method which returns the player's name
        """
        return self.__name

    def getforehand(self):
        """
        Method which returns the player's forehand value
        """
        return self.__forehand

    def getbackhand(self):
        """
        Method which returns the player's backhand value
        """
        return self.__backhand

    def getvolley(self):
        """
        Method which returns the player's volley value
        """
        return self.__volley

    def getserve(self):
        """
        Method which returns the player's serve value
        """
        return self.__serve

    def getmentalstrength(self):
        """
        Method which returns the player's mental strength value
        """
        return self.__mentalstrength

    def getstamina(self):
        """
        Method which returns the player's stamina value
        """
        return self.__stamina

    def addpoint(self):
        """
        Method which adds a point for a player
        """
        self.__points += 1

    def subtractpoint(self):
        """
        Method which subtracts a point for a player
        """
        self.__points -= 1

    def setpoint0(self):
        """
        Method  which resets the points a player have to 0
        """
        self.__points = 0
    def addgame(self):
        """
        Method which adds a game when a player wins a game
        """
        self.__gameswon += 1

    def resetgameswon(self):
        """
        Method which reset the player's games won to 0 (when a player wins a set)
        """
        self.__gameswon = 0

    def addsetwon(self):
        """
        Method which adds a set for when a plyer wins a set
        """
        self.__setwon += 1

    def getpoints(self):
        """
        Method which returns the amount of points a player has for the game
        """
        return self.__points
    def getgameswon(self):
        """
        Method which returns the amount of games a player has won for the match
        """
        return self.__gameswon

    def getsetswon(self):
        """
        Method which returns the amount of games a player has won for the match
        """
        return self.__setwon

    def __str__(self):
        """
        Returns a string representation of a player and its stats
        """
        stringrep = ""
        stringrep += "PLAYER:          " + self.getname() + "\n"
        stringrep += "Forehand:        " + str(self.getforehand()) + "\n"
        stringrep += "Backhand:        " + str(self.getbackhand()) + "\n"
        stringrep += "Volley:          " + str(self.getvolley()) + "\n"
        stringrep += "Serve:           " + str(self.getserve()) + "\n"
        stringrep += "Mental Strength: " + str(self.getmentalstrength()) + "\n"
        stringrep += "Stamina:         " + str(self.getstamina()) + "\n"

        return stringrep

class Match:

    def __init__(self, p1, p2, numset):
        """
        Makes player 1 and player 2 (Both Player Objects)
        Asks for the user for best of how many sets they want to simulate
        """
        self.__player1 = p1
        self.__player2 = p2
        self.__setscore = []
        self.__settowin = numset//2 + 1
        self.tiebreaker = False
    def playpoint(self):
        """
        Simulate a point between 2 given players
        """

        DIFFERENCE = 4 #Constant variable to randomize
        p1total = 0
        p2total = 0

        p1pforehand = random.randrange(self.__player1.getforehand() - DIFFERENCE, self.__player1.getforehand() + DIFFERENCE)
        p2pforehand = random.randrange(self.__player2.getforehand() - DIFFERENCE, self.__player2.getforehand() + DIFFERENCE)

        p1pbackhand = random.randrange(self.__player1.getbackhand() - DIFFERENCE, self.__player1.getbackhand() + DIFFERENCE)
        p2pbackhand = random.randrange(self.__player2.getbackhand() - DIFFERENCE, self.__player2.getbackhand() + DIFFERENCE)

        p1pvolley = random.randrange(self.__player1.getvolley() - DIFFERENCE, self.__player1.getvolley() + DIFFERENCE)
        p2pvolley = random.randrange(self.__player2.getvolley() - DIFFERENCE, self.__player2.getvolley() + DIFFERENCE)

        p1pserve = random.randrange(self.__player1.getserve() - DIFFERENCE, self.__player1.getserve() + DIFFERENCE)
        p2pserve = random.randrange(self.__player2.getserve() - DIFFERENCE, self.__player2.getserve() + DIFFERENCE)

        p1pms = random.randrange(self.__player1.getmentalstrength() - DIFFERENCE, self.__player1.getmentalstrength() + DIFFERENCE)
        p2pms = random.randrange(self.__player2.getmentalstrength() - DIFFERENCE, self.__player2.getmentalstrength() + DIFFERENCE)

        #Makes the highest value 10
        if p1pforehand > 10:
            p1pforehand = 10
        if p2pforehand > 10:
            p2pforehand = 10
        if p1pbackhand > 10:
            p1pbackhand = 10
        if p2pbackhand > 10:
            p2pbackhand = 10
        if p1pvolley > 10:
            p1pvolley = 10
        if p2pvolley > 10:
            p2pvolley = 10
        if p1pserve > 10:
            p1pserve = 10
        if p2pserve > 10:
            p2pserve = 10
        if p1pms > 10:
            p1pms = 10
        if p2pms > 10:
            p2pms = 10
        p1total = p1pforehand + p1pbackhand + p1pvolley + p1pserve + p1pms
        p2total = p2pforehand + p2pbackhand + p2pvolley + p2pserve + p2pms

        p1total = p1total * (self.__player1.getstamina() / 100)
        p2total = p2total * (self.__player2.getstamina() / 100)


        if not self.tiebreaker:
            if p1total > p2total: #Determines the winner of the point
                self.__player1.addpoint()
                print('Point winner: ', self.__player1.getname())
            elif p2total > p1total:
                self.__player2.addpoint()
                print('Point winner: ', self.__player2.getname())
            else:
                self.playpoint()
        elif self.tiebreaker:
            if p1total > p2total: #Determines the winner of the point
                self.__player1.tiebreakpoints +=1
                print('Point winner: ', self.__player1.getname())
            elif p2total > p1total:
                self.__player2.tiebreakpoints +=1
                print('Point winner: ', self.__player2.getname())
            else:
                self.playpoint()



    def simulatematch(self):
        """
        Simulates a match situation between two given players
        """
        print('Match is starting...')
        print('-------------------------------------------------------\n')
        while self.__player1.getsetswon() != self.__settowin and self.__player2.getsetswon() != self.__settowin:
            string1 = "{:<15}  |{}|{}|{}".format(self.__player1.getname(), self.__player1.getsetswon(), self.__player1.getgameswon(), self.__player1.getpoints())
            string2 = "{:<15}  |{}|{}|{}".format(self.__player2.getname(), self.__player2.getsetswon(), self.__player2.getgameswon(), self.__player2.getpoints())
            print(string1)
            print(string2)
            self.playpoint()

            #Below are all the ways for players to win a set
            #if they win, it resets the amount of points and games they have won
            if self.__player1.getgameswon() == 6 and self.__player2.getgameswon() <= 4:
                self.__setscore.append(6)
                self.__setscore.append(self.__player2.getgameswon())
                self.__player1.addsetwon()
                self.__player1.resetgameswon()
                self.__player2.resetgameswon()
                self.__player1.setpoint0()
                self.__player2.setpoint0()
            elif self.__player2.getgameswon() == 6 and self.__player1.getgameswon() <= 4:
                self.__setscore.append(self.__player1.getgameswon())
                self.__setscore.append(6)
                self.__player2.addsetwon()
                self.__player1.resetgameswon()
                self.__player2.resetgameswon()
                self.__player1.setpoint0()
                self.__player2.setpoint0()
            elif self.__player1.getgameswon() == 7 and self.__player2.getgameswon() <= 5:
                self.__setscore.append(7)
                self.__setscore.append(self.__player2.getgameswon())
                self.__player1.addsetwon()
                self.__player1.resetgameswon()
                self.__player2.resetgameswon()
                self.__player1.setpoint0()
                self.__player2.setpoint0()
            elif self.__player2.getgameswon() == 7 and self.__player1.getgameswon() <= 5:
                self.__setscore.append(self.__player1.getgameswon())
                self.__setscore.append(7)
                self.__player2.addsetwon()
                self.__player1.resetgameswon()
                self.__player2.resetgameswon()
                self.__player1.setpoint0()
                self.__player2.setpoint0()
            elif self.__player2.getgameswon() == 6 and self.__player1.getgameswon() == 6:
                print("ENTERING A TIEBREAK")
                print('-------------------\n')
                self.tiebreaker = True
                tiebreaktowin = 7
                while (self.__player1.tiebreakpoints < tiebreaktowin) or (self.__player2.tiebreakpoints < tiebreaktowin):
                    playpoint()
                if self.__player1.tiebreakpoints == tiebreaktowin:
                    self.__setscore.append(7)
                    self.__setscore.append(6)
                    self.__player1.tiebreakpoints = 0
                    self.__player2.tiebreakpoints = 0
                elif self.__player2.tiebreakpoints == tiebreaktowin:
                    self.__setscore.append(6)
                    self.__setscore.append(7)
                    self.__player1.tiebreakpoints = 0
                    self.__player2.tiebreakpoints = 0
                self.__player1.resetgameswon()
                self.__player2.resetgameswon()
                self.__player1.setpoint0()
                self.__player2.setpoint0()
                self.tiebreaker = False

            #Below are ways to win a game
            if self.__player1.getpoints() == 4 and self.__player2.getpoints() <= 3:
                self.__player1.addgame()
                self.__player1.setpoint0()
                self.__player2.setpoint0()
            elif self.__player2.getpoints() == 4 and self.__player1.getpoints() <= 3:
                self.__player2.addgame()
                self.__player2.setpoint0()
                self.__player1.setpoint0()

            print('---------------------------------------------------\n')

        string1 = "{:<15}  |{}|{}|{}".format(self.__player1.getname(), self.__player1.getsetswon(), self.__player1.getgameswon(), self.__player1.getpoints())
        string2 = "{:<15}  |{}|{}|{}".format(self.__player2.getname(), self.__player2.getsetswon(), self.__player2.getgameswon(), self.__player2.getpoints())
        print(string1)
        print(string2)

        #See if a player has won
        if self.__player1.getsetswon() == self.__settowin:
            print("The winner is ", self.__player1.getname(), '!!' )
            print('Score:')
            for i in range(0, len(self.__setscore), 2):
                print(self.__setscore[i], '-', self.__setscore[i+1])
        elif self.__player2.getsetswon() == self.__settowin:
            print('Score:')
            print("The winner is ", self.__player2.getname(), '!!' )
            for i in range(1, len(self.__setscore), 2):
                print(self.__setscore[i], '-', self.__setscore[i-1])
