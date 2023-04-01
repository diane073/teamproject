import random
import math
import time

# 플레이어 클래스 / 지명


class Character:
    def __init__(self, name, hp, mp, power, mpower, exp, level, skill_name):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.power = power
        self.mpower = mpower
        self.exp = exp  # 김주영수정
        self.max_exp = 100  # 김주영수정
        self.level = level

        self.skill_name = skill_name  # 수정하면 스킬도 획득 등으로 수정가능
        # self.get_skill = ''
        self.power_item = 0
        self.mpower_item = 0
        self.heal_item = 0
        self.mana_item = 0
        self.alive = True

    # 상태확인
    def show_stat(self):
        print(f"직업 : {self.name} \n"
              f"HP : [{min(self.hp + self.heal_item, self.max_hp)}/{self.max_hp}] \n"
              f"MP : [{min(self.mp + self.mana_item, self.max_mp)}/{self.max_mp}]\n"
              f"exp: [{self.exp}/{self.max_exp}]\n"  # 김주영수정
              f"물리공격력 : {self.power+self.power_item}({self.power} + {self.power_item})\n"
              f"마법공격력 : {self.mpower + self.mpower_item}({self.mpower} + {self.mpower_item}) \n"
              f"보유스킬 : {self.skill_name}")
    # 플레이어 생존확인

    def alive_check(self):
        if self.hp <= 0:
            self.alive = False

    # 일반공격

    def attack(self, monster):

        if monster.hp > 0:  # 혹은 monster.alive == True:
            damage = random.randint(self.power - 3, self.power+3)
            monster.hp = max(monster.hp - damage, 0)
            print(f"{self.name}의 일반공격! {monster.name}에게 {damage}의 피해를 입혔습니다.")
            if monster.hp == 0:
                print(f"{monster.name}을 쓰러트렸습니다.")
                # 경험치확인 #김주영 수정
                self.exp += 20
                if self.exp >= 100:
                    self.level_up()  # 100이상일때 levelup메소드 실행

        else:
            print('이미 죽은 몬스터입니다. 다른 몬스터를 공격합니다.')
            # 나중에 while문을 통해 재선택 가능하게

    # 스킬공격
    def special_attack(self, monster):

        if monster.hp > 0:  # 혹은 monster.alive == True:
            mdamage = random.randint(self.mpower - 3, self.mpower+3)
            monster.hp = max(monster.hp - mdamage, 0)
            print(
                f"{self.name}의 {self.skill_name}! {monster.name}에게 {mdamage}의 피해를 입혔습니다.")
            if monster.hp == 0:
                print(f"{monster.name}을 쓰러트렸습니다.")
                # 경험치확인 #김주영 수정
                self.exp += 20
                if self.exp >= 100:
                    self.level_up()  # 100이상일때 levelup메소드 실행

        else:
            print('이미 죽은 몬스터입니다. 다른 몬스터를 공격합니다.')
            # 나중에 while문을 통해 재선택 가능하게

    def get_equipitem(self, new_item):
        """
        아이템을 외부에서 생성,
        Player가 인풋받음

        적용..player.get_equipitem(매개변수)
        """
        print(f"{self.name}이(가) {new_item.name}을(를) 얻었습니다.")
        new_item.item_power(self)

        # 아이템 얻었을 시 // 현재는 random, 추가 후 변경   #이 코드 아이템으로 떼갑니다^.^
        # def a_item(self):
        #     item_num = random.randint(1, 5)
        #     if item_num == 1:
        #         print("검을 얻었다")
        #         self.attack_item = 10
        #     elif item_num == 2:
        #         print("지팡이를 얻었다")
        #         self.magic_item = 10
        #     elif item_num == 3:
        #         print("체력포션")
        #         self.heal_item = 150
        #     else:
        #         print("마나포션")
        #         self.mana_item = 30

        # 이런 식으로 스킬 추가도 가능

        # def add_skill(self, geted_skill):
        #     if self.name == "전사":
        #         self.skill_name = geted_skill  # 기존 스킬을 변경
        #         self.get_skill = geted_skill  # 새로 스킬을 획득
        #         print(f"{geted_skill}을 얻었다")
        ############ 김주영 수정##########

    def level_up(self):
        if self.exp >= 200:
            # 경험치가 200 넘었을경우
            self.level += math.floor(self.exp / self.max_exp)
            self.power += math.floor(self.exp / self.max_exp)*2
            self.hp = self.max_hp
        # exp = int(숫자) print(exp % 100), 끝자리 두개나옴
            self.exp = self.exp % 100

            print(f"{self.name}의 level이: {self.level}로 상승했습니다.")
            print(f"{self.name}의 power가: {self.power}로 상승했습니다.")
        else:
          # 경험치가 200이 안 넘은 경우
            self.level += 1
            self.power += 2
            self.hp = self.max_hp
            self.exp = self.exp-100
            print(f"{self.name}의 level이: {self.level}로 상승했습니다.")
            print(f"{self.name}의 power가: {self.power}로 상승했습니다.")

    def __str__(self):
        return f'{self.name}'

 ##########################################################
# 전사


class Warrior(Character):
    def __init__(self, name, hp, mp, power, mpower, exp, level, skill_name):

        super().__init__(name, hp, mp, power, mpower, exp, level, skill_name)
# 마법사


class Wizard(Character):
    def __init__(self, name, hp, mp, power, mpower, exp, level, skill_name):

        super().__init__(name, hp, mp, power, mpower, exp, level, skill_name)

# 도적


class Thief(Character):
    def __init__(self, name, hp, mp, power, mpower, exp, level, skill_name):
        super().__init__(name, hp, mp, power, mpower, exp, level, skill_name)


# 몬스터 클래스 코드 - 예지


class Monster:
    def __init__(self, name, hp, level, power):
        self.name = name
        self.max_hp = hp
        self.hp = max(hp, 0)
        self.level = level
        self.power = power
        self.alive = True

    def level_up(self):
        self.level += 1
        self.power += 5

    def alive_check(self):
        if self.hp <= 0:
            self.alive = False

    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f"{self.name}의 레벨: level {self.level}")
        print(f"{self.name}의 상태: HP {self.hp}   {self.max_hp}")

# 제일 첫 스테이지에서 나올 만한 몬스터 공격력 약함


class Monster_Base_C(Monster):
    def __init__(self, name, hp, level, power):
        super().__init__(name, hp, level, power)

    def attack(self, player):
        damage = random.randint(self.power - 2, self.power + 2)
        player.hp = max(player.hp - damage, 0)
        print(f"{self.name}의 공격! {player.name}님에게 {damage}의 데미지를 입혔습니다.")
        if player.hp == 0:
            print(f"{player.name}님이 쓰러졌습니다. {player.name}님 패배 😣")  # player


# 마법공격을 쓰는 몬스터 플레이어처럼 마나를 다쓰면 일반공격만 함


class Monster_Magical_C(Monster):
    def __init__(self, name, hp, level, mp, power):
        super().__init__(name, hp, level, power)
        self.mp = mp

    def attack(self, player):
        damage = random.randint(self.power, self.power + 4)
        if self.mp != 0:
            player.hp = max(player.hp - damage, 0)
            self.mp = self.mp - 20
            print(f"{self.name}의 마법 공격! {player.name}님에게 {damage}의 데미지를 입혔습니다.")

        elif self.mp == 0:
            print("마법공격을 사용할 수 없습니다.일반공격으로 전환합니다.")
            time.sleep(2)
            damage = random.randint(self.power - 2, self.power + 2)
            player.hp = max(player.hp - damage, 0)
            print(f"{self.name}님의 공격! {player.name}에게 {damage}의 데미지를 입혔습니다.")

        elif player.hp == 0:
            print(f"{player.name}님이 쓰러졌습니다. {player.name}님 패배 😣")


# 공격력 강한 바람몬스터 아래의 불몬스터와 조합해서 보스몬스터같이 선택해서 해도 좋을것 같습니다.


class Monster_Wind_C(Monster):
    def __init__(self, name, hp, level, power):
        super().__init__(name, hp, level, power)

    def attack(self, player):
        damage = random.randint(self.power + 5, self.power + 10)
        player.hp = max(player.hp - damage, 0)
        print(f"{self.name}의 공격! {player.name}님에게 {damage}의 데미지를 입혔습니다.")
        if player.hp == 0:
            print(f"{player.name}님이 쓰러졌습니다. {player.name}님 패배 😣")


# 공격력 강한 불몬스터


class Monster_Fire_C(Monster):
    def __init__(self, name, hp, level, power):
        super().__init__(name, hp, level, power)

    def attack(self, player):
        damage = random.randint(self.power + 10, self.power + 15)
        player.hp = max(player.hp - damage, 0)
        print(f"{self.name}의 공격! {player.name}님에게 {damage}의 데미지를 입혔습니다.")
        if player.hp == 0:
            print(f"{player.name}님이 쓰러졌습니다. {player.name}님 패배 😣")


class ItemEffect:
    """
    아이템별 효과
    Character.attack_item = 0        
    Character.magic_item = 0
    Character.heal_item = 0
    Character.mana_item = 0

    """

    def __init__(self, name: str, effect_info: str, power_up, magic_power_up):  # 플레이어 객체가 필요함
        self.name = name
        self.effect_info = effect_info
        self.power_up = power_up
        self.magic_power_up = magic_power_up

    def item_power(self, player):
        player.power_item += self.power_up
        player.mpower_item += self.magic_power_up

    def __str__(self):
        return f'ItemEffect({self.name})'
