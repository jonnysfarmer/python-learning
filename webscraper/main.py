from bs4 import BeautifulSoup
import requests

search = input('Search For: ')
params = {'q': search}
# does a request for first page of bing search resuls
r = requests.get('https://www.bing.com/search', params=params)

# uses beautiful soup to pass the html into text
soup = BeautifulSoup(r.text, 'html.parser')

# So it finds the 'ol' / ordered list with the id 'b_results'
results = soup.find('ol', {'id': 'b_results'})
# within results, we find ALL the 'li' with the class 'b_algo'
links = results.findAll('li', {'class': 'b_algo'})

# We iteratate of Links and set Item_text to the text within the linke
# and href as the arribute href of the 'a' tags
for item in links:
    item_text = item.find('a').text
    item_href = item.find('a').attrs['href']
    # This is an example how you can look at parents etc of attributes
    item_summary = item.find('a').parent.parent.find('p').text

# if both of these excist, then we print them
    if item_text and item_href and item_summary:
        print(item_text)
        print(item_href)
        print('Summary:', item_summary) 
