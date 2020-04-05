

from django.shortcuts import render
from django.http import HttpResponse




def covid(request):
    import requests
    from bs4 import BeautifulSoup

    covid19 = 'https://www.trackcorona.live/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    full_page = requests.get(covid19, headers=headers)
    print(full_page.content)

    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll('a', {'id': 'valueTot'})
    context = {'convert':convert[0].text}
    return render(request,'covid/covid.html', context)
