letter = '''
Dear <|NAME|>,
From now, you are the lover of Vishal.
Thank You!'''
# Date = <|DATE|>

name = input("Enter your name:")
# date = input("Enter DaTe:")
letter = letter.replace("<|NAME|>",name)
# letter = letter.replace("<|DATE|>",date)
if name == "Vishal" or "Vishu" :
    print(letter)
else :
    print("Who are you? We doesn't know you.")