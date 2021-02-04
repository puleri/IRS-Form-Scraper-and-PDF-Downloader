# Import packages
from datetime import date
from pathlib import Path
import os
import json
# Packages not part of Python
import requests
from bs4 import BeautifulSoup

# datetime
todays_date = date.today()

# Use requests package to make GET req. to webpage to scrape
response = requests.get('https://apps.irs.gov/app/picklist/list/priorFormPublication.html')
# response = requests.get('https://apps.irs.gov/app/picklist/list/priorFormPublication.html?value=Form+W-2&criteria=formNumber&submitSearch=Find')

# Set up BeautifulSoup variable to parse GET req. made above
soup = BeautifulSoup(response.text, 'html.parser')

# Table we want to search through
# Found by inspecting web page and we are using BS4 to find and parse HTML
table = soup.find_all(class_='picklist-dataTable')[0]
posts = table.find_all('tr')
# i = type('', (), {})()
# i.form = 'wow'
# print(i.form)


# create empty array variable
formList = []
# print('initial list:', formList)

    # create empty object
class I:
    def __init__(self, form_number, form_title, min_year, max_year, pdf):
        self.form_number = form_number.strip()
        self.form_title = form_title.strip()
        self.min_year = min_year.strip()
        self.max_year = str(max_year)
        self.pdf = pdf.strip()

    # class method to access the get method without a specific instance

    def get(min, max):
        search = []
        if not os.path.exists('./PDFs'):
            os.makedirs("./PDFs")
        for el in formList:
            if min <= el.min_year and max >= el.min_year:
                search.append(el)
                url = el.pdf
                r = requests.get(url)
                home = str(Path.home())
                downloadPath = home+"/Downloads/ "+el.form_number+" - "+el.min_year+".pdf"
                subdirectoryPath = "./PDFs/"+el.form_number+" - "+el.min_year+".pdf"
                # print("home is", home)
                with open(subdirectoryPath, 'wb') as f:
                    f.write(r.content)
        return search

    def __repr__(self):
        return json.dumps({"form_number": self.form_number, "form_title": self.form_title,"min_year": self.min_year,"max_year": self.max_year}, indent=4, sort_keys=True)

    def __str__(self):
        return json.dumps({"form_number": self.form_number, "form_title": self.form_title,"min_year": self.min_year,"max_year": self.max_year}, indent=4, sort_keys=True)
        # "form_number: %s,\nform_title: %s,\nmin_year: %s,\nmax_year: %s" % (self.form_number, self.form_title, self.min_year, self.max_year)

# Iterate through posts
for el in posts:
    # initialize left, middle, and right so we have access to the changed
    # values outside of the "try" chunks
    form_number = 'Form Number'
    form_title = 'Form Title'
    min_year = 'Min Year'
    max_year = 'Max Year'
    pdf = 'PDF'
    # store the data from each of the points of the table
    try:
        form_number = el.find(class_='LeftCellSpacer').get_text()
    except AttributeError:
        print ("")

    try:
        form_title = el.find(class_='MiddleCellSpacer').get_text()
    except AttributeError:
        print ("")

    try:
        min_year = el.find(class_='EndCellSpacer').get_text()
        # Use current date from python datetime package to give max_year
        max_year = todays_date.year
    except AttributeError:
        print ("")

    try:
        pdf = el.find('a', href=True).get('href')
    except AttributeError:
        print ("")


    # print(left, middle, end, todays_date.year)

    # data = I(left, middle, end, todays_date.year)
    # print(data)

    # checks if original title was overwrittern with data. If not, do not append
    if form_title != 'Form Title':
        # append object onto the formList
        formList.append(I(form_number, form_title, min_year, max_year, pdf))
# print(formList)

instances = I.get('2002', '2012')
print(instances)
