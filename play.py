import unit_set
import random
import time

# monsters를 인자로 받는 몬스터 생성함수


def team_select(monsters):
    for i in range(2):
        monster_random = random.randint(1, 4)
        monsters.append(unit_set.team_dict[monster_random])


# 전체적인 게임 플레이 코드 / 지명

# 플레이어수 유효성검사
def check_player():
    while True:
        check = input("원하는 플레이어 수를 선택해주세요")
        if check == '':
            print("정확한 값을 입력해주세요.")
        elif not check.isdigit():
            print("숫자만 입력해주세요")
        elif int(check) < 1 or int(check) > 3:
            print("1에서 3사이를 입력해 주세요")
        else:
            return int(check)

# 직업선택 유효성검사


def player_select(players):
    for i in range(check_player()):  # 인자 i라고 되어있는데 확인필요
        unit_set.job.show_job_list()
        players.append(unit_set.job.select_job())

# players와 monsters를 인자로 받는 battle 함수


def battle(players, monsters):

    print("전투를 시작합니다.")
    while (True):
        now_stat(players, monsters)
        if defeat(players):
            print('패배하였습니다.')

            return False
        elif defeat(monsters):
            print('승리하였습니다.')

            return True
        else:
            menu = select_menu()

        if menu == 1:
            for player in players:
                if live(player):
                    player_attack(player, monsters)

            if defeat(monsters):
                print('승리하였습니다.')
                return True

            for monster in monsters:
                print(monster.hp)
                monster_attack(players, monster)

            if defeat(players):
                print('패배하였습니다.')
                return False

        elif menu == 2:
            now_stat(players, monsters)

# 플레이어, 몬스터 전체 생존 확인 life 인자 = players, monsters를 받음 // 전부 죽었을 경우 True 반환을 통해 다음으로 넘어감


def defeat(life):
    for i in life:
        i.alive_check()
        if i.alive == True:
            return False
    else:
        return True

# 단일 개체가 살아 있는지 확인 죽으면 False를 반환


def live(uni):
    if uni.hp > 0:
        return True
    else:
        return False
# 메뉴 선택


def select_menu():
    while True:
        check = input("1. 공격하기\n"
                      "2. 현재 상황 보기")
        if check == '':
            print("입력된 값이 없습니다. 다시 입력해주세요. \n")
        elif not check.isdigit():
            print('숫자로만 입력해주세요.')
        elif int(check) < 1 or int(check) > 2:
            print("1 또는 2 중에서 선택해주세요.\n")
        else:
            return int(check)
 # 몬스터와 플레이어 스탯 현상황


def now_stat(players, monsters):
    for player in players:
        player.show_stat()
    for monster in monsters:
        monster.show_status()
# 플레이어 공격 종류 선택


def player_attack(player, monsters):
    if defeat(monsters):
        return

    attack = input("1. 일반공격\n"
                   "2. 스킬공격")
    if attack == '1':
        monster_num = select_monster(monsters)
        player.attack(monsters[monster_num])

    elif attack == '2':
        monster_num = select_monster(monsters)
        player.special_attack(monsters[monster_num])

    else:
        print("1 또는 2중에서 선택해주세요.")
        return player_attack(player, monsters)

# 플레이어가 공격시 어떤 몬스터 공격할 것인지 선택. enumerate로 인덱스 값을 주어 몬스터 네임과 번호 출력.
# 값이 유효하지 않으면 재출력


def select_monster(monsters):
    print("어떤 몬스터를 공격하시겠습니까? ")
    for i, mon in enumerate(monsters):
        print(f"{i}. 이름 : {mon.name} HP : {mon.hp}")
    index = input(f"[ 0 ~ {len(monsters)-1}]")
    if index.isnumeric():
        index = int(index)
    else:
        return select_monster(monsters)
    for i, mon in enumerate(monsters):
        if i == index and live(mon):
            return index
    print("잘못된 선택입니다. 다시 선택해주세요")
    return select_monster(monsters)
# 몬스터가 플레이어 공격할 시
# 플레이어 리스트에서 랜덤으로 공격


def monster_attack(players, monster):
    if defeat(players):
        return
    if not live(monster):
        return
    if len(players) != 1:
        random_player = random.randint(0, len(players)-1)
    else:
        random_player = 0

    if live(players[random_player]):
        monster.attack(players[random_player])

    else:
        return monster_attack(players, monster)


def player_get_item(players):
    for player in players:
        new_item = unit_set.equipitem.get_random_equipitem()
        player.get_equipitem(new_item)
    time.sleep(3)


# 게임 실행 함수
# 플레이어 선택 후 while문 안에서 몬스터 생성 //// 해결 못한점 : 몬스터가 한마리 죽었을 때 바로 재생성//
# 턴 = 층수 / 10층까지 진행 한 후 break


def game():
    players = []
    monsters = []
    # 시작 부분 만들기
    print("탑에 찾아온 것을 환영하네 용사여\n")

    print("몇 명과 함께 도전할텐가?\n")
    player_select(players)

    print("좋아! 그럼 행운을 빌며 선물을 주도록 하지!\n")
    # 시작 시 장비 아이템 1개 랜덤 지급
    # unit.GiveItem()
    player_get_item(players)

    max_turn = 2
    print(f"탑은 {max_turn}층까지 올라야 끝난다네, 행운을 비네!\n")

    for turn in range(1, max_turn+1):
        print(f"지금 {turn}층인 것 같다.")
        monsters.clear()
        team_select(monsters)
        result = battle(players, monsters)
        if not result:
            print('패배')
            break
