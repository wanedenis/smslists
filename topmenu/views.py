from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from .models import Listing, User 
from django.http import Http404
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .languages import *
import plivo



PLIVO_NUMBER = "18058643381" # in the future will call deployment.txts
auth_id = "MANGVIYZY0ZMFIMTIWOG"
auth_token = "Yzc3OTgzZmU4MGIyNDI4ODgzMWE1MWExOWYxZTcx"


###############
def index(request):
	print "index"
	latest_listing_list = Listing.objects.order_by('-pub_date')[:6]
	context = {'latest_listing_list': latest_listing_list,}
	return render(request, 'topmenu/index.html', context)

def detail(request, detail_id):
	print "detail"
	detail_display = get_object_or_404(Listing, pk = detail_id)
	return render(request, 'topmenu/detail.html', {'apples': detail_display})
###############

"""
# receieve sms method
@csrf_exempt
@require_POST
def plivo_endpoint(request):
	source = request.POST['From']
	destination = request.POST['To']
	messageuuid = request.POST['MessageUUID']
	message_content = request.POST['Text']

	try:
		User.objects.filter(source=phone_num).user_state
		if user_state == 2:
			if int(message_content)==1:
				listings(phone_num, 1)
			elif int(message_content)==2:
				listings(phone_num, 2)
			elif int(message_content)==3:
				listings(phone_num, 3)
			elif int(message_content)==4:
				listings(phone_num, 4)
		# need to get this working ^



	except User.DoesNotExist:
		# create new User_data entry
		User.objects.create(phone_num=source, user_state=1)
		menu_text = ""
		send_message(source=destination, destination=source, menu_text=
			"""Welcome! Your phone number has been recorded as %s""" % source)
		menu_2(source)
		# https://docs.djangoproject.com/en/1.9/ref/request-response/#django.http.HttpResponse.status_code
		return HttpResponse(status=200)
"""

def send_message(source, destination, menu_text):
	p = plivo.RestAPI(auth_id, auth_token)
	params = {
    'src': source,  # Sender's phone number with country code
    'dst': destination,  # Receiver's phone Number with country code
    'text' : menu_text, # Your SMS Text Message - English
    'url' : "", # The URL to which with the status of the message is sent
    'method' : 'POST' # The method used to call the url
	}
	response = p.send_message(params)	
	return response

def menu_2(phone_num):
	request.Session["user_state"]="menu_2" # NEEDS TO TIMEOUT AFTER 5 MIN
	# get user language
	current_language = LANGUAGES[User.objects.get(phone_num=phone_num).user_language] #ADD THIS TO SESSION

	menu_text = "1. %s, 2. %s, 3. %s, 4. %s" % (current_language.for_sale, 
		current_language.wanted, current_language.jobs,
		current_language.announcements)

	send_message(source = PLIVO_NUMBER, destination=phone_num,
		menu_text=menu_text)
	return HttpResponse(status=200)

def listings(message_content, ):
	message_content == 

	
	if user_state==2:







