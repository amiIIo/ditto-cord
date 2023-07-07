import hikari
import lightbulb
from ditto import OUTPUT_KEY

plugin = lightbulb.Plugin('Utilities')

@plugin.command
@lightbulb.command('ping', 'Responds with the latency of the app.')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond(f"Pong! My latency was roughly {round(plugin.bot.heartbeat_latency*1000)}ms.")


def load(bot):
    bot.add_plugin(plugin)