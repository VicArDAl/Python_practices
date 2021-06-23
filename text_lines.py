"""Write a Python program to print the following string in a specific format (see the output).
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

Twinkle, twinkle, little star, 0
	How I wonder what you are! 1
		Up above the world so high,2
		Like a diamond in the sky.3
Twinkle, twinkle, little star,
	How I wonder what you are
"""
count=0
paragraph=[]
a = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
"""Separate the string in a list of words"""
b = a.split()
for i in b:
    """Separate the word in single letters, this is to later identify if the first letter is uppercase"""
    c=list(i)
    """this search if the first letter is uppercase and adds enter to the paragraph"""
    if c[0].isupper() and c[0]!="I":
        """this join the list into a string"""
        if count == 0:
            paragraph.append(i)
            count += 1
        elif count == 1:
            paragraph.append("\n    ")
            paragraph.append(i)
            count += 1
        elif count == 2:
            paragraph.append("\n        ")
            paragraph.append(i)
            count += 1
        elif count ==3:
            paragraph.append("\n        ")
            paragraph.append(i)
            count += 1
        else:
            paragraph.append("\n")
            paragraph.append(i)
            count=1
    else:
        paragraph.append(i)
print(' '.join(paragraph))



