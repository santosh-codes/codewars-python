# Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.

# Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.

# My Solution

def lovefunc( flower1, flower2 ):
    timmy = flower1 % 2
    sarah = flower2 % 2
    if ( timmy == 1 and sarah == 0) or (sarah == 1 and timmy == 0):
        return(True)
    elif (timmy == 1 and sarah == 1) or (sarah == 2 and timmy == 2):
        return(False)
    else:
        return(False)


# Best Solution

def lovefunc(flower1, flower2):
    return flower1 % 2 != flower2 % 2