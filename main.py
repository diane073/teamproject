<<<<<<< HEAD
import sys
import time
import play

"""Ctrl + Z 금지!!!!!!!!!!!!"""


""" 사전준비를 하고있었습니당
스토리 시작부분

캐릭터 선택
+아이템 지급?

몬스터 만나고 전투 진행

전투 마무리 후 경험치, 보상, 아이템 지급

전투를 몇 번까지 진행할지,

그외 회복수단
 ex. 마을에서 쉬고오면 충전된다거나(보상과 연계할 수 있을 듯)


게임 종료 
 ending : 승리 패배
"""



"""============게임 실행 코드============"""


play.game()




# 전투 턴 진행

def reward():
    if player.mp < player.hp:                     # 마나와 체력을 비교하여 마나가 더 작으면 마나 회복, 체력이  더 작으면 체력 회복
        if player.mp + 30 < player.max_mp:
            player.mp += 30
            print(
                f"{player.name}님의 마나가 30 회복하였습니다. ({player.mp}/{player.max_mp})")
        else:
            player.mp = player.max_mp
            print(
                f"{player.name}님의 마나가 완전히 회복되었습니다. ({player.mp}/{player.max_mp})")
    elif player.mp >= player.hp:
        if player.hp + 30 < player.max_hp:
            player.hp += 30
            print(
                f"{player.name}님의 체력이 30 회복하였습니다. ({player.hp}/{player.max_hp})")
        else:
            player.hp = player.max_hp
            print(
                f"{player.name}님의 체력이 완전히 회복되었습니다! ({player.hp}/{player.max_hp})")






# 엔딩

print("\n\n용사(와 그 동료들이)여! 10층에 도달해 보스를 처리했군!\n")
time.sleep(1)
print("11층에 와본 소감은 어떤가? 별이 참 예쁘지 않은가?\n")
time.sleep(1)
print("*  *   *           *  *       *  *      *  \n")
time.sleep(0.2)
print(" *  *       * * *    * * *         *  *    \n")
time.sleep(0.2)
print("          *        *       *     *       * \n")
time.sleep(0.2)
print("      *   *                *      *        \n")
time.sleep(0.2)
print("  *         *             *          *     \n")
time.sleep(0.2)
print("         *    *        *   *  *          * \n")
time.sleep(0.2)
print("                 *   *              *      \n")
time.sleep(0.2)
print("   *   *      *    *          *         *  \n")
time.sleep(0.2)
print("여기 11층에서만 볼 수 있는 장관이지...")
print("이 별들은 애스터리스크 자리라고 한다네^^.\n")
time.sleep(1)
print("아, 11층은 됐고 보상을 달라고?\n")
time.sleep(1.3)
print("..보상은 자네들이 함께한 여정이라네\n\n")
time.sleep(0.5)
print("그대들이 함께 울고 웃었던 시간들을 소중히 여기며..\n")
time.sleep(0.5)
print("이젠 현생을 살아가시게! 그럼 이만...\n\n")
time.sleep(1.5)
print("용사(와 동료)는 즐거운 추억을 가지고 현생으로 돌아갔다.\n")
print("               ~fin~                 ") 



=======
import random
import time


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
    def __init__(self, name, hp, mp, power):
        super().__init__(name, hp, power)
        self.mp = mp
        self.max_mp = mp
        name = p_name

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
player = Player(p_name, hp=100, mp=100, power=10)
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
>>>>>>> dfdb39cdaa3deede077ccfb3a7450f5ef7d4a53c
