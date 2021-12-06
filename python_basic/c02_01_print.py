# Print 사용법

# 기본 출력
print('Python start!')
print("Python start!")
print('''Python start!''')
print("""Python start!""")

print()

# separator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
print('010', '7777', '1234', sep='-')
print('python', 'google.com', sep='@')

print()

# end 옵션
print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')

print()

# file 옵션
import sys
print('Learn Python', file=sys.stdout) # 콘솔아웃 옵션 터미널에 그대로 출력
print()

# format 사용 (d : 정수(1,2,3), s : '문자열', f : 실수(3.14))
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one','two'))

print()

# %s
print('%10s' %('nice'))
print('{:>10}'.format('nice')) # 열자리 중 오른쪽이 글자

print('%-10s' %('nice'))
print('{:10}'.format('nice')) # 열자리중 왼쪽이 글자

print('{:_>10}'.format('nice')) # 왼쪽에 _출력 후 문자열 출력
print('{:^10}'.format('nice')) # 중앙 정렬

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy')) # 절삭(반올림) 5글자만 출력하라
print('{:10.5}'.format('pythonstudy')) # 공간은 10개 글자는 5개만 출력하라


# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42)) # 4자리 중 뒤에 2자리 정수 출력

print()

# %f
print('%f' % (3.14123123)) # 정수부 소수부 지정 가능 (%1.8f -> 정수 1자리 소수 8자리)
print('{:f}'.format(3.14123123))

print('%06.2f' % (3.1415926)) # 출력하면 => 003.14
print('{:06.2f}'.format(3.1415926)) # 출력하면 => 003.14 
