import hikari
import lightbulb
from ditto import OUTPUT_KEY

plugin = lightbulb.Plugin('Events')

@plugin.listener(hikari.StartedEvent)
async def on_started(event: hikari.StartedEvent):
    bot = plugin.app
    print(f"----\nditto-cord is running.\nCLIENT-ID: 1126714035782557769\n----")
    stdout = await bot.rest.fetch_channel(OUTPUT_KEY)

@plugin.listener(lightbulb.CommandErrorEvent)
async def on_error(event: lightbulb.CommandErrorEvent) -> None:
    if isinstance(event.exception, lightbulb.CommandInvocationError):
        await event.context.respond(f"Yikes! Something weird happened when you tried to use `{event.context.command.name}`.")
        raise event.exception

    exception = event.exception.__cause__ or event.exception

    if isinstance(exception, lightbulb.NotOwner):
        await event.context.respond("Whoops! Only the developer is authorized to use the command.")
    elif isinstance(exception, lightbulb.CommandIsOnCooldown):
        await event.context.respond(f"Woah! This command is on cooldown. Retry in `{exception.retry_after:.2f}` seconds.")
    else:
        raise exception
    
def load(bot):
    bot.add_plugin(plugin)