# Jordan Weiss
# RTS LABS 'take-home'
# Problem #1

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

# Function uses scan_int calls to fill an array of specified length
def fill_val_array(arr_len):
    # List initialization
    val_list = []
    # Iterate through and append new entries
    for i in range(0,arr_len):
        # Use scan_int calls to prompt user for valid input, and append
        val = scan_int("")
        val_list.append(val)
    # Return the list
    return val_list

# Function does the comparison between each val in list and the input thresh
def compare_thresh(val_list, thresh):
    # Make sure num_above/below are starting at zero
    num_above = 0
    num_below = 0
    # Iterate through list and compare values to thresh
    for i in val_list:
        if i > thresh:
            num_above += 1
        if i < thresh:
            num_below += 1
    # Return data to function call
    return num_above, num_below

def main():
    # Scan user input for threshold
    thresh  = scan_int("Please enter the desired threshold: ")
    # Scan user input for array length
    arr_len = scan_int("Please enter the number of values in the array: ")
    
    # Initialize and fill value array using function call
    val_list = fill_val_array(arr_len)

    # Sanity check to print array contents
    # print("Array contains :", val_list)

    # Use compare_thresh call to complete the comparisons
    num_above, num_below = compare_thresh(val_list, thresh)

    # Display result
    print("number above:",num_above)
    print("num below:",num_below)

if __name__ == '__main__':
    main()

