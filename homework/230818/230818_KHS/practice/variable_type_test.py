# 실수형에서 계산 결과 확인시 차이가 나는 부분
# 우리는 10진수를 사용하지만, 컴퓨터에서는 모든 연산의 처리를 이진법으로 함
# 실수 ->

a = 1.2
b = 1.4
c = 2.6
print(a+b == 2.6)
print(f"a의 메모리 위치 주소값(임시) id(a) : {id(a)}")
print(f"a의 메모리 위치 주소값(임시) id(b) : {id(b)}")
print(f"a와 b의 메모리 주소값 비교 is : {a is b}")