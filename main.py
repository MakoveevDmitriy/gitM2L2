

@bot.command()
async def ekologia(ctx):
    images = os.listdir('ekologia')

    img_name = random.choice(images)

    with open(f'ekologia/{img_name}', 'rb') as f:
            picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)



@bot.command()
async def musor(ctx):
    await ctx.send("Привет!!!Ты хочешь помочь планете в плане экологии? Молодец! Ты можешь помочь утилизируя отходы, не покупая лишнее, переходя на естественную энергию, экономя воду.")

    images = os.listdir('ekologia')

    img_name = random.choice(images)

    with open(f'ekologia/{img_name}', 'rb') as f:
            picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

