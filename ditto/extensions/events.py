import hikari
import lightbulb
from ditto import OUTPUT_KEY

plugin = lightbulb.Plugin('Events')

@plugin.listener(hikari.StartedEvent)
async def on_started(event: hikari.StartedEvent):
    bot = plugin.app
    print(f"----\nditto-cord is running.\nCLIENT-ID: 1126714035782557769\n----")
    stdout = await bot.rest.fetch_channel(OUTPUT_KEY)
    await stdout.send("I'm awake! How can I assist you?")

def load(bot):
    bot.add_plugin(plugin)