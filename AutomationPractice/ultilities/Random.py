import random

class Random():
    def randomString(self,length):
        string = []
        char_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        for i in range(length):
            string.append(random.choice(char_list))
        return ''.join(string)
    def randomNumber(self,min,max):
        ranNum = random.randint(min,max)
        return ranNum
    def randomNumber1(self,length,chars):
        string = []
        for i in range(length):
            string.append(random.choice(chars))
        return ''.join(string)