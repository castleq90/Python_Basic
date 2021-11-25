# 파이썬 변수

# 기본 선언
n = 700

# 출력
print(n)
print(type(n))

# 동시 선언
x = y = z = 700
print(x, y, z)

# 선언 
var = 75

# 재 선언
var = "Change Value"

# 출력
print(var)
print(type(var))


# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔에 출력

# 예1)
print(300)

# 예2)
# n -> 777
n = 777

print(n)
print(type(n))

m = n
# m-> 777 <- n

print(m, n)
print(type(m), type(n))

m = 400
# m-> 400, 777 <-n

print(m)
print(type(m))

# id(identity)확인 : 객체의 고유값 확인

m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 같은 오브젝트를 참조
m = 800
n = 800

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 다양한 변수 선언
# Camel Case :  numberOfCollegeGraduates
# Pascal Case :  NumberOfCollegeGraduates
# Snake Case :  number_of_college_graduates