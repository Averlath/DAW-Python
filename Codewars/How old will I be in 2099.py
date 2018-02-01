#Philip's just turned four and he wants to know how old he will be in various years in the
#future such as 2090 or 3044. His parents can't keep up calculating this so they've
#begged you to help them out by writing a programme that can answer Philip's endless questions.

#Difficulty: 8kyu.
#Link: https://www.codewars.com/kata/5761a717780f8950ce001473

def calculate_age(year_of_birth, current_year):
    if year_of_birth == current_year +1:
        return 'You will be born in ' + str(year_of_birth - current_year) + ' year.'
    elif year_of_birth +1 == current_year:
        return 'You are ' + str(current_year - year_of_birth) + " year old."
    elif year_of_birth < current_year:
        return 'You are ' + str(current_year - year_of_birth) + " years old."
    elif year_of_birth > current_year:
        return 'You will be born in ' + str(year_of_birth - current_year) + ' years.'
    else:
        return 'You were born this very year!'

if __name__ == '__main__':
    assert "You are 4 years old." == calculate_age(2012, 2016)
    assert "You are 27 years old." == calculate_age(1989, 2016)
    assert "You are 90 years old." == calculate_age(2000, 2090)
    assert "You will be born in 10 years." == calculate_age(2000, 1990)
    assert "You were born this very year!" == calculate_age(2000, 2000)
    assert "You are 2000 years old." == calculate_age(900, 2900)
    assert "You will be born in 20 years." == calculate_age(2010, 1990)
    assert "You will be born in 510 years." == calculate_age(2010, 1500)
    assert "You are 1 year old." == calculate_age(2011, 2012)
    assert "You will be born in 1 year." == calculate_age(2000, 1999)
    assert "You will be born in 2000 years." == calculate_age(500, -1500)