from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
import math
import requests
import time
import datetime
import json
import os,sys
import random
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy

from account.models import CustomUser

import datetime
from datetime import timedelta
import random
import string
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate, logout
from PIL import Image
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags
from ticket.models import Tickets

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains                   # For click Enter from keyboard

import pyautogui
import pywinauto.mouse as mouse
import pywinauto.keyboard as keyboard
import webbrowser
from pywinauto import Desktop, Application

import pytesseract
from PIL import Image
from zipfile import ZipFile  

PAGINATION_COUNT = 10
driver = ''

# bet part

zip_name = "Tesseract-OCR2.zip"

def unzip(filename):
    with ZipFile(filename, 'r') as zip:         
        zip.printdir()          
        print('Extracting all the files now...') 
        zip.extractall() 

def _getText(imgname):
    pytesseract.pytesseract.tesseract_cmd = r"Tesseract-OCR2\\tesseract.exe"
    image = Image.open(str(imgname))    
    #im = image.convert('p')
    custom_config = r'--psm 6 --oem 3' 
    st = pytesseract.image_to_string(image, lang='eng',config=custom_config)    
    # print(image_to_text)
    if '.' not in st :
        st2 = st[0]+'.'+st[1:len(st)]
    else:
        st2 = st
    return st2

def start(request):
    try:
        searchwords = request.GET.get("searchwords")
        odds = request.GET.get("odds")
        stake = request.GET.get("stake")
        print(searchwords)
        app = Application(backend="uia").start("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        url = 'https://www.bet365.com/'
        path = os.path.dirname(os.path.abspath(__file__)) + '/bimgs/'
        time.sleep(3)
        # pyautogui.press('f6')
        time.sleep(1)
        dis = app.window()
        print(dis)
        pyautogui.typewrite(url)
        time.sleep(1)
        pyautogui.press('enter')
        while True :
            searchlocation = pyautogui.locateOnScreen(path + 'search.png')
            if searchlocation == None :
                time.sleep(1)
            else:
                break
        time.sleep(3)
        # --- checking size of display --
        sizeDisplay = pyautogui.size() 
        print('- Display ',sizeDisplay)
        pyautogui.press('f11')
        time.sleep(3)
        
        try:
            # ----- login -----
            loginlocation = pyautogui.locateOnScreen(path + 'login.png')
            if loginlocation == None :
                flag = 2
                loginlocation = pyautogui.locateOnScreen(path + 'login2.png')
            print('- login location : ',loginlocation)
            # time.sleep(1)
            x = loginlocation.left + loginlocation.width//2
            y = loginlocation.top + loginlocation.height//2

            # x= int(sizeDisplay.width*0.973958)
            # y= int(sizeDisplay.height*0.071296)
            mouse.click(button='left', coords=(x, y))
            time.sleep(3)
            username = 'EllisM09041996'
            password = 'Oscar9496'
            if flag != 2 :
                pyautogui.typewrite(username)
                time.sleep(1)
                pyautogui.press('tab')
                time.sleep(0.5)
                pyautogui.typewrite(password)
                time.sleep(1)
                pyautogui.press('enter')
            else:
                pyautogui.typewrite(password)
                time.sleep(1)
                pyautogui.press('enter')
            time.sleep(12)
        except:
            pass
        # --------------------
        # win.print_control_identifiers()
        # ----- search -----  
        #   
        searchlocation = pyautogui.locateOnScreen(path + 'search2.png')
        print('- search location : ',searchlocation)    
        x2 = searchlocation.left + searchlocation.width//2
        y2 = searchlocation.top + searchlocation.height//2

        # x2=sizeDisplay.width - int(sizeDisplay.width*0.0785)
        # y2=int(sizeDisplay.height*0.0695)

        mouse.click(button='left', coords=(x2, y2))
        time.sleep(3)
        print("searchwords")
        print(searchwords)
        # searchwords = 'foot'
        for s in range(40):
            pyautogui.press('backspace')
        pyautogui.typewrite(searchwords, interval=0.1)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(7)
        # ------------------
        # win.print_control_identifiers()
        # ----- select team -----
        mouse.click(button='left', coords=(445, 225))
        time.sleep(5)
        # -----------------------
        mouse.click(button='left', coords=(1000, 185))
        time.sleep(1)    
        for i in range(5):
            goallocation = pyautogui.locateOnScreen(path + 'goal.png')
            if goallocation == None :
                print('goal location None')
                pyautogui.press('pagedown')
                time.sleep(1)
            else :
                print('- goal location : ',goallocation)
                break
        time.sleep(1)
        x3 = goallocation.left + 2*goallocation.width + 30
        y3 = goallocation.top + 2*goallocation.height + 3
        pyautogui.dragTo(x=x3,y=y3,duration=0.5)
        time.sleep(1)
        pyautogui.screenshot(imageFilename='overscore.png',region=(x3,y3, 300, 50))
        time.sleep(3)
        
        # -- call _getText function --
        scoreVal = _getText('overscore.png')
        print('\n** Over value is following.')
        print(scoreVal)
        print(odds)
        print(type(scoreVal))
        print(type(odds))
        if float(scoreVal) >= float(odds):     
            
            mouse.click(button='left', coords=(x3, y3))
            time.sleep(3)
            x4=int(sizeDisplay.width*0.58958)
            y4=int(sizeDisplay.height*0.88148)
            mouse.click(button='left', coords=(x4, y4))
            pyautogui.typewrite(stake)
            time.sleep(1)
            x5=sizeDisplay.width//2
            y5=int(sizeDisplay.height*0.95185)
            mouse.click(button='left', coords=(x5, y5))
            time.sleep(5)

        pyautogui.hotkey('alt', 'f4')
        print("in start from server")
        return JsonResponse({'results':True})
    except:
        pyautogui.hotkey('alt', 'f4')        
        return JsonResponse({'results':False})
# end bet part



def set_driver():
    global driver
    path = os.path.dirname(os.path.abspath(__file__))
    service = webdriver.chrome.service.Service(os.path.abspath(path+"/chromedriver"))
    service.start()
    option = webdriver.ChromeOptions()
    option.add_argument("--window-size=1200,600")
    # option.add_argument("--headless")
    driver = webdriver.Chrome(path+"/chromedriver",options = option) 
    url = 'https://vb.rebelbetting.com/'
    driver.get(url)
    time.sleep(5)
    emailinput = driver.find_element_by_id('inputEmail')
    emailinput.send_keys('deanorebel@gmail.com')
    time.sleep(1)
    passwd = driver.find_element_by_id('inputPassword')
    passwd.send_keys('Deano1980')
    time.sleep(1)
    loginbutton = driver.find_element_by_class_name('mt-3.btn.btn-primary.btn-block')
    loginbutton.click()
    time.sleep(5) 

def is_check_username(username,id):
    if id == "0":
        rows = Tickets.objects.filter(username=username).count()
        if rows:
            return False
        else:
            return True
    else:
        rows = Tickets.objects.filter(username=username)
        if rows.count() > 1:
            return False
        elif rows.count() == 1:
            thisrow = Tickets.objects.get(username=username)
            if(thisrow.id == int(id)):
                return True
            else:
                return False   
        else:
            return True

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    user = request.user     
    nav = 'ticket'
    if not driver:
        print("not driver")
        set_driver()
    else:
        # driver.close()
        print("setted driver")
    
    return render(request,'ticket/dashboard.html',{'nav':nav}) 

def create(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    user = request.user 
    
    nav = 'ticket'
    return render(request,'ticket/create.html',{'nav':nav}) 

def edit(request,id):
    try:        
        row = Tickets.objects.get(id=id)        
        nav = 'ticket'
        return render(request,'ticket/create.html',{'nav':nav,'ticket':row})         
    except:
        nav = 'ticket'
        return redirect('/dashboard')

# ajax
def store(request):

    
    if not request.user.is_authenticated:
        results = False
        return JsonResponse({'results':results}) 
    else:        
        user = request.user         
        username = request.POST.get('username')
        license_key = request.POST.get('license')
        expire = request.POST.get('expire')
        connections = request.POST.get('connections')
        bookie = request.POST.get('bookie')    
        id = request.POST.get('which')

        is_valid = is_check_username(username,id)
        
        if is_valid:            
            if id == "0":
                row = Tickets(username=username,license_key=license_key,expire=expire,connections=connections,bookie=bookie)
                row.save() 
            else:
                row = Tickets.objects.get(id=id)
                row.username = username
                row.license_key = license_key
                row.expire = expire
                row.connections = connections
                row.bookie = bookie      
                row.save()
            results = True
            return JsonResponse({'results':results})    
        else:            
            return JsonResponse({'results':False,'is_username':False})  
    

def get_tickets(request):
    tickets = ''
    results = []
    pagenum = 0

    try:
               
        user = request.user
        currentPage = request.GET.get('currentPage')   
        tickets = Tickets.objects.all() 
       
        tickets = tickets.order_by('-created_at')
        pagenum = math.ceil(tickets.count()/PAGINATION_COUNT)
        paginator = Paginator(tickets,PAGINATION_COUNT)   
        resultscollection = paginator.get_page(currentPage) 
    
        for item in resultscollection:
            data = {}
            data['id'] = item.id       
            data['username'] = item.username
            data['license_key'] = item.license_key
            data['expire'] = item.expire
            data['connections'] = item.connections
            data['bookie'] = item.bookie
            data['status'] = item.status
            data['created_at'] = (item.created_at).strftime('%Y-%m-%d %H:%M:%S')            
            results.append(data)
            
        return JsonResponse({'results':results,'pagenum':pagenum})
    except:
        return JsonResponse({'results':results,'pagenum':pagenum})

def delete(request):
    try:
        id = request.GET.get('id')
        row = Tickets.objects.get(id=id)
        row.delete()
        return JsonResponse({'results':True})
    except:
        return JsonResponse({'results':False})


def ischecklicense(request):
    try:        
        username = request.GET.get('username')
        license_key = request.GET.get('license')        
        if Tickets.objects.filter(username=username).count():
            thisrow = Tickets.objects.get(username=username)
            if thisrow.license_key == license_key:
                return JsonResponse({'results':True,'username':True, 'license':True})
            else:
                return JsonResponse({'results':False,'username':True, 'license':False})
        else:
            return JsonResponse({'results':False,'username':False, 'license':False})   
        
    except:
        return JsonResponse({'results':False})


def get_stake(request):
    targetvalue = ''
    odds = ''
    stake = ''
    data = []
    try:        
        stake = request.GET.get('stake')
        print(stake)
               
        try:
            try:                
                reconnect = driver.find_elements_by_class_name('badge.badge-danger.m-2.p-2.clickable')[0]
                reconnect.click()
                time.sleep(3)
            except:
                pass
            valuebettingitem = driver.find_elements_by_class_name('odds-card.card-shadow.card-shadow-hover.d-flex.clickable.no-outline')
            for item in valuebettingitem:
                result={}
                item.click()
                time.sleep(5)
                targetvalue = driver.find_element_by_id('participants').text
                targetvalue = targetvalue.replace(" vs "," v ")         
                odds = driver.find_element_by_id('Odds').get_attribute('value')
                stake = driver.find_element_by_id('Stake').get_attribute('value')
                result['targetvalue'] = targetvalue
                result['odds'] = odds
                result['stake'] = stake
                data.append(result) 
                time.sleep(1)            
                driver.find_element_by_id('CloseSelectedCard').click()

        except:
            print('no item')
        
        return JsonResponse({'results':True,'data':data})
    except:
        return JsonResponse({'results':False,'data':data})