import os
import hashlib
import requests
import time
from django.shortcuts import render, redirect
from ttlockwrapper import TTLock
from dotenv import load_dotenv
from api.models import *


load_dotenv()

clientId = os.getenv("CLIENT_ID")
clientSecret = os.getenv('CLIENT_SECRET')

ttlock = TTLock(clientId, clientSecret)

# Create your views here.
def register(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		if password == request.POST['confirm']:
			username = str(email.split('@')[0])
			password = hashlib.md5(password.encode()).hexdigest()
			new_user = ttlock.create_user(clientId=clientId, clientSecret=clientSecret, username=username, password=password)
			access_token = ttlock.get_token(clientId=clientId, clientSecret=clientSecret, username=new_user['username'], password=password, redirect_uri='/')
			new_client = Client(email=email, password=password, username=username, access_token=access_token['access_token'])
			if new_client:
				new_client.save()

	context = {'title':'Register'}
	
	return render(request, 'ekey/register.html', context)


def locksList(request):
	user = request.user
	payload = {'clientId':clientId, 'accessToken':user.access_token, 'date':time.time()}
	headers = {'Content-Type': 'application/x-www-form-urlencoded'}
	r = requests.get('', headers=headers, params=payload)
