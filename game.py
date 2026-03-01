import sys

def guess_next_number(left: int, mid: int, right: int, range: str) -> tuple[int, int, int]:
    if range == "Higher":
        left = mid + 1
    if range == "Lower":
        right = mid - 1

    mid = (left + right) // 2

    return left, mid, right

print("=" * 50)
print("Welcome to the number guessing game!")
print("=" * 50)
print("This game was created to show you how optimal binary search can be")
print()
print("Think of a number between 0 and 100.")
print()
print("When you're ready, type 'Y' to begin.")
print()

game = False
game_start = input("Have you picked a number? (Y/N): ")

if game_start.lower() == "y":
    game = True
    print("Let's begin!")
else:
    print("Understandable, have a good day.")
    sys.exit(0)

counter = 1
left = 1
mid = 50
right = 100
while game:
    print()
    answer = input(f"Is your number {mid}? (y/n): ")

    if answer.lower() == 'y':
        print(f"Yay! I got your number in {counter} attempts! Have a nice day!")
        game = False
    else:

        range = input(f"Hmm, interesting... Is your number higher or lower than {mid}? (h/l): ")
        if range.lower() == 'l':
            range = 'Lower'
        else:
            range = 'Higher'

        left, mid, right = guess_next_number(left, mid, right, range)
        counter += 1
