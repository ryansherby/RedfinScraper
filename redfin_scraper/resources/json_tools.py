import json

import redfin_scraper.config as rsc

    
config=rsc.CONFIG


def _convert(json_file): #Internal only                                                           
    """                                                                            
    Attempt to convert JSON to dict.

    AKA don't pass garbage to the config.                                                        
    """                                                                            
    try:                                                                           
        with open(json_file) as test:
            json.load(test)                                                 
        return True                                                            
    except:                                                                                    
        return False

def get_config_value(key):
    try:
        value =json_file.get(key)
        return value
    except:
        return None

if _convert(config):
        with open(config) as f:
            json_file=json.load(f)