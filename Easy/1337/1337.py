import sys
import math
import time
def main():

    #Check if the number of arguments is correct and if the argument is a number
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        findPrimeNumbers(int(sys.argv[1]))
    else:
        generatePrimeNumbers()
        

def generatePrimeNumbers():
    listOfPrimeNumbers = []
    try:
        initialNumber = 2
        while True:
            is_prime = True
            for primeNumber in listOfPrimeNumbers:
                if primeNumber * primeNumber > initialNumber:
                    break
                if initialNumber % primeNumber == 0:
                    is_prime = False
                    break    

            if is_prime:
                listOfPrimeNumbers.append(initialNumber)
                print(initialNumber)
                time.sleep(0.5)
            initialNumber += 1
    except KeyboardInterrupt:
        pass
    
    

def findPrimeNumbers(number):
        
    #Creates a list with all the numbers from 2 to the number
    listOfNumbers = list(range(2,number+1))
    
    #The Sieve of Eratosthenes implies that we only 
    #need to check the numbers up to the square root of the number
    maxNumberToCheck = int(math.sqrt(number))
    
    for checkNumber in range(2,maxNumberToCheck + 1):
        for number in listOfNumbers:
            if number % checkNumber == 0 and number != checkNumber:
                listOfNumbers.remove(number)
        
    print(listOfNumbers)

if __name__ == "__main__":
    main()