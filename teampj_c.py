import random
import time

# 아래의 몬스터들은 조합과 hp,파워를 강하게 설정하는 등의 방법으로 강약 조절하면 좋을것 같습니다.
# 예시
# stage5_monster_dict = {
#     week_monster : Monster_Base_C("슬라임", 100, 20)
#     middle_monster : Monster_Magical_C("오크", 150, 200, 30)
#     strong_monster : Monster_Wind_C("가고일", 200, 50)
#     boss_monster : Monster_Fire_C("드래곤", 300, 60)
# }


# 몬스터의 기본이 되는 클래스
class Monster:
    def __init__(self, name, hp, power):
        self.name = name
        self.max_hp = hp
        self.hp = max(hp, 0)
        self.power = power

    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}   {self.max_hp}")

# 제일 첫 스테이지에서 나올 만한 몬스터 공격력 약함
class Monster_Base_C(Monster):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)

    def attack(self):
        damage = random.randint(self.power - 2, self.power + 2)
        player.hp = max(player.hp - damage, 0)
        print(f"{self.name}의 공격! {player.name}님에게 {damage}의 데미지를 입혔습니다.")
        if player.hp == 0:
           print(f"{player.name}님이 쓰러졌습니다. {player.name}님 패배 😣")


    def show_status(self):
        print(f"{self.name}의 상태 :{self.hp}/{self.max_hp}")

# 마법공격을 쓰는 몬스터 플레이어처럼 마나를 다쓰면 일반공격만 함
class Monster_Magical_C(Monster):
    def __init__(self, name, hp, mp, power):
        super().__init__(name, hp, power)
        self.mp = mp

    def magic_attack(self):
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
            print(f"{self.name}님의 공격! {player.name}에게 {damage}의 데미지를 입혔습니다.ㄴ

        elif player.hp == 0:
           print(f"{player.name}님이 쓰러졌습니다. {player.name}님 패배 😣")


    def show_status(self):
        print(f"{self.name}의 상태 :{self.hp}/{self.max_hp}")

# 공격력 강한 바람몬스터 아래의 불몬스터와 조합해서 보스몬스터같이 선택해서 해도 좋을것 같습니다.
class Monster_Wind_C(Monster):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)

    def wind_attack(self):
        damage = random.randint(self.power + 5, self.power + 10)
        player.hp = max(player.hp - damage, 0)
        print(f"{self.name}의 공격! {player.name}님에게 {damage}의 데미지를 입혔습니다.")
        if player.hp == 0:
           print(f"{player.name}님이 쓰러졌습니다. {player.name}님 패배 😣")


    def show_status(self):
        print(f"{self.name}의 상태 :{self.hp}/{self.max_hp}")

# 공격력 강한 불몬스터 
class Monster_Fire_C(Monster):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)

    def fire_attack(self):
        damage = random.randint(self.power + 10, self.power + 15)
        player.hp = max(player.hp - damage, 0)
        print(f"{self.name}의 공격! {player.name}님에게 {damage}의 데미지를 입혔습니다.")
        if player.hp == 0:
           print(f"{player.name}님이 쓰러졌습니다. {player.name}님 패배 😣")


    def show_status(self):
        print(f"{self.name}의 상태 :{self.hp}/{self.max_hp}")

