import random

from transitions.extensions import GraphMachine

from utils import send_text_message, is_mami, compare, is_kazuya, is_command, send_image_message, send_button_message

from linebot.models import MessageTemplateAction

from picture import get_pic

love_name = "mami"

user_gender = "男"
request_url = ""
last_com = "戀愛相談"

#male_pic = get_pic("男")
#female_pic = get_pic("女")


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    # love_consultant
    def is_going_to_love_consultant(self, event):
        text = event.message.text
        return text == "戀愛相談"

    def on_enter_love_consultant(self, event):
        print("I'm entering love_consultant")
        global last_com
        last_com = "戀愛相談"
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
            send_image_message(reply_token, "https://i.imgur.com/iPQLCJ1.png")
        elif num == 4:
            send_image_message(reply_token, "https://i.imgur.com/3bk1GCr.jpg")
        elif num == 1:
            send_image_message(reply_token, "https://i.imgur.com/9miZbSs.jpg")
        elif num == 5:
            send_text_message(reply_token, "這是我的角色曲呦～\nhttps://youtu.be/ZAC0smU1SnU")
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

    # analyze
    def is_going_to_analyze(self, event):
        text = event.message.text
        global love_name
        love_name = '' + text
        if is_mami(text) or is_kazuya(text):
            return False
        return True

    def on_enter_analyze(self, event):
        print("I'm entering analyze")
        angel = 'https://i.imgur.com/1sKHooH.png'
        urusai = 'https://i.imgur.com/EvJOMq2.jpg'
        g8 = 'https://i.imgur.com/F5C3eQt.png'
        simple = 'https://i.imgur.com/1HAb14C.jpg'
        myfault = 'https://i.imgur.com/uAQQ1ab.jpg'
        trash = 'https://i.imgur.com/MZwLZHd.png'
        url = angel
        reply_token = event.reply_token
        global last_com
        global love_name
        if last_com == "戀人配對":
            num1 = compare(event.source.user_id, request_url)
        else:
            num1 = compare(event.source.user_id, love_name)
        if num1 == 0:
            url = myfault
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
        if last_com == "戀人配對":
            btn = [
                MessageTemplateAction(
                    label='再試一次',
                    text=last_com
                ),
                MessageTemplateAction(
                    label='獲取圖片',
                    text='獲取圖片'
                ),
            ]
            send_button_message(reply_token, '結果出爐啦！', mess, btn, url)
        else:
            btn = [
                MessageTemplateAction(
                    label='再試一次',
                    text=last_com
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
            # send_image_message(reply_token, get_pic("男"))
        self.go_back()

    def is_going_to_help(self, event):
        text = event.message.text
        return text.lower() == "help"

    def on_enter_help(self, event):
        print("I'm entering help")
        reply_token = event.reply_token
        mess = "輸入「戀愛相談」，我會為您做戀愛匹配度分析喲～"+"\n輸入「戀人配對」，我會為幫您找對象，並且回傳照片給您喔！"
        btn = [
            MessageTemplateAction(
                label='戀愛相談',
                text='戀愛相談'
            ),
            MessageTemplateAction(
                label='戀人配對',
                text='戀人配對'
            ),
        ]
        send_button_message(reply_token, '需要幫忙嗎？', mess, btn, "https://i.imgur.com/hHJHXDI.jpg")
        self.go_back()

    def is_going_to_pair(self, event):
        text = event.message.text
        return text == "戀人配對"

    def on_enter_pair(self, event):
        print("I'm entering pair")
        global last_com
        last_com = "戀人配對"
        reply_token = event.reply_token
        btn = [
            MessageTemplateAction(
                label='男',
                text='男'
            ),
            MessageTemplateAction(
                label='女',
                text='女'
            ),
        ]
        mess = "記得要選生理性別呦<3"
        send_button_message(reply_token, '請選擇您的性別！', mess, btn, "https://i.imgur.com/jq59nLS.jpg")

    def is_going_to_gender(self, event):
        text = event.message.text
        global user_gender
        user_gender = text
        return not is_command(text) and text != "獲取圖片" and text != "匹配度分析"

    def on_enter_gender(self, event):
        print("I'm entering gender")
        global user_gender
        global request_url
        reply_token = event.reply_token
        if user_gender != "男" and user_gender != "女" and is_kazuya(user_gender) == False:
            send_text_message(reply_token, "請輸入正確的指令凸^_^凸")
            self.go_back()
        else:
            btn = [
                MessageTemplateAction(
                    label='匹配度分析',
                    text='匹配度分析'
                ),
                MessageTemplateAction(
                    label='再試一次',
                    text=user_gender
                ),
                MessageTemplateAction(
                    label='獲取圖片',
                    text='獲取圖片'
                ),
            ]
            mess = "以下是為您精挑細選的對象！請選擇您的下一步^_^"
            request_url = get_pic(user_gender)
            print(love_name)
            send_button_message(reply_token, '結果出爐啦！', mess, btn, request_url)

    def is_going_to_get_pic(self, event):
        text = event.message.text
        return text == "獲取圖片" and last_com == "戀人配對"

    def on_enter_get_pic(self, event):
        print("I'm entering get_pic")
        reply_token = event.reply_token
        global request_url
        send_image_message(reply_token, request_url)
        self.go_back()
