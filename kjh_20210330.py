#파이썬300제 130~
과일 = ["사과", "귤","수박"]
for 변수 in 과일:
    print(변수)
    print("####")

for 변수 in ["A","B","C"]:
    print(변수)

변수 = "A"
print(변수)
변수 = "B"
print(변수)
변수 = "C"
print(변수)

변수 = "A"
b = 변수.lower()
print("변환:",b)
변수 = "B"
b = 변수. lower()
print("변환:",b)
변수 = "C"
b = 변수. lower()
print("변환:",b)
for a in [10,20,30]:
    print(a)
    print("-------")

print("++++")
for a in [10,20,30]:
    print(a)

for a in [1,99,3]:
    print("-------")

리스트 = [100,200,300]
for a in [100,200,300]:
    print(a * 1.1)

리스트 = ["김밥","라면","튀김"]
for 오늘의_메뉴 in ["김밥","라면","튀김"]:
    print("오늘의 메뉴:"+오늘의_메뉴)

리스트 = ["sk하이닉스","삼성전자","LG전자"]
for 종목 in ["sk하이닉스","삼성전자","LG전자"] :
    길이 = len(종목) 
    print(길이)

print("="*90)
a = [1,2,3]
print(id(a))

b = a
print(id(b))

a[0] = 100

print(a, id(a))
print(b, id(b))

a= [1,2,3]
b= a[:]
a[0] = 100
print(a,id(a))
print(b,id(b))

print("="*90)

from copy import copy
a = [1,2,3]
b = copy(a)
a[0] = 100
print(a, id(a))
print(b, id(b))

print('-'* 20)

# 튜플 선언
a = ('hello','python')
print(a)
(a,b) = 'hello', 'python'
print(a)
print(b)


print('-'* 20)

a=b='python'
a= 'hi'
print(a,id(a))
print(b,id(b))
a=3
b=2
a,b = b,a  #a와 b가 바뀜
print(a)
print(b)
# 함수
def add(a,b): #함수 정의
    return a + b
print(add(1,2)) #함수 사용
print(add(3,2)) #a-->3, b-->2

result = add(5,7)
print(result)

print('-'* 20)
def say():
    return 'Hi'
result = say()
print(result)

print('-'*80)

def add(a,b):   #결괏값이 없는 함수
    print(f"{a},{b}의 합은 {a+b}입니다")

add(77,88)
result = add(33,44)
print(result)   #리턴이 없다, 아무것도 반환하지 않았따

def say():  #입력값과 결괎값이 모두 없는 함수
    print('Hi')
say()
result = say()
print(result) # 입력값이 없고 결괏값만 있는 함수는 다음과 같이 사용된다.
              # 결괏값을 받을 변수 = 함수이름()

print('-'*80)
a = [2,3,1,4]
a.sort()    #입력값도 없고결과값이 없는 함수
print(a.sort())
print(sorted(a)) #입력값은 없지만 결과값이 있는 함수)

#print 함수의 형태는? (입력값!)
# result = print('abc')    
# print(result)    # None이 나오므로, 결과값이 없는 함수




def add(a,b):
    return a-b

print(add(a=1, b=2))
print(add(b=1, a=2))    # 매개변수 순서 무관

print('-'* 80)
def add_many(*args):    # args: Tuple
    print(type(args))
    print((args))
    result = 0
    for i in args:  # (1,2,3)
        result = result + i
    return result

print(add_many(1,2))
print(add_many(1,2,3))
print(add_many(1,2,3.4,5,6,7,8,9,10))

def print_kwargs(**kwargs):
     print(kwargs)

print_kwargs(a=1)
print_kwargs(a=1, b=2, test=100)

print('-'* 80)

def add_and_mul(a,b):
    return a+b, a*b

result = add_and_mul(2,3)
print(result)   #Tuple(5,6)

result1, result2 = add_and_mul(2,3)
print(result1) # a+b
print(result2) # a*b

print('-'*80)

def say_nick(nick):
    if nick == "바보":
        return 'hi'     # 함수
    print("나의 별명은 %s 입니다." % nick)

say_nick('홍길동')
say_nick('바보')

def say_myself(name,  man= True, old=10): # 초기값을 설정하는 매개변수(선택요소)는 마지막에
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살 입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

# say_myself('홍길동', man=True, old=10)
# say_myself('홍길동',10, man=True)
# say_myself('홍길동',30, True)

print('-'* 80)

# a = 1
# def vartest(b):
#     a= a + 1
#     return a

# a = vartest(a)
# print(a)

# print('-'* 80)

def add(a,b):
    return a+b

add = lambda a, b: a+b

print (add(2,7))

print('-'* 80)
# a = input('값을 입력하세요:')
# print("life" "is" "too short")
# print("life" + "is" + "too short")
# print("life" , "is" , "too short", sep='#')
# print("life" , "is" , "too short", sep='')
# print("life" , "is" , "too short", end='')
# print("life" , "is" , "too short", end='')
# print("life" , "is" , "too short", end='')

for i in range(10):
    print(i, end='')
 #파일 입출력
print('-' *20)

f = open('새파일.txt', 'w') #쓰기 모드 : 기존내용 덮어씌움
f.write('python1234')
f.close()

f = open('새파일.txt', 'a') #추가 모드 :
f.write('hello\n')
f.write('hello\n')
f.write('2x1 =2\n')
f.write('2x2 =4\n')
f.write('2x3 =6\n')
f.write('2x4 =8\n')
f.write('2x5 =10\n')
f.write('2x6 =12\n')
f.write('2x7 =14\n')
f.write('2x8 =16\n')
f.write('2x9 =18\n')


f.close()