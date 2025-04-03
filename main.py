translations = {
    "hello": "hola",
    "thank you": "gracias",
    "sorry": "lo siento",
    "goodbye": "adios",
    "day": "día",
    "chair": "silla",
    "house": "casa",
    "car": "coche",
    "bread": "pan",
    "book": "libro",
    "paper": "papel",
    "child": "muchacho"
}

done = False

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

print('Type "done" at any time to exit')
