import hikari
import lightbulb
from lightbulb.utils import pag, nav
from datetime import datetime as dt
from datetime import timezone
import time

plugin = lightbulb.Plugin('Moderation')

@plugin.command
@lightbulb.add_checks(lightbulb.has_role_permissions)


def load(bot):
    bot.add_plugin(plugin)