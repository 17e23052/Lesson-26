word = "sandwich"
wordlength = len(word)
guesses = 0
print("Guess a word:")
guess = input()
while guesses < 5:
  if guess == word:
    print("Correct, you win!")
    break
  else:
    print("Incorrect.")
    guesses = guesses + 1
    if guesses == 1:
      print(f"The first letter of the word is {word[0]}")
    elif guesses == 3:
      print(f"The last letter of the word is {word[wordlength - 1]}")
    elif guesses == 5:
      print("You have had 5 incorrect guesses.")
      print("You lose!")
      break
    print("Guess a word:")
    guess = input()