'''This checks if a number is Prime'''
def getPrime(number):
    factors = []
    primeNums = []
    for i in range(2, number):
        if number % i == 0:
            factors.append(i)
    if len(factors) == 0:
        return True


'''This prints two Prime numbers that sum up to user's input'''
def listSum(number):
    if number % 2 == 0:
        for i in range(1, number):
            addition = number - i
            if getPrime(i) == True and getPrime(addition) == True:
                print(f"{i} + {addition}")
    else:
    	print(f"{number} is not even")


x = int(input("Enter a number: "))
listSum(x)