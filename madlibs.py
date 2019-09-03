import os as os

bashCmd = "clear"
os.system(bashCmd)

print('Hi! So happy you are here!')


name = input("Enter a name")
verb = input('Enter an -ing verb')
adjective = input('Enter an adjective')
noun = input('Enter a noun')
place = input('Enter a place')
color = input('Enter a color')
feeling = input('Enter a feeling')
number = input('Enter a number')
year = input('Enter a year')
song = input('Enter a song')
noun2 = input('Enter a noun (plural)')
noun3 = input('Enter a noun3')

print("I was sitting on a" + noun + " right outside of my house, when suddenly" + name + " drives up my driveway with"
+ color + noun2 + "." + name + " gets out of the car, looks at me in the eyes and with both arms in the air screams 'Let's go"
+ verb + "!'"".So I run inside to grab my" + adjective + noun3 + ",run back outside, hop on the passanger's seat and waved goodbye."
"We arrived to" + place + " and proceeeded to set up camp while listening to" + song + ". I was feeling" + feeling + color +
". It was the year of" + year)
