#string concatenation (aka how to put strings together)
#suppose we want to create a string that says "subscribe to __________"
#youtuber = "Chris" #some string variable

#a few ways to do this
#print("subscribe to " + youtuber)
#print("subscribe t0 {}".format(youtuber))
#print(f"sucribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("verb: ")
verb2 = input("verb: ")
famous_person = input("Famous person: ")

madlip = f"Computer programming is so {adj}! It makes me so excited all the time because \
Ilove to {verb1}. Stay hydrated and{verb2} like you are {famous_person}!"

print(madlip)
