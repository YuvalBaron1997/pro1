#Yuval Bar-On , 4212532
#1.RGBColor
class RGBColor:

    def __init__(self, red=0, green=0, blue=0):
        self.red = red
        self.green = green
        self.blue = blue
        
    def getRed(self):
        return self.red 

    def getGreen(self):
        return self.green

    def getBlue(self):
        return self.blue

    def setRed(self,newRed):
        if newRed in range(0,256):
            self.red = newRed
        else:
            raise ValueError("The num not in range")

    def setGreen(self,newGreen):
        if newGreen in range(0,256):
            self.green = newGreen
        else:
            raise ValueError("The num not in range")

    def setBlue(self,newBlue):
        if newBlue in range(0,256):
            self.blue = newBlue
        else:
            raise ValueError("The num not in range")    
            
    
    def __eq__(self,other):
        return self.red == other.red and self.green == other.green and self.green == other.green


    def mix(self,other):
        mixedred = (self.red + other.red) / 2
        mixedgreen = (self.green + other.green) / 2
        mixedblue = (self.blue + other.blue) / 2
        return RGBColor(mixedred, mixedgreen, mixedblue)

    def convertToGrayscale(self):
        grayred = (self.red * 30) / 100
        graygreen = (self.green * 59) / 100
        grayblue = (self.blue * 11) / 100
        return RGBColor(grayred, graygreen, grayblue)

    def invert(self):
        invertred = 255 - self.red
        invertgreen = 255 - self.green
        invertblue = 255 - self.blue
        return RGBColor(invertred, invertgreen, invertblue)
             

    def __repr__(self):
        return "(" + str(self.red)+ "," + str(self.green)+ "," + str(self.blue)+")"



red = RGBColor(255,0,0)
green = RGBColor(0,255,0)
blue = RGBColor(0,0,255) 
color2 = RGBColor(0,30,200)
color3 = RGBColor(20,10,97)
color1 = RGBColor(90,100,80)
#chek
print("The color is: ", red.getRed())
print("The color is: ", green.getRed())
print("The color is: ", green.getGreen())
print("The color is: ", blue.getBlue())
print("The color is: ", color2.__repr__())
print("__eq__()\t",red == green == blue)
print(color2.mix(color2))
print(color2.convertToGrayscale())
print(color2.invert())



#2.LightBulb
class LightBulb:

    def __init__(self, color):
        self.color = RGBColor()
        self.switchedOn = False

    def getColor(self):
        return self.color

    def setColor(self,color):
        self.color = color

    def isSwitchedOn(self):
        return self.switchedOn

    
    def switchLight(self):
        if self.switchedOn == True:
            self.switchedOn = False
        else:
            self.switchedOn = True
    

    def __repr__(self):
        return "The color is: " + str(self.color.__repr__()) + \
               " Is the light on? " + str(self.switchedOn)
        

light1 = LightBulb(color1)
light2 = LightBulb(color2)
light3 = LightBulb(color3)

#check
print("This lightbulb is: ", light1.getColor())
print("This lightbulb is: ", light1.isSwitchedOn())
print("This lightbulb is: ", light2.switchLight())
print("This lightbulb is: ", light1.__repr__())

#3.Disco
class Disco:

    def __init__(self, bulb1, bulb2, bulb3):
        self.bulb1 = bulb1
        self.bulb2 = bulb2
        self.bulb3 = bulb3     
        
    def getFirstBulb(self):
        return self.bulb1

    def getSecondBulb(self):
        return self.bulb2

    def getThirdBulb(self):
        return self.bulb3

    def switchBulb(self,bulbNumber):
        if bulbNumber in range(1,4):
            if bulbNumber == 1 :
                self.bulb1.switchLight()
            elif bulbNumber == 2:
                self.bulb2.switchLight()
            else:
                self.bulb3.switchLight()
        else:
            None 

    def trunAllOn(self):
        if self.bulb1.isSwitchedOn() == True:
            self.bulb1 = self.bulb1
        else:
            self.bulb1.switchLight()
        
        if self.bulb2.isSwitchedOn() == True:
            self.bulb2 = self.bulb2
        else:
            self.bulb2.switchLight()
        
        if self.bulb3.isSwitchedOn() == True:
            self.bulb3 = self.bulb3
        else:
            self.bulb3.switchLight()

    def turnAllOff(self):
        if self.bulb1.isSwitchedOn() == False:
            self.bulb1 = self.bulb1
        else:
            self.bulb1.switchLight()
        
        if self.bulb2.isSwitchedOn() == False:
            self.bulb2 = self.bulb2
        else:
            self.bulb2.switchLight()
        
        if self.bulb3.isSwitchedOn() == False:
            self.bulb3 = self.bulb3
        else:
            self.bulb3.switchLight()
        

    def areAllOn(self):
        return self.bulb1.isSwitchedOn() == self.bulb2.isSwitchedOn() == self.bulb3.isSwitchedOn() == True
        


    def areAllOff(self):
        return self.bulb1.isSwitchedOn() == self.bulb2.isSwitchedOn() == self.bulb3.isSwitchedOn() == False
         


    def allSameColor(self):
        return self.bulb1.getColor() == self.bulb2.getColor() == self.bulb3.getColor()

    def __repr__(self):
        return f'bulb 1: {self.bulb1} bulb 2: {self.bulb2} bulb 3: {self.bulb3}' + "\U0001F600"
        
            
discoball = Disco(light1,light2,light3)
discoball1 = Disco(light2,light1,0)



#check
print("Disco bulb1 ", discoball.getFirstBulb())
print("Disco bulb2 ", discoball.getSecondBulb())
print("Disco bulb3 ", discoball.getThirdBulb())
discoball.switchBulb(4) 
discoball.turnAllOff()
print("Disco samecolor ", discoball.allSameColor())
print("Disco TurnOn ", discoball.areAllOn())
print("Disco TurnOff ", discoball.areAllOff())
# to check if the methods are working
print("Disco bulb1 ", discoball.getFirstBulb())
print("Disco bulb2 ", discoball.getSecondBulb())
print("Disco bulb3 ", discoball.getThirdBulb())
print(discoball)

