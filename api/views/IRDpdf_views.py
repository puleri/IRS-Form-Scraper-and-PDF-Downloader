# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
import requests
import json
from bs4 import BeautifulSoup

from ..models.IRSpdf import IRSpdf
from ..serializers import IRSpdfSerializer

class IRSpdfs (generics.ListCreateAPIView):
    def post(self, request):
        # Create request
        IRSpdf = IRSpdfSerializer
        def post(self, request):
            # Use requests package to make GET req. to webpage to scrape
            response = requests.get('https://apps.irs.gov/app/picklist/list/priorFormPublication.html')
            # Set up BeautifulSoup variable to parse GET req. made above
            soup = BeautifulSoup(response.text, 'html.parser')
            # Table we want to search through
            # Found by inspecting web page and we are using BS4 to find and parse HTML
            table = soup.find_all(class_='picklist-dataTable')[0]
            posts = table.find_all('tr')
            for el in posts:
                print(json.dumps(el.get_text().replace('\n', ' ').replace('\t', '')))









    # revisionDate = el.find(class_='EndCellSpacer')
    # titleTag = el.find(class_='MiddleCellSpacer')
    # productNumber = el.find(class_='LeftCellSpacer')
    # PDF = el.find(class_='LeftCellSpacer')
    # Link = PDF.find('a')['href']
    #
    # print(el.find(class_="LeftCellSpacer"))
