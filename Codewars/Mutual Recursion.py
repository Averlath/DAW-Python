#You'll want to create two functions F and M such that the following equations are true:
#F(0) = 1
#M(0) = 0
#F(n) = n - M(F(n - 1))
#M(n) = n - F(M(n - 1))

#Difficulty: 6 kyu.
#Link: https://www.codewars.com/kata/53a1eac7e0afd3ad3300008b
def f(n):
    if n == 0:
        return 1
    else:
        return n - m(f(n-1))
    
def m(n):
    if n == 0:
        return 0
    else:
        return n - f(m(n-1))

if __name__ == "__main__":
    assert 1 == f(0)
    assert 3 == f(5)
    assert 6 == f(10)
    assert 0 == m(0)
    assert 3 == m(5)
    assert 6 == m(10)