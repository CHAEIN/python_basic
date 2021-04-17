"""
문자열 테스트
"""

print(3**4)
print('hello')
print("hello")
print("""hello""")
print('''hello''')
print("he'llo")
print('he"llo')
print("he\"llo")
print("hello\nworld")
print("hello\nworld")

multiLine = """
Hello
World
1234
"""
print(multiLine)

"""
매우 특이하게도 파이썬에서는 주석을 변수에 담을 수 있고
출력 명령어 안에 주석이 들어가도 주석으로 인식하지 않고 문자열을 리턴한다.
"""

print("hello\rw")
print("hello\r ew")
print("hello\r 111w")
print("hello\rw\nabc")
print("hello\rw\nabc\f123")
print("hello\a")

"""
\r: 캐리지 리턴 (줄 바꿈 문자, 현재 커서를 가장 앞으로 이동)
Spyder 와 Pycharm의 동작이 다르다. 이유가 뭐지..
1. 컴파일러의 차이, 툴 별로 메모리를 사용하는 방식이 달라서 표현방식이 달라질 수 있다.
print("hello\rw")는 wello 로 표현되는것이 맞다.
2. 컴파일러가 \r을 만나 처음으로 돌아가는데 이후 w 뒤에 \0 이 숨겨져있어서 
실제 문자열이 남아있지만 문자열 종료라고 생각하고 출력하지 않았을 수 있다.
3. 컴파일러가 \r을 만나 처음으로 돌아가면서 뒤의 문자열을 지웠을 수 있다. (이럴 확률은 희박..) 
"""

print("hello\babc")
print("hello\0abc")
print("hello\000abc")
#\000: null 문자. 문자열의 끝을 의미.