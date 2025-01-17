import discord
from discord.ext import commands

from math import ceil, sqrt

from core.log import log
import core.nomic_time as nomic_time
import config.config as config


class Cycle(commands.Cog, name='Current Cycle'):
    '''
    Commands related to the current Cycle of Infinite Nomic.
    '''

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        brief='Get information about the time relevant to the current Cycle',
        help=('Get current time and day in UTC, as well asn any relevant '
              'information regarding time in the current Cycle')
    )
    async def time(self, ctx):
        try:
            await ctx.send(nomic_time.get_current_utc_string())
        except Exception as e:
            log.exception(e)
            await ctx.send(config.GENERIC_ERROR)

    @commands.command(
        brief='Calculate photosynthesis length for the plant',
        help=('Calculate photosynthesis length for the plant and provide the '
              'forumla that derives that value'),
        aliases=['psynth']
    )
    async def photosynthesis(self, ctx, length=None, leaves=None):
        try:
            length = int(length)
            leaves = int(leaves)
        except TypeError:
            return await ctx.send('Please provide an numerical length and '
                                  'number of leaves')
        except ValueError:
            return await ctx.send('Please provide an numerical length and '
                                  'number of leaves')

        days = ceil(length/sqrt(leaves))
        await ctx.send(f'With a total length of `{length}` and `{leaves}` '
                       f'leaves, photosynthesis will last '
                       f'`ceil({length}/√{leaves}) = {days}` days.')


async def setup(bot):
    await bot.add_cog(Cycle(bot))
