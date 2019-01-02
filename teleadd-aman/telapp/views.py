from django.shortcuts import render
from telethon import TelegramClient, sync
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from time import sleep
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChannelAdminRights
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from telethon.tl.functions.channels import InviteToChannelRequest
import time
# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
"""api_id = 627710
api_hash = '0a6cb002fc0c62fe84afe84932c3d1db'
client = TelegramClient('session_name', api_id, api_hash).start()
me=client.get_me(input_peer=True).user_id
user = client.get_entity('ameet777')
print(str(user.status))
"""

#Amit-api-id
api_id=627710
api_hash='0a6cb002fc0c62fe84afe84932c3d1db'

#prateek-api-id
#api_id=551364
#api_hash='acd98e9ff77cf2a0f96877923b64dbc3'
client = TelegramClient('session_name', api_id, api_hash).start()
me=client.get_me(input_peer=True).user_id

def index(request):
    context = {}
    channels = {d.entity.username: d.entity
                for d in client.get_dialogs()
                if d.is_channel}
    group1 = 'entrepreneurialjourney'
    group2 = 'joinexample3'
    context['group1'] = 'MillionNetworkMedia'
    context['group2'] = 'fordemoonly'

    #channel='entrepreneurialjourney'
    #channel2= 'joinexample3'
    participants = client.get_participants(group1)
    count=1
    act = input("press 1 to add all, 2 to add one by one, 3 to cancel: ")
    if str(act) == "1":
        print("Adding all members")
    if str(act) == "1" or str(act) == "2":
        for u in participants:
            print(count)
            print(u.first_name)
            u_id=u.id
            last_seen = client.get_entity(u_id)
            time.sleep(1)
            print(str(last_seen))
            print()
            time.sleep(1)
            if str(act) == str(2):
                acte = input("press 1 to add, 2 to skip: ")
                if str(acte) == str(1):
                        client(InviteToChannelRequest(group2,[u_id]))
                        print("Privacy Issue")
            if str(act) == str(1):

                        client(InviteToChannelRequest(group2,[u_id]))

                        print("Privacy Issue")
            time.sleep(1)
            if count==20:
                break
            count=count+1


    if request.method == "POST":
        group1 = request.POST.get('group1')
        group2 = request.POST.get('group2')


    return render(request, 'index.html', context)



"""
def add_users(client):
    channels = {d.entity.username: d.entity
                for d in client.get_dialogs()
                if d.is_channel}

    channel=input("Enter group1: ")
    channel2=input("Enter group2: ")

    #channel='entrepreneurialjourney'
    #channel2= 'joinexample3'
    participants = client.get_participants(channel)
    count=1
    act = input("press 1 to add all, 2 to add one by one, 3 to cancel: ")
    if str(act) == "1":
        print("Adding all members")
    if str(act) == "1" or str(act) == "2":
        for u in participants:
            print(count)
            print(u.first_name)
            u_id=u.id
            last_seen = client.get_entity(u_id)
            time.sleep(1)
            print(str(last_seen))
            print()
            time.sleep(1)
            if str(act) == str(2):
                acte = input("press 1 to add, 2 to skip: ")
                if str(acte) == str(1):
                        client(InviteToChannelRequest(channel2,[u_id]))
                        print("Privacy Issue")
            if str(act) == str(1):
                    try:
                        client(InviteToChannelRequest(channel2,[u_id]))
                    except:
                        print("Privacy Issue")
            time.sleep(1)
            if count==20:
                break
            count=count+1
    return

add_users(client)

"""
