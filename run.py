import discord
import asyncio
import config
import time
import os
import datetime

from config import link, prefix, ownerid
from dontpingthedevslist import nmlist, splist, rolesk
from discord.ext.commands import Bot
from discord.ext import commands
from datetime import datetime, timezone, timedelta

intents = discord.Intents.all()
client = commands.Bot(command_prefix=(prefix),intents=intents)
client.remove_command('help')

@client.event
async def on_ready():    
    print("----------------------")
    print("Logged in")
    print("Username: %s"%client.user.name)
    print("ID: %s"%client.user.id)
    datenastarcie = datetime.now().strftime("**Date: **%A, %B %d, %Y\n**Time: **%I:%M:%S %p")
    #await client.get_channel(716353904601858109).send(str(datenastarcie))
    data = (datetime.now() - timedelta(hours = 2)).strftime("**Date: **%A, %B %d, %Y\n**Time: **%I:%M:%S %p")
    await client.get_channel(716353904601858109).send(str(data))    
    for guild in client.guilds:
        print(str(guild))
    print("----------------------")    

@client.event
async def on_command_error(ctx, error):
    print(error)
    embed = discord.Embed(colour = 0x4d3c31)
    
    if isinstance(error, discord.HTTPException):
       description = str("css```"  + '\n' + "[HTTP EXCEPTION]"+'\n')
    elif isinstance(error, discord.InvalidArgument):
       description = str("Invalid argument provided. ")
    elif isinstance(error, discord.ext.commands.BadArgument):
        description = str("Bad argument provided. ") #elif
    elif isinstance(error, discord.ext.commands.MissingRequiredArgument):
        description = str("Missing required argument: ")
    elif isinstance(error, discord.ext.commands.CommandNotFound):
        return
    elif isinstance(error, discord.errors.Forbidden):
        embed.add_field(name='The command raised an exception', value=str(str(error) + "."))
        try:
            await ctx.send(embed = embed)
        except Exception as e:
            try:
                return await ctx.send("Exeption occured, error code: " + str(error))
            except:
                return
        return
    elif isinstance(error, discord.Forbidden):
        embed.add_field(name='The command raised an exception', value=str(str(error) + "."))
        try:
            await ctx.send(embed = embed)
        except Exception as e:
            try:
                await ctx.send("Exeption occured, error code: " + str(error))
            except:
                return
        return
       
    #elif isinstance(error.original, discord.Forbidden):
    #    embed.add_field(name='The command raised an exception', value=str(str(error) + "."))
    #    try:
    #        await ctx.send(embed = embed)
    #    except Exception as e:
    #        try:
    #            await ctx.send("Exeption occured, error code: " + str(error))
    #        except:
    #            return
    #    return
       #description = str(None)#"Error code: Forbidden. Missing access.")
       #description = str(None)#"Error code: Forbidden. Missing access.")

    else:
        #if isinstance(error, discord.DiscordException): #handles any other discord expection
               #description = str(error)
        #else:
        description = str("```css"  + '\n' + "[ISSUE TICKET]" +'\n')
        embed.add_field(name='The command raised an exception:', value=str(str(description))+str(error) + "```")
        await client.get_channel(716381888561807554).send(embed = embed) #nie usuwać tego return na początku
        return ctx.send("The command raised an exception. Error code unknown, an issue ticket has been created.")
    embed.add_field(name='The command raised an exception', value=str(str(description))+str(error))
    try:
        buja = await ctx.send(embed = embed)
    except Exception as e:
        try:
            await ctx.send("Exception occured, error code: " + str(error))
        except:
            return
        

@client.event
async def on_message(message):
    channel = message.channel
    channel.id = message.channel.id
    server = message.guild
    server.id = message.guild.id
    bum=server.get_member(message.author.id)
    if bum is None:
        return

    mutedrole = discord.utils.get(server.roles,name="Muted")
    warningrole = discord.utils.get(server.roles,name="Warning")   
    kergo = await client.fetch_channel(str("719548306887540766")) #moj-log       
    date = datetime.now().strftime("**Date: **%A, %B %d, %Y\n**Time: **%I:%M:%S %p")
    #await client.change_presence(activity=discord.Game(name="Don't ping the devs || v1.01"))
    user_roles = [r.name.lower() for r in bum.roles]
    belo = int(message.guild.id)
    chano = int(message.channel.id)
    mem = str(message.author)
    memid = str(message.author.id)
    
    if int(message.author.id) == int(client.user.id):
        return
                                    
    if any(x in message.content for x in nmlist) or (any(x in message.content for x in splist) and (not any(r in user_roles for r in rolesk))):
                                
        if belo == 433640988074967040: #kogama
            if ((any(x in message.content for x in nmlist) and not any(r in user_roles for r in["senior moderator", "moderators", "junior moderators", "staff", "kogamate", "bots"])) or (any(x in message.content for x in splist) and (not any(r in user_roles for r in list(rolesk))))):                   
                try:
                    msg = await channel.send("Don't ping the devs," + " " + str(mem) + " with userid " + str(memid))                   
                except Exception as e:
                    print(e)
                if "warning" in user_roles:
                    try:
                        await message.author.add_roles(mutedrole, reason = "Pinging the developer")
                    except:
                        try:
                            await kergo.send("Server: " + str(server) + ", server id: " + str(server.id) + '\n' + "**Channel**: " + str(channel) + ", channel id: " + str(channel.id) + '\n' + "**User:** " + str(mem) + " " + str(memid) + '\n' + str(date) + '\n' + "**Punishment:** ~~Mute~~ / exeption occured - no punishment" + '\n' + "**Message content**: ```" + str(message.content) + "```")
                        except:
                            pass
                        norolemuted = await channel.send("``` I can't find Muted role, it's the higher rank than my highest role or I don't have permission to manage roles."  + '\n' + "-- This message will be deleted automatically in 30 seconds. --```", delete_after=30)
                        return
                    try:
                        await kergo.send("Server: " + str(server) + ", server id: " + str(server.id) + '\n' + "**Channel**: " + str(channel) + ", channel id: " + str(channel.id) + '\n' + "**User:** " + str(mem) + " " + str(memid) + '\n' + str(date) + '\n' + "**Punishment:** Mute" + '\n' + "**Message content**: ```" + str(message.content) + "```")
                    except:
                        pass
                    warn = await channel.send(message.author.mention + ", you have been muted for disregarding the previous warning and pinging the developer.")
                    try:
                        await message.author.remove_roles(warningrole)
                    except:
                        pass
                    await asyncio.sleep(600)
                    try:                        
                        await message.author.remove_roles(mutedrole, reason = "Auto")
                    except:
                        return
                else:   
                    try:
                        await message.author.add_roles(warningrole, reason = "Pinging the developer")
                    except Exception as e:
                        try:
                            await kergo.send("Server: " + str(server) + ", server id: " + str(server.id) + '\n' + "**Channel**: " + str(channel) + ", channel id: " + str(channel.id) + '\n' + "**User:** " + str(mem) + " " + str(memid) + '\n' + str(date) + '\n' + "**Punishment:** ~~Warning~~ / exeption occured - no punishment" + '\n' + "**Message content**: ```" + str(message.content) + "```")
                        except Exception as zero:
                            print(zero)
                            pass
                        norolewarning = await channel.send("``` I couldn't find Warning role, it's the higher rank than my highest role or I don't have permission to manage roles."  + '\n' + "-- This message will be deleted automatically in 30 seconds. --```", delete_after=30)
                        return
                    try:
                        await kergo.send("Server: " + str(server) + ", server id: " + str(server.id) + '\n' + "**Channel**: " + str(channel) + ", channel id: " + str(channel.id) + '\n' + "**User:** " + str(mem) + " " + str(memid) + '\n' + str(date) + '\n' + "**Punishment:** Warning" + '\n' + "**Message content**: ```" + str(message.content) + "```")
                    except:
                        pass
                    
        
    await client.process_commands(message)

    
#m1 
@client.command(pass_context=True)
async def help(ctx):

#Ordinary BOT COMMANDS   
    m1 = str("<:Working:694869641079685120> help")
    m2 = str("<:Working:694869641079685120> ping")
    m3 = str("<:Working:694869641079685120> setgame")
    m4 = str("<:Working:694869641079685120> botinvite")
    m5 = str("<:Disabled:694869604392239115> selfdestruct")
#Server commands    
    g1 = str("<:Needs_2_be_rewritten:694869685300363285> serverinvite")
    g2 = str("<:Needs_2_be_rewritten:694869685300363285> serverbans")    
    g3 = str("<:Maintenance:694869666207760415> userinfo @user")
    g4 = str("<:Needs_2_be_rewritten:694869685300363285> serverinfo**")
    g5 = str("<:Working:694869641079685120> roles**")
#Moderation commands
    t1 = str("<:Maintenance:694869666207760415> mute @user [duration in mins]")
    t2 = str("<:Needs_2_be_rewritten:694869685300363285> unmute @user")
    t3 = str("<:Needs_2_be_rewritten:694869685300363285> delwarn @user")
    t4 = str("<:Working:694869641079685120> purge [amount]")
    t5 = str("<:Working:694869641079685120> lockdown")
    t6 = str("<:Working:694869641079685120> slock")   
    t7 = str("<:Needs_2_be_rewritten:694869685300363285> unlock")
    t8 = str("<:Working:694869641079685120> sunlock")
    t9 = str("<:Needs_2_be_rewritten:694869685300363285> warn @user [reason]")
    t10 = str("<:Needs_2_be_rewritten:694869685300363285> kick @user <reason>")
    t11 = str("<:Needs_2_be_rewritten:694869685300363285> ban @user <reason>")
    t12 = str("<:Needs_2_be_rewritten:694869685300363285> soft @user <reason>")
         
    mwot = str(m1 + '\n' + m2 + '\n' + m3 + '\n' + m4 + '\n' + m5) 
    gwot = str(g1 + '\n' + g2 + '\n' + g3 + '\n' + g4)
    twot = str(t1 + '\n' + t2 + '\n' + t3 + '\n' + t4 + '\n' + t5 + '\n' + t6 + '\n' + t7 + '\n' + t8 + '\n' + t9 + '\n' + t10 + '\n' + t11 + '\n' + t12)
    
    join = discord.Embed(title = 'All the available bot commands', description = 'Glop Blop v1.0', colour = 0x0085ff);
    join.add_field(name = ' Bot:', value = str(mwot), inline=False);
    join.add_field(name = ' Server:', value = str(gwot),inline=False);
    join.add_field(name = ' Administration:', value = str(twot), inline=False);
    join.set_footer(text = "Green circle next to command name means the command working properly, the orange one means a command is being under the maintenance, thus making it possible for minor bugs to occur. The red circle means the major bug can occur or the command works only partially and needs a rework, but you can still check what it does (or at least you can try). Grey circle next to a commad name means the command is disabled.")
    #join.add_field(name = '> Info:', value = str(got));
    #join.add_field(name = '> Bot:', value = (str(mwot)+str(gwot)+str(twot)))
    try:
        await ctx.message.channel.send(embed = join);
    except Exception as e:
        return await ctx.message.channel.send(ctx.message.author.mention+ " "+ str(e) + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)


#m2
@client.command()
async def ping(ctx):
    pingtime = time.time()
    ping = time.time() - pingtime
    buja = str('`%.0001f seconds`' %ping)
    await ctx.send(f'Ping is {round(client.latency * 1000)} ms')

#m3
@client.command(pass_context=True)
async def setgame(ctx, *, game):
    if ctx.message.author.id == ownerid:
        await client.change_presence(activity=discord.Game(name=game))
        try:
            await ctx.message.delete()
            await ctx.message.author.send("Game was set to **{}**!".format(game))
        except Exception as e:
            return

#m6
@client.command(pass_context=True, aliases=['an', 'a'])
async def announce(ctx, channel : discord.TextChannel, *, content):
    if ctx.message.author.id == (ownerid):
        #try:
        join = discord.Embed(title = None, description = str(content), colour = 0x0085ff);
        #await ctx.send(embed = join)
        await channel.send(embed = join)
        await ctx.message.delete()
        #except Exception as error:
         #   await ctx.send("```css" + '\n' + "[ERROR]" + '\n' + '\n' + str(error) + "```")


    
#niepubliczne1
@client.command(pass_context=True, aliases=['so', 's'])
async def solve(ctx, cte : discord.TextChannel, number : int, *, mte : str):
    if ctx.message.author.id == (ownerid):
        try:
            message = await client.get_message(channel = cte, id = number)
            join = discord.Embed(title = ":white_check_mark: Zrobione", description = str(mte), colour = 0x15e254);
            await ctx.send(embed = join)        
            await client.edit_message(message, embed = join)       
            await client.delete_message(ctx.message)       
        except Exception as error:
            #py albo css
            await ctx.send("```py" + '\n' + "[ERROR]" + '\n' + '\n' + "{AN ERROR OCCURED: " + str(error) + "}```")
        return    
    
#m4    
           
@client.command()
async def botinvite(ctx):
    try:
        await ctx.message.author.send(link)
    except:
        return await ctx.message.channel.send("I can't send messages to this user.")
    await ctx.message.channel.send("Check your DM's!")
    


#m5
#@client.command(pass_context=True)
#async def selfdestruct(ctx):
#    if ctx.message.author.server_permissions.kick_members == True:
#        message = ctx.message
#        await client.say(":boom: Boom :boom:")
    
@client.command(pass_context = True)
async def tbans(ctx, *, ser):
    '''Gets a list of banned users'''  
    if not ctx.message.author.id == (ownerid):     
        erg = await client.say(ctx.message.author.mention + " You don't have permission to use this command. " + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        await client.delete_message(erg)
        return
    try:
        sero = client.get_server(ser)
        await client.say(sero.name)
        x = await client.get_bans(sero)
    except Exception as e:
        await client.say("```" + str(e) + "```")
        return
        #miss = await client.say(ctx.message.author.mention + " I don't have permissions to do that." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        #await asyncio.sleep(10)
        #await client.delete_message(miss)
        #return
    
#    x = ('\n'.join([y.name for y in x] + [y.id for y in x] + [y.mention for y in x] + [y.discriminator for y in x]))
    for y in x:
        be = await client.say("**" + y.name + "#" + y.discriminator + "** " + y.id + " " + y.mention)
        await asyncio.sleep(2)
    
#g1 gets a server invite and pms it to the user who requested it  

@client.command(pass_context = True)
async def serverinvite(ctx):
    if not ctx.message.author.guild_permissions.create_instant_invite == True:
        if ctx.message.author.id == (ownerid):
            pass
        else:        
            return await client.say(ctx.message.author.mention + " You don't have permission to create instant invite. " + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10) 
    invite = await client.create_invite(ctx.message.channel,xkcd=True)
    await client.whisper(invite.url)
    await client.say("Check Your Dm's :wink: ")

#g2 Gets a List of Bans From The Server

@client.command(pass_context = True)
async def serverbans(ctx):
    '''Gets a list of banned users'''  
    if ctx.message.author.server_permissions.ban_members == False:
        if ctx.message.author.id == (ownerid):
            pass
        else:        
            erg = await client.say(ctx.message.author.mention + " You don't have permission to use this command. " + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
            await asyncio.sleep(10)
            await client.delete_message(erg)
            return
    try:
        x = await client.get_bans(ctx.message.server)
    except:
        miss = await client.say(ctx.message.author.mention + " I don't have permissions to do that." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        await client.delete_message(miss)
        return
    
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of the banned users", description = x, color = 0xFFFFF)
    try:
        await client.say(embed = embed);
    except:
        miss = await client.say(ctx.message.author.mention + " Embed links permission required." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        await client.delete_message(miss)
        return

####
#g3
@client.command(pass_context = True)
async def userinfo(ctx, member : discord.Member=None):
    '''Displays Info About The User ----- WORK IN PROGRESS! '\n' '''

    server = ctx.message.guild
    user = ctx.message.author
    
    joined_at = member.joined_at
    user_joined = joined_at.strftime("%d %b %Y %H:%M")
    joined_on = "{}".format(user_joined)

    created_at = member.created_at
    user_created = created_at.strftime("%d %b %Y %H:%M")
    created_on = "{}".format(user_created)

    roles = [x.name for x in member.roles]
    roles = ', '.join(roles)
    
######### NIE ZMIENIAC NIC PONIZEJ #################
    
    def getKey2(item):
        return item[1]
    def getKey1(item):
        return item[0]
    perms = tuple([x for x in member.guild_permissions])
    bergo=[]
    for x in member.guild_permissions:
        if(getKey2(x)) == True:
            if(getKey1(x)) == "add_reactions":
                bergo.append("add reactions")
            if(getKey1(x)) == "administrator":
                bergo.append("administrator")
            if(getKey1(x)) == "attach_files":
                bergo.append("attach files")
            if(getKey1(x)) == "ban_members":
                bergo.append("ban members")
            if(getKey1(x)) == "change_nickname":
                bergo.append("change nickname")
            if(getKey1(x)) == "connect":
                bergo.append("connect")
            if(getKey1(x)) == "create_instant_invite":
                bergo.append("create instant invite")
            if(getKey1(x)) == "deafen_members":
                bergo.append("deafen members")
            if(getKey1(x)) == "embed_links":
                bergo.append("embed links")
            if(getKey1(x)) == "external_emojis":
                bergo.append("external emojis")
            if(getKey1(x)) == "kick_members":
                bergo.append("kick members")
            if(getKey1(x)) == "manage_channels":
                bergo.append("manage channels")
            if(getKey1(x)) == "manage_emojis":
                bergo.append("manage emojis")
            if(getKey1(x)) == "manage_messages":
                bergo.append("manage messages")
            if(getKey1(x)) == "manage_nicknames":
                bergo.append("manage nicknames")
            if(getKey1(x)) == "manage_roles":
                bergo.append("manage roles")
            if(getKey1(x)) == "manage_server":
                bergo.append("manage server")
            if(getKey1(x)) == "manage_webhooks":
                bergo.append("manage webhooks")
            if(getKey1(x)) == "mention_everyone":
                bergo.append("mention everyone")
            if(getKey1(x)) == "move_members":
                bergo.append("move members")
            if(getKey1(x)) == "mute_members":
                bergo.append("mute members")
            if(getKey1(x)) == "read_message_history":
                bergo.append("read message history")
            if(getKey1(x)) == "read_messages":
                bergo.append("read messages")
            if(getKey1(x)) == "send_messages":
                bergo.append("send messages")
            if(getKey1(x)) == "send_tts_messages":
                bergo.append("send tts messages")
            if(getKey1(x)) == "speak":
                bergo.append("speak")
            if(getKey1(x)) == "use_voice_activation":
                bergo.append("use voice activation")
            if(getKey1(x)) == "view_audit_logs":
                bergo.append("view audit logs")
                #bergo.append(getKey1(x))
            myString = "*"+ '*, *'.join(bergo) + "*";
            
######### NIE ZMIENIAC NIC POWYZEJ #################
           

    if member == None:
        nous = await ctx.send(ctx.message.author.mention + " No user mentioned." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
        await asyncio.sleep(10)
        await client.delete_message(nous)
        return     
   
    emb = discord.Embed(title= '%s '%str(member), description = member.mention + ' (ID: ' + str(member.id) + ')', colour = 0x0085ff);
    emb.set_thumbnail(url = member.avatar_url);
    emb.add_field(name = '__Joined Server__', value = joined_on);
    emb.add_field(name = '__Created Account__', value = created_on)
    emb.add_field(name = '__Status__', value = member.status);
    emb.add_field(name = '__Activity__', value = member.activity);
    emb.add_field(name = '__Server permissions__', value = str(myString), inline=False);
    emb.add_field(name = '__Roles__', value = "```" + str(roles) + "```");
    emb.set_footer(text = 'Requested by: ' + str(user) + " (ID: "+ str(user.id) + ")" );

    try:
        await ctx.send(embed = emb);
    except Exception as e:
        miss = await ctx.send(ctx.message.author.mention + " Embed links permission required or embed is too big." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
        await asyncio.sleep(10)
        await client.delete_message(miss)
        return    


#g4 - Lists Info About The server

@client.command(pass_context = True, aliases=['sinfo', 'si'])
async def serverinfo(ctx):

        guild = ctx.message.guild
        roles = [x.name for x in guild.roles]
        role_length = len(roles)
        roles = ', '.join(roles);
        channels = len(guild.channels);
        time = str(guild.created_at); time = time.split(' '); time= time[0];
        flag = str(guild.region)

        if any(word in flag for word in["eu", "us", "singapore", "sydney", "hongkong", "japan", "brazil", "russia"]):        
            if "eu" in flag:
                flag = str(":flag_eu:")
            if "us" in flag:
                flag = str(":flag_us:")
            if "singapore" in flag:
                flag = str(":flag_sg:")
            if "sydney" in flag:
                flag = str(":flag_au:")
            if "russia" in flag:
                flag = str(":flag_ru:")
            if "hongkong" in flag:
                flag = str(":flag_hk:")
            if "japan" in flag:
                flag = str(":flag_jp:")
            if "brazil" in flag:
                flag = str(":flag_br:")
        else:
            flag = str(1)
                               
        embed = discord.Embed(description= "(ID: " + str(guild.id) + ")",title = 'Info on ' + str(guild), colour = 0x0085ff);
        embed.set_thumbnail(url = guild.icon_url);
        embed.add_field(name = ' > Channels', value = "* " + str(channels) + " channels" + '\n' + "* AFK: " + str(guild.afk_channel) + '\n' + "* AFK Timeout: " + str(guild.afk_timeout));
        embed.add_field(name = ' > Members', value = "* " + str(guild.member_count) + " members" + '\n' + "* Owner: " + str(guild.owner) + '\n' + "* Owner ID: " + str(guild.owner.id));
        if flag == 1:
            embed.add_field(name = ' > Other', value = "* Server Region: '%s'"%str(guild.region) + '\n' + "* Created on: " + guild.created_at.__format__(' %d %B %Y at %H:%M:%S') + '\n' + "* Verification Level: " + str(guild.verification_level) + '\n' + "* Roles: '%s'"%str(role_length));
        else:
            embed.add_field(name = ' > Other', value = "* Server Region: '%s'"%str(guild.region) + " " + str(flag) +'\n' + "* Created on: " + guild.created_at.__format__(' %d %B %Y at %H:%M:%S') + '\n' + "* Verification Level: " + str(guild.verification_level) + '\n' + "* Roles: '%s'"%str(role_length));            
        try:
            await ctx.send(embed = embed);
        except:
            return await ctx.send(ctx.message.author.mention + " Embed links permission required." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
  
#g5
@client.command(pass_context=True)
async def roles(ctx):
    guild = ctx.message.guild
    roles = [x.name for x in guild.roles]
    role_length = len(roles)
    roles = ', '.join(roles);
    channels = len(guild.channels);
    
    embed = discord.Embed(description= "```" + (roles) + "```",title = 'Server roles', colour = 0x0085ff);
    
    if ctx.message.author.guild_permissions.manage_roles == False:
        if ctx.message.author.id == (ownerid):
            pass
        else:
            return await ctx.send(ctx.message.author.mention + " You don't have permission to use this command." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
    try:
        await ctx.send(embed = embed);
    except Exception as e:
        await ctx.send("An error occured. Error message: " + str(e))
  
    
#t1 - Mutes a Member From The server

@client.command(pass_context = True)
async def mute(ctx, member : discord.Member = None, time = 0, *, reason = None): #time : int = 0, reason : str = None):
    guild = ctx.message.guild
    channel = ctx.message.channel
    can_manage_roles = channel.permissions_for(guild.me).manage_roles
    role = discord.utils.get(guild.roles,name="Muted")

    if ctx.message.author.guild_permissions.kick_members == False:
        if ctx.message.author.id == (ownerid):
            pass
        else:
            return await ctx.send(ctx.message.author.mention + " You don't have permission to use this command." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
        
    if member == None:
        return await ctx.send(ctx.message.author.mention +  " No user mentioned." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
    
    if member.guild_permissions.kick_members == True:
        return await ctx.send(ctx.message.author.mention +  " I can't mute users with permission to kick members." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
   
    if can_manage_roles == False:
        return await ctx.send(ctx.message.author.mention + " I don't have permission to manage roles." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
    
    if not role:
        embed = discord.Embed(title="Please wait", description="I couldn't find Muted role, I'lll create it for you") # creates the embed 
        message = await ctx.send(embed = embed) # sends the message and assign it to the variable message
        roleks = guild.default_role
        overwrite = discord.PermissionOverwrite()
        overwrite = guild.default_role.permissions
        overwrite.send_messages = False
        belo = str("Muted")
        colour = discord.Colour.dark_grey()
        role = discord.utils.get(guild.roles,name="Muted")
        await asyncio.sleep(1)
        embed.description = "checkgate no. 1"
        await message.edit(embed = embed)
        await asyncio.sleep(1)
        try:
            embed.description = "I'm trying to create Muted role"
            await message.edit(embed = embed)
        except:
            pass
        try:           
            await guild.create_role(name = belo, colour = colour, hoist = False, mentionable = False)
        except Exception as e:
            embed.description = ("Failed to create Muted role, errormessage: " + str(e))
            return await message.edit(embed = embed)
        await asyncio.sleep(5)
        try:
            embed.description = "Muted role created successfully. Wait for me to finish the configuration"
            await message.edit(embed = embed)
        except:
            pass
        await asyncio.sleep(5)
        role = discord.utils.get(guild.roles,name="Muted")        
        moverwrite = discord.PermissionOverwrite()
        moverwrite = guild.default_role.permissions
        moverwrite.send_messages = False
        try:
            await role.edit(colour = colour, permissions = moverwrite)            
        except Exception as e:
            try:
                embed.description = "Something went wrong, it's likely that someone deleted the role. Please try to use the command again or contact Superplus#2392. // Error code: 'mute-2'"
                await message.edit(embed = embed)             
            except:
                pass
            await client.delete_role(guild, role)
            return
        try:      
            embed.description = "Role permissions have been changed."
            await message.edit(embed = embed)
        except:
            pass
        await asyncio.sleep(2)
        try:
            await role.edit(position = 1)
        except:
            pass
        embed.title = "Configuration complete"
        embed.description = "I have successfully created Muted role for you. Make sure this role has right position in role hierarchy and try to mute the user again if they haven't been muted yet."
        await message.edit(embed = embed)              
    role = discord.utils.get(guild.roles,name="Muted")
    member_roles = [r.name.lower() for r in member.roles] 
    if "muted" in member_roles:
        return await ctx.send(ctx.message.author.mention + " I can't mute this user, they are already muted." + '\n' + "-- This message will be deleted automatically in 30 seconds. --", delete_after=30)       
    try:
        if time == 0:
            return await ctx.send(ctx.message.author.mention +  " No valid mute duration entered." + '\n' + "-- This message will be deleted automatically in 30 seconds. --", delete_after=30)   
        time = int(time)
        if time > 10080 or time < 1:
            return await ctx.send(ctx.message.author.mention +  "Please enter a mute duration in valid time format. Enter the time in minutes (1-10080)" + '\n' + "-- This message will be deleted automatically in 30 seconds. --", delete_after=30)
        time = str(time)
    except Exception as e:
        return await ctx.send(ctx.message.author.mention +  " No mute duration entered in **valid time format**. Try to mute the user again. " + '\n' + "-- This message will be deleted automatically in 30 seconds. --", delete_after=30)
    pass
    try:
        await member.add_roles(role, reason = "chwilowo żaden")
    except Exception as e:
        await ctx.send(e)
        rolahigher = await ctx.send(ctx.message.author.mention +  " Couldn't assign a role to the player. Please check if the bot role is higher in role hierarchy that the Muted role. " + '\n' + "-- This message will be deleted automatically in 30 seconds. --")
        await asyncio.sleep(30)
        await client.delete_message(rolahigher)
        return
    mutestart = await ctx.send(":mute: **%s** is now muted for "%member.mention + str(time) +" minute(s)!")
    channel = ctx.message.channel
    
    join = discord.Embed(title = "Mute", colour = 0xFF7A00);
    join.add_field(name = 'User', value = str(member.mention) + '\n' + str(member));
    join.add_field(name = 'Moderator', value = str(ctx.message.author.mention) + '\n' + str(ctx.message.author));
    join.add_field(name = 'Duration', value = str(str(time) + " minute(s)"));
    join.add_field(name = 'Reason', value = str((reason)));
    join.set_footer(text ='Glop Blop v1.0');
        
    ujoin = discord.Embed(title = "Mute", colour = 0xFF7A00);
    ujoin.add_field(name = 'User', value = str(member.mention) + '\n' + str(member));
    ujoin.add_field(name = 'Moderator', value = str(ctx.message.author.mention) + '\n' + str(ctx.message.author));
    ujoin.add_field(name = 'Duration', value = str(str(time) + " minute(s)"));
    ujoin.set_footer(text ='Glop Blop v1.0');

    #if channel == channel:    #It used to be if reason == 1:
    if not reason:
        try:
            await ctx.send(embed = ujoin);
        except:
            await ctx.send("Moderator: " + str(ctx.message.author))
            return
    else:
        try:
            await ctx.send(embed = join);
        except:
            await ctx.send("Moderator: " + str(ctx.message.author) + ", reason: " + str(reason) + ".")
            return
        
    time = int(60*int(time))
    time = int(time)

    overwrite = channel.overwrites_for(role)
    overwrite.send_messages = False
    overwrite.add_reactions = False
    overwritebot = channel.overwrites_for(guild.me)
    overwritebot.send_messages = True 
    
    #overwrite = ctx.PermissionOverwrite()        
    #overwrite = channel.overwrites_for(role)
    #overwrite.send_messages = False
    #overwrite.add_reactions = False
    
    #overwritebot = channel.overwrites_for(guild.me)
    #overwritebot.send_messages = True     
    
    for TextChannel in guild.channels:
        try:
            await TextChannel.set_permissions(target=role, overwrite=overwrite)
        except Exception as f:
            pass    
    
    for TexChannel in guild.channels:
        try:
            await TextChannel.set_permissions(target=guild.me, overwrite=overwritebot)
        except Exception as f:
            pass    
    await asyncio.sleep(time)
    role = discord.utils.get(guild.roles,name="Muted")
    member_roles = [r.name.lower() for r in member.roles]
    if "muted" in member_roles:
        try:
            await member.remove_roles(role, reason = "Auto")
        except Exception as e:
            if 'Forbidden' in str(e):
                return await ctx.send(ctx.message.author.mention + " I tried to unmute **" + str(member) + "** but I don't have necessary permissions to do so.")
            else:
                return await ctx.send(ctx.message.author.mention + " I tried to unmute **" + str(member) + "** but I couldn't do so.")
        await ctx.send(":loud_sound: **%s** is now unmuted!"%member.mention)
    return





#t2 - Unmutes a member

@client.command(pass_context = True)
async def unmute(ctx, *, member : discord.Member = None):
    try:
    
        user_roles = [r.name.lower() for r in ctx.message.author.roles] 
        server = ctx.message.guild
        channel = ctx.message.channel
        can_manage_roles = channel.permissions_for(guild.me).manage_roles
        role = discord.utils.get(guild.roles,name="Muted")  

        if ctx.message.author.guild_permissions.kick_members == False:
            if ctx.message.author.id == (ownerid):
                pass
            else:
                return await ctx.send(ctx.message.author.mention + " You don't have permission to use this commmand." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
              
        if member == None:
            return await ctx.send(ctx.message.author.mention +  " No user mentioned." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
      
        member_roles = [r.name.lower() for r in member.roles]
        
        if can_manage_roles == False:
            return await ctx.send(ctx.message.author.mention + " I don't have permission to manage roles." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
             
        if "muted" not in member_roles:
            return await ctx.send(ctx.message.author.mention + " I can't unmute them, they're not muted." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
              
        pass
        try:
            await client.remove_roles(member, role)
        except Exception as e:
            if 'Forbidden' in str(e):
                return await ctx.send(ctx.message.author.mention + " I tried to unmute **" + str(member) + "** but I don't have necessary permissions to do so."+ '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
            else:
                return await ctx.send(ctx.message.author.mention + " I tried to unmute **" + str(member) + "** but I couldn't do so."+ '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
        await ctx.send(":loud_sound: **%s** is now unmuted!"%member.mention)
        
    except Exception as e:
        print (e)
        await ctx.send(e)

#t3        
@client.command(pass_context = True)
async def delwarn(ctx, *, member : discord.Member = None):

    user_roles = [r.name.lower() for r in ctx.message.author.roles] 
    server = ctx.message.guild
    channel = ctx.message.channel
    can_manage_roles = channel.permissions_for(guild.me).manage_roles
    role = discord.utils.get(server.roles,name="Ping Warning")  

    if ctx.message.author.server_permissions.kick_members == False:
        if ctx.message.author.id == (ownerid):
            pass
        else:
            return await ctx.send(ctx.message.author.mention + " You don't have permission to use this commmand." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
        
    if member == None:
        return await ctx.send("```" + str(ctx.message.author) +  ", no user mentioned." + '\n' + "-- This message will be deleted automatically in 30 seconds. --```", delete_after=30)
    member_roles = [r.name.lower() for r in member.roles]
        
    if can_manage_roles == False:
        return await ctx.send("```" + str(ctx.message.author) + ", I don't have permission to manage roles." + '\n' + "-- This message will be deleted automatically in 30 seconds. --```", delete_after=30)
       
    if "ping warning" not in member_roles:
        return await ctx.send("```" + str(ctx.message.author) + ", this user doesn't have Ping Warning role." + '\n' + "-- This message will be deleted automatically in 30 seconds. --```", delete_after=30)       
    pass
        
    await client.remove_roles(member, role)
    await ctx.send("**" + str(member) + "** has no longer Ping Warning role!")

        
#t4 - Clears The Chat

@client.command(pass_context=True)       
async def purge(ctx, number : int = 34871):
    '''Clears The Chat 2-100'''
    user_roles = [r.name.lower() for r in ctx.message.author.roles]
    guild = ctx.message.guild
    channel = ctx.message.channel
    can_deletemessages = channel.permissions_for(guild.me).manage_messages
    can_sendmessages = channel.permissions_for(guild.me).send_messages
    
    if ctx.message.author.guild_permissions.manage_messages == False:
        if ctx.message.author.id == (ownerid):
            pass
        else:        
            return await ctx.send(ctx.message.author.mention + " You don't have permission to use this command." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
    
    if  not can_deletemessages:
        return await ctx.send(ctx.message.author.mention + " Manage messages permission required." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
    
    if not number > 1 or not number <= 100:
        return await ctx.send(ctx.message.author.mention + " You can only delete messages in the range of [2, 100]." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
    try:
        await ctx.message.delete()
    except Exception as e:
        return await ctx.send(e)
    mgs = []
    number1 = int(number)
    data = (ctx.message.created_at - timedelta(days = 14, minutes = -1)) ####Zajebiscie wazne, wiec niczego tu nie zmieniac
    deleted = await channel.purge(limit=number1, after=data)
    if len(deleted) == 0:
        await asyncio.sleep(1)
        return await ctx.send("No messages to delete.")
    if len(deleted) == 1:
        await asyncio.sleep(1)
        return await ctx.send('Successfully deleted 1 message.')
    await asyncio.sleep(1)
    await ctx.send('Successfully deleted {} messages.'.format(len(deleted)))

#t5
@client.command(pass_context = True)
async def lockdown(ctx):
    channel = ctx.message.channel
    guild = ctx.message.guild
    roleks = guild.default_role
    overwrite = discord.PermissionOverwrite()
    user_roles = [r.name.lower() for r in ctx.message.author.roles]

    try:
        if ctx.message.author.id == (ownerid):
            pass
        else:
            belo = int(guild.id)
            #if belo == 469888879487483934: #checks if the command runs on my private server
            if channel.overwrites_for(ctx.message.author).manage_channels == False:
                return await ctx.send(ctx.message.author.mention + " You don't have permission to manage this channel." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
            if channel.overwrites_for(ctx.message.author).manage_channels == None:
                if ctx.message.author.guild_permissions.manage_channels == True:
                    pass
                else:
                    return await ctx.send(ctx.message.author.mention + " You don't have permission to manage this channel." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
            else:
                pass
            #else:
             #   if ctx.message.author.guild_permissions.ban_members == False:  
              #      return await ctx.send(ctx.message.author.mention + " You don't have permission to use this command." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
        
        overwrite = channel.overwrites_for(roleks)
        overwrite.send_messages = False

        overwritebot = channel.overwrites_for(guild.me)
        overwritebot.send_messages = True
    
        try:
            await channel.set_permissions(target=roleks, overwrite=overwrite)
            await channel.set_permissions(target=guild.me, overwrite=overwritebot)
        except Exception as e:
            await ctx.send("```" + str(e) + "```")
            return
        await ctx.send("The channel has been locked.")
    except Exception as f:
        await ctx.send(str(f) + "cos sie zepsulo")
        
        
#t6
@client.command(pass_context = True)
async def slock(ctx):
    channel = ctx.message.channel
    guild = ctx.message.guild
    roleks = guild.default_role
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    
    if ctx.message.author.guild_permissions.ban_members == False:
        if ctx.message.author.id == (ownerid):
            pass
        else:        
            return await ctx.send(ctx.message.author.mention + " You don't have permission to use this command." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
    pass

    overwrite = guild.default_role.permissions
    overwrite.send_messages = False

    overwritebot = channel.overwrites_for(guild.me)
    overwritebot.send_messages = True  
    try:
        await roleks.edit(permissions = overwrite)
        #await (guild.me).edit(permissions = overwritebot)
    except Exception as e:
        await ctx.send("```" + str(e) + "```")
        return
    try:
        await channel.set_permissions(target=guild.me, overwrite=overwritebot)
    except:
        pass
    await ctx.send("All of the channels have been locked.")   
    
#t7
@client.command(pass_context = True)
async def unlock(ctx):
    channel = ctx.message.channel
    guild = ctx.message.guild
    roleks = guild.default_role
    overwrite = discord.PermissionOverwrite()
    try:
        if ctx.message.author.id == (ownerid):
            pass
        else:
            belo = int(guild.id)
            if belo == 469888879487483934: #checks if the command runs on my private server
                if channel.overwrites_for(ctx.message.author).manage_channels == False:
                    return await ctx.send(ctx.message.author.mention + " You don't have permission to manage this channel." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
                if channel.overwrites_for(ctx.message.author).manage_channels == None:
                    if ctx.message.author.guild_permissions.manage_channels == True:
                        pass
                    else:
                        return await ctx.send(ctx.message.author.mention + " You don't have permission to manage this channel." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
                else:
                    pass
            else:
                if ctx.message.author.guild_permissions.ban_members == False:  
                    return await ctx.send(ctx.message.author.mention + " You don't have permission to use this command." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
                else:
                    pass


        overwrite = channel.overwrites_for(roleks)
        overwrite.send_messages = True

        overwritebot = channel.overwrites_for(guild.me)
        overwritebot.send_messages = True
    
        try:
            await channel.set_permissions(target=roleks, overwrite=overwrite)
            await channel.set_permissions(target=guild.me, overwrite=overwritebot)
        except Exception as e:
            await ctx.send("```" + str(e) + "```")
            return
        await ctx.send("The channel has been locked.")
    except Exception as f:
        await ctx.send(str(f) + "cos sie zepsulo")



##############        
    overwrite = channel.overwrites_for(roleks)
    overwrite.send_messages = None
    
    try:
        await client.edit_channel_permissions(channel, roleks, overwrite)
    except Exception as e:
        await ctx.send("```" + str(e) + "```")
        return
    await ctx.send("'Send messages' permission for server default role for this channel has been changed to 'None'.")   

#t8
@client.command(pass_context = True)
async def sunlock(ctx):
    channel = ctx.message.channel
    guild = ctx.message.guild
    roleks = guild.default_role
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = True
    role = discord.utils.get(guild.roles,name="everyone")
    
    if ctx.message.author.guild_permissions.ban_members == False:
        if ctx.message.author.id == (ownerid):
            pass
        else:        
            return await ctx.send(ctx.message.author.mention + " You don't have permission to use this command." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
    pass

    overwrite = guild.default_role.permissions
    overwrite.send_messages = True
    
    try:
        await roleks.edit(permissions = overwrite)
    except Exception as e:
        await ctx.send("```" + str(e) + "```")
        return
    await ctx.send("All of the channels have been unlocked.")  
    
    
#t9
@client.command(pass_context = True)
async def warn(ctx, member : discord.Member = None, *, reason : str = 1):
    
    guild = ctx.message.guild
    role = discord.utils.get(guild.roles,name="Mute")
    channel = ctx.message.channel
    can_manage_roles = channel.permissions_for(guild.me).manage_roles
    can_send_messages = channel.permissions_for(guild.me).send_messages
    #belo = int(server.id)  
    #if not belo == 359426518730145802: #checks if the command runs on my private 
        #await client.say("ugabanga!")
        #return
    if ctx.message.author.guild_permissions.kick_members == False:
        if ctx.message.author.id == (ownerid):
            pass
        else:
            return await ctx.send(ctx.message.author.mention + " You don't have permission to use this command." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
    
    if can_manage_roles == False:
        return await ctx.send(ctx.message.author.mention + " I don't have permission to manage roles." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10) 
    if can_send_messages == False:
        return await ctx.send(ctx.message.author.mention + " I don't have permission to manage roles." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)        
    if member == None:
        return await ctx.send(ctx.message.author.mention +  " No user mentioned." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
    if reason == 1:
        return await ctx.send(ctx.message.author.mention +  " No reason entered." + '\n' + "-- This message will be deleted automatically in 30 seconds. --", delete_after=10)
    pass

    blindedrole = discord.utils.get(guild.roles,name="Blinded")
    warn1role = discord.utils.get(guild.roles,name="First Warning")
    warn2role = discord.utils.get(guild.roles,name="Second Warning")
    warn3role = discord.utils.get(guild.roles,name="Third Warning")
    
    member_roles = [r.name.lower() for r in member.roles]
    
    if "blinded" in member_roles:
        return await ctx.send(ctx.message.author.mention + ", I can't warn this user, they are already blinded."  + '\n' + "-- This message will be deleted automatically in 30 seconds. --", delete_after=30)
               
    if "third warning" in member_roles:
        try:
            await client.add_roles(member, blindedrole)
        except:
            return await ctx.send(ctx.message.author.mention + ", I couldn't find `Blinded` role or it's the higher rank than my highest role."  + '\n' + "-- This message will be deleted automatically in 30 seconds. --", delete_after=10)
        await ctx.send(":warning: " + (member.mention) + ", you have been blinded for disregarding the previous three warnings." '\n' + '\n' + "**Reason: ** ```" + str(reason) + "```")
        try:
            await client.remove_roles(member, warn3role)
        except:
            pass
        await asyncio.sleep(1)
        try:
            await client.remove_roles(member, warn2role)
        except:
            pass
        await asyncio.sleep(1)
        try:
            await client.remove_roles(member, warn1role)
        except:
            pass
        return await ctx.send(member, ":warning: " + (member.mention) + ", you have been blinded for disregarding the previous three warnings. Server name: " + str(guild) +'\n' + '\n' + "**Reason: ** ```" + str(reason) + "```")
    if "second warning" in member_roles:
        try:
            await client.add_roles(member, warn3role)
        except:
            return await ctx.send(ctx.message.author.mention + ", I couldn't find `Third Warning` role or it's the higher rank than my highest role."  + '\n' + "-- This message will be deleted automatically in 30 seconds. --", delete_after=30)
        await ctx.send(":warning: " + (member.mention) + ", you have been warned. This is your third warning." '\n' + '\n' + "**Reason: ** ```" + str(reason) + "```")
        try:
            await client.remove_roles(member, warn2role)
        except:
            pass
        await asyncio.sleep(1)
        try:
            await client.remove_roles(member, warn1role)
        except:
            pass
        return await ctx.send(member, str(member) + ", you have been warned. Server name: " + str(guild) +'\n' + '\n' + "**Reason: ** ```" + str(reason) + "```")  
    
    if "first warning" in member_roles:
        try:
            await client.add_roles(member, warn2role)
        except:
            return await ctx.send(ctx.message.author.mention + ", I couldn't find `Second Warning` role or it's the higher rank than my highest role." + '\n' + "-- This message will be deleted automatically in 30 seconds. --", delete_after=30)
        await ctx.send(":warning: " + (member.mention) + ", you have been warned. This is your second warning." '\n' + '\n' + "**Reason: ** ```" + str(reason) + "```") 
        try:
            await client.remove_roles(member, warn1role)
        except:
            pass
        return await ctx.send(member, str(member) + ", you have been warned. Server name: " + str(guild) +'\n' + '\n' + "**Reason: ** ```" + str(reason) + "```")    
    else:
        try:
            await client.add_roles(member, warn1role)
        except:
            return await ctx.send(ctx.message.author.mention + ", I couldn't find `First Warning` role or it's the higher rank than my highest role." + '\n' + "-- This message will be deleted automatically in 30 seconds. --", delete_after=30)
        await ctx.send(":warning: " + (member.mention) + ", you have been warned. This is your first warning." '\n' + '\n' + "**Reason: ** ```" + str(reason) + "```")
        try:
            return await ctx.send(member, str(member) + ", you have been warned. Server name: " + str(guild) +'\n' + '\n' + "**Reason: ** ```" + str(reason) + "```")
        except:
            pass
        return    
    
#t10 - Kicks a Member From The Server

@client.command(pass_context = True)
async def kick(ctx, member : discord.Member = None, *, reason : str = 1):
    """Kicks specified member from the server."""
    
    guild = ctx.message.guild
    channel = ctx.message.channel
    can_kick = channel.permissions_for(guild.me).kick_members
  
    if ctx.message.author.guild_permissions.kick_members == False:
        if ctx.message.author.id == (ownerid):
            pass
        else:
            missed = await client.say(ctx.message.author.mention + " You don't have permission to kick members." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
            await asyncio.sleep(10)
            await client.delete_message(missed)
            return
    
    if not can_kick:
        wong = await client.say(ctx.message.author.mention + " I don't have permission to kick members." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
        await asyncio.sleep(10)
        await client.delete_message(wong)
        return
    
    if member == None:
        spec = await client.say(ctx.message.author.mention + " No user mentioned." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
        await asyncio.sleep(10)
        await client.delete_message(spec)
        return

    #    if any(word in message.content for word in["bitch", "dick", "porn", "fuck"]

    user_roles = [r.name.lower() for r in ctx.message.author.roles]
    member_roles = [r.name.lower() for r in member.roles]
    
                
    if member.id == ctx.message.author.id:
        self = await client.say(ctx.message.author.mention + ", you cannot kick yourself." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
        await asyncio.sleep(10)
        await client.delete_message(self)
        return
    
    if member.guild_permissions.manage_messages == True:
        wong = await client.say(ctx.message.author.mention + " I can't ban members with permission to Manage Messages." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
        await asyncio.sleep(10)
        await client.delete_message(wong)
        return 
    
    pass
               
    try:
        await client.kick(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            lol = await client.say(ctx.message.author.mention +  "I can't kick this user." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
            await asyncio.sleep(10)
            await client.delete_message(lol)
            return
    channel = ctx.message.channel
    time = str(guild.created_at); time = time.split(' '); time= time[0];

    join = discord.Embed(title = "Kick", colour = 0xF00000);
    join.add_field(name = 'USER', value = str(member.mention) + '\n' + str(member) + '\n' + str(member.id));
    join.add_field(name = 'MODERATOR', value = str(ctx.message.author.mention) + '\n' + str(ctx.message.author));
    join.add_field(name = 'REASON', value = str((reason)));
    join.set_footer(text = 'Glop Blop v1.0');
        
    ujoin = discord.Embed(title = "Kick", colour = 0xF00000);
    ujoin.add_field(name = 'USER', value = str(member.mention) + '\n' + str(member) + '\n' + str(member.id));
    ujoin.add_field(name = 'MODERATOR', value = str(ctx.message.author.mention) + '\n' + str(ctx.message.author));
    ujoin.set_footer(text = 'Glop Blop v1.0');


    if reason == 1:
        try:
            await client.say(embed = ujoin);
        except:
            await client.say(str(member) + " has been kicked.")
    else:
        try:
            await client.say(embed = join);
        except:
            await client.say(str(member) + " has been kicked. Reason:" + str(reason))
    return

#t11 - BAN DZIALA #

@client.command(pass_context = True)
async def ban(ctx, member : discord.Member = None, *, reason : str = 1):
    """Bans specified member from the server."""
    
    guild = ctx.message.guild
    channel = ctx.message.channel
    can_ban = channel.permissions_for(guild.me).ban_members
  
    if ctx.message.author.guild_permissions.ban_members == False:
        if ctx.message.author.id == (ownerid):
            pass
        else:
            missed = await client.say(ctx.message.author.mention + " You don't have permission to ban members." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
            await asyncio.sleep(10)
            await client.delete_message(missed)
            return
    
    if not can_ban:
        wong = await client.say(ctx.message.author.mention + " I don't have permission to ban members." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
        await asyncio.sleep(10)
        await client.delete_message(wong)
        return
    
    if member == None:
        spec = await client.say(ctx.message.author.mention + " No user mentioned." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
        await asyncio.sleep(10)
        await client.delete_message(spec)
        return

    #    if any(word in message.content for word in["bitch", "dick", "porn", "fuck"]
    belo = int(guild.id)
    user_roles = [r.name.lower() for r in ctx.message.author.roles]
    member_roles = [r.name.lower() for r in member.roles]
      
                
    if member.id == ctx.message.author.id:
        self = await client.say(ctx.message.author.mention + ", you cannot ban yourself." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
        await asyncio.sleep(10)
        await client.delete_message(self)
        return   
    if member.guild_permissions.manage_messages == True:
        wong = await client.say(ctx.message.author.mention + " I can't ban members with permission to Manage Messages." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
        await asyncio.sleep(10)
        await client.delete_message(wong)
        return 
    
    pass
               
    try:
        await client.ban(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            lol = await client.say(ctx.message.author.mention +  "I can't ban this user." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
            await asyncio.sleep(10)
            await client.delete_message(lol)
            return
    channel = ctx.message.channel
    time = str(guild.created_at); time = time.split(' '); time= time[0];

    join = discord.Embed(title = ":regional_indicator_b: :regional_indicator_a: :regional_indicator_n:", colour = 0xF00000);
    join.add_field(name = 'USER', value = str(member.mention) + '\n' + str(member) + '\n' + str(member.id));
    join.add_field(name = 'MODERATOR', value = str(ctx.message.author.mention) + '\n' + str(ctx.message.author));
    join.add_field(name = 'REASON', value = str((reason)));
    join.set_footer(text = 'Glop Blop v1.0');
        
    ujoin = discord.Embed(title = ":regional_indicator_b: :regional_indicator_a: :regional_indicator_n:", colour = 0xF00000);
    ujoin.add_field(name = 'USER', value = str(member.mention) + '\n' + str(member) + '\n' + str(member.id));
    ujoin.add_field(name = 'MODERATOR', value = str(ctx.message.author.mention) + '\n' + str(ctx.message.author));
    ujoin.set_footer(text = 'Glop Blop v1.0');


    if reason == 1:
        try:
            await client.say(embed = ujoin);
        except:
            await client.say(str(member) + " has been banned.")
    else:
        try:
            await client.say(embed = join);
        except:
            await client.say(str(member) + " has been banned. Reason:" + str(reason))
    return


#t12
@client.command(pass_context=True)
async def soft(ctx, user: discord.Member = None, *, reason: str = None):
    """Kicks the user, deleting 1 day worth of messages."""
    guild = ctx.message.guild
    channel = ctx.message.channel
    can_ban = channel.permissions_for(guild.me).ban_members
    author = ctx.message.author

    if ctx.message.author.guild_permissions.ban_members == False:
        if ctx.message.author.id == (ownerid):
            pass
        else:        
            missed = await client.say(ctx.message.author.mention + " You don't have permission to ban members." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
            await asyncio.sleep(10)
            await client.delete_message(missed)
            return

    if not can_ban:
        wong = await client.say(ctx.message.author.mention + " I don't have permission to ban members." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
        await asyncio.sleep(10)
        await client.delete_message(wong)
        return
        
    if user == None:
        spec = await client.say(ctx.message.author.mention + " No user mentioned." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
        await asyncio.sleep(10)
        await client.delete_message(spec)
        return

    if user == ctx.message.author:
        self = await client.say(ctx.message.author.mention + ", you cannot ban yourself." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
        await asyncio.sleep(10)
        await client.delete_message(self)
        return
    
    if user.guild_permissions.manage_messages == True:
        wong = await client.say(ctx.message.author.mention + " I can't ban members with permission to Manage Messages." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
        await asyncio.sleep(10)
        await client.delete_message(wong)
        return
    
    member_roles = [r.name.lower() for r in author.roles]    

        
        
    try:
        invite = await client.create_invite(ctx.message.channel,max_uses=1,xkcd=True)        
        invite = invite.url

    except:
        invite = ""

    
    try:
        msg = await client.send_message(user, " You have been softbanned. Now, you can join the server again:" + invite)
    except:
        pass
    try:
        await client.ban(user, 1)
    except: 
        clog = await client.say(ctx.message.author.mention + " I can't ban this user." + '\n' + "-- This message will be deleted automatically in 10 seconds. --", delete_after=10)
        await asyncio.sleep(10)
        await client.delete_message(clog)
        return
    
    await client.unban(guild, user)
    
    if reason == None:
        await client.say("**" + str(user) + "** has been softbanned by **" + str(author) + "**.")
    else:
        await client.say("**" + str(user) + "** has been softbanned by **" + str(author) + "**, reason: " + str(reason))
    

        

    
 ###############################----------------------########################### 
                                ##~~~~In DEVELOPMENT ~~~~####
   
@client.command()
async def add(x: int, y: int = 1):
    """Adds 2 numbers together, if the 2nd number is not provided, it will add 1"""
    await client.say('answer: {}'.format(x+y))

@client.command(pass_context = True)
async def now(ctx):
    colour = discord.Colour.magenta()
    date = datetime.now().strftime("**Date: **%A, %B %d, %Y\n**Time: **%I:%M:%S %p")
    embed = discord.Embed(color = colour)
    embed.add_field(name="Bot's System Date & Time", value=date, inline=False)
    await client.say(embed=embed)
#must import os

client.run(os.getenv('TOKEN'))  
