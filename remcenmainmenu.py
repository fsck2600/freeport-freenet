def show_menu():
    print("\\ REMCentral - Main Menu")
    
    print("1 Start Here!")
    
    print("2 The Jay S. Rouman Memorial")
    
    print("3 Communications Center")
    
    print("4 User Services and Utilities")
    
    print("5 The Schools (projects, organizations, and schools)")
    
    print("6 Transporter Room")
    
    print("------------------------------------------------------------------")
    print("h=Help, x=Exit REMCen, “go help”=Extended Help, p=Previous Menu\n")







def get_user_choice():
    choice = input("Your Choice ==> ")
    return choice

def handle_choice(choice):
    if choice == "1":
        print("\nStart Here! section")
        # Add your code for Start Here! functionality
    elif choice == "2":
        print("\nThe Jay S. Rouman Memorial section")
        # Add your code for The Jay S. Rouman Memorial functionality
    elif choice == "3":
        print("\nCommunications Center section")
        # Add your code for Communications Center functionality
    elif choice == "4":
        print("\nUser Services and Utilities section")
        # Add your code for User Services and Utilities functionality
    elif choice == "5":
        print("\nThe Schools (projects, organizations, and schools) section")
        # Add your code for The Schools functionality
    elif choice == "6":
        print("\nTransporter Room section")
        # Add your code for Transporter Room functionality
    elif choice == "h":
        print("\nHelp section")
        # Add your code for Help functionality
    elif choice == "x":
        print("\nExiting REMCen...")
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
