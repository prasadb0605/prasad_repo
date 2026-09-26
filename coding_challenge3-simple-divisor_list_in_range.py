'''
Create a function that takes three parameters where:

x is the start of the range (inclusive).
y is the end of the range (inclusive).
n is the divisor to be checked against.
Return an ordered list with numbers in the range that are divisible by the third parameter n. Return an empty list if there are no numbers that are divisible by n.

'''
def divisor_list_in_range(x, y, n):
    result = []
    for num in range(x, y + 1):
        if num % n == 0:
            result.append(num)
    print(f"Numbers divisible by {n} in the range {x} to {y}: {result}")
    return result

divisor_list_in_range(1, 10, 2)  # Example usage: Get numbers divisible by 2 in the range 1 to 10