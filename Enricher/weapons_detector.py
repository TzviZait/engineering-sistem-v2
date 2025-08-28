from pathlib import Path
BASE_DIR = Path(__file__).resolve().parents[1]







class Weapons_detecter:


    @staticmethod
    def get_weapons_from_file()->list:
        with open('.\Enricher\weapon_list .txt' ,'r') as f:
            tlist =(f.read().split('\n'))
        return tlist
    

    @staticmethod
    def get_weapon_from_tweet(tweet:str)->list:
        weapons = Weapons_detecter.get_weapons_from_file()
        my_weapons = []
        for word in tweet.split(' '):
            if word in weapons:
                my_weapons.append(word)
        return my_weapons
    
# print(Weapons_detecter.get_weapons_from_file())