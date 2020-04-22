from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests 
from bs4 import BeautifulSoup
from .models import Feedback
from .models import update_log
import stripe
from django.urls import reverse
from .models import Crona_data
from django.contrib import messages
import csv,io


stripe.api_key = "sk_test_fWtvOu3yyC2jNKRLZRV5SHqt00GLxFZW4W"

def get_corona_data():
    url="https://www.worldometers.info/coronavirus/"
    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text
    # Parse the html content
    soup = BeautifulSoup(html_content, "lxml")
    gdp_table = soup.find("table", id = "main_table_countries_today")
    gdp_table_data = gdp_table.tbody.find_all("tr")

    # Getting all countries names
    dicts = {}
    for i in range(len(gdp_table_data)):
        try:
            key = (gdp_table_data[i].find_all('a', href=True)[0].string)
        except:
            key = (gdp_table_data[i].find_all('td')[0].string)

        value = [j.string for j in gdp_table_data[i].find_all('td')]
        dicts[key] = value
    return dicts
 
def home(request):
    data = get_corona_data()
    region = []
    confirmed = []
    deceased = []
    decease= []
    recovered = []
    serious = []
    details = []
    for i in data:
        region.append(data[i][0])
        confirmed.append(data[i][1])
        decease.append(data[i][3])
        recovered.append(data[i][5])
        serious.append(data[i][7])

    for j in decease:
        if(j.isspace()):
            deceased.append('None')
        else:
            deceased.append(j)
    
    total_confirm = confirmed[1]
    total_decresed = deceased[1]
    total_recovered = recovered[1]
    total_serious = serious[1]

    region =  region[2:]
    confirmed = confirmed[2:]
    deceased = deceased[2:]
    recovered = recovered[2:]
    serious = serious[2:]

    return render(request,'index.html',{'region':region,'confirmed':confirmed,'deceased':deceased,
                'recovered':recovered,'serious':serious,'total_confirm':total_confirm,'total_decresed':total_decresed,
                'total_recovered':total_recovered,'total_serious':total_serious})



def about(request):
    return render(request,'about.html')

def update(request):
    update_data = update_log.objects.all().order_by('-update_date')
    return render(request,'update.html',{'update_data':update_data})


def feedback(request):
    if request.method == 'POST':
        name = request.POST['user_name']
        email = request.POST['user_email']
        mesage = request.POST['user_message']
        new_feedback = Feedback(name=name,email=email,message= mesage)
        new_feedback.save()
        return redirect(feedback) 
    else:
        feedback_data = Feedback.objects.all().order_by('-date')
        return render(request,'feedback.html',{'data':feedback_data})

def payment(request):
	return render(request, 'payment.html')


def charge(request):
	if request.method == 'POST':
		print('Data:', request.POST)

		amount = int(request.POST['amount'])

		customer = stripe.Customer.create(
			email=request.POST['email'],
			name=request.POST['nickname'],
			source=request.POST['stripeToken']
			)

		charge = stripe.Charge.create(
			customer=customer,
			amount=amount*100,
			currency='usd',
			description="Donation"
			)
	return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
	amount = args
	return render(request, 'success.html', {'amount':amount})

def graph(request):
    return render(request,'graph.html')

def map_dire(request):
    feed = Feedback.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email_ = request.POST['email_']
        message = request.POST['message']
        ls = []
        for value in feed:
            ls.append(str(value))
        
        if name in ls:
            pass
        else:
            new_feed = Feedback(name= name, email= email_,message=message)
            new_feed.save()
    return render(request,'map.html')



def profile_upload(request):
    # declaring template
    template = "upload_file.html"
    data = Crona_data.objects.all()
    # prompt is a context variable that can have different values      depending on their context
    prompt = {
            'order': 'Order of the CSV should be name, email, address,    phone, profile',
            'profiles': data    
            }
        # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
        # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')

    data_set = csv_file.read()
    io_string = io.TextIOWrapper(data_set).file
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Crona_data.objects.update_or_create(
            country = column[0],
            total_case = column[1],
            new_cases = [2],
            total_death = [3],
            new_death = [4],
            total_recovery = [5],
            active_cases = [6],
            serious_critical  = [7],
            total_case_perM = [8],
            totalDeathperM = [9],
            total_test_perM = [10],
            test_perM = [11],
            continent = [12]
        )
    context = {}
    return render(request, template, context)

def save_data(request):
    template = 'upload_file.html'
    prompt = {
        'order':'File should be CSV'
    }
    if request.method == 'GET':
        return render(request,template,prompt)
    
    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request,'This is not a csv file')
    
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    #io_string = io.TextIOWrapper(data_set).file
    
    next(io_string)
    for column in csv.reader(io_string,delimiter=',',quotechar='|'):
        _, created  = Crona_data.objects.update_or_create(
            country = column[0],
            total_case = column[1],
            new_cases = [2],
            total_death = [3],
            new_death = [4],
            total_recovery = [5],
            active_cases = [6],
            serious_critical  = [7],
            total_case_perM = [8],
            totalDeathperM = [9],
            total_test_perM = [10],
            test_perM = [11],
            continent = [12]
        )

        context = {}

        return render(request,template,context)



    
    
    


    
