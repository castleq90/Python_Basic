# 파이썬 문자형

# 문자열 생성
str1 = "I am Python."
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

# 문자열 출력
print(type(str1))
print(type(str2))
print(type(str3))
print(type(str4))

# 문자열 길이
print(len(str1))
print(len(str2))
print(len(str3))
print(len(str4))

# 빈 문자열
str_t1 = ''
str_t2 = str()

print(type(str_t1), len(str_t1))
print(type(str_t2), len(str_t2))

# 이스케이프 문자 사용
"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...

"""

escape_str1 = "Do you have a \"retro games\"?"
escape_str2 = 'What\'s on TV?'


# 출력1
print(escape_str1)
print(escape_str2)

# 탭, 줄바꿈
t_s1 = "Click \tStart!"
t_s2 = "New Line\n Check!"

# 출력2
print(t_s1)
print(t_s2)

# Raw String
raw_s1 = r'D:\Python\python3'
raw_s2 = r"\\x\y\z\q"


# Raw String 출력
print(raw_s1)
print(raw_s2)

# 멀티 라인 (역 슬러쉬 사용)
multi_str1 = \
    """
    문자열
    멀티라인 입력
    테스트
    """
# 멀티라인 출력
print(multi_str1)

multi_str2 = \
    '''
    문자열 멀티라인 
    역슬래시(\) \
    테스트
    '''
# 멀티라인(역슬래시) 출력
print(multi_str2)

# 문자열 연산
str_o1 = "Python"
str_o2 = "Apple"
str_o3 = "How are you doing?"
str_o4 = "Seoul Deajeon Busan Jinju"

print(3 * str_o1)
print(str_o1 + str_o2)
print(dir(str_o1))
print('y' in str_o1)
print('n' in str_o1)
print('P' not in str_o2)

# 문자열 형 변환
print(str(66))  # type 확인 (스트링임)
print(str(10.1))
print(str(True))
print(str(complex(12)))

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha 등)
print("Capitalize: ", str_o1.capitalize()) # 시작 글자를 대문자로 스위칭
print("endswith?: ", str_o2.endswith("s")) # 끝 글자 참 거짓 확인
print("join str: ", str_o1.join(["I'm ", "!"])) # 첫 문장과 끝 문장에 문자열 추가
print("replace1: ", str_o1.replace('thon', ' Good'))
print("replace2: ", str_o3.replace("are", "was"))
print("split: ", str_o4.split(' '))  # Type 확인 (리스트)
print("sorted: ", sorted(str_o1))  # reverse=True
print("reversed1: ", reversed(str_o2)) #list 형 변환
print("reversed2: ", list(reversed(str_o2)))

# 반복(시퀀스) 설명
im_str = "Good Boy!"

print(dir(im_str))  # __iter__ 확인 (슬라이싱 처리 가능)

# 출력
for i in im_str:
    print(i)


# 슬라이싱
str_sl = 'Nice Python'

# 슬라이싱 연습
print(str_sl[0:3]) # 0, 1, 2 까지 출력
print(str_sl[:len(str_sl)])
print(str_sl[:len(str_sl) - 1])
print(str_sl[:])
print(str_sl[1:4:2])
print(str_sl[-4:-2])
print(str_sl[1:-2])
print(str_sl[::-1])
print(str_sl[::2])


# 아스키코드
a = 'z'

print(ord(a)) # 아스키 코드로
print(chr(122)) # 문자로

