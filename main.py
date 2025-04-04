import csv
# create an intro function to direct the user and state purpose of app
def intro()
  print(f'Welome to the Spanish and French translator app. \nPlease enter an English word and press the "Enter" key.')
  print(f' \nType "done" at any time to exit.')

# create an exit function
def exit()
  print(f'\nThanks for using the translator app. Have a good day!')

translations = {}

with open("translations.csv", "r") as words:
  reader = csv.DictReader(words, delimiter=",")
for line in reader:
  english = line["English"]
  line = ["English"].lower()
  spanish = line["Spanish"]
  line = ["Spanish"].lower()
  french = line["French"]
  line = ["French"].lower()

# translations[english] sets the English header as the dictionary key
# translations[english] should be equal to spanish and french values
translations[english] = [spanish, french]

done = False
# call intro function
intro()

# setting the while loop to not done means the loop will run as long as done is false
while not done:
  word = input("Type a word in English to translate.")
  word = word.lower()
  if word == "done":
    # setting done to true will end the loop
    done == True
    exit()
    # adjust the output of Spanish and French translations
    # word variable is the dictionary key; [0] is the Spanish word in index 0 - they were set here when spanish was placed in the first position of the dictionary keys
  elif word in translations:
    print(f'\nSPANISH:{translations[word][0]}')
  elif word in translations:
    print(f'\nFRENCH:{translations[word][1]}')
  else:
    print("Sorry that word is not listed in the dictionary.")

