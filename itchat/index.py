# -*- coding = utf-8 -*-

import itchat, time, re
from itchat.content import *

str1 = u"小灰兔祝您：鸡年大吉！"
str2 = u"怡然我爱你！"
str3 = u"我还是只小灰兔，只能回复文字哦！"
str_els = u"我想你了"

kw1 = u"年"
kw2 = u"爱"

@itchat.msg_register([TEXT])
def text_reply(msg):
	if re.search(kw1, msg['Text']):
		itchat.send(str1, msg['FromUserName'])
	elif re.search(kw2, msg['Text']):
		itchat.send(str2, msg['FromUserName'])
	else:
		itchat.send(str_els, msg['FromUserName'])

@itchat.msg_register([PICTURE, RECORDING, VIDEO, SHARING])
def other_reply(msg):
    itchat.send(str3, msg['FromUserName'])

itchat.auto_login(enableCmdQR=True,hotReload=True)
itchat.run()