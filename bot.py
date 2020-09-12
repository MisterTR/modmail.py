# bot token and prefix
BOTPREFIX = "$"
BOTTOKEN = ""
MODMAILCHANNEL = 

# imports
import discord
from discord.ext.commands import Bot

# declaring the client object
client = Bot(command_prefix = BOTPREFIX)

# removing the default help command so that a better one can be made using embeds
client.remove_command("help")

# changing the bot's status to "Listening to $help" and printing that the bot has logged in without any issues
@client.event
async def on_ready():
    ListeningTo = discord.Activity(type=discord.ActivityType.listening, name="dms to contact mods")
    await client.change_presence(status=discord.Status.online, activity=ListeningTo)
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(ctx):
    # checking that the message is a DM
    if isinstance(ctx.channel, discord.channel.DMChannel) and ctx.author != client.user:

        ThreadNumberText = open("./Tickets/ThreadNumber.txt", "r")
        ThreadNumber = int(ThreadNumberText.readline())
        ThreadNumberText.close()
        ThreadNumberText = open("./Tickets/ThreadNumber.txt", "w")
        
        if ThreadNumber == 3:
            ThreadNumber = 1
            ThreadNumberText.writelines(str(ThreadNumber))
            ThreadNumberText.close()
        else:
            ThreadNumber = ThreadNumber + 1
            ThreadNumberText.writelines(str(ThreadNumber))
            ThreadNumberText.close()


        # sending an embed to the modmail channel so the mods can view it
        channel = client.get_channel(MODMAILCHANNEL)
        ChannelEmbed = discord.Embed(
            colour = discord.Colour.light_gray()
        )
        ChannelEmbed.set_author(name = "ModMail", icon_url = "https://img.icons8.com/dusk/64/000000/mailbox-closed-flag-down.png")
        ChannelEmbed.add_field(name = "Sender", value = ctx.author, inline=False)
        ChannelEmbed.add_field(name = "Message", value = ctx.content, inline=False)
        ChannelEmbed.set_footer(text = "Thread number: " + str(ThreadNumber), icon_url = "https://img.icons8.com/dusk/64/000000/mailbox-closed-flag-down.png")
        await channel.send(embed = ChannelEmbed)

        # sending an embed to the user 
        UserEmbed = discord.Embed(
            colour = discord.Colour.light_gray()
        )
        UserEmbed.set_author(name = "ModMail", icon_url = "https://img.icons8.com/dusk/64/000000/mailbox-closed-flag-down.png")
        UserEmbed.add_field(name = "Your message has been sent", value = "Your message has been sent to a moderator and is now waiting for a reply, please be patient. The reply will be sent in this thread.")
        await ctx.channel.send(embed = UserEmbed)

        
        Thread1Text = open("./Tickets/thread" + str(ThreadNumber) + ".txt", "w")
        Thread1Text.writelines(str(ctx.author.id))
        Thread1Text.close()
    else:
        await client.process_commands(ctx)
        return;

@client.command()
async def ping(ctx):
    await ctx.send("pong")
    print("pong")

@client.command(name = "thread1")
async def thread1(ctx):
    Thread1Text = open("./Tickets/thread1.txt")
    Thread1 = Thread1Text.readline()
    Thread1Text.close()
    user = client.get_user(int(Thread1))
    print(user)
    ReplyEmbed = discord.Embed(
        colour = discord.Colour.light_grey()
    )
    ReplyEmbed.set_author(name = "ModMail", icon_url = "https://img.icons8.com/dusk/64/000000/mailbox-closed-flag-down.png")
    ReplyEmbed.add_field(name = "Response from:", value = ctx.author, inline = False)
    ReplyEmbed.add_field(name = "Response content:", value = ctx.message.content[9:], inline = False)

    await user.send(embed = ReplyEmbed)


@client.command(name = "thread2")
async def thread2(ctx):
    Thread1Text = open("./Tickets/thread2.txt")
    Thread1 = Thread1Text.readline()
    Thread1Text.close()
    user = client.get_user(int(Thread1))
    print(user)
    ReplyEmbed = discord.Embed(
        colour = discord.Colour.light_grey()
    )
    ReplyEmbed.set_author(name = "ModMail", icon_url = "https://img.icons8.com/dusk/64/000000/mailbox-closed-flag-down.png")
    ReplyEmbed.add_field(name = "Response from:", value = ctx.author, inline = False)
    ReplyEmbed.add_field(name = "Response content:", value = ctx.message.content[9:], inline = False)

    await user.send(embed = ReplyEmbed)


@client.command(name = "thread3")
async def thread3(ctx):
    Thread1Text = open("./Tickets/thread3.txt")
    Thread1 = Thread1Text.readline()
    Thread1Text.close()
    user = client.get_user(int(Thread1))
    print(user)
    ReplyEmbed = discord.Embed(
        colour = discord.Colour.light_grey()
    )
    ReplyEmbed.set_author(name = "ModMail", icon_url = "https://img.icons8.com/dusk/64/000000/mailbox-closed-flag-down.png")
    ReplyEmbed.add_field(name = "Response from:", value = ctx.author, inline = False)
    ReplyEmbed.add_field(name = "Response content:", value = ctx.message.content[9:], inline = False)

    await user.send(embed = ReplyEmbed)

client.run(BOTTOKEN)