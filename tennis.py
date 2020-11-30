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
