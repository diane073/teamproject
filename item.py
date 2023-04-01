from unit_set import equipitem
from unit import ItemEffect
"""여기부터 아이템 코드 추가"""


class ItemTools:
    def __init__(self, name, attribute='아이템'):
        self.name = name
        self.attribute = attribute

    def wear(self):
        print(f'{item.name}을 착용했다!')
        print(f'{item.effect_info}의 효과를 받았다.')

    def yes_or_no(question):  # 사용여부에 대한 질문 및 답변 반환 yes or no
        while "":
            reply = str(
                input(f'{question} (y/n): ')).lower().strip()
            if reply[0] == 'y':
                return True
            if reply[0] == 'n':
                return False
            elif reply[0] != 'y' or 'n':
                print("y나 n을 입력해주세요.")
                continue


item = ItemEffect()
item_tools = ItemTools

inventory = []
