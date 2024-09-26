import os
import json
import requests

from typing import List, Optional
from business_object.attack.attack_factory import AttackFactory
from business_object.attack.abstract_attack import AbstractAttack
from utils.singleton import Singleton

END_POINT = "/attack"


class AttackClient(metaclass=Singleton):
    def __init__(self) -> None:
        # Using an environment variable defined in the .env file
        self.__HOST = os.environ["HOST_WEBSERVICE"]

    def get_attack(self, id: int) -> Optional[AbstractAttack]:
        """
        Get a specific attack from the webservice by calling the GET endpoint
        with a specific resource identifier.Do not raise any
        exception if any attack is found, just return None.

        :param id: attack id wanted
        :type id: int
        :return: The attack object with all value if the attack is found.
                 else None
        :rtype: AbstractAttack
        """
        url = f"{self.__HOST}{END_POINT}/{id}"
        print("GET  " + url + "\n")
        req = requests.get(url)

        attack = None

        # Check if the request is ok
        if req.status_code == 200:
            raw_attack = req.json()

            print("Réponse JSON obtenue :\n" + json.dumps(raw_attack, indent=2) + "\n")

            # TODO
            attack=AttackFactory().instantiate_attack(**raw_attack)
            #   create an attack using the data contained in the json
            #   see class AttackFactory to do this

        return attack
    
    def get_all_attacks(self):

        url = f"{self.__HOST}{END_POINT}"
        print("GET  " + url + "\n")
        req = requests.get(url)
        attack_list=[]
        if req.status_code == 200:
            raw_attack = req.json()
            att1=raw_attack["results"]
            for val in att1:
                print(val)
                attack=AttackFactory().instantiate_attack(**val)
                attack_list.append(attack)
        return attack_list

    def create_attack(self,AbstractAttack):
        



        





# Execute Code When the File Runs as a Script
if __name__ == "__main__":
    # To load environment variables contained in the .env file
    import dotenv

    dotenv.load_dotenv(override=True)

    attack_client = AttackClient()

    attack_id = 1
    attack_client.get_attack(attack_id)
    attack_client.get_all_attacks()
