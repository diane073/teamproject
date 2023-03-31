
class ItemEffect:
    """
    아이템별 효과 적용
    self.attack_item = 0  
    self.magic_item = 0
    self.heal_item = 0
    self.mana_item = 0
    """

    def __init__(self, effect, player):  # 플레이어 객체가 필요함
        self.effect = effect

    def power_up(self, power: int):
        self.effect = player.power + power

    def magicpower_up(self, magic_power: int):
        self.effect = player.magic_power + magic_power

    def hp_up(self, hp: int):
        self.effect = player.hp + hp

    def mp_up(self, effect, mp: int):
        self.effect = player.mp + mp

    def resurrection(self, player):
        if player.alive == False:
            self.effect = player.hp + player.max_hp
            self.effect = player.mp + player.mp(max_mp/2)
            return player.alive == True


class Items:
    def __init__(self, name, can_use, dropable: bool, attribute='아이템'):
        self.name = name
        self.can_use = can_use
        self.dropable = dropable
        self.attribute = attribute

    def throw_away(self):
        """버리는 기능"""
        if self.dropable == True:
            print(f'{self.name}을 버렸습니다.')
        else:
            print(f'{self.name}을 버릴 수 없습니다.')

    inventory = []  # 빈 인벤토리에 dict형태로 아이템 저장

    def get_item(self):
        if item.name not in self.inventory:
            self.inventory[item.name] = 0
        self.inventory[item.name] += 1

    def using(self, num):  #
        i = input(f"{self.name}을 얻었다. 사용할까?")
        if int(i) == inventory.keys():
            player_S.a_item_S(1)


class EquipmentItem(Items):
    """
    장착 / 해제형 아이템
    검 스태프 활 등등
    """

    def __init__(self, name, effect: ItemEffect):
        super().__init__(name, can_use=True, dropable=False, attribute='장비아이템')
        self.effect = effect

    def wear(self):
        if self.can_use:
            print(f'{self.name}을 착용했다!')
            print(f'{self.effect}의 효과를 받았다.')


class UseTypeItem(Items):
    """
    사용형 아이템
    1회만 사용할 수 있음
    """

    def __init__(self, name, effect: ItemEffect):
        super().__init__(name, can_use=True, dropable=True, attribute='소비아이템')
        self.effect = effect

    def use_once(self, player):
        # 한 번 사용하면 사용할 수 없음 >> 조건을 0개가 되면 사용 못하는 것으로 수정함
        if self.can_use:
            print(f'{self.name}을 사용했다!')
            print(f'{self.effect}')
            if player.heal_item == 0:
                return self.can_use == False

            elif player.mana_item == 0:
                return self.can_use == False


"""---------------이 아래에 선언-----------------"""


class Player:
    """코드 구동용"""
    name = "test"
    max_hp: int = 1
    max_mp: int = 1
    hp: int = 1
    mp: int = 1
    power: int = 1
    magic_power: int = 1


player = Player


item = Items


def example():
    """
    내가 만든 코드 돌려보기/테스트하기
    1. 여기다가 사용 예제 적는거
    2. test 코드 만드는거
    """
    sword = EquipmentItem(
        '강철 검', '힘이 10', ItemEffect.power_up(player.name, 10))
    staff = EquipmentItem('겉만 화려한 스태프', '지식이 1', ItemEffect.magicpower_up(1))

    hp_potion = UseTypeItem('빨간포션', 'hp가 10', ItemEffect.hp_up(10)).use_once()
    mp_potion = UseTypeItem('파란포션', 'mp가 10', ItemEffect.mp_up(10)).use_once()
    resurrect_potion = UseTypeItem(
        '부활포션', '부활', ItemEffect.resurrection()).use_once()

    sword.using()
    staff.using()

    hp_potion.using()
    mp_potion.using()
    resurrect_potion.using()


if __name__ == '__main__':
    example()
