#  👨‍💻 Como usar
Se requiere installar Python en tu computadora, descargalo del sigiente link
https://www.python.org/downloads/

## 👨‍💻 Configuracion de Api GPT
En el archivo Keys.json, debes modificar los sigiente, tu Key de OpenAI:

    "api_key" = "sk-********"

obtenla en https://platform.openai.com/account/api-keys

## 👨‍💻 Configuracion API Twitch
En el archivo Key.json, debes modificar lo siguientes datos: 

Tu nombre de usuario de la cuanta que usara la IA

    "nickname": ""

El token que obtienes usando la cuenta con la que respondera la IA, se obtine en:
 https://twitchapps.com/tmi/

    "tokenTwitch": "oauth:***"

El canal en el que escuhara el chat

    "channel": "Tu canal"

## 🤖 Como inicar
Abre una consola de comandos `cmd`, y escribe lo sigueinte:

    python.exe .\Twitch.py

`!!!No debes cerrar la consola de comandos mienstras el bot esta activo, si la cierras no funcionara el bot.!!!`

Usa en tu chat el comando `!test` para verificar que el bot lee el chat.

Usa `!sillaUwU` o `!UwU`, segido una pregunta, para que te responda la IA.

Para salir oprime `CTRL + C` o cierra la consola de comandos.

## ⭐ Personalizacion
Cambia la parsonalidad de la IA indicandocela en el archivo Key.js, en la propiedad `personality`

Cambia el comando a usar en la propiedad `comman`, y sus distintas variaciones en `comman_alias` (cada una entre comillas dobles y separadas por coma `["uwu","UwU"]`)

### 📝 Notas
Los mensajes siguientes son comunes, y se deben ignorar:

Mensaje ocasionado por la API de OpenIA, no encontrado la manera de evitarlo, pero no presenta problemas para el funcionamiento: 

    ****** MESSAGE_RE Failed! ******

Mensaje mostrado cuando se usa un comando que no existe.

    Ignoring exception in command: No command "a" was found.:
    twitchio.ext.commands.errors.CommandNotFound: No command "a" was found