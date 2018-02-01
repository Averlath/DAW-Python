#Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.
#Example: solution(1000) should return 'M'.

#Difficulty: 4kyu.
#Link: https://www.codewars.com/kata/51b62bf6a9c58071c600001b

def solution(n):
    val = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    syb = ('M', 'CM', 'D', 'CD','C','XC','L','XL','X','IX','V','IV','I')
    roman_num = ""
    for i in range(len(val)):
        count = int(n / val[i])
        roman_num += syb[i] * count
        n -= val[i] * count
    return roman_num

if __name__ == '__main__':
    assert 'M' == solution(1000)
    assert 'I' == solution(1)
    assert 'IV' == solution(4)
    assert 'XV' == solution(15)
    assert 'C' == solution(100)
    assert 'CLII' == solution(152)