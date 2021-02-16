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

        self.debug = False # Use this variable to enable or disable debugging mode

    def getDebugMode(self) -> bool:
        """   
            Use this method to get your actual debug mode. 

            :return: Actual debug mode.
            :rtype: Boolean

            .. note:: For more info -> https://github.com/xSklero/python-telegram-api/wiki/getDebugMode
        """

        return self.debug

    def setDebugMode(self, mode: bool) -> bool:
        """   
            Use this method to set debug mode. 
            
            :param mode: When True all responses from Telegram APIs are printed to console.

            :type mode: Boolean

            :return: True if mode has been set correctly.
            :rtype: Boolean

            .. note:: For more info -> https://github.com/xSklero/python-telegram-api/wiki/setDebugMode 
        """

        try:
            self.debug = mode
            return True
        except:
            return False

    def getToken(self) -> str:
        """   
            Use this method to get your actual bot token. 

            :return: Bot token.
            :rtype: String

            .. note:: For more info -> https://github.com/xSklero/python-telegram-api/wiki/getToken 
        """

        return self.token

    def setToken(self, token: str) -> bool:
        """   
            Use this method to set your actual bot token. 
            
            :param token: New bot token.

            :type token: String

            :return: True if token has been set correctly.
            :rtype: Boolean

            .. note:: For more info -> https://github.com/xSklero/python-telegram-api/wiki/setToken 
        """

        try:
            self.token = token
            return True
        except:
            return False

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

        response = requests.get(f"https://api.telegram.org/bot{token}/getUpdates?offset={offset}&limit={limit}&timeout={timeout}&allowed_updates={allowed_updates}").json()
        
        if self.debug:
            print(response)

        if len(response["result"]) >= 1:
            # If there are updates available

            self.setLastUpdateId(response["result"][-1]["update_id"]) # Set lastUpdateId

        return response["result"]

    def getLastUpdateId(self) -> int:
        """   
            Use this method to get lastUpdateId attribute. 

            :return: lastUpdateId attribute.
            :rtype: int

            .. note:: For more info -> https://github.com/xSklero/python-telegram-api/wiki/getLastUpdateId 
        """

        return self.lastUpdateId

    def setLastUpdateId(self, lastUpdateId: int):
        """   
            Use this method to set lastUpdateId attribute. 
            
            :param lastUpdateId: New lastUpdateId.

            :type lastUpdateId: int

            :return: True if lastUpdateId has been set correctly.
            :rtype: Boolean

            .. note:: For more info -> https://github.com/xSklero/python-telegram-api/wiki/setLastUpdateId
        """

        try:
            self.lastUpdateId = lastUpdateId
            return True
        except:
            return False

    def setWebhook(self, url: str, ip_address='', max_connections=40, allowed_updates=[]) -> bool:
        """   
            Use this method to receive incoming updates using long polling. 
            
            :param url: HTTPS url to send updates to.
            :param ip_address: The fixed IP address which will be used to send webhook requests instead of the IP address resolved through DNS.
            :param max_connections: Maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery, 1-100. Defaults to 40.
            :param allowed_updates: List of the update types you want your bot to receive.

            :type url: String
            :type ip_address: String
            :type max_connections: int
            :type allowed_updates: List

            :return: Returns True on success.
            :rtype: Boolean

            .. note:: For more info -> https://github.com/xSklero/python-telegram-api/wiki/setWebhook 
        """

        token = self.token

        response = requests.get(f"https://api.telegram.org/bot{token}/setWebhook?url={url}&ip_address={ip_address}&max_connections={max_connections}&allowed_updates={allowed_updates}").json()

        if self.debug:
            print(response)

        return response['ok']

    def deleteWebhook(self, drop_pending_updates=True) -> bool:
        """   
            Use this method to remove webhook integration.
            
            :param drop_pending_updates: HTTPS url to send updates to.

            :type drop_pending_updates: Boolean

            :return: Returns True on success.
            :rtype: Boolean

            .. note:: For more info -> https://github.com/xSklero/python-telegram-api/wiki/deleteWebhook
        """

        token = self.token

        response = requests.get(f"https://api.telegram.org/bot{token}/deleteWebhook?drop_pending_updates={drop_pending_updates}").json()

        if self.debug:
            print(response)

        return response['ok']

    def getWebhookInfo(self) -> Dict:
        """   
            Use this method to get current webhook status.

            :return: Returns a WebhookInfo object.
            :rtype: Dict

            .. note:: For more info -> https://github.com/xSklero/python-telegram-api/wiki/getWebhookInfo
        """

        token = self.token

        response = requests.get(f"https://api.telegram.org/bot{token}/getWebhookInfo").json()

        if self.debug:
            print(response)

        return response['result']
