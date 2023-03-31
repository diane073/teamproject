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



