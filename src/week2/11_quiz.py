# q1
'''
class Foo:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('I am' + self.name)


class Bar(Foo):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print('You are ' + self.name)
bar = Bar('John')
bar.speak()
'''

# q2
# AttributeError : 속성 이름이 잘못 되었꺼나 없는 속성을 가져오려고 하는 경우
# ValueError : 타입은 맞지만 값이 다를때
# FileNotFoundError : 파일을 읽으려고 할떄 없을 떄 : r모드
# TypeError : 데이터 타입 관련 오류

# q3
'''
def int_sum(*args):
    try:
        for n in args:
            sum+=n
    except:
        print('error')
    return sum
int_sum((10,))
'''
# q8
import datetime
# now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
now = datetime.datetime.now()
print(now)