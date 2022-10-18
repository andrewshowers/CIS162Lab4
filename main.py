def isValidColor(red, green, blue):
    if red >= 0 and red <= 225:
        if green >= 0 and green <= 225:
            if blue >= 0 and blue <= 225:
                return True
    else:
        return False

#NEED HELP WITH THE ZONE PART
def calcFine(speed: int, limit: int, zone: bool):
    overlimit = speed - limit
    if zone is True:
        return 1000
    elif overlimit < 9:
        return 100
    elif overlimit >= 10 and overlimit <= 15:
        return 500

def determinePay(rate, hours):
    if hours is "":
        hours = 40

def gradeWork(grade):
    if grade >= 93:
        return 'a'
    elif grade >= 84:
        return 'b'
    elif grade >= 77:
        return 'c'
    elif grade >= 70:
        return 'd'
    else:
        return 'f'

def processBill()








