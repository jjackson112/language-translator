import csv

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
print('Type "done" at any time to exit')

# setting the while loop to not done means the loop will run as long as done is false
while not done:
  word = input("Type a word in English to translate.")
  word = word.lower()
  if word == "done":
    # setting done to true will end the loop
    done == True
  elif word in translations:
    print(translations[word])
  else:
    print("Sorry that word is not listed in the dictionary.")

