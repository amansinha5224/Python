import random

# Function Check for Winner
def winner(user1, user2):
    result = [
        ["D", "W", "L"], 
        ["L", "D", "W"], 
        ["W", "L", "D"]
    ]

    return result[user1][user2]

if __name__ == "__main__":
    print("snake water gun".upper().center(100))

    scoreUser1 = 0
    scoreUser2 = 0

    while True:

        print("""
1. Snake
2. Water
3. Gun
""")
        choice = ["Snake", "Water", "Gun"]

        user1 = int(input("\nEnter Your Choice (0 to Quit): "))

        if(not user1): break

        user2 = random.randint(0, 2)

        print(f"\nYOUR CHOICE: {choice[user1-1]} \nCOMPUTER CHOICE: {choice[user2]}\n")

        result = winner(user1-1, user2)

        match result:
            case "W":
                print("YOU WON")
                scoreUser1 += 1
            case "D":
                print("DRAW")
            case "L":
                print("YOU LOST")
                scoreUser2 += 1

        print(f"\nUSER SCORE: {scoreUser1} \nCOMPUTER SCORE: {scoreUser2}")
    

