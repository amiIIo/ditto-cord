import hikari
import lightbulb
from ditto import OUTPUT_KEY

plugin = lightbulb.Plugin('Utilities')

@plugin.command
@lightbulb.add_cooldown(3, 1, lightbulb.UserBucket)
@lightbulb.command('ping', 'Responds with the latency of the app.')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond(f"Pong! My latency was roughly {round(plugin.bot.heartbeat_latency*1000)}ms.")

@plugin.command
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.add_cooldown(5, 1, lightbulb.UserBucket)
@lightbulb.command('close', 'Close the connection to discord.')
@lightbulb.implements(lightbulb.SlashCommand)
async def close(ctx):
    await ctx.respond("Closing the connection. - Ditto")
    quit()

def load(bot):
    bot.add_plugin(plugin)