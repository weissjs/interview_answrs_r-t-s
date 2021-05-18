# Jordan Weiss
# RTS LABS 'take-home'
# Problem #2


# Function that takes a prompt as input, and displays for the user,
# and scans until user enters an integer value
def scan_int(prompt):
    # Iterate until break condition i.e. try clause works
    while(1):
        # Scan user input following prompt
        string = input(prompt)
        # Exception handling for non-valid entries
        try: 
            integer=int(string)
        except (ValueError):
            print("Please enter a valid integer...")
            continue
        else:
            break
    # Return integer after valid user input
    return integer

def main():
    # Prompt user for string input
    strng = input("Enter a string: ")
    
    # Prompt user for input string and input shift val
    shift_amt = scan_int("Rotate string by.. ? ")
    
    # Concatenate left hand and right hand side of string for reconstruction
    
    ### ex. MyString shifted by 2 
    #
    #   [ng] + [MyStri]
    #   
    ###
    
    strng_rotate = strng[len(strng)-shift_amt :] + \
                    strng[:len(strng)-shift_amt]
                    
    # Display result
    print(strng_rotate)

if __name__ == '__main__':
    main()