# string concatenation (aka how to put a strings together)
# suppose we want to create a string that says 'subscribe to _____

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famouse_person = input("Famouse person:  ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time becasue" \
         f"I Love to {verb1}. Stay hydrated and {verb2} like you are {famouse_person}!"

print(madlib)