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
# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 627710
api_hash = '0a6cb002fc0c62fe84afe84932c3d1db'
client = TelegramClient('session_name', api_id, api_hash).start()
me=client.get_me(input_peer=True).user_id
user = client.get_entity('ameet777')
print(str(user.status))

def index(request):
    context = {}
    context['group1'] = 'entrepreneurialjourney'
    context['group2'] = 'joinexample3'
    if request.method == "POST":
        group1 = request.POST.get('group1')
        group2 = request.POST.get('group2')
        context['group1_client'] = client.get_participants(context['group1'])
        context['group2_client'] = client.get_participants(context['group2'])
    '''
    UserStatusOffline(was_online=datetime.datetime(2019, 1, 2, 9, 4, 8, tzinfo=datetime.timezone.utc))
	UserStatusRecently()
    '''
    return render(request, 'index.html', context)
