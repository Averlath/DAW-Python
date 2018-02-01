#In your class, you have started lessons about arithmetic progression.
#Since you are also a programmer, you have decided to write a function that will return
#the first 'n' elements of the sequence with the given common difference 'r' and first
#element 'a'. Result should be separated by comma and space.
#Example: arithmetic_sequence_elements(1, 2, 5) == '1, 3, 5, 7, 9'

#Difficulty: 7kyu.
#Link: https://www.codewars.com/kata/55caf1fd8063ddfa8e000018

def arithmetic_sequence_elements(a, r, n):
    list = []
    i = 1
    list.append(a)
    while i < n:
        a = a + r
        list.append(a)
        i = i+1
        x = str(list)
    change = ('[', ']')
    for element in x:
        if element in change:
            x = x.replace(element, "")
    return x

if __name__ == '__main__':
    assert '1, 3, 5, 7, 9' == arithmetic_sequence_elements(1, 2, 5)
    assert '1, -2, -5, -8, -11, -14, -17, -20, -23, -26' == arithmetic_sequence_elements(1, -3, 10)
    assert '5, 13, 21, 29, 37, 45, 53' == arithmetic_sequence_elements(5, 8, 7)