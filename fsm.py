import random

from transitions.extensions import GraphMachine

from utils import send_text_message, is_mami, compare, is_kazuya, is_command, send_image_message, send_button_message

from linebot.models import MessageTemplateAction

love_name = "mami"


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    # love_consultant
    def is_going_to_love_consultant(self, event):
        text = event.message.text
        return text == "戀愛相談"

    def on_enter_love_consultant(self, event):
        print("I'm entering love_consultant")
        reply_token = event.reply_token
        send_text_message(reply_token,
                          "こんにちわ~マミちゃんですっヾ(〃^∇^)ﾉ\n好きな人の名前を入力してください。\n您好！我是Mami！\n請輸入心儀對象的姓名：")

    # idle
    def is_going_to_idle(self, event):
        text = event.message.text
        if is_command(text):
            return False
        return True

    def on_enter_idle(self, event):
        print("I'm entering idle")

        reply_token = event.reply_token
        num = random.randint(1, 5)
        if num == 2:
            send_image_message(reply_token, "https://i.imgur.com/GctntXv.jpg")
        elif num == 3:
            send_image_message(reply_token, "https://i.imgur.com/hHJHXDI.jpg")
        elif num == 4:
            send_image_message(reply_token, "https://i.imgur.com/uAQQ1ab.jpg")
        elif num == 1:
            send_image_message(reply_token, "https://i.imgur.com/9miZbSs.jpg")
        elif num == 5:
            send_image_message(reply_token, "https://i.imgur.com/3bk1GCr.jpg")
        self.go_back()

    # mad
    def is_going_to_mad(self, event):
        text = event.message.text
        return is_kazuya(text)

    def on_enter_mad(self, event):
        print("I'm entering mad")
        url1 = 'https://i.imgur.com/23fugco.jpg'
        url2 = 'https://i.imgur.com/7rMai9B.jpg'
        url3 = 'https://i.imgur.com/3LFHMAL.jpg'
        reply_token = event.reply_token
        num = random.randint(1, 4)
        if num == 1:
            send_text_message(reply_token, "幹X娘和也這個廢物的怎麼才剛被我甩掉就有新歡我肏他X的咧")
        elif num == 2:
            send_image_message(reply_token, url1)
        elif num == 3:
            send_image_message(reply_token, url2)
        elif num == 4:
            send_image_message(reply_token, url3)
        self.go_back()

    # acquire_name
    def is_going_to_acquire_name(self, event):
        text = event.message.text
        global love_name
        love_name = '' + text
        if is_mami(text) or is_kazuya(text):
            return False
        return True

    def on_enter_acquire_name(self, event):
        print("I'm entering acquire_name")
        angel = 'https://i.imgur.com/1sKHooH.png'
        urusai = 'https://i.imgur.com/EvJOMq2.jpg'
        g8 = 'https://i.imgur.com/F5C3eQt.png'
        simple = 'https://i.imgur.com/1HAb14C.jpg'
        myfault = 'https://i.imgur.com/uAQQ1ab.jpg'
        trash = 'https://i.imgur.com/MZwLZHd.png'
        url = angel
        reply_token = event.reply_token
        num1 = compare(event.source.user_id, love_name)
        if num1 == 0:
            url = trash
            mess = "您與心上人的匹配度是：" + str(
                num1) + "%，強烈建議您趕緊轉換目標，免得受到太大的打擊喲^_^"
        elif 0 < num1 <= 20:
            url = g8
            mess = "您與心上人的匹配度是：" + str(num1) + "%，建議您趕緊下船，免得迷失在茫茫大海中喲^_^！"
        elif 20 < num1 <= 40:
            url = simple
            mess = "您與心上人的匹配度是：" + str(num1) + "%，處於不高的數值，建議您試探一下對方的喜好，抓住對方的好感喲！"
        elif 40 < num1 <= 60:
            url = 'https://i.imgur.com/EDIvEcB.jpg'
            mess = "您與心上人的匹配度是：" + str(num1) + "%，可喜可賀！"
        elif 60 < num1 <= 80:
            url = 'https://i.imgur.com/x6qWg2A.jpg'
            mess = "您與心上人的匹配度是：" + str(num1) + "%，說不定稍微注意一下自身的形象，就能夠勾住對方的心囉！"
        elif 80 < num1 < 100:
            mess = "您與心上人的匹配度是：" + str(num1) + "%，看來您需要鼓起勇氣，踏出最勇敢的那一步囉*\\^0^/*！"
        else:
            url = urusai
            mess = "您與心上人的匹配度是：" + str(num1) + "%，給我原地結婚。"
        btn = [
            MessageTemplateAction(
                label='再試一次',
                text='戀愛相談'
            ),
        ]
        send_button_message(reply_token, '結果出爐啦！', mess, btn, url)
        self.go_back()

    def is_going_to_pride(self, event):
        text = event.message.text
        return is_mami(text)

    def on_enter_pride(self, event):
        print("I'm entering pride")
        reply_token = event.reply_token
        num = random.randint(1, 2)
        if num == 1:
            send_text_message(reply_token, "啊咧？可是我現在不想交男朋友耶 凸^_^凸")
        elif num == 2:
            send_image_message(reply_token, 'https://i.imgur.com/6C6V5fT.jpg')
        self.go_back()

    def is_going_to_help(self, event):
        text = event.message.text
        return text.lower() == "help"

    def on_enter_help(self, event):
        print("I'm entering idle")
        reply_token = event.reply_token
        send_text_message(reply_token,
                      "こんにちわ~マミちゃんですっヾ(〃^∇^)ﾉ\n您好！我是Mami！\n輸入「戀愛相談」，我會為您做戀愛匹配度分析喲～")
        self.go_back()