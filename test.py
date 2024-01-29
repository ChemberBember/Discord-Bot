# class testClass:
#     def __init__(self, w = 1, x = 2, y = 3, z = 4):
#         self.w = w
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def getClass(self):
#         return "w: " + str(self.w)
# class testChild(testClass):
#     def __init__(self, w, x, y, z):
#         super().__init__(w, x, y, z)
#
# parent = testClass(1, 2, 3, 4)
# child = testChild(10,2,3,4)
#
# print("Класс родитель:")
# print(parent.getClass())
# print("Класс сын:")
# print(child.getClass())


import random

def generate_objects():
    num_objects = random.randint(2, 8)
    objects = random.choices([0, 1], k=num_objects-2)
    objects.append(0)
    objects.append(1)
    random.shuffle(objects)
    count_1 = objects.count(1)
    count_2 = objects.count(0)
    result = {
        'RealBullets': count_1,
        'FakeBullets': count_2,
        'Pool': objects
    }
    return result

# Пример использования
objects = generate_objects()
print(objects)
#
# async def get_emoji(ctx: discord.Interaction):
#     emoji = discord.utils.get(ctx.guild.emojis, name="real")
#     print(emoji)
#     return emoji