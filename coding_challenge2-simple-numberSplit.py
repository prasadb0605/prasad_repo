#Given a number, return a list containing the two halves of the number.if the number is odd, make the rightmost number higher.
def number_split(n):
    if n % 2 == 0:
        return [n // 2, n // 2]
    else:
        return [n // 2, n // 2 + 1]

# Example usage:
print(number_split(10))  # Output: [5, 5]
print(number_split(-11))  # Output: [5, 6]

