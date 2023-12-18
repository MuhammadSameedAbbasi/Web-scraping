# Import requests and BeautifulSoup libraries
import requests
from bs4 import BeautifulSoup

# Define the URL of the page
url = "https://www.yellowpages-uae.com/uae/freight-forwarders"

# Send a GET request and get the response
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")
outputfile = open("G:\Projects VS\webScraping\outputfilecarge.txt", "a")
# Find all the div elements that have the class "company-details"
divs = soup.find_all("div", class_="row box premium")

# Loop through each div element
for div in divs:
    # Find the h2 element that contains the name of the company
    h2 = div.find("h2",class_="cmp_name")
    # Get the text of the h2 element and strip any whitespace
    name = h2.text.strip()
    outputfile.write(name+"||")
    # Find the span element that contains the address of the company
    span = div.find("span", class_="location")
    # Get the text of the span element and strip any whitespace
    address = span.text.strip()
    outputfile.write(address+"||")
    
    #city
    spancity = div.find("span", class_="locationCity")
    # Get the text of the span element and strip any whitespace
    address = spancity.text.strip()
    outputfile.write(address+"||")

    # Find the span element that contains the phone number of the company
    span = div.find("span", class_="phone")
    # Get the text of the span element and strip any whitespace
    phone = span.text.strip()
    # Print the name, address, and phone number of the company
    outputfile.write(phone)
    outputfile.write("\n")



divs2 = soup.find_all("div", class_="row box regular")

# Loop through each div element
for div in divs2:
    # Find the h2 element that contains the name of the company
    h2 = div.find("h2",class_="cmp_name")
    # Get the text of the h2 element and strip any whitespace
    name = h2.text.strip()
    outputfile.write(name+"||")
    # Find the span element that contains the address of the company
    span = div.find("span", class_="location")
    # Get the text of the span element and strip any whitespace
    address = span.text.strip()
    outputfile.write(address+"||")
    
    #city
    spancity = div.find("span", class_="locationCity")
    # Get the text of the span element and strip any whitespace
    address = spancity.text.strip()
    outputfile.write(address+"||")

    # Find the span element that contains the phone number of the company
    span = div.find("span", class_="phone")
    # Get the text of the span element and strip any whitespace
    phone = span.text.strip()
    # Print the name, address, and phone number of the company
    outputfile.write(phone)
    outputfile.write("\n")

divs2 = soup.find_all("div", class_="row box foc")

# Loop through each div element
for div in divs2:
    # Find the h2 element that contains the name of the company
    h2 = div.find("h2",class_="cmp_name")
    # Get the text of the h2 element and strip any whitespace
    name = h2.text.strip()
    outputfile.write(name+"||")
    try:
        # Find the span element that contains the address of the company
        span = div.find("span", class_="location")
        # Get the text of the span element and strip any whitespace
        address = span.text.strip()
        outputfile.write(address+"||")
    except:
        pass
    
    #city
    spancity = div.find("span", class_="locationCity")
    # Get the text of the span element and strip any whitespace
    address = spancity.text.strip()
    outputfile.write(address+"||")

    # Find the span element that contains the phone number of the company
    span = div.find("span", class_="phone")
    # Get the text of the span element and strip any whitespace
    phone = span.text.strip()
    # Print the name, address, and phone number of the company
    outputfile.write(phone)
    outputfile.write("\n")
