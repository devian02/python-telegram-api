"""
This module contains useful functions to get some Telegram API's objects.

Author: Eric Damian (xSklero)

"""

from typing import List, Dict
import json

def getInlineKeyboard(rows: List) -> Dict:
    """ Use this function to get an InlineKeyboard

    Notes:
        For more info -> https://github.com/xSklero/python-telegram-api/wiki/InlineKeyboardMarkup

    Args:
        rows (Array of Array of InlineKeyboardButton): Array of button rows, each represented by an Array of InlineKeyboardButton objects

    Returns:
        Dict: InlineKeyboard object.
    """

    return {'inline_keyboard': rows}

def getInlineKeyboardButtonWithUrl(text: str, url: str) -> Dict:
    """ Use this function to get an InlineKeyboardButton object with an url

    Notes:
        For more info -> https://github.com/xSklero/python-telegram-api/wiki/InlineKeyboardButton

    Args:
        text (str): Label text on the button.
        url (str): HTTP or tg:// url to be opened when button is pressed.

    Returns:
        Dict: InlineKeyboardButton object.
    """

    return {'text': text, 'url': url}


def getInlineKeyboardButtonWithCallback(text: str, callback_data: str) -> Dict:
    """ Use this function to get an InlineKeyboardButton object with an callback

    Notes:
        For more info -> https://github.com/xSklero/python-telegram-api/wiki/InlineKeyboardButton

    Args:
        text (str): Label text on the button.
        callback_data (str): Data to be sent in a callback query to the bot when button is pressed, 1-64 bytes

    Returns:
        Dict: InlineKeyboardButton object.
    """

    return {'text': text, 'callback_data': callback_data}


def getInlineKeyboardButtonWithSwichInline(text: str, switch_inline_query="") -> Dict:
    """ Use this function to get an InlineKeyboardButton object that sends a message to a chat

    Notes:
        For more info -> https://github.com/xSklero/python-telegram-api/wiki/InlineKeyboardButton

    Args:
        text (str): Label text on the button.
        switch_inline_query (str, optional): Message to be displayed in selected chat. Can be empty, in which case just the bot's username will be inserted. Defaults to "".

    Returns:
        Dict: InlineKeyboardButton object.

    """

    return {'text': text, 'switch_inline_query': switch_inline_query}


def getInlineKeyboardButtonWithSwichInlineCurrentChat(text: str, switch_inline_query_current_chat="") -> Dict:
    """ Use this function to get an InlineKeyboardButton object that sends a message to current chat

    Notes:
        For more info -> https://github.com/xSklero/python-telegram-api/wiki/InlineKeyboardButton
        
    Args:
        text (str): Label text on the button
        switch_inline_query_current_chat (str, optional): Message to be displayed in current chat. Can be empty, in which case just the bot's username will be inserted. Defaults to "".

    Returns:
        Dict: InlineKeyboardButton object.
    """

    return {'text': text, 'switch_inline_query_current_chat': switch_inline_query_current_chat}


def getReplyKeyboard(rows: List, resize_keyboard=False, one_time_keyboard=False, selective=False) -> Dict:
    """ Use this function to get an ReplyKeyboard

    Notes:
        For more info -> https://github.com/xSklero/python-telegram-api/wiki/ReplyKeyboardMarkup

    Args:
        rows (List): Array of button rows, each represented by an Array of KeyboardButton objects
        resize_keyboard (bool, optional): Requests clients to resize the keyboard vertically for optimal fit. Defaults to False.
        one_time_keyboard (bool, optional): Requests clients to hide the keyboard as soon as it's been used. Defaults to False.
        selective (bool, optional): Use this parameter if you want to show the keyboard to specific users only. Defaults to False.

    Returns:
        Dict: ReplyKeyboard object.
    """

    return {'keyboard': rows, 'resize_keyboard': resize_keyboard, 'one_time_keyboard': one_time_keyboard, 'selective': selective}


def getKeyboardButton(text: str, request_contact=False, request_location=False) -> Dict:
    """ This object represents one button of the reply keyboard

    Notes:
        For more info -> https://github.com/xSklero/python-telegram-api/wiki/KeyboardButton

    Args:
        text (str): Text of the button.
        request_contact (bool, optional): If True, the user's phone number will be sent as a contact when the button is pressed. Defaults to False.
        request_location (bool, optional):  If True, the user's current location will be sent when the button is pressed. Defaults to False.

    Returns:
        Dict: KeyboardButton object.
    """

    return {'text': text, 'request_contact': request_contact, 'request_location': request_location}

def getKeyboardButtonPollType(type="") -> Dict:
    """

    Notes:
        For more info -> https://github.com/xSklero/python-telegram-api/wiki/KeyboardButton

    Args:
        type (str): If quiz is passed, the user will be allowed to create only polls in the quiz mode. If regular is passed, only regular polls will be allowed. Otherwise, the user will be allowed to create a poll of any type

    Returns:
        Dict: KeyboardButtonPollType object.
    """

    return {'type': type}

def getKeyboardButtonPoll(text: str, request_poll={}) -> Dict:
    """ This object represents poll button of the reply keyboard

    Notes:
        For more info -> https://github.com/xSklero/python-telegram-api/wiki/KeyboardButton

    Args:
        text (str): Text of the button.
        request_poll (Dict, optional): If specified, the user will be asked to create a poll and send it to the bot when the button is pressed. Defaults to {}.

    Returns:
        Dict: KeyboardButton object.
    """

    return {'text': text, 'request_poll': request_poll}


def getReplyKeyboardRemove(selective=False) -> Dict:
    """ This object will remove the current custom keyboard and display the default letter-keyboard.

    Notes:
        For more info -> https://github.com/xSklero/python-telegram-api/wiki/ReplyKeyboardRemove

    Args:
        selective (bool, optional): Use this parameter if you want to remove the keyboard for specific users only. Defaults to False.

    Returns:
        Dict: ReplyKeyboardRemove object.
    """

    return {'remove_keyboard': True, 'selective': selective}


def getForceReply(selective=False) -> Dict:
    """ Upon receiving a message with this object, Telegram clients will display a reply interface to the user

    Notes:
        For more info -> https://github.com/xSklero/python-telegram-api/wiki/ForceReply

    Args:
        selective (bool, optional): Use this parameter if you want to force reply from specific users only. Defaults to False.

    Returns:
        Dict: ForceReply object.
    """

    return {'force_reply': True, 'selective': selective}
