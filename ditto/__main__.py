import os
import hikari
import lightbulb
from ditto import DEV_GUILD, OUTPUT_KEY

with open("./secrets/token") as f:
    _token = f.read().strip()

bot = lightbulb.BotApp(
    token = _token,
    prefix = ">",
    intents = hikari.Intents.ALL,
    default_enabled_guilds = DEV_GUILD,
    case_insensitive_prefix_commands = True
)

bot.load_extensions_from("./ditto/extensions")

if __name__ == "__main__":
    if os.name != "nt":
        import uvloop
        uvloop.install()
    
    bot.run(
        activity = hikari.Activity(
            name = "for commands!",
            type = hikari.ActivityType.WATCHING,
        )
    )