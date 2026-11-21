


def getNumbers():
    numberArray = []
    f = open("imput.txt","r")
    for line in f:
        numberArray.append(int(line.rstrip("\n")))
    f.close

    return numberArray

def findEquation(numberArray):
    number1 = 0
    number2 = 0
    numbersMultiple = 0

    for loops in range(0,len(numberArray)):
        number1 = numberArray[loops]

        for loops in range(0,len(numberArray)):
            number2 = numberArray[loops]

            if number1 + number2 == 2020:
                print("The numbers that sum up to 2020 are ",number1," and ",number2,".",sep='')
                numbersMultiple = number1 * number2
                print("They times together to make ",numbersMultiple,".",sep='')
                return 

    if numbersMultiple == 0:
        print("Unable to find a pair that add up to 2020")

### MAIN ###

numberArray = getNumbers()
findEquation(numberArray) 