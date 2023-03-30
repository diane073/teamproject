import random
import time
import math


class Character:
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


class Monster(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)

    def attack(self):
        damage = random.randint(self.power - 2, self.power + 2)
        player.hp = max(player.hp - damage, 0)
        print(f"{monster.name}의 공격! {player.name}님에게 {damage}의 데미지를 입혔습니다.")
        if player.hp == 0:
            print(f"{player.name}님이 쓰러졌습니다. {player.name}님 패배 😣")

    def show_status(self):
        print(f"{monster.name}의 상태 :{self.hp}/{self.max_hp}")


class Player(Character):
    def __init__(self, name, hp, mp, power, exp, level):
        super().__init__(name, hp, power)
        self.mp = mp
        self.max_mp = mp
        name = p_name
        self.exp = exp
        self.max_exp = 100
        self.level = level

    def attack(self):
        damage = random.randint(self.power - 2, self.power + 2)

        monster.hp = max(monster.hp - damage, 0)
        print(f"{self.name}님의 공격! {monster.name}에게 {damage}의 데미지를 입혔습니다.")

        if monster.hp == 0:
            print(f"{monster.name}가 쓰러졌습니다.{player.name}님의 승리! 🤩")

    def magic_attack(self):
        damage = random.randint(self.power + 4, self.power + 10)
        if player.mp != 0:
            monster.hp = max(monster.hp - damage, 0)
            self.mp = self.mp - 20
            print(f"{self.name}님의 마법공격! {monster.name}에게 {damage}의 데미지를 입혔습니다.")

        elif player.mp == 0:
            print("마법공격을 사용할 수 없습니다.일반공격으로 전환합니다.")
            time.sleep(2)
            damage = random.randint(self.power - 2, self.power + 2)
            monster.hp = max(monster.hp - damage, 0)
            print(f"{self.name}님의 공격! {monster.name}에게 {damage}의 데미지를 입혔습니다.")

        elif monster.hp == 0:
            print(f"{monster.name}가 쓰러졌습니다 {player.name}님의 승리! 🤩.")

    def show_status(self):
        print(
            f"{self.name}의 상태 : \n hp :{self.hp}/{self.max_hp} \n mp :{self.mp}/{self.max_mp}")
        print(f"{self.name}의 상태 :\n exp :{self.exp}/{self.max_exp}")


def level_up(self):
    if player.exp >= 200:
        # 경험치가 200 넘었을경우
        player.level += math.floor(player.exp / player.max_exp)
        player.power += math.floor(player.exp / player.max_exp)*2
        player.hp = player.max_hp
        # exp = int(숫자) print(exp % 100), 끝자리 두개나옴
        player.exp = player.exp % 100

        print(f"{self.name}의 level이: {player.level}로 상승했습니다.")
        print(f"{self.name}의 power가: {player.power}로 상승했습니다.")
    else:
        # 경험치가 200이 안 넘은 경우
        player.level += 1
        player.power += 2
        player.hp = player.max_hp
        player.exp = player.exp-100
        print(f"{self.name}의 level이: {player.level}로 상승했습니다.")
        print(f"{self.name}의 power가: {player.power}로 상승했습니다.")


def check_answer():
    while True:
        check = input("선택 : \n")
        if check == '':
            print("입력된 값이 없습니다. 다시 입력해주세요. \n")
        elif not check.isdigit():
            print('숫자로만 입력해주세요.')
        elif int(check) < 1 or int(check) > 2:
            print("1 또는 2 중에서 선택해주세요.\n")
        else:
            return int(check)


print("이름을 입력해주세요.")
p_name = input("이름:")
player = Player(p_name, hp=100, mp=100, power=10, exp=0, level=1)
monster = Monster("오크", hp=100, power=8)
turn = 1

while player.hp != 0 and monster.hp != 0:
    if player.hp == 0 or monster.hp == 0:
        break
    else:
        print(f"{turn}번째 게임을 시작합니다.")
        print(f"{player.name}님 공격 턴!")
        print("------------------------------")
        player.show_status()
        print("------------------------------")
        monster.show_status()
        print("------------------------------")
        print("공격 타입을 선택해주세요. 1.일반공격 2.마법공격")
        choice = check_answer()
        if choice == 1:
            player.attack()
            print("------------------------------")

            if monster.hp == 0 or player.hp == 0:
                break
            else:
                player.show_status()
                print("------------------------------")
                monster.show_status()
                print("------------------------------")
                print(f"{monster.name} 공격 턴!")
                time.sleep(2)

                monster.attack()
                print("------------------------------")
                print(f"{player.name}님의 남은 hp는 {player.hp}")
                print("------------------------------")
                print(f"{monster.name}의 남은 hp는 {monster.hp}")
                print("------------------------------")
                time.sleep(2)

        else:
            player.magic_attack()
            print("------------------------------")
            player.show_status()
            print("------------------------------")
            monster.show_status()
            print("------------------------------")
            time.sleep(2)

            if player.hp == 0:
                print(f"{monster.name} 승리 ,{player.name}님 패배 😣")
            elif monster.hp == 0:
                print(f"{player.name}님의 승리!🤩")
                # 경험치확인
                player.exp += 20
                if player.exp >= 100:
                    player.level_up()  # 100이상일때 levelup메소드 실행
            else:
                print(f"{monster.name} 공격 턴!")
                time.sleep(2)
                monster.attack()
                print("------------------------------")
                player.show_status()
                print("------------------------------")
                monster.show_status()
                print("------------------------------")
                time.sleep(2)

    turn += 1

