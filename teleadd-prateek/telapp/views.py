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
from django.urls import reverse
from .models import *
from django.http import *
from django.views.decorators.csrf import csrf_exempt
import json
import pandas as pd
import os

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.

#AMit

#Divyesh
"""api_id = 308919
api_hash = 'fff3e8b75bf9a6f147dda738eb2c640f'
"""
"""
try:
	if ClientApiKey.objects.all().count() == 0:
    		dks = [{'id': 5, 'apikey': '627710', 'apihash': '0a6cb002fc0c62fe84afe84932c3d1db',
    'mobile_no': '+919893918907'}, {'id': 7, 'apikey': '688377', 'apihash': 'bb9b6c7edbdc58e2a9ce082f3577559d', 'mobile_no': '+919074415913'}, {'id': 8, 'apikey': '308919', 'apihash': 'fff3e8b75bf9a6f147dda738eb2c640f', 'mobile_no': '+919174704877'}]
    		for dk in dks:
        	try:
            		client = ClientApiKey.objects.get(mobile_no=dk["mobile_no"])
            		print(client,"got")
        	except:
            		client = ClientApiKey.objects.create(mobile_no=dk["mobile_no"],
                apikey=dk["apikey"],
                apihash=dk["apihash"]
                )
	            	print(client,"created")
"""
if ClientApiKey.objects.all().count() == 0:
    dks = [{'id': 5, 'apikey': '627710', 'apihash': '0a6cb002fc0c62fe84afe84932c3d1db',
    'mobile_no': '+919893918907'}, {'id': 7, 'apikey': '688377', 'apihash': 'bb9b6c7edbdc58e2a9ce082f3577559d', 'mobile_no': '+919074415913'}, {'id': 8, 'apikey': '308919', 'apihash': 'fff3e8b75bf9a6f147dda738eb2c640f', 'mobile_no': '+919174704877'}]
    for dk in dks:
        try:
            client = ClientApiKey.objects.get(mobile_no=dk["mobile_no"])
            print(client,"got")
        except:
            client = ClientApiKey.objects.create(mobile_no=dk["mobile_no"],
                apikey=dk["apikey"],
                apihash=dk["apihash"]
                )
            print(client,"created")


def index(request):
    context = {}

    context['mobile'] = ClientApiKey.objects.all()
    if request.method=="POST":
        context['group1'] = group1 = request.POST.get('group1')
        context['group2'] = group2 = request.POST.get('group2')
        time.sleep(1)
        group1_id=group1
        group2_id=group2

        context['mobile_no'] = thephone = request.POST.get('mobile_no')
        print(thephone)
        client = getClient(thephone)
        client.connect()
        context['group1_client'] = client.get_participants(group1_id)
        context['group2_client'] = client.get_participants(group2_id)

        if "all" in request.POST:
            context = {}
            channels = {d.entity.username: d.entity
                        for d in client.get_dialogs()
                        if d.is_channel}

            #channel='entrepreneurialjourney'
            #channel2= 'joinexample3'
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
                    if count==45:
                        context["group1"] = "It reached to 50 members addition"
                        return render(request, 'index.html', context)
                    count=count+1
        print(context['group2_client'])
        client.disconnect()
    return render(request, 'index.html', context)

def getClient(thephone):
	thephone = ClientApiKey.objects.get( mobile_no = thephone )
	api_id = thephone.apikey
	api_hash = thephone.apihash
	try:
		client = TelegramClient('session_name'+str(api_id), api_id, api_hash)
	except:
		if not client.is_user_authorized():
			phone_code_hash = client.send_code_request(thephone).phone_code_hash
			request.session['phone_code_hash'] = phone_code_hash
        	me = client.sign_in(thephone, otp, phone_code_hash=phone_code_hash)
			return render(request, "otp.html", {'mob':thephone, 'title': 'Enter OTP to Sign in'})
	return client

@csrf_exempt
def addtogrp(request, u_id=None, group=None, mobile_no=None):

        client=getClient(mobile_no)
        try:
            client.connect()
        except:
            pass
        client(InviteToChannelRequest(group,[u_id]))
        try:
            client.disconnect()
        except:
            pass
        return HttpResponse('success')

def apigen(request):
    if request.method == "POST":
        apikey = request.POST.get('apikey')
        apihash = request.POST.get('apihash')
        mob = request.POST.get('mob')

        if len(mob)==10:
            mob = "+91"+mob
            client = TelegramClient('session_name'+str(apikey), apikey, apihash)
            client.connect()
            if not client.is_user_authorized():
                phone_code_hash = client.send_code_request(mob).phone_code_hash
                request.session['phone_code_hash'] = phone_code_hash
            try:
                ca = ClientApiKey.objects.get(apikey=apikey, apihash=apihash, mobile_no=mob)
            except:
                ca = ClientApiKey.objects.create(apikey=apikey, apihash=apihash, mobile_no=mob)
            ca.save()
            return render(request, "otp.html", {'mob':mob, 'title': 'OTP'})
        else:
            return render(request, "requestform.html", {'moberror':'invalid mobile number'})
    else:
        return render(request, "requestform.html")

def putOtp(request):
    context = {}
    if request.method == "POST":
        mob = request.POST.get('mob')
        otp = request.POST.get('otp')
        thephone = ClientApiKey.objects.get( mobile_no = mob )
        api_id = thephone.apikey
        api_hash = thephone.apihash
        phone_code_hash = request.session['phone_code_hash']
		os.remove('session_name'+str(api_id))
        client = TelegramClient('session_name'+str(api_id), api_id, api_hash)
        client.connect()
        me = client.sign_in(mob, otp, phone_code_hash=phone_code_hash)
        context['mobile'] = ClientApiKey.objects.all()
        context['mob'] = mob

        return HttpResponseRedirect(reverse('index'))
        #context['otperror'] = "invalid OTP"
    else:
        return render(request, "otp.html", context)

def uploadexcel(request):
    context = {}
    context['mobile'] = ClientApiKey.objects.all()
    print(context['mobile'])
    #context['mobile'] = ClientApiKey.objects.all()
    if request.method == "POST":
        status = handle_uploaded_file(request.FILES['excel_file'])
        context['group1'] = group1 = request.POST.get('group1')
        context['mobile_no'] = thephone = request.POST.get('mobile_no')

        if status == True:
            group2 = pd.read_excel('excelfiles/contact.xlsx')
            context['group2'] = "ExcelSheet"
        try:
            context['excel_data'] = []
            for index, row in group2.iterrows():
                context['excel_data'].append({'id': row['id'], 'username': row['username']})
            #print(row['id'], row['username

            client = getClient(thephone)
            try:
                client.connect()
                context['group1_client'] = client.get_participants(group1)
                client.disconnect()
            except Exception as e:
                print(e)
        except ClientApiKey.DoesNotExist:
            context['excel_error'] = "Excel sheet error"
    return render(request, "excel.html", context)

def handle_uploaded_file(f):
    with open('excelfiles/contact.xlsx', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return True
