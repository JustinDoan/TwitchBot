#!/usr/bin/env python3

import re
import socket
import math
import random
from lxml import html
import requests
import time
import json
import UserJson as UJ
# --------------------------------------------- Start Settings ----------------------------------------------------
HOST = "irc.twitch.tv"                          # Hostname of the IRC-Server in this case twitch's
PORT = 6667                                     # Default IRC-Port
CHAN = "#ydibz"                               # Channelname = #{Nickname}
NICK = "soxyfoxy25"                                # Nickname = Twitch username
PASS = "oauth:qielsaps3wtodw4tglxymgncqdhpdw"   # www.twitchapps.com/tmi/ will help to retrieve the required authkey
flag = 0
info = ""
msg2 = ""

# --------------------------------------------- End Settings -------------------------------------------------------


# --------------------------------------------- Start Functions ----------------------------------------------------
def send_pong(msg):
    con.send(bytes('PONG %s\r\n' % msg, 'UTF-8'))


def send_message(chan, msg):
    con.send(bytes('PRIVMSG %s :%s\r\n' % (chan, msg), 'UTF-8'))


def send_nick(nick):
    con.send(bytes('NICK %s\r\n' % nick, 'UTF-8'))


def send_pass(password):
    con.send(bytes('PASS %s\r\n' % password, 'UTF-8'))


def join_channel(chan):
    con.send(bytes('JOIN %s\r\n' % chan, 'UTF-8'))


def part_channel(chan):
    con.send(bytes('PART %s\r\n' % chan, 'UTF-8'))
# --------------------------------------------- End Functions ------------------------------------------------------


# --------------------------------------------- Start Helper Functions ---------------------------------------------
def get_sender(msg):
    result = ""
    for char in msg:
        if char == "!":
            break
        if char != ":":
            result += char
            
    return result


def get_message(msg):
    result = ""
    i = 3
    length = len(msg)
    while i < length:
        result += msg[i] + " "
        i += 1
    result = result.lstrip(':')
    return result


def parse_message(msg):
    global msg2
    if len(msg) >= 1:
        
        msg = msg.split(' ',2)
        
        #print(msg)
        
        msg2 = str(msg[1])
        msg1 = str(msg[0])
        msg1 = msg1.lower()


        try:
            
            msg3 = str(msg[2])

        except IndexError:
            msg3 = ""

        
        #print(msg2)
        options = {'!roll': command_roll,
                   '!flip': command_flip,
                   'lul': command_LUL,
                   '!info': command_info,
                   '!addinfo': command_addinfo,
                   '!rsitem': command_item,
                   '!rsmob': command_mob,
                   '!run': command_run,
                   '!dibz': command_dibz,
                   '!adddibz': command_adddibz,
                   '!minusdibz': command_minusdibz,
                   '!getviewers': get_viewers,
                   '!help': command_help,
                   '!test': command_test}
        #options =  {'enter': marble}
        
        if msg1 in options:
            options[msg1](msg2,msg3)
        
            
# --------------------------------------------- End Helper Functions -----------------------------------------------


# --------------------------------------------- Start Command Functions --------------------------------------------

def command_test(arg1,arg2):
    User = UJ.Viewer(sender)
    User.SetDibz(10)
    print(User.name)
    print(User.dibz)
    print(UJ.Viewer.GetAllViewers())



def command_roll(arg1,arg2):
    
    die = random.randrange(1,6)
    send_message(CHAN, sender + ' has rolled a ' + str(die))

def command_run(arg1,arg2):
    run = "Runescape Speed Run" #default text
    send_message(CHAN, run)

def command_LUL(arg1,arg2):
    global flag
    if flag == 0:
        send_message(CHAN, 'NigelW LUL NigelW')
        flag = 1
    else:
        send_message(CHAN, 'rsNoob LUL rsNoob')
        flag = 0
        
def command_info(arg1,arg2):
    global infofile
    infofileR = open('info.txt', 'r')

    infotext = infofileR.read()
    infofileR.close()
    

    
    send_message(CHAN, "\"" + infotext + "\"")

def command_addinfo(arg1,arg2):
    global msg2
    global infofile
    
    


    
    if sender == "ivigideon":
        infofileW = open('info.txt', 'w')
        
        infofileW.write(msg2)

        infofileW.close()
        send_message(CHAN, '/w ' + sender + ' ' + msg2 + ' has been added to info')
    else:
        send_message(CHAN, 'You\'re not yDibZ, you pleb. ')
        
        
        
        
def command_help(arg1,arg2):
    global options
    send_message(CHAN, "Here is the command list for Ydibz bot. " + "!roll !flip !lul !info !addinfo !rsitem !rsmob !run !dibz !adddibz !minusdibz !getviewers !help !test")
    

    
    
    
def command_grab(arg1,arg2):
    # this is a grab bag function, which will spawn a ranodm amount of money up for grabs in the chat, random amounts will be chosen, and a speacial code will have to be typed after the bag name in order to claim the bag.
    
    #create a code generetor, RT35T4 2 letters 2 numbers 1 letter 1 number, random char?
    
    ()
    
    
    
    
    
            
def get_viewers(arg1,arg2):
    
            
            #https://tmi.twitch.tv/group/user/ydibz/chatters
    # this link will provide all users within a channel.

    page = requests.get('http://tmi.twitch.tv/group/user/ydibz/chatters')
    tree = html.fromstring(page.content)
    #print(tree)
    Viewers = tree.xpath('/html/body/p/text()')
    #print(Viewers)

    json_data = json.loads(Viewers[0])

    #print(json_data)

    return("{chatters[viewers]}".format(**json_data))

    #this returns all of the viewers currently in the chat

    #send_message(CHAN,"These are the viewers {chatters[viewers]} and the Moderators {chatters[moderators]}".format(**json_data))        
    #Work on intergrating this list with the !dibz command, allowing for account creation upon login. Running one check as they get upadted within the chat.
        
        
        
        
def DibzTime(arg1,arg2):
   
    
    
    #this will be the timer to count the amount of time a viewer has been in the chat, got to decide how often to search for users. every 30 seconds check the chat?
    
    
    # search only for the users known to be in the chat, don't search from the user list to find these.
    
    
    #make  avarible amount that increases the longer you are in the chat? Could allow for people who leave the webpage up and farm the dibz, maybe make a fuction that will make them lose dibz after long enough time within the chat, eg 15 or 20 hours.
    
    
   #every 30 seconds will give 1 dibz, then add 1 dibz the the dibz adder, but make sperate for each user.

    
    
    
    
    
    
    #if User == Viewers:
     #   !adddibz (User, amount)
    
    ()
    
    
    
    
    
    
    
    

def command_flip(arg1,arg2):
    flipper = sender 
    coinFlip = random.randint(0,1)

    answer = arg2.strip().lower()

    
    if arg1 != "" and arg2 != "":
        amountOfDibz = command_dibz(flipper, arg1)
        
        amountOfDibz = str(amountOfDibz)
        
        if amountOfDibz == "No Account":
            send_message(CHAN, "/w flipper You have no account, please use !dibz to create your account. ")
            
        elif amountOfDibz < arg1:
            send_message(CHAN, "/w flipper You do not have enough money to place that bet.")
            
        elif arg1 < 0:
            send_message(CHAN, "/w flipper You cannot flip negative money. ")
        
        else:
            ()
        
        
        if coinFlip == 1:
            coin = "Heads"
        else:
            coin = "Tails"
            
        print(coin,answer) #debug
        
        if answer.strip().lower() == coin.strip().lower():
            send_message(CHAN, flipper + ' flipped a coin and got ' + coin + ", winning " + arg1 + " dibz.")
            command_adddibz(arg1, flipper)
            
        else:
            send_message(CHAN, flipper + ' flipped a coin and got ' + coin + ", losing  " + arg1 + " dibz.")
            command_minusdibz(arg1, flipper)
            

            
    # no arguement if/else

    else:
        if coinFlip == 1:
            coin = "Heads"
        else:
            coin = "Tails"
        send_message(CHAN, sender + ' flipped a coin and got ' + coin)

def command_item(arg1,arg2):
    global msg2
    
    msg2 = msg2 + " " + arg2
    msg2 = msg2.strip()
    msg2 = msg2.lower()
    msg2 = msg2.replace(" ","-")
    print(msg2)
    page = requests.get('http://www.runehq.com/item/' + msg2)
    tree = html.fromstring(page.content)

    usage = tree.xpath('//*[@id="main"]/div[4]/div[2]/div/div[13]/text()')

    page1 = requests.get('https://ge.2007hq.com/item/' + msg2)
    tree1 = html.fromstring(page1.content)

    usage1 = tree1.xpath('/html/body/div/div[4]/div[2]/div/div[1]/div[2]/div[2]/ul/li[2]/text()')
    print(usage1)
    usage = str(usage)
    usage1 = str(usage1)
    usage = usage.strip("['")
    usage1 = usage1.strip("']")
    usage1 = usage1.strip("['")
    usage = usage.strip("']")
    
    usage = usage.replace("['", "")
    usage1 = usage1.replace("']", "")

    
    ItemPrintout = usage + " The live GE price for this item is " + usage1
    
    print(ItemPrintout)
    
    #print ('description', usage)
    if not usage:
        send_message(CHAN, "Couldn't find what you were looking for.")
    else:
        send_message(CHAN, ItemPrintout + " gp.")
    
def command_mob(arg1,arg2):
    global msg2
    msg2 = msg2.strip()
    msg2 = msg2.lower()
    msg2 = msg2.replace(" ","-")
    #print(msg2)
    page = requests.get('http://www.runehq.com/monster/' + msg2)
    tree = html.fromstring(page.content)

    usage = tree.xpath('//*[@id="main"]/div[4]/div[2]/div/div[10]/text()')
    #print ('description', usage)
    if not usage:
        send_message(CHAN, "Couldn't find what you were looking for.")
    else:
        send_message(CHAN, usage)


def command_adddibz(arg1, arg2):
    global msg2
    msg2 = msg2.split()
    print(msg2)
    name = arg2
    amount = int(arg1)
    success = 0
    counter = 0
    f = open('users.txt', 'r')
    users = f.readlines()
    f.close()
    f = open('users.txt', 'r')
    for line in f:
        print("IN LOOP")
        if success == 1:
            print(users[counter])
            currentAmount = users[counter]
            
            Totalamount = amount + int(currentAmount)
            
            users[counter] = str(Totalamount) + "\n"
            
            f.close()
            with open('users.txt', 'w') as file:
                file.writelines(users)
                
            #send_message(CHAN, "You've added " + str(amount) + " dibz to " + name)
            return


        
        if line.strip().lower() == name.strip().lower():
            success = 1
            print("WAS SUCCESSFULL")
            
        counter = counter + 1
        print(counter)
        print("LOOP FAILED")

    send_message(CHAN, sender + " That user either does not have a Dibz account yet, or does not exist.")

def command_minusdibz(arg1,arg2):
    name = arg2
    amount = int(arg1)
    success = 0
    counter = 0
    f = open('users.txt', 'r')
    users = f.readlines()
    f.close()
    f = open('users.txt', 'r')
    for line in f:
        print("IN LOOP")
        if success == 1:
            print(users[counter])
            currentAmount = users[counter]
            
            Totalamount = int(currentAmount) - amount

            if Totalamount < 0:
                Totalamount = 0

            
            users[counter] = str(Totalamount) + "\n"
            
            f.close()
            with open('users.txt', 'w') as file:
                file.writelines(users)
                
            #send_message(CHAN, "You've subtracted " + str(amount) + " dibz to " + name)
            return


        
        if line.strip().lower() == name.strip().lower():
            success = 1
            print("WAS SUCCESSFULL")
            
        counter = counter + 1
        print(counter)
        print("LOOP FAILED")

    send_message(CHAN, sender + " That user either does not have a Dibz account yet, or does not exist.")








    

def command_dibz(arg1,arg2):
    if arg1 == "" and arg2 == "":
        f = open('users.txt', 'r+')
        for line in f:
            if line.strip().lower() == sender.strip().lower():

                message = sender + " has " + str(next(f)).strip()
                message = message + " dibz."
                print(message)
                
                send_message(CHAN, message)
                f.close()
            
                return
            
        
        f.write("\n"+ sender + "\n" + "0")
        f.close()
        send_message(CHAN, sender +" Your Dibz account has been created. Use !Dibz to see how many dibz you have.")            
        
    elif arg1 != "" and arg2 != "":
        f = open('users.txt', 'r+')
        for line in f:
            if line.strip().lower() == arg1.strip().lower():
                amountOfDibz = int(str(next(f)).strip())
        
                return amountOfDibz
        
            else:
                return "No Account"
        
        
    else:
        f = open('users.txt', 'r+')
        for line in f:
            if line.strip().lower() == arg1.strip().lower():

                message = arg1 + " has " + str(next(f)).strip()
                message = message + " dibz."
                
                send_message(CHAN, message)
                f.close()
            
                return
        send_message(CHAN, arg1 + " does not have a dibz account.")



        
    
# def marble():
#    global msg2
#    marblemessage = msg2
#    sender2 = sender
 #   timewait = random.randrange(0,3)
    
 #   time.sleep(timewait)
 #   marblemessage = marblemessage.strip()
 #   if sender2 == "marbleracing":
 #       if msg2 == "marbles now!":
 #           print("SUCCESSFULL#################################################")
 #           send_message(CHAN, "!marble")
  #  else:
  #      print("Not real marbleracing")
# --------------------------------------------- End Command Functions ----------------------------------------------

con = socket.socket()
con.connect((HOST, PORT))

send_pass(PASS)
send_nick(NICK)
join_channel(CHAN)

data = ""

while True:
    try:
        data = data+con.recv(1024).decode('UTF-8')
        data_split = re.split(r"[~\r\n]+", data)
        data = data_split.pop()

        for line in data_split:
            line = str.rstrip(line)
            line = str.split(line)

            if len(line) >= 1:
                if line[0] == 'PING':
                    send_pong(line[1])

                if line[1] == 'PRIVMSG':
                    sender = get_sender(line[0])
                    message = get_message(line)
                    parse_message(message)

                    print(sender + ": " + message)

    except socket.error:
        print("Socket died")

    except socket.timeout:
        print("Socket timeout")

    except UnicodeEncodeError:
        print("Bot encountered Error, restarting.")

