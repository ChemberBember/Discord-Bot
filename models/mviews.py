import discord
from discord import ui
from contextlib import suppress
from asyncio import sleep
from models import embeds as emb
from models.models import RouletPlayer


fake = "<:fake:1198074203392458845>"
real = "<:real:1198073427920162837>"


# async def createShotgunGame(ctx: discord.Interaction, player_1, player_2):
#     delete_view = discord.ui.View()
#     delete_btn = discord.ui.Button(style=discord.ButtonStyle.red, label='')
#
#     pl_1 = RouletPlayer(id=player_1, client=ctx.client)
#     pl_2 = RouletPlayer(id=player_2, client=ctx.client)
#
#     async def delete_callback(interaction: discord.Interaction, player_1, player_2):
#         if interaction.user.id == player_1 or interaction.user.id == int(player_2.replace("<@", "").replace(">", "")):
#             await interaction.message.delete()
#             await interaction.channel.send(embeds=emb.Start_4(player_1, player_2), view=await createStartBtn(ctx, pl_1, pl_2))
#
#     delete_btn.callback = lambda i: delete_callback(i, player_1, player_2)
#     delete_view.add_item(delete_btn)
#     return delete_view
#
#
# async def createStartBtn(ctx: discord.Interaction,player_1,player_2):
#     delete_view = discord.ui.View()
#     delete_btn = discord.ui.Button(style=discord.ButtonStyle.red, label='Начать')
#
#     async def delete_callback(interaction: discord.Interaction,player_1,player_2):
#         if interaction.user.id == player_1 or interaction.user.id == int(player_2.replace("<@", "").replace(">", "")):
#             await interaction.message.delete()
#             await interaction.channel.send(embeds=emb.Start_4(player_1,player_2),
#                                            view=await createShotgunGame(ctx, player_1, player_2))
#
#     delete_btn.callback = lambda i: delete_callback(i, player_1, player_2)
#     delete_view.add_item(delete_btn)
#     return delete_view
#
#
# async def createFullUsersBtn(ctx: discord.Interaction,name):
#     delete_view = discord.ui.View()
#     delete_btn = discord.ui.Button(style=discord.ButtonStyle.red, label='Присоедениться')
#
#     async def delete_callback(interaction: discord.Interaction,player_1):
#         await interaction.message.delete()
#         await interaction.channel.send(embeds=emb.Start_3(player_1,interaction.user.mention)
#                                        ,view=await createStartBtn(ctx,interaction.user.id,int(player_1.replace("<@", "").replace(">", ""))))
#
#     delete_btn.callback = lambda i: delete_callback(i, name)
#     delete_view.add_item(delete_btn)
#     return delete_view
#
#
#
#
# async def createDeleteBtn(ctx: discord.Interaction):
#     delete_view = discord.ui.View()
#     delete_btn = discord.ui.Button(style=discord.ButtonStyle.red, label='Присоедениться')
#
#     async def delete_callback(interaction: discord.Interaction):
#         await interaction.message.delete()
#         await interaction.channel.send(embeds=emb.Start_2(interaction.user.mention),view=await createFullUsersBtn(ctx,interaction.user.mention))
#
#     delete_btn.callback = delete_callback
#     delete_view.add_item(delete_btn)
#     return delete_view


def create_button_and_callback(label, callback,style =discord.ButtonStyle.red):
    delete_view = discord.ui.View()
    delete_btn = discord.ui.Button(style=style, label=label)

    delete_btn.callback = callback
    delete_view.add_item(delete_btn)
    return delete_view


async def delete_callback_factory(ctx, player_1, player_2,embed, view):
    async def delete_callback(interaction: discord.Interaction):
        if interaction.user.id == player_1 or interaction.user.id == player_2:
            await interaction.message.delete()
            await interaction.channel.send(embeds=embed,
                                           view=await view(ctx, player_1, player_2))

    return delete_callback


async def createShotgunGame(ctx: discord.Interaction, player_1, player_2):
    delete_view = create_button_and_callback('', await delete_callback_factory(ctx, player_1, player_2, emb.Start_4(player_1.name,player_2.name),view=await createStartBtn(ctx, player_1, player_2)))
    return delete_view


async def createStartBtn(ctx: discord.Interaction, player_1, player_2):
    player_1 = RouletPlayer(id=player_1.user.id, name=player_1.user.mention)
    player_2 = RouletPlayer(id=player_2.user.id, name=player_2.user.mention)
    async def delete_callback(interaction: discord.Interaction, player_1, player_2):

            await interaction.message.delete()
            await interaction.channel.send(embeds=emb.Start_4(player_1, player_2),
                                           view=await createShotgunGame(ctx, player_1, player_2))

    delete_view = create_button_and_callback('Начать', await delete_callback_factory(ctx, player_1, player_2, emb.Start_4(player_1.name,player_2.name),view=await createShotgunGame(ctx, player_1, player_2)))

    return delete_view


async def createFullUsersBtn(ctx: discord.Interaction, name):
    async def delete_callback(interaction: discord.Interaction):
        await interaction.message.delete()
        await interaction.channel.send(embeds=emb.Start_3(name.user.mention, interaction.user.mention),
                                       view=await createStartBtn(ctx, interaction,
                                                                 name))

    delete_view = create_button_and_callback('Присоедениться', delete_callback)
    return delete_view


async def createDeleteBtn(ctx: discord.Interaction):
    async def delete_callback(interaction: discord.Interaction):
        await interaction.message.delete()
        await interaction.channel.send(embeds=emb.Start_2(interaction.user.mention),
                                       view=await createFullUsersBtn(ctx, interaction))

    delete_view = create_button_and_callback('Присоедениться', delete_callback)
    return delete_view
