##########################################################################################################
# Name:        1.py
# Description: Function to count digits in number
# Input:       Number
# Output:      Digits count
# Date:        02-07-2026
# Author:      Ritesh Jillewad
##########################################################################################################

def count_digits(number: int) -> int:
    """
    Counts the total number of digits in a number

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    int
        Total number of digits
    """

    digitCount = 0

    if number == 0:
        return 1
    
    if number < 0:
        number = abs(number)
    
    while number != 0:
        digitCount = digitCount + 1
        number = number // 10

    return digitCount

def main():

  print("Enter number: ")
  num = int(input())

  ret = count_digits(num)
  print(f"Digits count: {ret})

if __name__ == "__main__":
  main()
