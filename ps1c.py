# Problem Set 1A
# Name: Caroline Liu
# Collaborators: N/A
# Time Spent: 3 hrs

'''
reuse code from problem 2
assume annual raise is 0.03, investment return of 0.05
bisection search method to find best savings rate as a function of starting salary
'''
#import pdb
#pdb.set_trace()

def modifiedRetirement():
    salary = float(raw_input('Enter the starting salary:'))
    increase = 0.03
    rate = 0.05
    time = 45*12
    nestEgg = 0
    goalNestEgg = 2000000
    epsilon = 1000
    lowNestEgg = 2000000 - 1000
    highNestEgg = 2000000 + 1000
    highPercent = 10000
    lowPercent = 0
    percentSaved = (highPercent+lowPercent)/2.0
    numGuesses = 0
    while abs(goalNestEgg-nestEgg) >= epsilon:
        print(numGuesses, lowPercent, highPercent, percentSaved, nestEgg, abs(goalNestEgg-nestEgg))
        numGuesses += 1
        for i in range(time):
            if i % 12 == 0 and i != 0:
                salary += salary*increase
            nestEgg += (percentSaved/100/100)*(salary/12)+rate*(nestEgg/12)
        if nestEgg > highNestEgg:
            highPercent = percentSaved
        else:
            lowPercent = percentSaved
        percentSaved = (highPercent+lowPercent)/2.0
        if abs(goalNestEgg-nestEgg) <= epsilon:
            break

    print('Best savings rate = '+ str(percentSaved))
    print('Steps in bisection search = '+ str(numGuesses))

modifiedRetirement()

