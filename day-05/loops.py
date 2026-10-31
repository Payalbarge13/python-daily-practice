#1
print("***1st loop code***")
for letter in "Python":
    print(letter)
#2
print("***2nd loop code***")
for num in range(1, 6):
    if num == 3:
        continue  # Skips 3
    if num == 5:
        break     # Stops the loop entirely at 5
    print(num)
