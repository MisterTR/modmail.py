# bot token and prefix
BOTPREFIX = "/"
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
    ListeningTo = discord.Activity(type=discord.ActivityType.listening, name="to your concerns")
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

        
        ThreadText = open("./Tickets/thread" + str(ThreadNumber) + ".txt", "w")
        ThreadText.writelines(str(ctx.author.id))
        ThreadText.close()
    else:
        await client.process_commands(ctx)
        return;


@client.command()
async def ping(ctx):
    await ctx.send("pong")
    print("pong")


@client.command(name = "thread")
async def thread(ctx):
    MessageContent = ctx.message.content
    MessageSplit = MessageContent.split(" ")
    ThreadNumber = MessageSplit[1]
    ThreadNumberLen = len(ThreadNumber)
    MessageIndex = ThreadNumberLen + 8
    ModReply = MessageContent[MessageIndex:]

    ThreadText = open("./Tickets/thread" + ThreadNumber + ".txt")
    Thread = ThreadText.readline()
    ThreadText.close()
    user = client.get_user(int(Thread))

    ReplyEmbed = discord.Embed(
        colour = discord.Colour.light_gray()
    )
    ReplyEmbed.set_author(name = "ModMail", icon_url = "https://img.icons8.com/dusk/64/000000/mailbox-closed-flag-down.png")
    ReplyEmbed.add_field(name = "Response from:", value = ctx.author, inline = False)
    ReplyEmbed.add_field(name = "Response content:", value = ModReply, inline = False)

    ConfirmEmbed = discord.Embed(
        colour = discord.Colour.light_gray()
    )
    ConfirmEmbed.set_author(name = "ModMail - Sent message", icon_url = "https://img.icons8.com/dusk/64/000000/mailbox-closed-flag-down.png")
    ConfirmEmbed.add_field(name = "Sent to:", value = user, inline = False)
    ConfirmEmbed.add_field(name = "Response content:", value = ModReply, inline = False)
    ConfirmEmbed.set_footer(text = "Thread number: " + str(ThreadNumber), icon_url = "https://img.icons8.com/dusk/64/000000/mailbox-closed-flag-down.png")

    await user.send(embed = ReplyEmbed)
    await ctx.send(embed = ConfirmEmbed)

@client.command(name = "help")
async def help(ctx):
    HelpEmbed = discord.Embed(
        colour = discord.Colour.light_gray()
    )
    HelpEmbed.set_author(name = "ModMail help", icon_url = "https://img.icons8.com/dusk/64/000000/mailbox-closed-flag-down.png")
    HelpEmbed.add_field(name = "How to contact mods:", value = "To contact a moderator, please send a dm to this bot, you will recieve a reply in the same thread afterwards", inline = False)

    await ctx.send(embed = HelpEmbed)


client.run(BOTTOKEN)