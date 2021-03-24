def prt1():
    print("I'm a Niceboy!")

def prt2():
    print("I'm a Goodboy!")

## 테스트?
## 실행해도 결과를 확인 불가능함
## 이때 단위 실행이 필요
## 단위 실행 : 독립적으로 파일 실행
## 메인으로 실행할떄만 실행되는 코드 작성 가능
## 다른 곳에서 호출해서 사용했을떄는 실행이 되지 않음
if __name__=="__main__":
    prt1()
    prt2()