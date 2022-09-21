aList = [1, 2, 3]


def sum_squere(list):
    return ((sum([i**2 for i in list])))


print(sum_squere(aList))


def triangular(number):
    return sum([i for i in range(number + 1)])


print(triangular(5))


def pangkat(number, exponent):
    if exponent == 1:
        return number
    else:
        return number * pangkat(number, exponent - 1)


print(pangkat(3, 2))


def is_palindrome(words):
    return True if words == words[::-1] else False


print("True" if is_palindrome("rotator") else "False")
