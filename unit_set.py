import unit
import random


team_dict = {
    1: unit.Monster_Base_C("슬라임", 100, 1, 20),
    2: unit.Monster_Magical_C("오크", 150, 1, 200, 30),
    3: unit.Monster_Wind_C("가고일", 200, 1, 50),
    4: unit.Monster_Fire_C("드래곤", 300, 1, 60)
}


job_dict = {
    1: unit.Warrior("전사", 200, 30, 30, 5, 0, 1, '스매쉬'),
    2: unit.Wizard("마법사", 120, 80, 10, 30, 0, 1, '화염구'),
    3: unit.Thief("도적", 150, 40, 30, 20, 0, 1, '급습')
}


class Job:
    def show_job_list(self):

        key_list = job_dict.keys()  # key 리스트가 됐어(iterate)
        for i in key_list:
            print(f'{i}. {job_dict[i]}')

    def select_job(self):
        idx = input(f'원하는 직업을 선택해주세요.\n1 부터 {len(job_dict)}을 입력하세요: ')
        if idx.isdigit():
            idx = int(idx)
            if idx in range(1, len(job_dict) + 1):
                job_seleted = job_dict[idx]
                print(f'{job_seleted.name}를 선택했습니다.\n')
                return job_seleted
            else:
                print(f"1에서 {len(job_dict)}사이를 입력해주세요")
                return self.select_job()
        else:
            print("숫자만 입력해주세요")
            return self.select_job()


equipitem_list = [
    unit.ItemEffect("강철 검", "물리공격력이 10 증가", 10, 0),
    unit.ItemEffect("날카로운 창", "물리공격력이 15 증가", 8, 0),
    unit.ItemEffect("끝판왕 활", "물리공격력이 30 증가", 30, 0),
    unit.ItemEffect("겉이 화려한 지팡이", "마법공격력이 2 증가", 0, 2),
    unit.ItemEffect("투박한 스태프", "마법공격력이 12 증가", 0, 12),
    unit.ItemEffect("메이스", "마법공격력이 8 증가", 0, 8),
]


class EquipItem:

    def show_equipitem_list(self):
        for i in range(len(equipitem_list)):
            print(f'{i+1}. {equipitem_list[i]}')

    def select_equipitem(self):
        idx = int(input(f'1 부터 {len(equipitem_list)}을 입력하세요: '))
        item = equipitem_list[idx-1]
        print(f'{item}를 선택했습니다.')
        return item

    def get_random_equipitem(self):
        idx = random.randint(0, len(equipitem_list) - 1)
        return equipitem_list[idx]


equipitem = EquipItem()
job = Job()


def test_job():
    job.show_job_list()
    job.select_job()


def test_equipment():
    equipitem.show_equipitem_list()
    item = equipitem.select_equipitem()
    print(f'{item}을 얻었다!')
    # print(f'{equipitem.get_random_equipitem()}를 랜덤하게 얻었습니다.')


if __name__ == "__main__":
    test_job()
