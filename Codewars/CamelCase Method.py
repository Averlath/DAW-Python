#All words must have their first letter capitalized without spaces.
#Example: camelcase("hello case") => HelloCase; camelcase("camel case word") => CamelCaseWord

#Difficulty: 6kyu.
#Link: https://www.codewars.com/kata/587731fda577b3d1b0001196

def camel_case(string):
    string = str.title(string)
    change = " "
    for element in string:
        if element in change:
            string = string.replace(element, "")
    return string

if __name__ == "__main__":
    assert "TestCase" == camel_case("test case")
    assert "CamelCaseMethod" == camel_case("camel case method")
    assert "SayHello" == camel_case("say hello")
    assert "CamelCaseWord" == camel_case(" camel case word ")
    assert "CamelCaseIsFun" == camel_case("CAMEL CASE IS FUN")
    assert "" == camel_case("")