print("""###########################
# modmail.py setup script #
###########################
""")
BotToken = input("\nPlease input the bot token; ").strip()
MessageChannel = input("Please input the modmail text channel (channel that mods recieve messages in); ").strip()
print("\nPlease confirm these details are correct;\nBot token; " + BotToken + "\nMod message channel; " + MessageChannel)
yn = input("\nAre these details correct (y/n); ")

if yn == "y":
    print("\nWriting config file now...")
    ConfigFile = open("./config.txt", "w")
    ConfigFile.writelines(BotToken + "\n" + MessageChannel)
    ConfigFile.close()
    input("Config file written, please press enter to exit...")
elif yn == "n":
    print("Please run this script again and type 'y' to confirm the details are correct")
else:
    print("Please run this script again and type 'y' or 'n'")