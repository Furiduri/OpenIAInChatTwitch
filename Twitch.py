import pdb
import json
import openai
from twitchio.ext import commands

with open('Keys.json') as f:
    secrets = json.load(f)

bot = commands.Bot(
    token= secrets["tokenTwitch"],
    nick=secrets["nickname"],
    prefix='!',
    initial_channels=[secrets["channel"]],    
)

@bot.event
async def event_ready():
    print(f'Ready | {bot.nick}')

@bot.event
async def event_message(message):
    print(message.content)
    await bot.handle_commands(message)

@bot.command(name='test')
async def test_command(ctx):
    await ctx.send(f'Hello {ctx.author.name}!')

@bot.command(name=secrets["comman"], aliases=["comman_alias"])
async def iachat_command(ctx, *args):    
        pregunta = agregar_interrogacion(' '.join(args))
        print(f'Q: {pregunta}')
        resp = get_short_answer(pregunta)
        print(f'A: {resp}')
        await ctx.send(resp)


openai.api_key = secrets["api_key"]

def get_short_answer(question):
    prompt = f'Estamos en el Stream de @{secrets["channel"]}, {secrets["personality"]}: {question}'
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=65,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['text']

def agregar_interrogacion(cadena):
    if not cadena.startswith('¿'):
        cadena = '¿' + cadena
    if not cadena.endswith('?'):
        cadena = cadena + '?'
    return cadena

if __name__ == "__main__":
    bot.run()