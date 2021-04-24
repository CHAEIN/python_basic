"""
문자열 포메팅
서식문자, 포멧 지시어를 이용해 문자열 포메팅

C언어에서 사용하던 방식
printf("현재 온도는 %d도 입니다.", 17);
"""

a = 3
print("I eat %d apples." % a)
print("I eat %s apples." % "five")
b = "six"
print("I eat %s apples." % b)


n = 2
m = 3

print("%d단" % n)
print("%d x %d = %d" % (n, m, n*m))

"""
포맷 지시어 사용 시 주의할 점.
ch = 'a'
print("%c %d" % (ch,ch))
TypeError: %d format: a number is required, not str
"""
ch = "a"
print("%c %s" % (ch, ch))
"문자열을 정수"

t = 65
print("%c, %s" % (t, t))

"""
%s는 모든 형식을 다 표현해준다
%c는 문자 1개를 표현하는데 파이썬은 ''를 사용하나 ""를 사용하나 모두 문자열로 취급하기 때문에
문자(캐릭터)를 %d로 출력하려 할 때 에러가 발생한다.

C언어 / 파이썬에서 포멧 지시어 종류에 따른 데이터 출력 결과
C언어 
숫자 97 --> 
%d로 출력할 경우 97 
%c로 출력할 경우 a

문자 a --> 
%d로 출력할 경우 97 
%c로 출력할 경우 a

파이썬 
숫자 97 --> 
%d로 출력할 경우 97 
%c로 출력할 경우 a

문자 a --> 
%d로 출력할 경우 에러 발생 
%c로 출력할 경우 a
"""

"""오른쪽 정렬"""
print("%10s" % "hi")
"""왼쪽 정렬"""
print("%-10sjane." % 'hi')
print("%-10s world." % 'hello')
print("%10d" % 5)
print("%10s" % "hello")
print("%.2f" % 3.141592)

"""format 함수를 이용한 대입"""
h = 'hello'
print("I eat {0} apples.".format(4))
print("{0} {1}".format(h, "world"))
print("{s1} {s2}".format(s2 = h, s1 = "world"))

print("{0:10}".format('hello'))
"""오른쪽 정렬"""
print("{0:<10}".format('hello'))
"""왼쪽 정렬"""
print("{0:>10}".format('hello'))
"""가운데 정렬"""
print("{0:^10}".format('hello'))

"""공백 채우기"""
print("{0:@>10}".format('hello'))
print("{0:_>10}".format('hello'))
print("{0:-^13}".format('hello'))

"""f 문자열 포매팅"""
name="이정민"
print(f'my name is {name}')
age = [20,21,22,23,24]
print(f'나이는 {age[0]}')
print(f'나이는 {age[1]}')
my = {'job' : '회사원', 'age' : 27}
print(f'직업은 {my["job"]}, 나이는 {my["age"]}')
print(f'나는 내년이면 {my["age"]+1}살이 된다.')


abcd = [{'a':10, 'b': 20}, {'c':30, 'd': 40}]
print(f'{abcd[0].get("a")}')
ab = abcd[0]
print(f'{ab["a"]}')
a = (abcd[0])['a']
print(f'{a}')
print("%d" % (abcd[0])['a'])


xy = {'x' : [1,2,3], 'y' : [4,5,6]}
#xy 안에 있는 값 중 5만 출력
print(xy)
print((xy["y"])[1])