aList = [1, 2, 3]  # List Number


def sum_squere(list):  # Fungsi yang menerima parameter list
    # menggunakan list comprehension jadi sum menerima hasil perulangan
    return ((sum([i**2 for i in list])))
    # setelah di lakukan perulangan dan perpangkatan lalu di tambahkan lalu di return


print(sum_squere(aList))


def triangular(number):
    # sama seperti sum_squere tetapi disini perluangan yang terjadi dalam list comprehension perluangan dilakukan untuk mendapatkan nilai panjang loop dari number
    return sum([i for i in range(number + 1)])
    # setelah itu masuk kedalam function sum


print(triangular(5))


def pangkat(number, exponent):
    if exponent == 1:  # kondisi untuk memberhentikan fungsi rekursi
        return number
    else:
        return number * pangkat(number, exponent - 1)
        # memangil recursion fungsi agara recursion tidak terjadi terus menerus maka dibuatkan satu kondisi yaitu ketika exponentnya atau pangkat sudah 1 maka akan berhenti


print(pangkat(3, 2))


def is_palindrome(words):
    return True if words == words[::-1] else False
    # list comprehension jika words yang di balik dengan memanipulasi words dengan [::-1] jika benar maka akan mereturn true jika tidak maka false


print("True" if is_palindrome("rotator") else "False")

