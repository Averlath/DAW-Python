#Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer.
#You don't need to validate the form of the Roman numeral.
#Example: solution('XXI') should return 21.

#Difficulty: 4kyu.
#Link: https://www.codewars.com/kata/51b6249c4612257ac0000005

def solution(roman):
    numerals = [{'letter': 'M', 'value': 1000}, {'letter': 'D', 'value': 500}, {'letter': 'C', 'value': 100}, {'letter': 'L', 'value': 50}, {'letter': 'X', 'value': 10}, {'letter': 'V', 'value': 5}, {'letter': 'I', 'value': 1},]
    index_by_letter = {}
    for index in range(len(numerals)):
        index_by_letter[numerals[index]['letter']] = index
    result = 0
    previous_value = None
    for letter in reversed(roman):
        index = index_by_letter[letter]
        value = numerals[index]['value']
        if (previous_value is None) or (previous_value <= value):
            result += value
        else:
            result -= value
        previous_value = value
    return result

if __name__ == '__main__':
    assert 1000 == solution('M')
    assert 1 == solution('I')
    assert 4 == solution('IV')
    assert 15 == solution('XV')
    assert 100 == solution('C')
    assert 152 == solution('CLII')