# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 



# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

import re
import requests
from bs4 import BeautifulSoup

base_url = 'https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions'
r = requests.get(base_url)		#request to webpage
soup = BeautifulSoup(r.text, 'lxml')

text = soup.prettify()



one = text.replace("student", "“AMAZING student")


pic = re.findall('<iframe allowfullscreen=.+"',one)
two = one.replace(pic[0], '<img src="/Users/Khyatee1/Documents/2009/Halloween 2009/FILE0486.JPG" alt="UMSI logo">')


src =re.findall('img alt=.+ (src=.+/>)',two)
a = two.replace(src[0], 'src="/Users/Khyatee1/Desktop/logo.png"/>')
b = a.replace(src[2], 'src="/Users/Khyatee1/Desktop/logo.png"/>')


html= open("bsoup.html",'w')
html.write(b)
html.close()
 # <p>
 #             <iframe allowfullscreen="" frameborder="0" height="315" src="https://www.youtube.com/embed/mimp_3gquc4?feature=oembed" width="560">
 #             </iframe>
 #            </p>