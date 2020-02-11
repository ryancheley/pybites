num_hundreds = -1

def sum_numbers(numbers: list) -> int:
    """Sums passed in numbers returning the total, also
       update the global variable num_hundreds with the amount
       of times 100 fits in total"""
    numbers_total = sum(numbers)
    global num_hundreds
    num_hundreds = num_hundreds + int(numbers_total / 100)
    return numbers_total
