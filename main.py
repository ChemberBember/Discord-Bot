import discord
from discord import app_commands, Intents, Client
from discord.ext import tasks , commands
from itertools import cycle
from models.embeds import embed, createEmbed , Start
from models.models import CreateUser, User
from asyncio import sleep
import models.embeds as emb
import models.mviews as vw


class BackRooms(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        await self.tree.sync()


bot = BackRooms(intents=discord.Intents.all())

status = cycle(['Жаждит служить',
                'Чего желает мой повелитель?',
                'Склоняется перед вашей волей',
                'Да свершится предначертаное',
                'Тьфу...Опять капюшен сполз на глаза',
                '{Another acolytes phrase}',
                'Хотите узнать секрет вечного счастья?\n'
                'Откройте страницу 2.46'])

@tasks.loop(hours = 1)
async def change_status():
    await  bot.change_presence(activity=discord.Game(next(status)))

@bot.event
async def on_ready():
    change_status.start()
    print("Я жажду служить...")


async def addToBackrooms(ctx,*members: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Backrooms")
    for member in members:
        await member.add_roles(role)

@bot.tree.command (name="start", description="...")
async def start(ctx,name:str):
    user = CreateUser(name,ctx.user.id)
    if user.dead == False:
        status = 'Жив'
    else:
        status = 'Мертв'
    await ctx.response.send_message(embed=createEmbed(title=f"**{name}**\n**Статус:** {status}"
                                                      ,description=f"Хар-ки вашего персонажа:"
                                                      ,thumbnail=ctx.user.avatar))
def test_12(lst):
    for el in lst:
        return el


@bot.tree.command(name="clear")
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)


@bot.tree.command(name='test',description="...")
async def test(ctx: discord.Interaction):
    await ctx.response.send_message(embeds=emb.Start_1(),view=await vw.createDeleteBtn(ctx))

@bot.tree.command(name='talk',description="???")
async def talk(ctx,title: str,description:str,img:str):
    talk_E = discord.Embed(title=f"{title}",description=f"{description}", color=0x00ff00)
    if img != '-':
        talk_E.set_thumbnail(url=img)

    await ctx.response.send_message(embed=talk_E)

# @bot.tree.command(name='loot',description="???")
# async def spawnLoot(ctx,*tems):
#     lootEmbed = createEmbed(title="Вам выпало:",description=" ".join(items))
#     await ctx.response.send_message(embed=lootEmbed)
#

# @bot.tree.command()
# async def shotgun(ctx):
#
#


@bot.tree.command(name='roulette',description="...")
async def roulette(ctx):
    await ctx.response.send_message(embed=Start)
bot.run('MTA2Mjg2NTI5MDI3MjE5MDYxNQ.GST3ST.Yw2aLchPbSrRt7-NMNqT6jyu4GXMeluUVdyRmI')
