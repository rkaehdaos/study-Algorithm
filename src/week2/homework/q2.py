'''
아래 기반 코드를 완성하여, 입력받은 값 중 중앙값을 출력하는 클래스를 완성하시오. 입력받은 값이 짝수개이면, 중앙값 2개의 평균을 출력하시오. (단, clear 메소드는 입력받은 내역을 모두 삭제)

'''


class Median:
    def __init__(self):
        self.items = []

    def get_item(self, item):
        self.items.append(item)

    def clear(self):
        self.items.clear()

    def show_result(self):
        self.items.sort()  # sort
        item_len = len(self.items)
        if item_len == 0:  # 비었을 때
            return None
        if item_len % 2 == 1:  # 홀수 : n-1
            print(self.items[(item_len - 1) // 2])
        else:  # 짝수 : 중앙 2값의 avg( n-1, n)
            list_mid = item_len // 2
            print((self.items[list_mid - 1] + self.items[list_mid]) / 2)

median = Median()
for x in range(10):
    median.get_item(x)
median.show_result()
median.clear()
for x in [0.5, 6.2, -0.4, 9.6, 0.4]:
    median.get_item(x)
median.show_result()
