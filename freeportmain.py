def show_menu():
    print("Welcome to the Freeport Freenet package\n")
    print("1 Start Here!")
    print("2 New to Freeport? Here's a how-to?")
    print("3 Communications Center")
    print("4 User Services and Utilities")
    print("5 File Libraries!")
    print("6 The WWW via Lynx")
    print("------------------------------------------------------------------")
    print("h=Help, x=Exit Freeport, “go help”=Extended Help, p=Previous Menu\n")

def get_user_choice():
    choice = input("Your Choice ==> ")
    return choice

def handle_choice(choice):
    if choice == "1":
        print("\nStart Here! section")
        # Add your code for Start Here! functionality
    elif choice == "2":
        print("\nNew to Freeport? Here's a how-to? section")
        # Add your code for New to Freeport? Here's a how-to? functionality
    elif choice == "3":
        print("\nCommunications Center section")
        # Add your code for Communications Center functionality
    elif choice == "4":
        print("\nUser Services and Utilities section")
        # Add your code for User Services and Utilities functionality
    elif choice == "5":
        print("\nFile Libraries! section")
        # Add your code for File Libraries! functionality
    elif choice == "6":
        print("\nThe WWW via Lynx section")
        # Add your code for The WWW via Lynx functionality
    elif choice == "h":
        print("\nHelp section")
        # Add your code for Help functionality
    elif choice == "x":
        print("\nExiting Freeport...")
        exit()
    elif choice == "go help":
        print("\nExtended Help section")
        # Add your code for Extended Help functionality
    elif choice == "p":
        print("\nReturning to previous menu...")
        # Add your code for going back to the previous menu
    else:
        print("\nInvalid choice. Please try again.")

# Main program loop
while True:
    show_menu()
    user_choice = get_user_choice()
    handle_choice(user_choice)
