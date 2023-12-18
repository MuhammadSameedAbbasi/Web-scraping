import requests as req

from bs4 import BeautifulSoup as bs

#url = "https://www.curefip.com/oral-fip-treatment"
url="https://www.curefip.com/shop-gs441524"
r = req.get(url)

soup = bs(r.content, 'html.parser')

#product_containers = soup.find_all('div', class_='sXCF_kh o__17P3j2---resize-5-cover o__17P3j2--fluid o__17P3j2--stretchImage o__17P3j2--verticalContainer s__65YAB3 v_lwe5')
product_containers = soup.find_all('div', class_='ETPbIy')
# Loop through each product container and extract the details
for product in product_containers:

    #get image sources in this class
    img_element = product.find('img')
    img_src = img_element['src']
    imglink= img_src.split('/v1/')[0]
    name = img_element['alt']
    
    price = product.find('span', class_='cfpn1d').text
    
    
    # Print the details of the product
    print(f'{name}\t {price}\t {imglink}\n')
#class="S4WbK_ uQ5Uah c2Zj9x"class="S4WbK_ uQ5Uah c2Zj9x"
#src="https://static.wixstatic.com/media/458dcb_17f692458cb740e685f77ca155d3f3cf~mv2.png/v1/fill/w_321,h_321,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/458dcb_17f692458cb740e685f77ca155d3f3cf~mv2.png"
#src="https://static.wixstatic.com/media/458dcb_17f692458cb740e685f77ca155d3f3cf~mv2.png/v1/fill/w_49,h_49,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_auto/458dcb_17f692458cb740e685f77ca155d3f3cf~mv2.png