import os
import re
from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


def send_image_message(reply_token, url):
    line_bot_api = LineBotApi(
        'ulHXhTUhvVRiyWI1RptU4vXRvsCGAM/xbIjXuiswUaFx/H66XkoQCEBKOkpESnCD8qpgwIQu590JUA4GhcLQ1B65a4nHD4a770LZB9VqluslKKR8OpPZR9Nn4yweNqz2a+CzaP81CBfjK/ny+QZ4VAdB04t89/1O/w1cDnyilFU=')
    message = ImageSendMessage(
        original_content_url=url,
        preview_image_url=url
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"


def cjk_cleaner(string):
    # Keep CJS Characters, Latin Letters and Digits (listed above)
    filters = re.compile(
        u'[^0-9a-zA-Z\u0083\u008a\u008c\u008e\u009a\u009c\u009e\u009f\u00c0-\u00d6\u00d8-\u00f6\u00f8-\u00ff\u0100-\u017f\u4e00-\u9fff\u3040-\u309f\u30a0-\u30ff\u3130-\u318f\uff00-\uffef]+',
        re.UNICODE)
    return filters.sub('', string)


def is_mami(text):
    if text.lower() == "mami" or text == "七海麻美" or text == "麻美" or text.lower() == "nanami mami" or text == "ななみまみ" or text == "まみ" or text == "ナナミマミ" or text == "マミ" or text == "你" or text == "妳":
        return True
    return False


def is_kazuya(text):
    if text.lower() == "kazuya" or text == "木之下和也" or text == "和也":
        return True
    return False


def compare(uid, love_name):
    print(uid)
    numm = 0
    for i in range(len(uid)):
        numm = numm + ord(uid[i])
    num = love_name
    num = num.replace('\'', "")
    num = num.replace('\\', "")
    res = 0
    num = cjk_cleaner(num)
    for i in range(len(num)):
        c = "" + str(num[i])
        if c.isalpha() or c.isnumeric():
            res = res + ord(num[i])
    res = res * numm
    res = res % 101
    print(res)
    return res


def is_command(text):
    if text == "戀愛相談" or is_kazuya(text) or text.lower() == "help":
        return True
    return False


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
