"""

This is a Python Library that helps you to use telegram APIs.

Author: Eric Damian

"""

import requests
from typing import List, Dict

class TelegramBotApi():
    """ The implementation of the Telegram APIs Bot """
    
    def __init__(self, token: str):
        
        self.token = token # Bot token
        self.lastUpdateId = 0

    def getToken(self) -> str:
        return self.token

    def setToken(self, token: str):
        self.token = token

    def getUpdates(self, offset=0, limit=100, timeout=0, allowed_updates=[]) -> List:
        """   
            Use this method to receive incoming updates using long polling. 
            
            :param offset: Identifier of the first update to be returned.
            :param limit: Limits the number of updates to be retrieved.
            :param timeout: Timeout in seconds for long polling.
            :param allowed_updates: List of the update types you want your bot to receive.

            :type offset: int
            :type limit: int
            :type timeout: int
            :type allowed_updates: List

            :return: An Array of Update objects is returned.
            :rtype: List

            .. note:: For more info -> https://github.com/xSklero/python-telegram-api/wiki/getUpdates 
        """

        token = self.token

        updates = requests.get(f"https://api.telegram.org/bot{token}/getUpdates?offset={offset}&limit={limit}&timeout={timeout}&allowed_updates={allowed_updates}").json()
        
        self.lastUpdateId = updates["result"][-1]["update_id"]

        return updates["result"]

    def getLastUpdateId(self) -> int:
        return self.lastUpdateId

    def setLastUpdateId(self, lastUpdateId: int):
        self.lastUpdateId = lastUpdateId
