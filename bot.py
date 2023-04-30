import discord
from gforms import getresp
import os

bot = discord.Bot()


class buttonView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Click me!", style=discord.ButtonStyle.primary, emoji="✅", custom_id="verify")
    async def button_callback(self, button, interaction):
        await interaction.response.defer(ephemeral=True)
        username = interaction.user.name
        if username in getresp():
            await interaction.followup.send("Verified", ephemeral=True)
            await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name="verified"))
        else:
            await interaction.followup.send("Verification failed, please open support ticket", ephemeral=True)


@bot.event
async def on_ready():
    bot.add_view(buttonView()) # Registers a View for persistent listening
    print("Bot is ready")


@bot.slash_command(name="send_veri", guild_ids=[1056136438011416646])
async def send_veri(ctx):
    if ctx.author.id != 759719245503791125: return
    embed = discord.Embed(title="Verification", description="Click button to verify. If verification fails, please open a support ticket.")
    await ctx.respond(embed=embed, view=buttonView())

bot.run(os.environ["TOKEN"])
