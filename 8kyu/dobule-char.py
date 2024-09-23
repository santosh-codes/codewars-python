# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "


#  My Solution 

def double_char(s):
    myList = list(s)
    newList = [ x*2 for x in myList]
    convert = ''.join(newList)
    return(convert)