from discord.ext import commands,tasks
import discord
import random
from discord import ui
from discord import app_commands
from discord.utils import get
from discord.ui import View
import datetime

TOKEN = "MTE0NTQyNjA3OTcyOTg1NjY0Mw.Gf2gY3.8mIHc75wErRyjfH2Ra-fqMm39OZhk0wJLGGlXs"


intents = discord.Intents.default()
intents.members = True
intents.typing=False
MY_GUILD=discord.Object(id=896332817498267668)
class MyClient(discord.Client):
    def __init__(self,*,intents:discord.Intents):
        super().__init__(intents=intents)
        self.tree=app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        self.add_view(SelectRoleCourse())
        self.add_view(SelectRoleSpec())
        await self.tree.sync(guild=MY_GUILD)

intents.message_content = True
intents.members = True
client=MyClient(intents=intents)

async def giveCourseRole(user,guild,roleid): # guild id 896332817498267668
    role = discord.utils.get(guild.roles, id = roleid)
    await user.add_roles(role)




# class SelectRole1st090201(View):
#     def __init__(self):
#         super().__init__(timeout=None)
        
#     @discord.ui.select(
#         placeholder = "Выберите роль",
#         options=
#         [
#             discord.SelectOption(label="В2201а", value="1", description="взять роль В2201а"), 
#             discord.SelectOption(label="В2201б", value="2", description="взять роль В2201б"), 
#             discord.SelectOption(label="В2202в", value="3", description="взять роль В2202в"),
            
            
#         ]
#         ,
#     )
#     async def select_callback(self,interaction,select):

        
#         select.disabled=False
#         if select.values[0]=="1":
#             user_roles = [role for role in interaction.user.roles if role.id == 1145437002955751504]
#             if user_roles:
#                 await interaction.response.send_message("У вас уже есть данная роль",ephemeral=True)
#             else:
#                 await giveCourseRole(interaction.user,interaction.guild,1145437002955751504)
#                 await interaction.response.send_message(view = SelectRoleSpec(),ephemeral=True)
#             pass
            
            

            
#         if select.values[0]=="2":
#             user_roles = [role for role in interaction.user.roles if role.id == 1145437036497616996]
#             if user_roles:
#                 await interaction.response.send_message("У вас уже есть данная роль",ephemeral=True)
#             else:
#                 await giveCourseRole(interaction.user,interaction.guild,1145437036497616996)
#                 await interaction.response.send_message(view = SelectRoleSpec(),ephemeral=True)
#             pass
            
             
#         if select.values[0]=="3":
#             user_roles = [role for role in interaction.user.roles if role.id == 1145437061906698343 ]
#             if user_roles:
#                 await interaction.response.send_message("У вас уже есть данная роль",ephemeral=True)
#             else:
#                 await giveCourseRole(interaction.user,interaction.guild,1145437061906698343)
#                 await interaction.response.send_message(view = SelectRoleSpec(),ephemeral=True)
#             pass
            









class SelectRoleCourse(View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @discord.ui.select(
        placeholder = "Выберите роль",
        options=
        [
            discord.SelectOption(label="1й курс", value="1", description="взять роль 1го курса + продолжить "), # 877574875638796318
            discord.SelectOption(label="2й курс", value="2", description="взять роль 2го курса + продолжить "), #1128388535880253461
            discord.SelectOption(label="3й курс", value="3", description="взять роль 3го курса + продолжить "),#1128388543320969446
            discord.SelectOption(label="4й курс", value="4", description="взять роль 4го курса + продолжить "), #1128388546433130496
            
        ]
        ,custom_id="1"
    )
    async def select_callback(self,interaction,select):

        
        select.disabled=False
        if select.values[0]=="1":
            user_roles = [role for role in interaction.user.roles if role.id == 1145428481346375751]
            if user_roles:
                await interaction.response.send_message("У вас уже есть данная роль",ephemeral=True)
            else:
                await giveCourseRole(interaction.user,interaction.guild,1145428481346375751)
                await interaction.response.send_message(view = SelectRoleSpec(),ephemeral=True)
            pass
            
            

            
        if select.values[0]=="2":
            user_roles = [role for role in interaction.user.roles if role.id == 1145428551869419623]
            if user_roles:
                await interaction.response.send_message("У вас уже есть данная роль",ephemeral=True)
            else:
                await giveCourseRole(interaction.user,interaction.guild,1145428551869419623)
                await interaction.response.send_message(view = SelectRoleSpec(),ephemeral=True)
            pass
            
             
        if select.values[0]=="3":
            user_roles = [role for role in interaction.user.roles if role.id == 1145429018716414122 ]
            if user_roles:
                await interaction.response.send_message("У вас уже есть данная роль",ephemeral=True)
            else:
                await giveCourseRole(interaction.user,interaction.guild,1145429018716414122)
                await interaction.response.send_message(view = SelectRoleSpec(),ephemeral=True)
            pass
            
             
        if select.values[0]=="4":
            user_roles = [role for role in interaction.user.roles if role.id == 1145429087498797067]
            if user_roles:
                await interaction.response.send_message("У вас уже есть данная роль",ephemeral=True)
            else:
                await giveCourseRole(interaction.user,interaction.guild,1145429087498797067)
                await interaction.response.send_message(view = SelectRoleSpec(),ephemeral=True)
            pass
            
            
class SelectRoleSpec(View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @discord.ui.select(
        placeholder = "Выберите роль",
        options=
        [
            discord.SelectOption(label="09.02.01 БАЗА", value="1", description="взять роль специальности 09.02.01 + продолжить для выбора группы"), # 877574875638796318
            discord.SelectOption(label="09.02.07 БАЗА", value="2", description="взять роль специальности 09.02.07 + продолжить для выбора группы"),
            discord.SelectOption(label="09.02.01 СПО", value="3", description="взять роль специальности 09.02.01 СПО + продолжить для выбора группы"),
            discord.SelectOption(label="09.02.03 СПО", value="4", description="взять роль специальности 09.02.03 СПО + продолжить для выбора группы"), 
            discord.SelectOption(label="09.02.07 СПО", value="5", description="взять роль специальности 09.02.07 СПО + продолжить для выбора группы")
            
            
        ]
        ,custom_id="2"
    )
    async def select_callback(self,interaction,select):

        
        select.disabled=False
        if select.values[0]=="1":
            user_roles = [role for role in interaction.user.roles if role.id == 1145428578478063647]
            if user_roles:
                await interaction.response.send_message("У вас уже есть данная роль",ephemeral=True)
            else:
                await giveCourseRole(interaction.user,interaction.guild,1145428578478063647)
                await interaction.response.send_message("Роль выдана",ephemeral=True)
            pass

            
        if select.values[0]=="2":
            user_roles = [role for role in interaction.user.roles if role.id == 1145428619531927726]
            if user_roles:
                await interaction.response.send_message("У вас уже есть данная роль",ephemeral=True)
            else:
                await giveCourseRole(interaction.user,interaction.guild,1145428619531927726)
                await interaction.response.send_message("Роль выдана",ephemeral=True)
            pass
        if select.values[0]=="3":
            user_roles = [role for role in interaction.user.roles if role.id == 1145439293339344978]
            if user_roles:
                await interaction.response.send_message("У вас уже есть данная роль",ephemeral=True)
            else:
                await giveCourseRole(interaction.user,interaction.guild,1145439293339344978)
                await interaction.response.send_message("Роль выдана",ephemeral=True)
            pass
        if select.values[0]=="4":
            user_roles = [role for role in interaction.user.roles if role.id == 1145439265988288692]
            if user_roles:
                await interaction.response.send_message("У вас уже есть данная роль",ephemeral=True)
            else:
                await giveCourseRole(interaction.user,interaction.guild,1145439265988288692)
                await interaction.response.send_message("Роль выдана",ephemeral=True)
            pass
        if select.values[0]=="5":
            user_roles = [role for role in interaction.user.roles if role.id == 1145439193116450888]
            if user_roles:
                await interaction.response.send_message("У вас уже есть данная роль",ephemeral=True)
            else:
                await giveCourseRole(interaction.user,interaction.guild,1145439193116450888)
                await interaction.response.send_message("Роль выдана",ephemeral=True)
            pass
             
            
@client.event
async def on_ready():
    channel = client.get_channel(1145431487991263332)
    messages = [message async for message in channel.history(limit=5)]
    for message in messages:
        await message.delete()
    embed = discord.Embed(title="Тут можно пикнуть роли",
                      description="Чтобы пикнуть роль нужно просто нажать на дропдаун-меню ниже :)")

    embed.set_image(url="https://dic.academic.ru/pictures/wiki/files/99/ci_nsu_logo.gif")
    
    view = SelectRoleCourse()
    await channel.send(embed=embed,view=view)
    

#1145440182431129681




@client.event
async def on_voice_state_update(member, before, after):
    if after.channel and after.channel.id == 1145440182431129681:  # Replace with your desired voice channel ID
        guild = member.guild  # Get the guild object
        category = discord.utils.get(guild.categories, id=896332817498267670)

        # Create a new voice channel
        new_channel = await guild.create_voice_channel(
            name=f"{member.name}\'s room",
            category=category,
            position=after.channel.position + 1
        )

        # Move the user to the new voice channel
        await member.move_to(new_channel)

        @client.event
        async def on_voice_state_update(member, before, after):
            if before.channel and before.channel.id == new_channel.id:
                # Delete the voice channel when the user leaves
                await new_channel.delete()

@client.event
async def on_disconnect():
    await client.login(TOKEN)
    await client.connect()

client.run(TOKEN)