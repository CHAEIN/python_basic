"""
문자열 연산
특이한 기능이 많다.
"""

head = "Python"
tail = " is fun"
print(head + tail)
a = "hello"
print(a*3)

print("=" * 50)
print("My Program")
print("=" * 50)
# 정말 탐나는 기능!!!

print("a의 길이는", len(a))

life = "Life is too short"
print("life의 길이는 ", len(life))
print("life[0]:", life[0])
print("life[1]:", life[1])
print("life[2]:", life[2])
print("life[3]:", life[3])
print("life[4]:", life[4])
print("life[5]:", life[5])
#print("life[17]: ", life[17]) 17번째 값이 없기때문에 에러 발생
print("life[-1]:", life[-1])
print("life[-3]:", life[-3])
print("life[-5]:", life[-5])
#life[-1]은 뒤에서부터 첫번째의 값을 가져온다.
print("life[0:2]:", life[0:2])
print("life[0:4]:", life[0:4])
print("life[0:12]:", life[0:12])
print("life[12:17]:", life[12:17])
print("life[3:4]:", life[3:4])
#3번째부터 4번째 앞까지를 의미 (3 <= life < 4)
print("life[1:]:", life[1:])
print("life[1:-3]:", life[1:-3])

today = "20210417Rainy"
date = today[:8]
weather = today[8:]
year = today[:4]
month = today[4:6]
day = today[6:8]
print(date, weather)
print(date)
print(year)
print(month)
print(day)
print(weather)