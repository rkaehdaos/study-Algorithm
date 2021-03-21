# class
# self, class, instance
class UserInfo:
    # 속성
    calss_var=0
    # 메소드
    # 매직 메소드
    def __init__(self,name): # Constructor
        print('초기화')
        self.name=name
    def user_info_p(self):
        print('이름: ',self.name)

# instance : user1, user2
user1 = UserInfo('철수')
user2 = UserInfo('영희')
user1.user_info_p()
user2.user_info_p()

# 메모리 확인
print(id(user1))
print(id(user2))

# namespace : 객체 인스턴스화시 저장되는 공간
print(user1.__dict__)
print(user2.__dict__)
print(UserInfo.__dict__)

# 클래스 변수
print(UserInfo.calss_var)
print(user1.calss_var) # 인스턴스로 접근시 인스턴스에 없으면 클래스에서 찾는다
print(user2.calss_var)





