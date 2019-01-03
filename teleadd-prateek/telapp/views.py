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

#AMit
api_id = 627710
api_hash = '0a6cb002fc0c62fe84afe84932c3d1db'

#Divyesh
"""api_id = 308919
api_hash = 'fff3e8b75bf9a6f147dda738eb2c640f'
"""
client = TelegramClient('session_name'+str(api_id), api_id, api_hash)

client.connect()



def index(request):
    context = {}
    context['group1'] = 'Airdropbountycommunity'
    context['group2'] = 'latestairdro'
    if not client.is_user_authorized():
        if request.method=="POST":
            thephone = request.POST.get('group1')
            client.send_code_request(thephone)
            if request.POST.get('group2'):
                thecode = request.POST.get('group2')
                me = client.sign_in(thephone, thecode)
                print("GOTIT")
            else:
                group1 = request.POST.get('group1')
                return render(request, 'index.html', context)
        else:
            return render(request, 'index.html', context)
    else:
        me=client.get_me(input_peer=True).user_id

    if request.method == "POST":
        context['group1'] = group1 = request.POST.get('group1')
        context['group2'] = group2 = request.POST.get('group2')
        context['group1_client'] = client.get_participants(context['group1'])
        context['group2_client'] = client.get_participants(context['group2'])

        if "all" in request.POST:
            context = {}
            channels = {d.entity.username: d.entity
                        for d in client.get_dialogs()
                        if d.is_channel}

            #channel='entrepreneurialjourney'
            #channel2= 'joinexample3'
            print("ALL PRESSED")
            participants = client.get_participants(group2)
            count=1
            if str(1) == "1":
                for u in participants:
                    print(count)
                    print(u.first_name)
                    u_id=u.id
                    last_seen = client.get_entity(u_id)
                    print(str(last_seen))
                    print()
                    client(InviteToChannelRequest(group1,[u_id]))
                    if count==20:
                        context["group1"] = "It reached to 50 members addition"
                        return render(request, 'index.html', context)
                    count=count+1
    else:
            context['group1_client'] = client.get_participants(context['group1'])
            context['group2_client'] = client.get_participants(context['group2'])
    return render(request, 'index.html', context)