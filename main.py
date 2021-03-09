word = "sandwich"
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
      print("The first letter of the word is 's'")
    elif guesses == 3:
      print("The last letter of the word is 'h'")
    elif guesses == 5:
      print("You have had 5 incorrect guesses.")
      print("You lose!")
      break
    print("Guess a word:")
    guess = input()