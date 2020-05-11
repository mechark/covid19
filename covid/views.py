from django.shortcuts import render
import requests
from bs4 import BeautifulSoup




def covid(request):
    url = 'https://www.worldometers.info/coronavirus/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    finall = soup.find('div', class_="maincounter-number").text
    context = {
        'finall':finall
    }
    return render(request,'covid/covid.html', context)
