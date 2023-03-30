import random

class Character_S :
    def __init__(self, name, hp, mp, power, mpower, skill_name):
        self.name = name
        self.max_hp =hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.power = power
        self.mpower = mpower
        self.alive = True
        self.skill_name = skill_name        #수정하면 스킬도 획득 등으로 수정가능
        self.get_skill = ''
        self.attack_item = 0        #
        self.magic_item = 0
        self.heal_item = 0
        self.mana_item = 0
      
    #상태확인    
    def show_stat_S(self):
        print(f"직업 : {self.name} \n"
              f"HP : [{min(self.hp + self.heal_item, self.max_hp)}/{self.max_hp}] \n"
              f"MP : [{min(self.mp+self.mana_item,self.max_mp)}/{self.max_mp}]\n"
              f"물리공격력 : {self.power + self.attack_item}\n"
              f"마법공격력 : {self.mpower + self.magic_item} \n"
              f"획득스킬 : {self.skill_name} {self.get_skill}")
    #플레이어 생존확인    
    def alive_check_S(self):
        if self.hp <= 0:
            self.alive = False
    #일반공격    
    def attack_S(self, monster):
          
            if monster.hp > 0: #혹은 monster.alive == True:
                damage = random.randint(self.power -3, self.power+3)
                monster.hp = max(monster.hp - damage, 0)
                print(f"{self.name}의 일반공격! {monster.name}에게 {damage}의 피해를 입혔습니다.")
                if monster.hp == 0:
                    print(f"{monster.name}을 쓰러트렸습니다.")
                
                                         
            else :
                print('이미 죽은 몬스터입니다. 다른 몬스터를 공격합니다.')
                #나중에 while문을 통해 재선택 가능하게
                
    #스킬공격
    def special_attack_S(self, monster):
           
            if monster.hp > 0: #혹은 monster.alive == True:
                mdamage = random.randint(self.mpower -3, self.mpower+3)
                monster.hp = max(monster.hp - mdamage, 0)
                print(f"{self.name}의 {self.skill_name}! {monster.name}에게 {mdamage}의 피해를 입혔습니다.")
                if monster.hp == 0:
                    print(f"{monster.name}을 쓰러트렸습니다.")
                
            else :
                print('이미 죽은 몬스터입니다. 다른 몬스터를 공격합니다.')
                #나중에 while문을 통해 재선택 가능하게
                
    #아이템 얻었을 시 // 현재는 random, 추가 후 변경
    def a_item_S(self):
        item_num = random.randint(1,5)
        if item_num == 1:
            print("검을 얻었다")
            self.attack_item = 10
        elif item_num == 2:
            print("지팡이를 얻었다")
            self.magic_item = 10
        elif item_num == 3:
            print("체력포션")
            self.heal_item = 150
        else :
            print("마나포션")
            self.mana_item = 30
    #이런 식으로 스킬 추가도 가능        
    def add_skill(self, geted_skill):
         if self.name == "전사":
            self.skill_name = geted_skill   #기존 스킬을 변경
            self.get_skill = geted_skill    #새로 스킬을 획득
            print(f"{geted_skill}을 얻었다")
             
#전사
class Warrior_S(Character_S):
    def __init__(self, name, hp, mp, power, mpower, skill_name):
        
        super().__init__(name,hp,mp,power,mpower, skill_name)
#마법사         
class Wizard_S(Character_S):
    def __init__(self, name, hp, mp, power, mpower, skill_name):
        
        super().__init__(name,hp,mp,power,mpower, skill_name)

#힐러
class Priest_S(Character_S):
    def __init__(self, name, hp, mp, power, mpower, skill_name):
        super().__init__(name,hp,mp,power,mpower, skill_name)
    #특수스킬 오버라이딩
    def special_attack_S(self, team):
        
            if team.hp >0 and team.hp < team.max_hp:
                mdamage = random.randint(self.mpower -5, self.mpower+5)
                team.hp = min(team.hp + mdamage, team.max_hp)
                print(f"{self.name}의 {self.skill_name}! {team.name}에게 {mdamage}의 체력을 회복시켰습니다.")
                
            elif team.hp == team.max_hp:
                print(f"{team.name}은 최대체력입니다")
                
            else :
                print('이미 죽은 팀원입니다. 다른 팀원을 회복시킵니다.')
                #나중에 while문을 통해 재선택 가능하게
                
                
                
            
#플레이어수 유효성검사
def check_player_S():
    while True :
        check = input("원하는 플레이어 수를 선택해주세요")
        if check == '':
            print("정확한 값을 입력해주세요.")
        elif not check.isdigit():
            print("숫자만 입력해주세요")
        elif int(check) < 1 or int(check) > 3:
            print("1에서 3사이를 입력해 주세요")
        else : 
            return int(check)
#직업선택 유효성검사        
def check_job_S():
    while True :
        check = input("원하는 직업을 선택해주세요\n"
                            "1.전사\n"
                            "2.마법사\n"
                            "3.힐러\n")
        if check == '':
            print("정확한 값을 입력해주세요.")
        elif not check.isdigit():
            print("숫자만 입력해주세요")
        elif int(check) < 1 or int(check) > 3:
            print("1에서 3사이를 입력해 주세요")
        else : 
            return int(check)        




#딕셔너리를 활용한 직업 선택    
job_dict_S = {
    1:  Warrior_S("전사",200,30,30,5,'스매쉬'),
    2:  Wizard_S("마법사",120,80,10,30,'화염구'),
    3: Priest_S("힐러",150,100,5,20,'회복')
}


player_list_S = []

for i_S in range(check_player_S()):
    player_select = check_job_S()
    character_class = int(player_select)
    player_list_S.append(job_dict_S[character_class])


        
    
#잘 작동하는 지 확인
for player_S in player_list_S:
    print(player_S.name)
    player_S.show_stat_S()
    player_S.a_item_S()
    player_S.show_stat_S()
    player_S.add_skill("방패공격")
    player_S.show_stat_S()
    