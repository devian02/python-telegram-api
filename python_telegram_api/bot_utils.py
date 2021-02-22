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


def getInputMediaPhoto(media: str, caption="", parse_mode='MarkdownV2') -> Dict:
    """ Represents a photo to be sent.

    Notes:
        For more info -> https://github.com/xSklero/python-telegram-api/wiki/InputMediaPhoto

    Args:
        media (str): pass an HTTP URL for Telegram to get a file from the Internet, or pass your local file.
        caption (str, optional): Caption of the photo to be sent, 0-1024 characters. Defaults to "".
        parse_mode (str, optional): Mode for parsing entities in the photo caption. Defaults to 'MarkdownV2'.

    Returns:
        Dict: Returns a photo to be sent with sendMediaGroup.
    """

    return {'type':'photo', 'media':media, 'caption':caption, 'parse_mode':parse_mode}


def getInputMediaVideo(media: str, caption="", thumb="", parse_mode='MarkdownV2', width=-1, height=-1, duration=-1, supports_streaming=False) -> Dict:
    """ Represents a video to be sent.

    Notes:
        For more info -> https://github.com/xSklero/python-telegram-api/wiki/InputMediaVideo

    Args:
        media (str): pass an HTTP URL for Telegram to get a file from the Internet, or pass your local file.
        caption (str, optional): Caption of the video to be sent, 0-1024 characters. Defaults to "".
        parse_mode (str, optional): Mode for parsing entities in the video caption. Defaults to 'MarkdownV2'.
        thumb (str, optional): Thumbnail of the file sent. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Defaults to "".
        width (int, optional): Video width. Defaults to -1.
        height (int, optional): Video height. Defaults to -1.
        duration (int, optional): Video duration. Defaults to -1.
        supports_streaming (bool, optional): Pass True, if the uploaded video is suitable for streaming. Defaults to False.

    Returns:
        Dict: Returns a video to be sent.
    """

    return {'type': 'video', 'media': media, 'caption': caption, 'parse_mode': parse_mode, 'thumb': thumb, 'width': width, 'height': height, 'duration': duration, 'supports_streaming': supports_streaming}


def getInputMediaAnimation(media: str, caption="", thumb="", parse_mode='MarkdownV2', width="", height="", duration="") -> Dict:
    """ Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent.

    Notes:
        For more info -> https://github.com/xSklero/python-telegram-api/wiki/InputMediaAnimation

    Args:
        media (str): pass an HTTP URL for Telegram to get a file from the Internet, or pass your local file.
        caption (str, optional): Caption of the animation to be sent, 0-1024 characters. Defaults to "".
        parse_mode (str, optional): Mode for parsing entities in the animation caption. Defaults to 'MarkdownV2'.
        thumb (str, optional): Thumbnail of the file sent. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Defaults to "".
        width (int, optional): Animation width. Defaults to -1.
        height (int, optional): Animation height. Defaults to -1.
        duration (int, optional): Animation duration. Defaults to -1.

    Returns:
        Dict: Returns a Animation to be sent.
    """

    return {'type': 'animation', 'media': media, 'caption': caption, 'parse_mode': parse_mode, 'thumb': thumb, 'width': width, 'height': height, 'duration': duration}


def getInputMediaAudio(media: str, caption="", thumb="", parse_mode='MarkdownV2', performer="", title="", duration=-1) -> Dict:
    """ Represents an Audio file (GIF or H.264/MPEG-4 AVC video without sound) to be sent.

    Notes:
        For more info -> https://github.com/xSklero/python-telegram-api/wiki/InputMediaAudio

    Args:
        media (str): pass an HTTP URL for Telegram to get a file from the Internet, or pass your local file.
        caption (str, optional): Caption of the Audio to be sent, 0-1024 characters. Defaults to "".
        parse_mode (str, optional): Mode for parsing entities in the Audio caption. Defaults to 'MarkdownV2'.
        thumb (str, optional): Thumbnail of the file sent. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Defaults to "".
        performer (str, optional): Audio performer. Defaults to "".
        title (str, optional): Audio title. Defaults to "".
        duration (int, optional): Audio duration. Defaults to -1.

    Returns:
        Dict: Returns a Audio to be sent.
    """

    return {'type': 'audio', 'media': media, 'caption': caption, 'parse_mode': parse_mode, 'thumb': thumb, 'performer': performer, 'title': title, 'duration': duration}


def getInputMediaDocument(media: str, caption="", parse_mode='MarkdownV2', thumb="") -> Dict:
    """ Represents a Document to be sent.

    Notes:
        For more info -> https://github.com/xSklero/python-telegram-api/wiki/InputMediaDocument

    Args:
        media (str): pass an HTTP URL for Telegram to get a file from the Internet, or pass your local file.
        caption (str, optional): Caption of the Document to be sent, 0-1024 characters. Defaults to "".
        parse_mode (str, optional): Mode for parsing entities in the Document caption. Defaults to 'MarkdownV2'.
        thumb (str, optional): Thumbnail of the file sent. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Defaults to "".
    
    Returns:
        Dict: Returns a Document to be sent with sendMediaGroup.
    """

    return {'type': 'document', 'media': media, 'caption': caption, 'thumb': thumb, 'parse_mode': parse_mode}
