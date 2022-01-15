from qmotor import QBot, WSCtx
from qmotor.message import FriendMessage, GroupMessage, AtMeCmdMsg, FriendMsg
from qmotor.message.builder import ChatBubble, face, text, dice, SendMsgBuilder
from random import randint

bot = QBot("ws://192.168.2.247:8080", 123, "tomcat")


@bot.handler(AtMeCmdMsg, me_qq=123, cmd=["测试命令"])
async def setu_cmd(ctx: WSCtx):
    msg = GroupMessage(ctx.msg)
    await ctx.ws.send_msg(SendMsgBuilder(receiver=msg.group_qq()).msg("asdf").build())


@bot.handler(FriendMsg)
async def reply(ctx: WSCtx):
    msg = FriendMessage(ctx.msg)
    await ctx.ws.send_friend(
        msg.friend_qq(), ChatBubble(text(f"hello {randint(1,100)}"), face.JI_DONG)
    )


@bot.handler(AtMeCmdMsg, me_qq=123, cmd=["比大小"])
async def dice_game(ctx: WSCtx):
    msg = GroupMessage(ctx.msg)
    await ctx.ws.send_group(
        msg.group_qq(),
        [
            ChatBubble(
                text("来比比谁的点数大吧"),
                face.DA_XIAO,
            ),
            dice(randint(1, 6)),
        ],
    )


bot.run()
