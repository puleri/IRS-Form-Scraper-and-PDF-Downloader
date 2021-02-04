# IRS Form Scraper and PDF Downloader

## Objectives

The code in IRS_Form_Scraper.py and PDF_downlader.py will:

- Convert form data on search results at [the IRS form site](https://apps.irs.gov/app/picklist/list/priorFormPublication.html?value=Form+W-2&criteria=formNumber&submitSearch=Find) to JSON
- Search and download PDFs in the given range of years from page in sub-directory

## Preparation
If you do not already have Beautiful Soup or Requests installed, you will need
to do so. Run `pip3 install beautifulsoup4` or `pip install beautifulsoup4` if
you are not on Mac. Do the same thing with `pip3 install requests` or `pip
install requests`.



## Technologies Used
- Python (version 3.8) and its built in libraries
- Beautiful Soup 4 - To parse and query HTML
- Requests - To make GET request to webpage for data
