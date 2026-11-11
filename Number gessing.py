import random

number = random.randint(1, 100)
attempts = 0

print("🎯 Number Guessing Game")
print("Maine 1 se 100 ke beech ek number socha hai.")

while True:
    guess = int(input("Apna guess enter karo: "))
    attempts += 1

    if guess < number:
        print("📉 Too low! Thoda bada number try karo.")

    elif guess > number:
        print("📈 Too high! Thoda chhota number try karo.")

    else:
        print("🎉 Correct!")
        print(f"Tumne {attempts} attempts mein number guess kar liya.")
        break
