votes = {"A":0,"B":0}

def vote():
    choice = input("Vote for candidate A or B: ").upper()

    if choice in votes:
        votes[choice] += 1
        print("Vote recorded on blockchain (simulation)")
    else:
        print("Invalid vote")

def results():
    print("\nVoting Results")
    for candidate,count in votes.items():
        print(candidate,":",count)

while True:
    print("\n1. Cast Vote")
    print("2. Show Results")
    print("3. Exit")

    option = input("Enter option: ")

    if option == "1":
        vote()
    elif option == "2":
        results()
    elif option == "3":
        break
    else:
        print("Invalid option")
