from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import insert_new_trial_Form, prepare_new_trial_Form
from jumpmetric.functions.functions import handle_uploaded_file
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import io
import urllib, base64
from io import StringIO
from django.core import serializers

from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status



@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by Type of trial': '/?type_of_trial=type_of_trial',
        'Search by Fullname': '/?fullname=fullname',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
 
    return Response(api_urls)





###########----User Register,Login,Logout Pages-----########

########### Sign up ##################################### 
def user_signup(request):
    if request.method == 'POST':
        
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system #################################### 
            # htmly = get_template('trivia/email.html')
            # d = { 'username': username }
            # subject, from_email, to = 'welcome', 'altemode@mail.com', email
            # html_content = htmly.render(d)
            # msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()
            ################################################################## 
            messages.success(request, f'Your account has been created ! You are now able to log in')
            #login(request, user)
            return redirect('login')
        else:
            print('form.errors')
            print(form.errors)
    else:
        form = UserRegisterForm()
    return render(request, 'jumpmetric/users/signup.html', {'form': form,'title':'register here'})

################ login form ################################################### 
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                form = login(request, user)
                messages.success(request, f' welcome {username} !!')  
                return redirect('dashboard')
            else:
                messages.info(request, f'account done not exit plz sign in')
                form = LoginForm()
    form = AuthenticationForm()
    return render(request, 'jumpmetric/users/login.html', {'form': form,'title':'log in'})

# logout page
def user_logout(request):
    print('3) user_logout')
    logout(request)
    return redirect('login')


def usersList(request):
    list_of_users = User.objects.all()

    return render (request, "jumpmetric/users/users_list.html", {"list_of_users":list_of_users})
###########----End of User Register,Login,Logout Pages-----########


# Create your views here.


def dashboard(request):

    return render(request, 'jumpmetric/dashboard.html')


def display_all_trials(request):

    return render(request, 'jumpmetric/display_all_trials.html')


def display_selected_trial(request):

    return render(request, 'jumpmetric/display_selected_trial.html')

def prepare_new_trial(request):
    form = prepare_new_trial_Form()
    context = {"form":form}
    if request.method == 'POST':
        uploaded_file = request.FILES.get('prepare_file')
        if uploaded_file:
            df_raw_data = pd.read_csv(uploaded_file,   skiprows=10, index_col = None) # 
            message = "OK"
            df_raw_data.columns = ['Time','Col_2','Mass_1','Mass_2','Mass_3','Mass_4','Col_7','Col_8','Col_9','Col_10','Mass_Sum']
            plt.plot(range(10))
            
            #plt.plot(range(10))
            fig = plt.plot(df_raw_data['Mass_Sum'], linestyle = 'dotted')
            #convert graph into dtring buffer and then we convert 64 bit code into image
            buf = io.BytesIO()

            plt.savefig(buf,format='png')
            buf.seek(0)
            string = base64.b64encode(buf.read())
            chart =  urllib.parse.quote(string)
            
            # # plt.show()

            # imgdata = StringIO()
            # plt.savefig(imgdata, format='svg')
            # imgdata.seek(0)

            # chart = imgdata.getvalue()
            #df_raw_data = df_raw_data.to_html()

            # for col in df_raw_data.columns %}
            #     <td>
            #     {{col}}
            #     </td>
            # {% endfor %}

            # for index, row in df_raw_data.iterrows
            #     if index = 'Mass_Sum':
            #         for cell in row
            #             cell
            print(df_raw_data['Mass_Sum'])
            Mass=df_raw_data['Mass_Sum']

            datapoints = []
            
            for csv_line in Mass:
                datapoints.append(csv_line)
                
            # datapoint_query_set = DataPoint.objects.all().order_by('x')
            
            # for index, row in df_raw_data.iterrows:
            #     if index == 'Mass_Sum':
            #          for cell in row:
                         
            #             data.cell= cell
        
            # datapoints = serializers.serialize('json', datapoint_query_set)
            # return render(request, "index.html", { "datapoints": datapoints})                        


            return render(request, 'jumpmetric/prepare_new_trial.html', {"form":form, "datapoints":datapoints, "Mass":Mass, "message":message, 'chart':chart})
        else:
            messages.warning(request, f'No file to process! Please upload a file to process.')


    return render(request, 'jumpmetric/prepare_new_trial.html',context)

def insert_new_trial(request):
    if request.method == 'POST':
        form = insert_new_trial_Form(request.POST, request.FILES)
        if form.is_valid():
            filename = request.FILES['trial_csv'].name
            form.instance.filename = request.FILES['trial_csv'].name
            form.save()
            message = "Thank you, new trial has inserted!"
            return render(request, 'jumpmetric/insert_new_trial.html', {"message": message, "form":form})
            #return HttpResponseRedirect("/thanks")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = insert_new_trial_Form()

    return render(request, 'jumpmetric/insert_new_trial.html', {"form": form})


def calculate_trial(request):

    return render(request, "jumpmetric/calculate_trial.html")



def index(request):
    datapoint_query_set = DataPoint.objects.all().order_by('x')
    
    for data in datapoint_query_set:
        data.x = int(datetime.timestamp(data.x)) * 1000
 
    datapoints = serializers.serialize('json', datapoint_query_set)
    return render(request, "index.html", { "datapoints": datapoints})                        


############ FRONTEND VIEWS ##############

def homepage(request):

    return render(request, "jumpmetric/frontend/homepage.html")

def about(request):

    return render(request, "jumpmetric/frontend/about.html")
