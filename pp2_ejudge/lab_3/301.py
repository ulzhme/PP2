def check_valid_number():

    n_str = input().strip()
    
    for digit_char in n_str:

        digit = int(digit_char)
        
        if digit % 2 != 0:
            print("Not valid")
            return
            
    print("Valid")

if __name__ == "__main__":
    check_valid_number()