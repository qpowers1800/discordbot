

TOKEN = "REMOVED TOKEN FOR SECURITY"

import discord
import asyncio
import random

info = 'As the founding student chapter, Temple AIS upholds an engaging and well-developed focal point for students studying Management Information Systems, or students interested in the practice of MIS, through professional development, social events, and community activities.'

motivation = {0:'“We cannot solve problems with the kind of thinking we employed when we came up with them.” — Albert Einstein', 1: '“Learn as if you will live forever, live like you will die tomorrow.” — Mahatma Gandhi', 2:'“Develop success from failures. Discouragement and failure are two of the surest stepping stones to success.” —Dale Carnegie', 3: '“Education is the most powerful weapon which you can use to change the world.” — Nelson Mandela', 4:'“You' + "'" + 'll find that education is just about the only thing lying around loose in this world, and it' + "'" + 's about the only thing a fellow can have as much of as he' + "'" + 's willing to haul away.” —John Graham', 5: '“Although you may not always be able to avoid difficult situations, you can modify the extent to which you can suffer by how you choose to respond to the situation. — Dalai Lama”'}

################
def getEvents():
    file= open("AISevents.txt", "r", encoding = "UTF8")
    text = file.read()
    return text
    
def addEvent(date,name,location):
    #print(date,name,location)
    string = 'Date:' + date + ' Name:' + name + ' Location:' + location
    #print(string)
    filename = 'AISevents.txt'
    outfile = open(filename, "a")
    outfile.write(string + '\n\n')
    outfile.close()
    return 'Event Added!'

def getQuote():
    randomnum = random.randint(0,5)
    return motivation[randomnum]


###############################################

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')


    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send("Hello! I'm the AIS Bot." + ' Type "$info" to learn what I can do!')
            return

        if message.content.startswith('$info'):
            await message.channel.send('$events returns a list of upcoming events \n $addevent adds a new event to the list (admin only) \n $AIS returns basic info on the organization \n $motivation gives you a random motivational quote')
            return

        if message.content.startswith('$motivation'):
            quote  = getQuote()
            await message.channel.send(quote)
            return

        if message.content.startswith('$events'):
            events  = getEvents()
            await message.channel.send(events)
            return
            
        if message.content.startswith('$addevent'):
            channel = message.channel
            if channel == 'announcements':
                await message.channel.send('Sorry this command can only be used in the admin channel')
                return
            
            await message.channel.send('When is the event?')
            try:
                date =await self.wait_for('message',timeout=10.0)
                date= date.content
                print(date)
            except asyncio.TimeoutError:
                await message.channel.send('Sorry, you took to long. Request Cancelled.')
                return
            
            await message.channel.send('What is the name of the event?')
            try:
                name =await self.wait_for('message',timeout=10.0)
                name= name.content
                print(name)
            except asyncio.TimeoutError:
                await message.channel.send('Sorry, you took to long. Request Cancelled.')
                return
            
            await message.channel.send('Where is the event?')
            try:
                location =await self.wait_for('message',timeout=10.0)
                location= location.content
                print(location)
            except asyncio.TimeoutError:
                await message.channel.send('Sorry, you took to long. Request Cancelled.')
                return
            
            result = addEvent(date,name,location)
            await message.channel.send(result)
            
        if message.content.startswith('$AIS'):
            await message.channel.send(info)
            return
        if message.content.startswith('$officehours'):
            await message.channel.send(info)
            return
            
client = MyClient()
    
client.run(TOKEN)





