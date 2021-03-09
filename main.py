word = "sheep"
count_e = 0
print("What character do you want to check?")
character = input()

for letter in word:
  if letter == character:
    count_e = count_e + 1

print(f"The letter {character} appears {count_e} time(s)")