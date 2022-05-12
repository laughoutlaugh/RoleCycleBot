from typing_extensions import Self
import discord
from discord.ext import commands, tasks
from discord.ext import commands, tasks
from discord_ui import SelectMenu, SelectOption, UI, components, Button
from discord.utils import get
from types import SimpleNamespace
import random


intents = discord.Intents().all()
bot = commands.Bot(intents=intents, command_prefix = commands.when_mentioned_or('rcb.'))
ui = UI(bot)

tguild = None


cycling_status_list = []
role_cycle_choices_dict = {}
speed_cycle_choices_dict = {}


@bot.event
async def on_ready():
    print("I am running on " + bot.user.name)
    print("With the ID: " + str(bot.user.id))
    print('Bot is ready to be used')

    tguild = bot.get_guild(755930762485825627)
    print(tguild.id)

    for guild in bot.guilds:
        print(guild)
        print(guild.id)

    four_loop.start()


"""
if user speed cycle == '1/2:
    current_roles = user.roles
    chosen_roles = choices_dict[user]
    number_chosen_roles = len(chosen_roles)
    
    role_switch_get = random.randint(0, number_chosen_roles)
    role_switch_num = number_chosen_role - role_switch_get
    give_roles = current_roles, chosen_roles[role_switch_num]
    
    user.edit(roles=give_roles)
    
"""


@tasks.loop(seconds = 4)
async def four_loop():
    tguild = bot.get_guild(755930762485825627)
    
    for gay in cycling_status_list:
        if speed_cycle_choices_dict[gay] == ['4']:
            tguild = bot.get_guild(755930762485825627)

            curr_user = gay
            total_user = tguild.get_member(user_id=int(curr_user))

            current_roles = discord.utils.get(tguild.roles, name=total_user.name) # gets role by name (not roles of user) Use to get roles to .add_roles Find way to get users roles
            chosen_roles = role_cycle_choices_dict[curr_user]
            number_chosen_roles = len(chosen_roles)
            
            role_switch_num = random.randrange(1, number_chosen_roles)
            give_roles = chosen_roles[1]
            print(current_roles)
            print(chosen_roles)
            print(number_chosen_roles)
            print(role_switch_num)
            
            await total_user.add_roles(give_roles)
        else:
            pass





@bot.command()
async def startcycle(message):
        tguild = bot.get_guild(755930762485825627)

        all_roles = tguild.me.roles
        del all_roles[0]
        del all_roles[24]
        del all_roles[24]
        available_roles =  all_roles
        role_number = len(available_roles)
        role_order = available_roles[::-1]

        await ui.components.send(message.channel, "Hello! Please remove any color roles you may already have. Then select all of the roles that you would like to cycle through :)", components=[
            SelectMenu(
                options=[
                    SelectOption(1, label=str(role_order[0])),
                    SelectOption(2, label=str(role_order[1])),
                    SelectOption(3, label=str(role_order[2])),
                    SelectOption(4, label=str(role_order[3])),
                    SelectOption(5, label=str(role_order[4])),
                    SelectOption(6, label=str(role_order[5])),
                    SelectOption(7, label=str(role_order[6])),
                    SelectOption(8, label=str(role_order[7])),
                    SelectOption(9, label=str(role_order[8])),
                    SelectOption(10, label=str(role_order[9])),
                    SelectOption(11, label=str(role_order[10])),
                    SelectOption(12, label=str(role_order[11])),
                    SelectOption(13, label=str(role_order[12])),
                    SelectOption(14, label=str(role_order[13])),
                    SelectOption(15, label=str(role_order[14])),
                    SelectOption(16, label=str(role_order[15])),
                    SelectOption(17, label=str(role_order[16])),
                    SelectOption(18, label=str(role_order[17])),
                    SelectOption(19, label=str(role_order[18])),
                    SelectOption(20, label=str(role_order[19])),
                    SelectOption(21, label=str(role_order[20])),
                    SelectOption(22, label=str(role_order[21])),
                    SelectOption(23, label=str(role_order[22])),
                    SelectOption(24, label=str(role_order[23]))
            ],min_values=2, max_values=8, placeholder="Pick some roles")
            ])

    


@bot.listen('on_menu_select')
async def on_role_menu(menu):
    role_cycle_choices_dict[menu.author.id]=[value.content for value in menu.selected_options]
    print(role_cycle_choices_dict)
    
    await menu.respond("You selected " + ', '.join([value.content for value in menu.selected_options]) + "\nNow, in seconds, how quickly should I switch between these roles?", components=[
        Button('1/2'),
        Button('1'),
        Button('2'),
        Button('3'),
        Button('4')
    ])


@bot.listen('on_button')
async def on_button(btn):
    speed_cycle_choices_dict[btn.author.id]=[btn.component.content]
    print(speed_cycle_choices_dict)

    cycling_status_list.append(btn.author.id)

    await btn.respond("You chose " + btn.component.content)




bot.run("OTcyMTU1NTY1NTQ1NDg4Mzk1.GhFo86.gB7jcvmwSJ33tTzEoJaU1YdgbOzcAcnHFUoIlw")





"""
When startcycle add author to cycling_status_dict[online] and define roles and speed
When endcycle add author to cycling_status_dict[offline]

make rolechoices dict
get all member with role
dict entry for each member
^same for speed


for user in [online]:
    role_number = 

    get roles
    get rolechoices[role_number]
    get speedchoice

    add_roles(roles) to user

    role_number += 1


Every .25 second cycle repeat
"""

"""
        dict_role_options = {'roles_dict':[]}
        option_number = 0
        value_number = 1

        while value_number <= role_number:

            if value_number == role_number:
                dict_role_options['roles_dict'].append(SelectOption(value=value_number, label=str(role_order[option_number])))
                break

            dict_role_options['roles_dict'].append(SelectOption(value=value_number, label=str(role_order[option_number])), )

            option_number += 1
            value_number += 1
        good_role_list = SimpleNamespace(**dict_role_options)
        print(good_role_list.roles_dict)
"""