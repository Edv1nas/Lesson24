"""write a function that accepts a number as a parameter. The function should return a number that’s the difference between the largest and smallest numbers that the digits can form in the number.
For example, if the parameter is “213”, the function should return “198”, which is the result of 123 subtracted from 321."""

from dotenv import dotenv_values


values = dotenv_values(".env")
number = values["NUMBER"]


def difference_largest_smallest_number(number: int) -> int:
    numbers = sorted(int(x) for x in number)
    smallest_number = int("".join(str(value) for value in numbers))
    largest_number = int("".join(str(value) for value in numbers[::-1]))
    return largest_number - smallest_number


difference = difference_largest_smallest_number(number)
print(difference)
