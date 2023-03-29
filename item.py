# 무슨 아이템을 구현해야할까?
# 포션 체력이 max_hp인 상태까지만 채워지게 하기


class Items:
    def __init__(self, name, can_use, dropable: bool, attribute='아이템'):
        self.name = name
        self.can_use = can_use
        self.dropable = dropable
        self.attribute = attribute

    def throw_away(self):
        if self.dropable == True:
            print(f'{self.name}을 버렸습니다.')
        else:
            print(f'{self.name}을 버릴 수 없습니다.')


class EquipmentItem(Items):
    """
    장착 / 해제형 아이템
    검 스태프 활 등등
    """

    def __init__(self, name, effect=1):
        super().__init__(name, can_use=True, dropable=False, attribute='장비아이템')
        self.effect = effect

    def wear(self, power_num, magic_num):
        if self.can_use:
            equipitem_effect = [self.effect *
                                power_num, self.effect * magic_num]
            print(f'{self.name}을 착용했다!')
            print(f'{self.effect}')


class UseTypeItem(Items):
    """
    사용형 아이템
    1회 사용 후 삭제
    포션, 랜덤효과 약초 등
    """

    def __init__(self, name, effect=1):
        super().__init__(name, can_use=True, dropable=True, attribute='소비아이템')
        self.effect = effect

    def get_items(self,  eft_num):
        self.effect = (self.effect * eft_num)

    # 사용 입력이 들어오면 사용
    def use(self):
        if self.can_use:
            print(f'{self.name}을 사용했다!')
            print(f'{self.effect}')
            self.can_use = False


"""---------------이 아래에 변수 선언-----------------"""


def example():
    """
    내가 만든 코드 돌려보기/테스트하기
    1. 여기다가 사용 예제 적는거
    2. test 코드 만드는거
    """
    포션 = UseTypeItem('파란포션')
    포션.use()
    포션.use()
    포션.use()
    # official_items = Items
    # equipments = EquipmentItem
    # use_type_items = UseTypeItem

    # official_items('여기에 플레이어 입력', "10")

    # # 장비 효과 [power, magic power]에 영향
    # equipitem_effect = []


if __name__ == '__main__':
    example()
