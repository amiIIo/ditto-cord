import hikari
import lightbulb
from lightbulb.utils import pag, nav
from datetime import datetime as dt
from datetime import timezone
import time

plugin = lightbulb.Plugin('Utilities')

@plugin.command
@lightbulb.add_cooldown(3, 1, lightbulb.UserBucket)
@lightbulb.command('ping', 'Responds with the latency of the app.')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond(hikari.ResponseType.DEFERRED_MESSAGE_CREATE, flags=hikari.MessageFlag.EPHEMERAL)
    embed = hikari.Embed(
        title = "Pong!",
        description = f"My latency is roughly {round(plugin.bot.heartbeat_latency*1000)}ms.",
        color = 0x42bce8,
        timestamp = dt.now(timezone.utc)
    )
    embed.set_footer("ditto-cord")
    await ctx.respond(embed=embed)

@plugin.command
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.add_cooldown(5, 1, lightbulb.UserBucket)
@lightbulb.command('close', 'Close the connection to discord.')
@lightbulb.implements(lightbulb.SlashCommand)
async def close(ctx):
    await ctx.respond(hikari.ResponseType.DEFERRED_MESSAGE_CREATE, flags=hikari.MessageFlag.EPHEMERAL)
    embed = hikari.Embed(
        title = "Goodbye!",
        description = "Closing the connection to discord.",
        color = 0x42bce8,
        timestamp = dt.now(timezone.utc)
    )
    embed.set_footer("ditto-cord")
    await ctx.respond(embed=embed)
    quit()

@plugin.command
@lightbulb.add_cooldown(5, 1, lightbulb.UserBucket)
@lightbulb.option("role", "Role to gather members from.", hikari.Role, required = True)
@lightbulb.command('members', 'List all members within a role.')
@lightbulb.implements(lightbulb.SlashCommand)
async def members(ctx):
    await ctx.respond(hikari.ResponseType.DEFERRED_MESSAGE_CREATE, flags=hikari.MessageFlag.EPHEMERAL)
    
    role = ctx.options.role
    members = [member for member in ctx.get_guild().get_members().values() if role in member.get_roles()]
    embeds = []
    fields = 0

    current = hikari.Embed(
        title = f'Members in {role}',
        description = f"`{len(members)} members total.`",
        color = 0x42bce8,
        timestamp = dt.now(timezone.utc)
    )
    current.set_footer("ditto-cord")

    for member in members:
        fields += 1
        if fields == 25:
            embeds.append(current)
            current = hikari.Embed(
                title = f'Members in {role}',
                description = f"`{len(members)} members total.`",
                color = 0x42bce8,
                timestamp = dt.now(timezone.utc)
            )
            current.set_footer("ditto-cord")
            fields = 0
            continue
        current.add_field(name=f'{member.get_top_role()}', value=f'`Member:` {member.user.mention} \n `Username:` {member.username}', inline = True)

    if not embeds:
        if not current.fields:
            embed = hikari.Embed(
                title = 'No members found',
                description = f"No members were found in {role}.",
                color = 0x42bce8,
                timestamp = dt.now(timezone.utc)
            )
            embed.set_footer("ditto-cord")
            await ctx.respond(embed=embed)
            return
        embeds.append(current)

    navigator = nav.ButtonNavigator(embeds)
    await navigator.run(ctx)

def load(bot):
    bot.add_plugin(plugin)