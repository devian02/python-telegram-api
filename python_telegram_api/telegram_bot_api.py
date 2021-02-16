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
        self.last_update_id = 0

    def _getToken(self) -> str:
        return self.token

    def _setToken(self, token: str):
        self.token = token

    def _getUpdates(self, offset=0, limit=100, timeout=0) -> Dict:
        """   
            Use this method to receive incoming updates using long polling. 
            
            :param offset: Identifier of the first update to be returned.
            :param limit: Limits the number of updates to be retrieved.
            :param timeout: Timeout in seconds for long polling.

            :type offset: int
            :type limit: int
            :type timeout: int

            :return: An Array of Update objects is returned.
            :rtype: list

            .. note:: For more info -> https://github.com/xSklero/python-telegram-api/wiki/getUpdates 
        """

        token = self.token

        updates = requests.get(f"https://api.telegram.org/bot{token}/getUpdates?offset={offset}&limit={limit}&timeout={timeout}")
        
        self.last_update_id = updates["result"][-1]["update_id"]

        return updates["result"]
