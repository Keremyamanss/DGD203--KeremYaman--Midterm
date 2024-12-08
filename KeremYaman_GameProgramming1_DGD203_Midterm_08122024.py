def start_game():
    print("Welcome to the 'Choices of Adventure!' game!")
    player_name = input("What is your name, adventurer? ")
    print(f"\nHello, {player_name}! Ready to begin your adventure?\n")
    ask_questions(player_name)
def ask_questions(player_name):
    print("Here are your first questions:\n")
    
    print("1. You find a treasure chest in the middle of a dark forest. What do you do?")
    print("a) Open the chest immediately.")
    print("b) Leave it alone, something feels off.")
    print("c) Look around the area to make sure no one is watching.")
    
    choice1 = input("\nChoose a) b) or c): ").lower()
    
    print("\n2. You meet a stranger offering you a map to a hidden city. What do you do?")
    print("a) Accept the map and follow their directions.")
    print("b) Politely decline, you're not trusting strangers.")
    print("c) Ask for more details before deciding.")
    
    choice2 = input("\nChoose a) b) or c): ").lower()
    
    print("\n3. A wild animal approaches. How do you react?")
    print("a) Try to pet it, it looks friendly.")
    print("b) Stay still and observe the animal.")
    print("c) Run away as fast as you can.")
    
    choice3 = input("\nChoose a) b) or c): ").lower()
    
    print("\n4. You encounter a fork in the road, one path leads to a village, the other to a mountain. What do you do?")
    print("a) Head toward the village, hoping for some safety.")
    print("b) Venture towards the mountain, seeking adventure.")
    print("c) Stay at the fork and wait to see who comes by.")
    
    choice4 = input("\nChoose a) b) or c): ").lower()
    
    conclude_game(player_name, choice1, choice2, choice3, choice4)
def conclude_game(player_name, choice1, choice2, choice3, choice4):
    print(f"\nThanks for playing, {player_name}!\n")
    
    if choice1 == 'a' and choice2 == 'a':
        print("You are adventurous and bold! You dive into every opportunity without hesitation. Be careful, though, not all treasure is gold!")
    elif choice1 == 'b' and choice3 == 'a':
        print("You are cautious but also kind-hearted. You prefer to take things slow and make sure everything feels right.")
    elif choice2 == 'b' and choice4 == 'b':
        print("You're a skeptic who values your independence. Adventure calls you, but you don't rush into anything without thinking it through.")
    elif choice3 == 'c' and choice4 == 'c':
        print("It seems like you're cautious and a bit hesitant. Sometimes you like to observe things before making decisions, and that's a wise choice.")
    else:
        print("You're a balanced adventurer, taking calculated risks when necessary and being cautious when the situation calls for it. A wise path indeed.")
    
    print("\nThanks for playing again, have a great day!")