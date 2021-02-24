"""

This is a Python Library that helps you to use telegram APIs.

Author: Eric Damian

"""

import requests
from typing import List, Dict
import json

class TelegramBotApi():
    """ The implementation of the Python Telegram APIs Bot """
    
    def __init__(self, token: str):
        """ Constructor of TelegramBotApi class

        Args:
            token (str): Bot token from BotFather.
        """

        self.botToken = token # Bot token
        self.lastUpdateId = 0

        self.debug = False # Use this variable to enable or disable debugging mode

    def getDebugMode(self) -> bool:
        """ Use this method to get your actual debug mode.
        
        Notes:
            For more info -> https://github.com/xSklero/python-telegram-api/wiki/getDebugMode

        Returns:
            bool: Actual debug mode
        """

        return self.debug

    def setDebugMode(self, mode: bool) -> bool:
        """ Use this method to set debug mode.

        Notes:
            For more info -> https://github.com/xSklero/python-telegram-api/wiki/setDebugMode

        Args:
            mode (bool): If True all responses from Telegram APIs are printed to console.

        Returns:
            bool: True if mode has been set correctly.
        """

        try:
            self.debug = mode
            return True
        except:
            return False

    def getToken(self) -> str:
        """ Use this method to get your actual bot token.

        Notes:
            For more info -> https://github.com/xSklero/python-telegram-api/wiki/getToken 

        Returns:
            str: Bot token.
        """

        return self.botToken

    def setToken(self, token: str) -> bool:
        """ Use this method to set your actual bot token.

        Notes:
            For more info -> https://github.com/xSklero/python-telegram-api/wiki/setToken 

        Args:
            token (str): New bot token.

        Returns:
            bool: True if token has been set correctly.
        """

        try:
            self.botToken = token
            return True
        except:
            return False

    def getUpdates(self, offset=0, limit=100, timeout=0, allowed_updates=[]) -> List:
        """ Use this method to receive incoming updates using long polling. 

        Notes:
            For more info -> https://github.com/xSklero/python-telegram-api/wiki/getUpdates

        Args:
            offset (int, optional): Identifier of the first update to be returned. Defaults to 0.
            limit (int, optional): Limits the number of updates to be retrieved. Defaults to 100.
            timeout (int, optional): Timeout in seconds for long polling. Defaults to 0.
            allowed_updates (list, optional): List of the update types you want your bot to receive. Defaults to [].

        Returns:
            List: An Array of Update objects is returned.
        """

        token = self.botToken

        params = (
            ('offset', offset),
            ('limit', limit),
            ('timeout', timeout),
            ('allowed_updates', allowed_updates)
        )

        response = requests.get(f"https://api.telegram.org/bot{token}/getUpdates", params=params).json()
        
        if self.debug:
            print(response)

        if len(response["result"]) >= 1:
            # If there are updates available

            self.setLastUpdateId(response["result"][-1]["update_id"]) # Set lastUpdateId

        if response['ok']:
            return response['result']
        else:
            return {'error': 'Error with getUpdates method. Enable debug mode for more info', 'description': response['description']}

    def getLastUpdateId(self) -> int:
        """ Use this method to get lastUpdateId attribute.

        Notes:
            For more info -> https://github.com/xSklero/python-telegram-api/wiki/getLastUpdateId

        Returns:
            int: lastUpdateId attribute
        """

        return self.lastUpdateId

    def setLastUpdateId(self, lastUpdateId: int) -> bool:
        """ Use this method to set lastUpdateId attribute.

        Notes:
            For more info -> https://github.com/xSklero/python-telegram-api/wiki/setLastUpdateId

        Args:
            lastUpdateId (int): New lastUpdateId

        Returns:
            [bool]: True if lastUpdateId has been set correctly
        """

        try:
            self.lastUpdateId = lastUpdateId
            return True
        except:
            return False

    def setWebhook(self, url: str, ip_address='', max_connections=40, allowed_updates=[]) -> bool:
        """ Use this method to specify a url and receive incoming updates via an outgoing webhook.

        Note:
            For more info -> https://github.com/xSklero/python-telegram-api/wiki/setWebhook

        Args:
            url (str): HTTPS url to send updates to.
            ip_address (str, optional): The fixed IP address which will be used to send webhook requests instead of the IP address resolved through DNS. Defaults to ''.
            max_connections (int, optional): Maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery, 1-100. Defaults to 40.
            allowed_updates (list, optional): List of the update types you want your bot to receive. Defaults to [].

        Returns:
            bool: Returns True on success
        """
        
        token = self.botToken

        params = (
            ('url', url),
            ('ip_address', ip_address),
            ('max_connections', max_connections),
            ('allowed_updates', allowed_updates)
        )

        response = requests.get(f"https://api.telegram.org/bot{token}/setWebhook", params=params).json()

        if self.debug:
            print(response)

        if response['ok']:
            return response['result']
        else:
            return {'error': 'Error with setWebhook method. Enable debug mode for more info', 'description': response['description']}

    def deleteWebhook(self, drop_pending_updates=True) -> bool:
        """ Use this method to remove webhook integration.

        Notes:
            For more info -> https://github.com/xSklero/python-telegram-api/wiki/deleteWebhook

        Args:
            drop_pending_updates (bool, optional): HTTPS url to send updates to. Defaults to True.

        Returns:
            bool: Returns True on success.
        """

        token = self.botToken

        params = (
            ('drop_pending_updates', drop_pending_updates),
        )

        response = requests.get(f"https://api.telegram.org/bot{token}/deleteWebhook", params=params).json()

        if self.debug:
            print(response)

        if response['ok']:
            return response['result']
        else:
            return {'error': 'Error with deleteWebhook method. Enable debug mode for more info', 'description': response['description']}

    def getWebhookInfo(self) -> Dict:
        """ Use this method to get current webhook status.

        Notes:
            For more info -> https://github.com/xSklero/python-telegram-api/wiki/getWebhookInfo

        Returns:
            Dict: Returns a WebhookInfo object.
        """

        token = self.botToken

        response = requests.get(f"https://api.telegram.org/bot{token}/getWebhookInfo").json()

        if self.debug:
            print(response)

        if response['ok']:
            return response['result']
        else:
            return {'error': 'Error with getWebhookInfo method. Enable debug mode for more info', 'description': response['description']}

    def getMe(self) -> Dict:
        """ Use this method to get basic bot informations.

        Notes:
            For more info -> https://github.com/xSklero/python-telegram-api/wiki/getMe

        Returns:
            Dict: Returns basic information about the bot in form of a User object.
        """

        token = self.botToken

        response = requests.get(f"https://api.telegram.org/bot{token}/getMe").json()

        if self.debug:
            print(response)

        if response['ok']:
            return response['result']
        else:
            return {'error': 'Error with getMe method. Enable debug mode for more info', 'description': response['description']}

    def getBotUsername(self) -> str:
        """ Use this method to get your actual bot username. 

        Notes:
            For more info -> https://github.com/xSklero/python-telegram-api/wiki/getBotUsername

        Returns:
            str: Bot username.
        """

        try:
            return self.getMe()['username']
        except:
            return ''
    
    def getBotFirstName(self) -> str:
        """ Use this method to get your actual bot first name.

        Notes:
            For more info -> https://github.com/xSklero/python-telegram-api/wiki/getBotFirstName

        Returns:
            str: Bot first name.
        """

        try:
            return self.getMe()['first_name']
        except:
            return ''

    def sendMessage(self, chat_id: str, text: str, parse_mode='MarkdownV2', disable_web_page_preview=False, disable_notification=False, reply_to_message_id=None, allow_sending_without_reply=True, reply_markup={}) -> Dict:
        """ Use this method to send text messages. 

        Notes:
            For more info -> https://github.com/xSklero/python-telegram-api/wiki/sendMessage
            
        Args:
            chat_id (str): Unique identifier for the target chat or username of the target channel.
            text (str): Text of the message to be sent (max 4096 chars).
            parse_mode (str, optional): Mode for parsing entities in the message text. Defaults to 'MarkdownV2'.
            disable_web_page_preview (bool, optional): If True disables link previews for links in this message. Defaults to False.
            disable_notification (bool, optional): If True sends the message silently (Users will receive a notification with no sound). Defaults to False.
            reply_to_message_id (int, optional): ID of the original message to reply to. Defaults to None.
            allow_sending_without_reply (bool, optional): If True the message will be sent even if the specified replied-to message is not found. Defaults to True.
            reply_markup (dict, optional): Additional interface options (A JSON-serialized object). Defaults to {}.

        Returns:
            Dict: On success, the sent Message is returned

        """

        token = self.botToken

        params = (
            ('chat_id', chat_id),
            ('text', text),
            ('parse_mode', parse_mode),
            ('disable_web_page_preview', disable_web_page_preview),
            ('disable_notification', disable_notification),
            ('reply_to_message_id', reply_to_message_id),
            ('allow_sending_without_reply', allow_sending_without_reply),
            ('reply_markup', json.dumps(reply_markup)),
        )

        response = requests.get(f"https://api.telegram.org/bot{token}/sendMessage", params=params).json()
        
        if self.debug:
            print(response)

        if response['ok']:
            return response['result']
        else:
            return {'error': 'Error with sendMessage method. Enable debug mode for more info', 'description': response['description']}


    def forwardMessage(self, chat_id: str, from_chat_id: str, message_id: int, disable_notification=False) -> Dict:
        """ Use this method to forward messages of any kind.

        Notes:
                For more info -> https://github.com/xSklero/python-telegram-api/wiki/forwardMessage

        Args:
            chat_id (str): Unique identifier for the target chat or username of the target channel.
            from_chat_id (str): Unique identifier for the chat where the original message was sent.
            message_id (int): Message identifier in the chat specified in from_chat_id.
            disable_notification (bool, optional): Sends the message silently. Users will receive a notification with no sound.. Defaults to False.

        Returns:
            Dict: The sent Message is returned on success.
        """

        token = self.botToken

        params = (
            ('chat_id', chat_id),
            ('from_chat_id', from_chat_id),
            ('message_id', message_id),
            ('disable_notification', disable_notification),
        )

        response = requests.get(f"https://api.telegram.org/bot{token}/forwardMessage", params=params).json()

        if self.debug:
            print(response)

        if response['ok']:
            return response['result']
        else:
            return {'error': 'Error with forwardMessage method. Enable debug mode for more info', 'description': response['description']}

    def copyMessage(self, chat_id: str, from_chat_id: str, message_id: int, caption="", disable_notification=False, reply_to_message_id=None, allow_sending_without_reply=True, reply_markup={}) -> Dict:
        """ Use this method to copy messages of any kind. The method is analogous to the method forwardMessage, but the copied message doesn't have a link to the original message.

        Notes:
                For more info -> https://github.com/xSklero/python-telegram-api/wiki/copyMessage

        Args:
            chat_id (str): Unique identifier for the target chat or username of the target channel.
            from_chat_id (str): Unique identifier for the chat where the original message was sent.
            message_id (int): Message identifier in the chat specified in from_chat_id.
            caption (str): New caption for media. Defaults to "".
            disable_notification (bool, optional): If True sends the message silently (Users will receive a notification with no sound). Defaults to False.
            reply_to_message_id (int, optional): ID of the original message to reply to. Defaults to None.
            allow_sending_without_reply (bool, optional): If True the message will be sent even if the specified replied-to message is not found. Defaults to True.
            reply_markup (dict, optional): Additional interface options (A JSON-serialized object). Defaults to {}.

        Returns:
            Dict: The MessageId of the sent message on success.
        """

        token = self.botToken

        params = (
            ('chat_id', chat_id),
            ('from_chat_id', from_chat_id),
            ('message_id', message_id),
            ('caption', caption),
            ('disable_notification', disable_notification),
            ('reply_to_message_id', reply_to_message_id),
            ('allow_sending_without_reply', allow_sending_without_reply),
            ('reply_markup', json.dumps(reply_markup)),
        )

        response = requests.get(f"https://api.telegram.org/bot{token}/copyMessage", params=params).json()

        if self.debug:
            print(response)

        if response['ok']:
            return response['result']
        else:
            return {'error': 'Error with copyMessage method. Enable debug mode for more info', 'description': response['description']}

    def sendPhoto(self, chat_id: str, photo_url="", local_photo="", caption="", parse_mode='MarkdownV2', disable_notification=False, reply_to_message_id=None, allow_sending_without_reply=True, reply_markup={}) -> Dict:
        """ Use this method to send photos

        Notes:
                For more info -> https://github.com/xSklero/python-telegram-api/wiki/sendPhoto

        Args:
            chat_id (str): Unique identifier for the target chat or username of the target channel.
            photo_url (str, optional): Pass an HTTP URL as a String for Telegram to get a photo from the Internet. Defaults to "".
            local_photo (str, optional): Your image path. The photo must be at most 10 MB in size. The photo's width and height must not exceed 10000 in total. Width and height ratio must be at most 20. Defaults to "".
            caption (str, optional): Photo caption. Defaults to "".
            parse_mode (str, optional): Mode for parsing entities in the message text. Defaults to 'MarkdownV2'.
            disable_notification (bool, optional): If True sends the message silently (Users will receive a notification with no sound). Defaults to False.
            reply_to_message_id (int, optional): ID of the original message to reply to. Defaults to None.
            allow_sending_without_reply (bool, optional): If True the message will be sent even if the specified replied-to message is not found. Defaults to True.
            reply_markup (dict, optional): Additional interface options (A JSON-serialized object). Defaults to {}.

        Returns:
            Dict: On success, the sent Message is returned.
        """

        token = self.botToken

        params = (
            ('chat_id', chat_id),
            ('photo', photo_url),
            ('parse_mode', parse_mode),
            ('caption', caption),
            ('disable_notification', disable_notification),
            ('reply_to_message_id', reply_to_message_id),
            ('allow_sending_without_reply', allow_sending_without_reply),
            ('reply_markup', json.dumps(reply_markup)),
        )

        if local_photo != "": # If using a local file

            try:
                response = requests.post(f"https://api.telegram.org/bot{token}/sendPhoto", params=params, files={'photo': (open(local_photo, 'rb'))}).json()
            except:
                return {'error': 'Error with sendPhoto method. Enable debug mode for more info', 'description': 'Bad file path'}
            
        else:

            response = requests.get(f"https://api.telegram.org/bot{token}/sendPhoto", params=params).json()

        if self.debug:
            print(response)

        if response['ok']:
            return response['result']
        else:
            return {'error': 'Error with sendPhoto method. Enable debug mode for more info', 'description': response['description']}

    def sendAudio(self, chat_id: str, audio_url="", local_audio="", caption="", performer="", title="", duration="", thumb="", parse_mode='MarkdownV2', disable_notification=False, reply_to_message_id=None, allow_sending_without_reply=True, reply_markup={}) -> Dict:
        """ Use this method to send audios

        Notes:
                For more info -> https://github.com/xSklero/python-telegram-api/wiki/sendAudio

        Args:
            chat_id (str): Unique identifier for the target chat or username of the target channel.
            audio_url (str, optional): Pass an HTTP URL as a String for Telegram to get a audio from the Internet. Your audio must be in the .MP3 or .M4A format. Defaults to "".
            local_audio (str, optional): Your audio path. Your audio must be in the .MP3 or .M4A format. Bots can currently send audio files of up to 50 MB in size, this limit may be changed in the future.
            caption (str, optional): Audio caption. Defaults to "".
            performer (str, optional): Performer.
            title (str, optional): Track name.
            duration (str, optional): Duration of the audio in seconds.
            thumb (str, optional): Thumbnail of the file sent. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320.
            parse_mode (str, optional): Mode for parsing entities in the message text. Defaults to 'MarkdownV2'.
            disable_notification (bool, optional): If True sends the message silently (Users will receive a notification with no sound). Defaults to False.
            reply_to_message_id (int, optional): ID of the original message to reply to. Defaults to None.
            allow_sending_without_reply (bool, optional): If True the message will be sent even if the specified replied-to message is not found. Defaults to True.
            reply_markup (dict, optional): Additional interface options (A JSON-serialized object). Defaults to {}.

        Returns:
            Dict: On success, the sent Message is returned.
        """

        token = self.botToken

        params = (
            ('chat_id', chat_id),
            ('audio', audio_url),
            ('parse_mode', parse_mode),
            ('caption', caption),
            ('duration', duration),
            ('title', title),
            ('performer', performer),
            ('disable_notification', disable_notification),
            ('reply_to_message_id', reply_to_message_id),
            ('allow_sending_without_reply', allow_sending_without_reply),
            ('reply_markup', json.dumps(reply_markup)),
        )

        if local_audio != "": # If using a local audio file

            try:

                if thumb != "": # If using a thumb

                    try:
                        response = requests.post(f"https://api.telegram.org/bot{token}/sendAudio", params=params, files={'audio': (open(local_audio, 'rb')), 'thumb': (open(thumb, 'rb'))}).json()
                    except:
                        return {'error': 'Error with sendAudio method. Enable debug mode for more info', 'description': 'Bad file path'}
                
                else:

                    try:
                        response = requests.post(f"https://api.telegram.org/bot{token}/sendAudio", params=params, files={'audio': (open(local_audio, 'rb'))}).json()
                    except:
                        return {'error': 'Error with sendAudio method. Enable debug mode for more info', 'description': 'Bad file path'}

            except:
                return {'error': 'Error with sendPhoto method. Enable debug mode for more info', 'description': 'Bad file path'}

        else:

            response = requests.get(f"https://api.telegram.org/bot{token}/sendAudio", params=params).json()

        if self.debug:
            print(response)

        if response['ok']:
            return response['result']
        else:
            return {'error': 'Error with sendPhoto method. Enable debug mode for more info', 'description': response['description']}

    def sendDocument(self, chat_id: str, document_url="", local_document="", caption="", disable_content_type_detection=False, thumb="", parse_mode='MarkdownV2', disable_notification=False, reply_to_message_id=None, allow_sending_without_reply=True, reply_markup={}) -> Dict:
        """ Use this method to send general files

        Notes:
                For more info -> https://github.com/xSklero/python-telegram-api/wiki/sendDocument

        Args:
            chat_id (str): Unique identifier for the target chat or username of the target channel.
            document_url (str, optional): Pass an HTTP URL as a String for Telegram to get a document from the Internet. Your document must be in any format. Defaults to "".
            local_document (str, optional): Your document path. Your document must be in any format. Bots can currently send document files of up to 50 MB in size, this limit may be changed in the future.
            caption (str, optional): document caption. Defaults to "".
            disable_content_type_detection (bool, optional): Disables automatic server-side content type detection for files uploaded. Defaults to False.
            thumb (str, optional): Thumbnail of the file sent. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320.
            parse_mode (str, optional): Mode for parsing entities in the message text. Defaults to 'MarkdownV2'.
            disable_notification (bool, optional): If True sends the message silently (Users will receive a notification with no sound). Defaults to False.
            reply_to_message_id (int, optional): ID of the original message to reply to. Defaults to None.
            allow_sending_without_reply (bool, optional): If True the message will be sent even if the specified replied-to message is not found. Defaults to True.
            reply_markup (dict, optional): Additional interface options (A JSON-serialized object). Defaults to {}.

        Returns:
            Dict: On success, the sent Message is returned.
        """

        token = self.botToken

        params = (
            ('chat_id', chat_id),
            ('document', document_url),
            ('parse_mode', parse_mode),
            ('caption', caption),
            ('disable_content_type_detection', disable_content_type_detection),
            ('disable_notification', disable_notification),
            ('reply_to_message_id', reply_to_message_id),
            ('allow_sending_without_reply', allow_sending_without_reply),
            ('reply_markup', json.dumps(reply_markup)),
        )

        if local_document != "":  # If using a local document file

            try:

                if thumb != "":  # If using a thumb

                    try:
                        response = requests.post(f"https://api.telegram.org/bot{token}/sendDocument", params=params, files={
                                                 'document': (open(local_document, 'rb')), 'thumb': (open(thumb, 'rb'))}).json()
                    except:
                        return {'error': 'Error with sendDocument method. Enable debug mode for more info', 'description': 'Bad file path'}

                else:

                    try:
                        response = requests.post(f"https://api.telegram.org/bot{token}/sendDocument", params=params, files={
                                                 'document': (open(local_document, 'rb'))}).json()
                    except:
                        return {'error': 'Error with sendDocument method. Enable debug mode for more info', 'description': 'Bad file path'}

            except:
                return {'error': 'Error with sendDocument method. Enable debug mode for more info', 'description': 'Bad file path'}

        else:

            response = requests.get(
                f"https://api.telegram.org/bot{token}/sendDocument", params=params).json()

        if self.debug:
            print(response)

        if response['ok']:
            return response['result']
        else:
            return {'error': 'Error with sendDocument method. Enable debug mode for more info', 'description': response['description']}

    def sendVideo(self, chat_id: str, video_url="", local_video="", caption="", width="", height="", duration="", supports_streaming=False, thumb="", parse_mode='MarkdownV2', disable_notification=False, reply_to_message_id=None, allow_sending_without_reply=True, reply_markup={}) -> Dict:
        """ Use this method to send video files

        Notes:
                For more info -> https://github.com/xSklero/python-telegram-api/wiki/sendVideo

        Args:
            chat_id (str): Unique identifier for the target chat or username of the target channel.
            video_url (str, optional): Pass an HTTP URL as a String for Telegram to get a video from the Internet. Your video must be in the .MP3 or .M4A format. Defaults to "".
            local_video (str, optional): Your video path. Your video must be in the .MP3 or .M4A format. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.
            caption (str, optional): Video caption. Defaults to "".
            width (str, optional): Video width. Defaults to "".
            height (str, optional): Video height. Defaults to "".
            duration (str, optional): Duration of the video in seconds. Defaults to "".
            supports_streaming (bool, optional): Pass True, if the uploaded video is suitable for streaming. Defaults to False.
            thumb (str, optional): Thumbnail of the file sent. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320.
            parse_mode (str, optional): Mode for parsing entities in the message text. Defaults to 'MarkdownV2'.
            disable_notification (bool, optional): If True sends the message silently (Users will receive a notification with no sound). Defaults to False.
            reply_to_message_id (int, optional): ID of the original message to reply to. Defaults to None.
            allow_sending_without_reply (bool, optional): If True the message will be sent even if the specified replied-to message is not found. Defaults to True.
            reply_markup (dict, optional): Additional interface options (A JSON-serialized object). Defaults to {}.

        Returns:
            Dict: On success, the sent Message is returned.
        """

        token = self.botToken

        params = (
            ('chat_id', chat_id),
            ('video', video_url),
            ('parse_mode', parse_mode),
            ('caption', caption),
            ('duration', duration),
            ('width', width),
            ('height', height),
            ('supports_streaming', supports_streaming),
            ('disable_notification', disable_notification),
            ('reply_to_message_id', reply_to_message_id),
            ('allow_sending_without_reply', allow_sending_without_reply),
            ('reply_markup', json.dumps(reply_markup)),
        )

        if local_video != "":  # If using a local video file

            try:

                if thumb != "":  # If using a thumb

                    try:
                        response = requests.post(f"https://api.telegram.org/bot{token}/sendVideo", params=params, files={
                                                 'video': (open(local_video, 'rb')), 'thumb': (open(thumb, 'rb'))}).json()
                    except:
                        return {'error': 'Error with sendVideo method. Enable debug mode for more info', 'description': 'Bad file path'}

                else:

                    try:
                        response = requests.post(f"https://api.telegram.org/bot{token}/sendVideo", params=params, files={
                                                 'video': (open(local_video, 'rb'))}).json()
                    except:
                        return {'error': 'Error with sendVideo method. Enable debug mode for more info', 'description': 'Bad file path'}

            except:
                return {'error': 'Error with sendVideo method. Enable debug mode for more info', 'description': 'Bad file path'}

        else:

            response = requests.get(
                f"https://api.telegram.org/bot{token}/sendVideo", params=params).json()

        if self.debug:
            print(response)

        if response['ok']:
            return response['result']
        else:
            return {'error': 'Error with sendVideo method. Enable debug mode for more info', 'description': response['description']}

    def sendAnimation(self, chat_id: str, animation_url="", local_animation="", caption="", width="", height="", duration="", thumb="", parse_mode='MarkdownV2', disable_notification=False, reply_to_message_id=None, allow_sending_without_reply=True, reply_markup={}) -> Dict:
        """ Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without sound)

        Notes:
                For more info -> https://github.com/xSklero/python-telegram-api/wiki/sendAnimation

        Args:
            chat_id (str): Unique identifier for the target chat or username of the target channel.
            animation_url (str, optional): Pass an HTTP URL as a String for Telegram to get a animation from the Internet. Your animation must be in the .MP3 or .M4A format. Defaults to "".
            local_animation (str, optional): Your animation path. Your animation must be GIF or H.264/MPEG-4 AVC video without sound. Bots can currently send animation files of up to 50 MB in size, this limit may be changed in the future.
            caption (str, optional): Video caption. Defaults to "".
            width (str, optional): Video width. Defaults to "".
            height (str, optional): Video height. Defaults to "".
            duration (str, optional): Duration of the video in seconds. Defaults to "".
            thumb (str, optional): Thumbnail of the file sent. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320.
            parse_mode (str, optional): Mode for parsing entities in the message text. Defaults to 'MarkdownV2'.
            disable_notification (bool, optional): If True sends the message silently (Users will receive a notification with no sound). Defaults to False.
            reply_to_message_id (int, optional): ID of the original message to reply to. Defaults to None.
            allow_sending_without_reply (bool, optional): If True the message will be sent even if the specified replied-to message is not found. Defaults to True.
            reply_markup (dict, optional): Additional interface options (A JSON-serialized object). Defaults to {}.

        Returns:
            Dict: On success, the sent Message is returned.
        """

        token = self.botToken

        params = (
            ('chat_id', chat_id),
            ('animation', animation_url),
            ('parse_mode', parse_mode),
            ('caption', caption),
            ('duration', duration),
            ('width', width),
            ('height', height),
            ('disable_notification', disable_notification),
            ('reply_to_message_id', reply_to_message_id),
            ('allow_sending_without_reply', allow_sending_without_reply),
            ('reply_markup', json.dumps(reply_markup)),
        )

        if local_animation != "":  # If using a local animation file

            try:

                if thumb != "":  # If using a thumb

                    try:
                        response = requests.post(f"https://api.telegram.org/bot{token}/sendAnimation", params=params, files={
                                                 'animation': (open(local_animation, 'rb')), 'thumb': (open(thumb, 'rb'))}).json()
                    except:
                        return {'error': 'Error with sendAnimation method. Enable debug mode for more info', 'description': 'Bad file path'}

                else:

                    try:
                        response = requests.post(f"https://api.telegram.org/bot{token}/sendAnimation", params=params, files={
                                                 'animation': (open(local_animation, 'rb'))}).json()
                    except:
                        return {'error': 'Error with sendAnimation method. Enable debug mode for more info', 'description': 'Bad file path'}

            except:
                return {'error': 'Error with sendAnimation method. Enable debug mode for more info', 'description': 'Bad file path'}

        else:

            response = requests.get(
                f"https://api.telegram.org/bot{token}/sendAnimation", params=params).json()

        if self.debug:
            print(response)

        if response['ok']:
            return response['result']
        else:
            return {'error': 'Error with sendAnimation method. Enable debug mode for more info', 'description': response['description']}

    def sendVoice(self, chat_id: str, voice_url="", local_voice="", caption="", duration="", parse_mode='MarkdownV2', disable_notification=False, reply_to_message_id=None, allow_sending_without_reply=True, reply_markup={}) -> Dict:
        """ Use this method to send audio files

        Notes:
                For more info -> https://github.com/xSklero/python-telegram-api/wiki/sendVoice

        Args:
            chat_id (str): Unique identifier for the target chat or username of the target channel.
            voice_url (str, optional): Pass an HTTP URL as a String for Telegram to get a voice from the Internet. Defaults to "".
            local_voice (str, optional): Your audio path. Bots can currently send voice messages of up to 50 MB. Your audio must be in an .OGG file encoded. Defaults to "".
            caption (str, optional): Voice caption. Defaults to "".
            duration (str, optional): Duration of the video in seconds. Defaults to "".
            parse_mode (str, optional): Mode for parsing entities in the message text. Defaults to 'MarkdownV2'.
            disable_notification (bool, optional): If True sends the message silently (Users will receive a notification with no sound). Defaults to False.
            reply_to_message_id (int, optional): ID of the original message to reply to. Defaults to None.
            allow_sending_without_reply (bool, optional): If True the message will be sent even if the specified replied-to message is not found. Defaults to True.
            reply_markup (dict, optional): Additional interface options (A JSON-serialized object). Defaults to {}.

        Returns:
            Dict: On success, the sent Message is returned.
        """

        token = self.botToken

        params = (
            ('chat_id', chat_id),
            ('voice', voice_url),
            ('parse_mode', parse_mode),
            ('caption', caption),
            ('duration', duration),
            ('disable_notification', disable_notification),
            ('reply_to_message_id', reply_to_message_id),
            ('allow_sending_without_reply', allow_sending_without_reply),
            ('reply_markup', json.dumps(reply_markup)),
        )

        if local_voice != "": # If using a local file

            try:
                response = requests.post(f"https://api.telegram.org/bot{token}/sendVoice", params=params, files={'voice': (open(local_voice, 'rb'))}).json()
            except:
                return {'error': 'Error with sendVoice method. Enable debug mode for more info', 'description': 'Bad file path'}
            
        else:

            response = requests.get(f"https://api.telegram.org/bot{token}/sendVoice", params=params).json()

        if self.debug:
            print(response)

        if response['ok']:
            return response['result']
        else:
            return {'error': 'Error with sendVoice method. Enable debug mode for more info', 'description': response['description']}

    def sendVideoNote(self, chat_id: str, local_video="", length="30", duration="", thumb="", parse_mode='MarkdownV2', disable_notification=False, reply_to_message_id=None, allow_sending_without_reply=True, reply_markup={}) -> Dict:
        """ Use this method to send rounded square mp4 videos of up to 1 minute long. Sending video notes by a URL is currently unsupported. 

        Notes:
                For more info -> https://github.com/xSklero/python-telegram-api/wiki/sendVideoNote

        Args:
            chat_id (str): Unique identifier for the target chat or username of the target channel.
            local_video (str, optional): Your video path. Your video must be in the .MP3 or .M4A format. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.
            length (str, optional): Video width and height, i.e. diameter of the video message. Defaults to "".
            duration (str, optional): Duration of the video in seconds. Defaults to "".
            thumb (str, optional): Thumbnail of the file sent. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320.
            parse_mode (str, optional): Mode for parsing entities in the message text. Defaults to 'MarkdownV2'.
            disable_notification (bool, optional): If True sends the message silently (Users will receive a notification with no sound). Defaults to False.
            reply_to_message_id (int, optional): ID of the original message to reply to. Defaults to None.
            allow_sending_without_reply (bool, optional): If True the message will be sent even if the specified replied-to message is not found. Defaults to True.
            reply_markup (dict, optional): Additional interface options (A JSON-serialized object). Defaults to {}.

        Returns:
            Dict: On success, the sent Message is returned.
        """

        token = self.botToken

        params = (
            ('chat_id', chat_id),
            ('parse_mode', parse_mode),
            ('duration', duration),
            ('length', length),
            ('disable_notification', disable_notification),
            ('reply_to_message_id', reply_to_message_id),
            ('allow_sending_without_reply', allow_sending_without_reply),
            ('reply_markup', json.dumps(reply_markup)),
        )

        if local_video != "":  # If using a local video file

            try:

                if thumb != "":  # If using a thumb

                    try:
                        response = requests.post(f"https://api.telegram.org/bot{token}/sendVideoNote", params=params, files={
                                                 'video_note': (open(local_video, 'rb')), 'thumb': (open(thumb, 'rb'))}).json()
                    except:
                        return {'error': 'Error with sendVideoNote method. Enable debug mode for more info', 'description': 'Bad file path'}

                else:

                    try:
                        response = requests.post(f"https://api.telegram.org/bot{token}/sendVideoNote", params=params, files={
                                                 'video_note': (open(local_video, 'rb'))}).json()
                    except:
                        return {'error': 'Error with sendVideoNote method. Enable debug mode for more info', 'description': 'Bad file path'}

            except:
                return {'error': 'Error with sendVideoNote method. Enable debug mode for more info', 'description': 'Bad file path'}

        else:

            response = requests.get(
                f"https://api.telegram.org/bot{token}/sendVideoNote", params=params).json()

        if self.debug:
            print(response)

        if response['ok']:
            return response['result']
        else:
            return {'error': 'Error with sendVideoNote method. Enable debug mode for more info', 'description': response['description']}


    def sendMediaGroup(self, chat_id: str, media_url=[], local_media=[], disable_notification=False, reply_to_message_id=None, allow_sending_without_reply=True) -> Dict:
            """ Use this method to send photos

            Notes:
                    For more info -> https://github.com/xSklero/python-telegram-api/wiki/sendMediaGroup

            Args:
                chat_id (str): Unique identifier for the target chat or username of the target channel.
                media_url (list, optional): Pass an array of HTTP URL as a String for Telegram to get a photo from the Internet. Defaults to "".
                local_media (list, optional): An array of image paths. The photos must be at most 10 MB in size. The photos' width and height must not exceed 10000 in total. Width and height ratio must be at most 20. Defaults to "".
                disable_notification (bool, optional): If True sends the message silently (Users will receive a notification with no sound). Defaults to False.
                reply_to_message_id (int, optional): ID of the original message to reply to. Defaults to None.
                allow_sending_without_reply (bool, optional): If True the message will be sent even if the specified replied-to message is not found. Defaults to True.

            Returns:
                Dict: On success, an array of sent Messages is returned.
            """

            token = self.botToken

            if len(local_media) != 0:  # If using a local file array

                files = {}
                
                inputMediaMediaArray = []

                for images_ref in range(len(local_media)): # each media

                    files[str(images_ref)] = (open(local_media[images_ref]['media'], 'rb'))

                    local_media[images_ref]['media'] = 'attach://' + str(images_ref)

                    inputMediaMediaArray.append(local_media[images_ref])

                try:

                    params = (
                        ('chat_id', chat_id),
                        ('media', json.dumps(inputMediaMediaArray)),
                        ('disable_notification', disable_notification),
                        ('reply_to_message_id', reply_to_message_id),
                        ('allow_sending_without_reply', allow_sending_without_reply),
                    )

                    response = requests.post(f"https://api.telegram.org/bot{token}/sendMediaGroup", params=params, files=files).json()

                except:
                    return {'error': 'Error with sendMediaGroup method. Enable debug mode for more info', 'description': 'Bad file path'}

            else: # If using urls file array

                inputMediaMediaArray = []

                for media in media_url:  # each media

                    inputMediaMediaArray.append(media)

                try:

                    params = (
                        ('chat_id', chat_id),
                        ('media', json.dumps(inputMediaMediaArray)),
                        ('disable_notification', disable_notification),
                        ('reply_to_message_id', reply_to_message_id),
                        ('allow_sending_without_reply', allow_sending_without_reply),
                    )

                    response = requests.post(f"https://api.telegram.org/bot{token}/sendMediaGroup", params=params).json()
                
                except:
                    return {'error': 'Error with sendMediaGroup method. Enable debug mode for more info', 'description': 'Bad file path'}

            if self.debug:
                print(response)

            if response['ok']:
                return response['result']
            else:
                return {'error': 'Error with sendMediaGroup method. Enable debug mode for more info', 'description': response['description']}

    def sendLocation(self, chat_id: str, latitude: float, longitude: float, horizontal_accuracy="", live_period="", heading="", proximity_alert_radius="", disable_notification=False, reply_to_message_id=None, allow_sending_without_reply=True, reply_markup={}) -> Dict:
        """ Use this method to send point on the map.

        Notes:
                    For more info -> https://github.com/xSklero/python-telegram-api/wiki/sendLocation

        Args:
            chat_id (str): Unique identifier for the target chat or username of the target channel.
            latitude (float): Latitude of the location.
            longitude (float): Longitude of the location.
            horizontal_accuracy (str, optional): The radius of uncertainty for the location, measured in meters; 0-1500. Defaults to "".
            live_period (str, optional): Period in seconds for which the location will be updated, should be between 60 and 86400. Defaults to "".
            heading (str, optional): For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified. Defaults to "".
            proximity_alert_radius (str, optional): For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.. Defaults to "".
            disable_notification (bool, optional): If True sends the message silently (Users will receive a notification with no sound). Defaults to False.
            reply_to_message_id (int, optional): ID of the original message to reply to. Defaults to None.
            allow_sending_without_reply (bool, optional): If True the message will be sent even if the specified replied-to message is not found. Defaults to True.
            reply_markup (dict, optional): Additional interface options (A JSON-serialized object). Defaults to {}.

        Returns:
            Dict: On success, the sent Message is returned.
        """

        token = self.botToken

        params = (
            ('chat_id', chat_id),
            ('latitude', latitude),
            ('longitude', longitude),
            ('horizontal_accuracy', horizontal_accuracy),
            ('live_period', live_period),
            ('heading', heading),
            ('proximity_alert_radius', proximity_alert_radius),
            ('horizontal_accuracy', horizontal_accuracy),
            ('disable_notification', disable_notification),
            ('reply_to_message_id', reply_to_message_id),
            ('allow_sending_without_reply', allow_sending_without_reply),
            ('reply_markup', json.dumps(reply_markup)),
        )

        response = requests.get(f"https://api.telegram.org/bot{token}/sendLocation", params=params).json()

        if self.debug:
            print(response)

        if response['ok']:
            return response['result']
        else:
            return {'error': 'Error with sendLocation method. Enable debug mode for more info', 'description': response['description']}

    def editMessageLiveLocation(self, latitude: float, longitude: float, chat_id="", message_id="", inline_message_id="", horizontal_accuracy="", heading="", proximity_alert_radius="", reply_markup={}) -> Dict:
        """ Use this method to edit live location messages. A location can be edited until its live_period expires or editing is explicitly disabled by a call to stopMessageLiveLocation.

        Notes:
                    For more info -> https://github.com/xSklero/python-telegram-api/wiki/editMessageLiveLocation

        Args:
            latitude (float): Latitude of new location.
            longitude (float): Longitude of new location.
            chat_id (str, optional): Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel. Defaults to "".
            message_id (str, optional): Required if inline_message_id is not specified. Identifier of the message to edit. Defaults to "".
            inline_message_id (str, optional): Required if chat_id and message_id are not specified. Identifier of the inline message. Defaults to "".
            horizontal_accuracy (str, optional): The radius of uncertainty for the location, measured in meters; 0-1500. Defaults to "".
            heading (str, optional): Direction in which the user is moving, in degrees. Must be between 1 and 360 if specified. Defaults to "".
            proximity_alert_radius (str, optional): Maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000. Defaults to "".
            reply_markup (dict, optional): Additional interface options (A JSON-serialized object). Defaults to {}.

        Returns:
            Dict: On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.
        """

        token = self.botToken

        params = (
            ('chat_id', chat_id),
            ('latitude', latitude),
            ('longitude', longitude),
            ('message_id', message_id),
            ('heading', heading),
            ('proximity_alert_radius', proximity_alert_radius),
            ('horizontal_accuracy', horizontal_accuracy),
            ('inline_message_id', inline_message_id),
            ('reply_markup', json.dumps(reply_markup)),
        )

        response = requests.get(f"https://api.telegram.org/bot{token}/editMessageLiveLocation", params=params).json()

        if self.debug:
            print(response)

        if response['ok']:
            return response['result']
        else:
            return {'error': 'Error with editMessageLiveLocation method. Enable debug mode for more info', 'description': response['description']}


    def stopMessageLiveLocation(self, chat_id="", message_id="", inline_message_id="", reply_markup={}) -> Dict:
        """ Use this method to stop updating a live location message before live_period expires.

            Notes:
                    For more info -> https://github.com/xSklero/python-telegram-api/wiki/stopMessageLiveLocation

            Args:
                chat_id (str, optional): Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel. Defaults to "".
                message_id (str, optional): Required if inline_message_id is not specified. Identifier of the message to edit. Defaults to "".
                inline_message_id (str, optional): Required if chat_id and message_id are not specified. Identifier of the inline message. Defaults to "".
                reply_markup (dict, optional): Additional interface options (A JSON-serialized object). Defaults to {}.

            Returns:
                Dict: On success, if the message was sent by the bot, the sent Message is returned, otherwise True is returned.
            """

        token = self.botToken

        params = (
            ('chat_id', chat_id),
            ('message_id', message_id),
            ('inline_message_id', inline_message_id),
            ('reply_markup', json.dumps(reply_markup)),
        )

        response = requests.get(
            f"https://api.telegram.org/bot{token}/stopMessageLiveLocation", params=params).json()

        if self.debug:
                print(response)

        if response['ok']:
            return response['result']
        else:
            return {'error': 'Error with stopMessageLiveLocation method. Enable debug mode for more info', 'description': response['description']}

    def sendVenue(self, chat_id: str, latitude: float, longitude: float, title: str, address: str, foursquare_id="", foursquare_type="", google_place_id="", google_place_type="", disable_notification=False, reply_to_message_id=None, allow_sending_without_reply=True, reply_markup={}) -> Dict:
        """ Use this method to send information about a venue.

        Notes:
                    For more info -> https://github.com/xSklero/python-telegram-api/wiki/sendVenue

        Args:
            chat_id (str): Unique identifier for the target chat or username of the target channel.
            latitude (float): Latitude of the location.
            longitude (float): Longitude of the location.
            title (str): Name of the venue.
            address (str): Address of the venue.
            foursquare_id (str, optional): Foursquare identifier of the venue. Defaults to "".
            foursquare_type (str, optional): Foursquare type of the venue. Defaults to "".
            google_place_id (str, optional): Google Places identifier of the venue. Defaults to "".
            google_place_type (str, optional): Google Places type of the venue. Defaults to "".
            disable_notification (bool, optional): If True sends the message silently (Users will receive a notification with no sound). Defaults to False.
            reply_to_message_id (int, optional): ID of the original message to reply to. Defaults to None.
            allow_sending_without_reply (bool, optional): If True the message will be sent even if the specified replied-to message is not found. Defaults to True.
            reply_markup (dict, optional): Additional interface options (A JSON-serialized object). Defaults to {}.

        Returns:
            Dict: [description]
        """

        token = self.botToken

        params = (
            ('chat_id', chat_id),
            ('latitude', latitude),
            ('longitude', longitude),
            ('title', title),
            ('address', address),
            ('foursquare_id', foursquare_id),
            ('foursquare_type', foursquare_type),
            ('google_place_id', google_place_id),
            ('google_place_type', google_place_type),
            ('disable_notification', disable_notification),
            ('reply_to_message_id', reply_to_message_id),
            ('allow_sending_without_reply', allow_sending_without_reply),
            ('reply_markup', json.dumps(reply_markup)),
        )

        response = requests.get(
            f"https://api.telegram.org/bot{token}/sendVenue", params=params).json()

        if self.debug:
            print(response)

        if response['ok']:
            return response['result']
        else:
            return {'error': 'Error with sendVenue method. Enable debug mode for more info', 'description': response['description']}
