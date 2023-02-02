
# karta_1 = "49927398716"     # Valid
# karta_2 = "215455557748"    # Valid
# karta_3 = "79927398714"     # Invalid

def turn_numbers(numbers: int) -> list:
    """Function to reverse the card number."""
    list_all_num = []
    for one_num in numbers:
        list_all_num.append(one_num)
    list_all_num.reverse()
    return list_all_num


def sum_odd_numbers(numbers: list) -> int:
    """Function counts every odd index."""
    list_odd_num = []
    # sum_odd_num = 0
    for one_num in range(0, len(numbers), 2):
        list_odd_num.append(int(numbers[one_num]))
    sum_odd_num = sum(list_odd_num)
    return sum_odd_num

    # result_sum_odd_num = sum_odd_numbers(result_turn_num)


def even_numbers(numbers: list) -> list:
    """Function prints each even number"""
    list_even_num = []
    for one_num in range(1, len(numbers), 2):
        list_even_num.append(int(numbers[one_num]))
    return list_even_num


def even_x_2(numbers: list) -> list:
    """Multiplies even number * 2"""
    list_even_x_2 = []
    for one_num in result_even_num:
        list_even_x_2.append(one_num * 2)
    return list_even_x_2


def sum_even_digit(numbers: list) -> int:
    """Calculates the digits of the even numbers"""
    result = 0
    for number in numbers:
        digits_sum = 0
        for digit in str(number):
            digits_sum += int(digit)
        result += digits_sum
    return result
    

def sum_odd_and_even(num_odd: int, num_even: int) -> int:
    """Calculates odd indices and digits of even numbers"""
    return num_odd + num_even

greet = "Welcome to the card verification app."
section = "-" * len(greet)
card_verification = True
print(greet+"\n"+section)

while card_verification == True:
    card_number = input("Enter card number: ")
    result_turn_num = turn_numbers(str(card_number))
    result_sum_odd_num = sum_odd_numbers(result_turn_num)
    result_even_num = even_numbers(result_turn_num)
    result_even_x_2 = even_x_2(result_even_num)
    sum_even = sum_even_digit(result_even_x_2)
    sum_all = sum_odd_and_even(result_sum_odd_num, sum_even)
    if sum_all % 10 == 0:
        print(">>> Valid card.")
        
    else:
        print(">>> Invalid card.")
        

    while True:
        again = input("Do you want to verify another card?\ny/n --> ")
        if again == "y":
            print(section)
            break
        else:
            print("OK, bye. ")
            print(section)
            quit()