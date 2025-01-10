import discord
import speech_recognition as speech_recog
from discord.ext import commands
import requests
import os
import webserver
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='S/', intents=intents)
def speech_es():
    mic = speech_recog.Microphone()
    recog = speech_recog.Recognizer()
    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)
        return recog.recognize_google(audio, language="es-ES")
@bot.command()
async def recognize(ctx):
    try:
        result = speech_es()
        await ctx.send(f'Recognized speech: {result}')
    except Exception as e:
        await ctx.send(f'Error: {e}')
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 1000):
    await ctx.send("he" * count_heh)
@bot.command()
async def poke(ctx,arg):
    try:
        pokemon = arg.split(" ",1)[0].lower()
        result = requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon)
        if result.text == "Not Found":
            await ctx.send("Pokemon no encontrado")
        else:
            image_url = result.json()["sprites"]["front_default"]
            print(image_url)
            await ctx.send(image_url)

    except Exception as e:
        print("Error:", e)
@poke.error
async def error_type(ctx,error):
    if isinstance(error,commands.errors.MissingRequiredArgument):
        await ctx.send("Tienes que darme un pokemon")
bot.command()
async def ayudame_en_un_nivel_porfi(ctx):
    await ctx.send("en qué nivel te ayudo, ayudo hasta easy demons, solo ponme 'S/gdnivel y su nombre' tendría que mejorar para más dificiles yo te aviso")
@bot.command()
async def gdnivel(ctx):
    await ctx.send("""1er paso: utiliza un truco que yo uso que lo llaman 'Npesta's trick' 
                   que consiste en vencer el nivel en modo práctica y vas eliminando checkpoints conforme los pasas
                   2do paso: acuérdate del nivel y los clicks que debes hacer juégalo en modo normal y así vas consiguiendo progreso
                   hasta pasártelo
                   3er paso: recuerda que a veces los checkpoints te trollean y no te dejan avanzar, así que eliminalo
                   Último paso: utilíza el truco para otros niveles y sigue progresando, si no te funciona juega niveles más fáciles y ve siendo más pro)   """)
@bot.command()
async def limpiar(ctx):
    await ctx.channel.purge()
    await ctx.send("Mensajes eliminados", delete_after = 3)
@bot.command()
async def hardest(ctx):
    await ctx.send("mi hardest actual es bicycle, by back, pero si quieres jugarlo, te dejo la ID: 120432, espera a un futuro para más dificiles")
@bot.command()
async def verificar(ctx):
    await ctx.send("ah, quieres saber qué nivel estoy verificando, eh, es el nivel: cant let buff, un nivel que buffea cant let go, cuando lo complete, te daré su id ¡estate atento!")

webserver.keep_alive()
bot.run(DISCORD_TOKEN)




 
