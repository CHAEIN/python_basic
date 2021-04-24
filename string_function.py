"""문자열 관련 함수"""
a = "hobbbbbby"
print(a.count('b'))
print(a.count('b',0,5))
print(a.count('b',4,7))
print(a.find('y'))
"""없는 문자를 찾을 경우 -1 리턴"""
print(a.find('a'))

b = "Life is too short"
print(b.index('t'))
"""없는 문자를 찾을 경우 not found 에러 발생
print(b.index('a'))
"""
print("|".join('apple'))

str = "hello world hi apple"
print(str.find('apple'))

print(str.replace('hi', 'hello'))
print(str.replace('hi', 'hello'))
print(str)
str = str.replace('hi', 'hello')
print(str)
print(str.replace(' ', ','))
print(str.split(" "))

fruit = 'Apple'
print(fruit)
print(fruit.upper())
print(fruit.lower())

d = "   test   "
print(d)
print(d.lstrip())
print(d.rstrip())
print(d.strip())

text = "!#$$!@$!!!!!!!!@$#231421234네123^&^#$#이!#12313_+{스"
text1 = "네이스"
text2 = "123123"
text3 = "!@#$"
text4 = "abcd"
print(text1.isalpha())
print(text2.isalpha())
print(text3.isalpha())
print(text4.isalpha())
print(text4.isascii())
print(text1.isascii())

