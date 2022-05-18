from typing_extensions import Self
from unicodedata import name
import discord
from discord.ext import commands, tasks
from discord_ui import SelectMenu, SelectOption, UI, components, Button
from types import SimpleNamespace
import random
from discord.utils import get


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
    
    one_loop.start()
    two_loop.start()
    three_loop.start()
    four_loop.start()


def rolecovert(role_cycle_choices_dict,curr_user):
    tguild = bot.get_guild(755930762485825627)
    user_role_converted = []

    for strole in role_cycle_choices_dict[curr_user]:
        role_full = get(tguild.roles, id=strole)
        user_role_converted.append(role_full)
    return user_role_converted


def commonelems(available_roles,role_user):
    common=0
    for value in available_roles:
        if value in role_user:
            common=1
    return int(common)


def roleidget(choice_role_names):
    tguild = bot.get_guild(755930762485825627)
    user_role_id = []

    for strole in choice_role_names:
        role_full = get(tguild.roles, name=strole)
        role_id = role_full.id
        user_role_id.append(role_full)
    return user_role_id


def notsimroleclear(role_user,available_roles):
    for simrole in role_user:
        not_color_roles = []

        if simrole not in available_roles:
            not_color_roles.append(simrole)
        else:
            pass
    return not_color_roles


def notsimrolefind(current_roles,color_roles_sim):
    for simrole in current_roles:
        not_color_roles = []
        yup_color_roles = []

        if simrole not in color_roles_sim:
            not_color_roles.append(simrole)
        else:
            pass
    return not_color_roles


@tasks.loop(seconds = 1)
async def one_loop():
    tguild = bot.get_guild(755930762485825627)
    
    for gay in cycling_status_list:
        if speed_cycle_choices_dict[gay] == ['1']:
            tguild = bot.get_guild(755930762485825627)
            total_user = tguild.get_member(gay)
            all_roles = tguild.me.roles
            del all_roles[0]
            del all_roles[22]
            del all_roles[22]

            current_roles = list(total_user.roles)
            color_roles_sim = list(all_roles)
            number_chosen_roles = len(role_cycle_choices_dict[gay])
            
            role_switch_num = random.randrange(0, number_chosen_roles, 1)
            get_role_list = list(role_cycle_choices_dict.get(gay))
            get_now_role = get_role_list[role_switch_num]
            now_role = get_now_role
            new_current_roles = notsimrolefind(current_roles,color_roles_sim)
            new_current_roles.append(now_role)

            if now_role in current_roles:
                pass
            else:
                await total_user.edit(roles=new_current_roles)
        else:
            pass


@tasks.loop(seconds = 2)
async def two_loop():
    tguild = bot.get_guild(755930762485825627)
    
    for gay in cycling_status_list:
        if speed_cycle_choices_dict[gay] == ['2']:
            tguild = bot.get_guild(755930762485825627)
            total_user = tguild.get_member(gay)
            all_roles = tguild.me.roles
            del all_roles[0]
            del all_roles[22]
            del all_roles[22]

            current_roles = list(total_user.roles)
            color_roles_sim = list(all_roles)
            number_chosen_roles = len(role_cycle_choices_dict[gay])
            
            role_switch_num = random.randrange(0, number_chosen_roles, 1)
            get_role_list = list(role_cycle_choices_dict.get(gay))
            get_now_role = get_role_list[role_switch_num]
            now_role = get_now_role
            new_current_roles = notsimrolefind(current_roles,color_roles_sim)
            new_current_roles.append(now_role)

            if now_role in current_roles:
                pass
            else:
                await total_user.edit(roles=new_current_roles)
        else:
            pass


@tasks.loop(seconds = 3)
async def three_loop():
    tguild = bot.get_guild(755930762485825627)
    
    for gay in cycling_status_list:
        if speed_cycle_choices_dict[gay] == ['3']:
            tguild = bot.get_guild(755930762485825627)
            total_user = tguild.get_member(gay)
            all_roles = tguild.me.roles
            del all_roles[0]
            del all_roles[22]
            del all_roles[22]

            current_roles = list(total_user.roles)
            color_roles_sim = list(all_roles)
            number_chosen_roles = len(role_cycle_choices_dict[gay])
            
            role_switch_num = random.randrange(0, number_chosen_roles, 1)
            get_role_list = list(role_cycle_choices_dict.get(gay))
            get_now_role = get_role_list[role_switch_num]
            now_role = get_now_role
            new_current_roles = notsimrolefind(current_roles,color_roles_sim)
            new_current_roles.append(now_role)

            if now_role in current_roles:
                pass
            else:
                await total_user.edit(roles=new_current_roles)
        else:
            pass


@tasks.loop(seconds = 4)
async def four_loop():
    tguild = bot.get_guild(755930762485825627)
    
    for gay in cycling_status_list:
        if speed_cycle_choices_dict[gay] == ['4']:
            tguild = bot.get_guild(755930762485825627)
            total_user = tguild.get_member(gay)
            all_roles = tguild.me.roles
            del all_roles[0]
            del all_roles[22]
            del all_roles[22]

            current_roles = list(total_user.roles)
            color_roles_sim = list(all_roles)
            number_chosen_roles = len(role_cycle_choices_dict[gay])
            
            role_switch_num = random.randrange(0, number_chosen_roles, 1)
            get_role_list = list(role_cycle_choices_dict.get(gay))
            get_now_role = get_role_list[role_switch_num]
            now_role = get_now_role
            new_current_roles = notsimrolefind(current_roles,color_roles_sim)
            new_current_roles.append(now_role)

            if now_role in current_roles:
                pass
            else:
                await total_user.edit(roles=new_current_roles)
        else:
            pass


@bot.command()
async def startcycle(message):
        tguild = bot.get_guild(755930762485825627)

        all_roles = tguild.me.roles
        del all_roles[0]
        del all_roles[22]
        del all_roles[22]
        available_roles =  all_roles
        role_number = len(available_roles)
        role_order = available_roles[::-1]

        roles_user = message.author.roles


        if commonelems(available_roles,roles_user) > 0:
            await message.channel.send('You already have a color role. Please remove it before running the bot.')
        
        if commonelems(available_roles,roles_user) == 0:
            await ui.components.send(message.channel, "Hello! Please select all of the roles that you would like to cycle through :)", components=[
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
                        SelectOption(22, label=str(role_order[21]))
                ],min_values=2, max_values=8, placeholder="Pick some roles")
                ])


@bot.listen('on_menu_select')
async def on_role_menu(menu):
    choice_role_names = [value.content for value in menu.selected_options]
    role_cycle_choices_dict[menu.author.id]=roleidget(choice_role_names)
    
    await menu.respond("You selected " + ', '.join([value.content for value in menu.selected_options]) + "\nNow, in seconds, how quickly should I switch between these roles?", components=[
        Button('1'),
        Button('2'),
        Button('3'),
        Button('4')
    ])

# If choose '1/2' warn about lagging

@bot.listen('on_button')
async def on_button(btn):
    speed_cycle_choices_dict[btn.author.id]=[btn.component.content]
    cycling_status_list.append(btn.author.id)

    await btn.respond("You chose " + btn.component.content)


@bot.command()
async def stopcycle(message):
    if message.author.id in cycling_status_list:
        cycling_status_list.remove(message.author.id)
        del role_cycle_choices_dict[message.author.id]
        del speed_cycle_choices_dict[message.author.id]

        tguild = bot.get_guild(755930762485825627)
        all_roles = tguild.me.roles
        
        del all_roles[0]
        del all_roles[22]
        del all_roles[22]
        available_roles =  all_roles

        role_user = message.author.roles

        await message.author.edit(roles=notsimroleclear(role_user,available_roles))
        await message.channel.send('Your cycle has been stopped')
    else:
        await message.channel.send('You are not currently cycling')


@bot.command()
async def pausecycle(message):
    if message.author.id in cycling_status_list:
        cycling_status_list.remove(message.author.id)
        await message.channel.send('Your cycle has been paused')
    else:
        await message.channel.send('You are not currently cycling')


@bot.command()
async def unpausecycle(message):
    if message.author.id not in cycling_status_list:
        cycling_status_list.append(message.author.id)
        await message.channel.send('Your cycle has been unpaused')
    else:
        await message.channel.send('You are already cycling')


@bot.command()
async def clearcolorroles(message):
        tguild = bot.get_guild(755930762485825627)

        all_roles = tguild.me.roles
        
        del all_roles[0]
        del all_roles[22]
        del all_roles[22]
        available_roles =  all_roles

        role_user = message.author.roles


        if commonelems(available_roles,role_user) > 0:
            await message.author.edit(roles=notsimroleclear(role_user,available_roles))
            await message.channel.send('Your color roles have been removed')

        if commonelems(available_roles,role_user) == 0:
            await message.channel.send('You have no color roles')
        

@bot.command()
async def commands(message):
    await message.channel.send(
        "rcb.startcycle -- Start a new cyle with new roles and a new speed\nrcb.endcycle -- Stop your current cycle and clear your current saved roles and speed\nrcb.pausecycle -- Stop your current cycle without clearing your saved roles and speed\nrcb.unpausecycle -- Start a cycle with the roles and speed that you had last (only if you used rcb.pausecycle)\nrcb.clearcolorroles -- Clear all color roles you have"
    )




bot.run("OTcyMTU1NTY1NTQ1NDg4Mzk1.GxeYXo.m3AmZfKivDniVAXj6Ozc4DlAwq04iXLnvKl4LU")

"""
rcb-discord
"""