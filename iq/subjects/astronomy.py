from .context import subjects
from .context import users
from discord.ext import commands
import discord


class Astronomy(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Astronomy online.')

    @commands.command()
    async def astronomy(self, ctx):
        """A astronomy question."""

        if not users.is_user(ctx.author.id):
            await ctx.send('You are not signed up for any subject. :x:')

        if users.users[ctx.author.id]['subject'] != 'astronomy':
            await ctx.send('You are not joined astronomy. :x:')

        else:
            user = users.users[ctx.author.id]

            quest_answer = subjects.get_quest_answer(ctx.author.id)

            user['quest'] = quest_answer[0]
            user['answer'] = quest_answer[1]

            await ctx.send(user['quest'])


def setup(client):
    client.add_cog(Astronomy(client))
