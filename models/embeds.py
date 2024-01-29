import discord
import datetime

def createEmbed(title=None, description=None, url=None, timestamp=datetime.datetime.utcnow(), author=None,
                thumbnail=None, fields=None, footer=None, thumbnail_url=None):
    embed = discord.Embed()
    if title:
        embed.title = title
    if description:
        embed.description = description
    if url:
        embed.url = url
    if timestamp:
        embed.timestamp = timestamp
    if author:
        embed.set_author(name=author)
    if thumbnail:
        embed.set_thumbnail(url=thumbnail)
    if fields:
        for field in fields:
            embed.add_field(name=field[0], value=field[1], inline=field[2])
    if footer:
        embed.set_footer(text=footer)
    return embed


embed = discord.Embed(
    title="Заголовок",
    description="Описание",
    color=discord.Color.blue(),
    url="https://example.com",
    timestamp=datetime.datetime.utcnow()
)

embed.set_author(
    name="Автор",
    url="https://author.com",
    icon_url="https://author.com/icon.png"
)

embed.set_thumbnail(
    url="https://thumbnail.com/image.png"
)

embed.add_field(
    name="Поле 1",
    value="Значение 1",
    inline=True
)

embed.add_field(
    name="Поле 2",
    value="Значение 2",
    inline=True
)

embed.add_field(
    name="Поле 3",
    value="Значение 3",
    inline=False
)

embed.set_image(
    url="https://image.com/image.png"
)

embed.set_footer(
    text="Футер",
    icon_url="https://footer.com/icon.png"
)


"""Roulette Game"""

class RouleJoinView(discord.ui.View):

    @discord.ui.button(label="Присоединиться", style=discord.ButtonStyle.green)
    async def join(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message(f"Вы присоединились к рулетке", ephemeral=True)
        self.stop()


Start_img = discord.Embed(title="",colour=3092790)
Start_img.set_image(url="https://discord.com/channels/400665156645945366/847784554764173342/1198019475023331420")
Start = discord.Embed(color=discord.Color.blue(),timestamp=datetime.datetime.utcnow())
Start.title = "Roulette Game"
Start.description = "Ожидание..."
Start.add_field(name = "Игрок_1", value= "Player_Name")
Start.add_field(name = "Игрок_2", value= "Player_Name")

def Start_1():
    test_1 = discord.Embed(title=" ", colour=3092790)
    test_1.set_image(url="https://cdn.discordapp.com/attachments/847784554764173342/1198032100373299270/-2.png?ex"
                         "=65bd6d57&is=65aaf857&hm=79189adfa14b5eb9f8d02cc5e0c0b5ab0cf21e6e4c3efe1490cc88e29005fee0&")

    test_2 = discord.Embed(title="**Участники:**",
                           color=3092790,
                           timestamp=datetime.datetime.utcnow())

    test_2.add_field(name="Игрок_1", value=f"Player_Name")
    test_2.add_field(name="Игрок_2", value="Player_Name")
    test_2.set_image(url="https://media.discordapp.net/attachments/924638898250985502/932813824703229992/1111.png?ex"
                         "=65b85592&is=65a5e092&hm=0304e8f267061566d46c7bc34de4fd535686bd4d322efe0e1e5b8de74390aa31&")
    return [test_1,test_2]


def Start_2(name):
    test_1 = discord.Embed(title=" ", colour=3092790)
    test_1.set_image(url="https://cdn.discordapp.com/attachments/847784554764173342/1198032100373299270/-2.png?ex"
                         "=65bd6d57&is=65aaf857&hm=79189adfa14b5eb9f8d02cc5e0c0b5ab0cf21e6e4c3efe1490cc88e29005fee0&")

    test_2 = discord.Embed(title="**Участники:**",
                           color=3092790,
                           timestamp=datetime.datetime.utcnow())

    test_2.add_field(name="Игрок_1", value=f"{name}")
    test_2.add_field(name="Игрок_2", value="Player_Name")
    test_2.set_image(url="https://media.discordapp.net/attachments/924638898250985502/932813824703229992/1111.png?ex"
                         "=65b85592&is=65a5e092&hm=0304e8f267061566d46c7bc34de4fd535686bd4d322efe0e1e5b8de74390aa31&")
    return [test_1,test_2]

def Start_3(Player_1,Player_2):
    test_1 = discord.Embed(title=" ", colour=3092790)
    test_1.set_image(url="https://cdn.discordapp.com/attachments/847784554764173342/1198032100373299270/-2.png?ex"
                         "=65bd6d57&is=65aaf857&hm=79189adfa14b5eb9f8d02cc5e0c0b5ab0cf21e6e4c3efe1490cc88e29005fee0&")

    test_2 = discord.Embed(title="**Участники:**",
                           color=3092790,
                           timestamp=datetime.datetime.utcnow())

    test_2.add_field(name="Игрок_1", value=f"{Player_1}")
    test_2.add_field(name="Игрок_2", value=f"{Player_2}")

    test_2.set_image(url="https://media.discordapp.net/attachments/924638898250985502/932813824703229992/1111.png?ex"
                         "=65b85592&is=65a5e092&hm=0304e8f267061566d46c7bc34de4fd535686bd4d322efe0e1e5b8de74390aa31&")
    return [test_1, test_2]


def Start_4(Player_1,Player_2):
    test_1 = discord.Embed(title=" ", colour=3092790)
    test_1.set_image(url="https://cdn.discordapp.com/attachments/847784554764173342/1198032100373299270/-2.png?ex"
                         "=65bd6d57&is=65aaf857&hm=79189adfa14b5eb9f8d02cc5e0c0b5ab0cf21e6e4c3efe1490cc88e29005fee0&")

    test_2 = discord.Embed(title="**Участники:**",
                           color=3092790,
                           timestamp=datetime.datetime.utcnow())

    test_2.add_field(name="Игрок_1", value=f"{Player_1}")
    test_2.add_field(name="Игрок_2", value=f"{Player_2}")

    test_2.set_image(url="https://media.discordapp.net/attachments/924638898250985502/932813824703229992/1111.png?ex"
                         "=65b85592&is=65a5e092&hm=0304e8f267061566d46c7bc34de4fd535686bd4d322efe0e1e5b8de74390aa31&")
    return [test_1, test_2]

def Start_5(Player_1,Player_2):
    test_1 = discord.Embed(title=" ", colour=3092790)
    test_1.set_image(url="https://cdn.discordapp.com/attachments/847784554764173342/1198032100373299270/-2.png?ex"
                         "=65bd6d57&is=65aaf857&hm=79189adfa14b5eb9f8d02cc5e0c0b5ab0cf21e6e4c3efe1490cc88e29005fee0&")

    test_2 = discord.Embed(title="**Участники:**",
                           color=3092790,
                           timestamp=datetime.datetime.utcnow())



    test_2.set_image(url="https://media.discordapp.net/attachments/924638898250985502/932813824703229992/1111.png?ex"
                         "=65b85592&is=65a5e092&hm=0304e8f")

