def isValidColor(red, green, blue):
    if red >= 0 and red <= 225:
        if green >= 0 and green <= 225:
            if blue >= 0 and blue <= 225:
                return True
    else:
        return False



