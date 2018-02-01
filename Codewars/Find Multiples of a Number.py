#build a program that takes a value, integer, and returns a list of its multiples
#up to another value, limit. If limit is a multiple of integer, it should be included as well.

#Difficulty: 7kyu.
#Link: https://www.codewars.com/kata/58ca658cc0d6401f2700045f

def find_multiples(integer, limit):
    list = []
    i = 1
    j = integer
    while integer <= limit:
        if j * i <= limit:
            integer = j * i
            i = i + 1
            list.append(integer)
        else:
            break
    return list

if __name__ == "__main__":
    assert [5, 10, 15, 20, 25] == find_multiples(5, 25)
    assert [1, 2] == find_multiples(1, 2)
    assert [4, 8, 12, 16] == find_multiples(4, 17)
    assert [3, 6, 9, 12, 15] == find_multiples(3, 17)
    assert [1] == find_multiples(1, 1)