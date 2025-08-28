from Enricher.classification import Classification
from Enricher.weapons_detector import Weapons_detecter
from Enricher.relevant_timestamp import Relevant_timestamp



class ProcesseData:
    
    @staticmethod
    def processing(data:str)->dict:
        new_filds = {}
        new_filds['sentiment'] = Classification.get_compound(data)
        new_filds['weapons_detected'] = Weapons_detecter.get_weapon_from_tweet(data)
        new_filds['relevant_timestamp'] = Relevant_timestamp.get_relevant_timestamp(data)
        return new_filds
    
print(ProcesseData.processing('sdsanddunes arms barbarian kkk nazi isi wirathu jvp zionazis hadhave constituent open closeted'))