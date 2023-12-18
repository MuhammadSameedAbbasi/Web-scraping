# Import requests and BeautifulSoup libraries
import requests
from bs4 import BeautifulSoup



def readdata(divs):
    outputfile = open("G:\Projects VS\webScraping\outputfilecarge.txt", "a")
    # Loop through each div element
    for div in divs:
        try:
            # Find the h2 element that contains the name of the company
            h2 = div.find("h2",class_="cmp_name")
            # Get the text of the h2 element and strip any whitespace
            name = h2.text.strip()
            outputfile.write(name+"|")
        except:
            pass
        try:
            # Find the span element that contains the address of the company
            span = div.find("span", class_="location")
            # Get the text of the span element and strip any whitespace
            address = span.text.strip()
            outputfile.write(address+"|")
        except:
            pass

        try:
            #city
            spancity = div.find("span", class_="locationCity")
            # Get the text of the span element and strip any whitespace
            address = spancity.text.strip()
            outputfile.write(address+"|")
        except:
            pass

        try:
            # Find the span element that contains the phone number of the company
            span = div.find("span", class_="phone")
            # Get the text of the span element and strip any whitespace
            phone = span.text.strip()
            # Print the name, address, and phone number of the company
            outputfile.write(phone)
        except:
            pass
        outputfile.write("\n")



def box_call(soup):
    divs = soup.find_all("div", class_="row box premium")
    readdata(divs)

    divs = soup.find_all("div", class_="row box regular")
    readdata(divs)

    divs = soup.find_all("div", class_="row box foc")
    readdata(divs)

def page_call():
    # Define the URL of the page
    url = "https://www.yellowpages-uae.com/uae/freight-forwarders"

    # Send a GET request and get the response
    # response = requests.get(url)

    # # Parse the HTML content using BeautifulSoup
    # soup = BeautifulSoup(response.content, "html.parser")
    # box_call(soup)

    for i in range(20,21):
        url += "-" + str(i) + ".html"
        # Send a GET request and get the response
        response = requests.get(url)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")
        box_call(soup)


page_call()