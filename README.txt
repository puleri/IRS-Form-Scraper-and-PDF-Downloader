# IRS Form Scraper and PDF Downloader

## Objectives

The code in IRS_Form_Scraper.py and PDF_downlader.py will:

- Convert form data on search results at [the IRS form site](https://apps.irs.gov/app/picklist/list/priorFormPublication.html) to JSON
- Search and download PDFs in the given range of years from page in a
sub-directory

## Preparation
If you do not already have Beautiful Soup or Requests installed, you will need
to do so. From the command line run `pip3 install beautifulsoup4` or
`pip install beautifulsoup4` if you are not on Mac. Do the same thing with
`pip3 install requests` or `pip install requests`.

## Form Scraping and JSON data
In order to run IRS_Form_Scraper.py as is, open to the root of the project
and execute `python IRS_Form_Scraper.py`. To scrape a different IRS form Table
simply replace the URL on line 13 with the url with the contents you want and
run the command.

The JSON data returned


## PDF Downloading
Like before, in order to run the PDF_downlader.py as is, open to the root of the
project and execute `python PDF_downlader.py`. To download from a different IRS
form Table simply replace the URL on line 13 with the url with the contents you
want and change the minimum and maximum year parameters on line 114 then run the
command.

### Technologies Used
- Python (version 3.8) and its built in libraries
- Beautiful Soup 4 - To parse and query HTML
- Requests - To make GET request to webpage for data
