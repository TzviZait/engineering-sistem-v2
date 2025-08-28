from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent  # מצביע על Enricher







class Weapons_detecter:


    @staticmethod
    def get_weapons_from_file()->list:
        file_path = Path(__file__).resolve().parent / 'weapon_list.txt'
        print(file_path)
        with open(file_path ,'r',encoding='utf-8') as f:
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
