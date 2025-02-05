def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    if total == 0:
        return 0  # Handle list of zeros
    return total / len(numbers)

# Example usage:
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_list_with_zero = [0,0,0]
average_zero = calculate_average(my_list_with_zero)
print(f"The average of the list with zero is: {average_zero}")

my_list_with_zero_and_numbers = [0,10,20]
average_zero_and_numbers = calculate_average(my_list_with_zero_and_numbers)
print(f"The average of the list with zero and numbers is: {average_zero_and_numbers}") 