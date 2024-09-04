import sys
import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def scrape_content(file_url):
    try:
        response = requests.get(file_url)
        response.raise_for_status()
        if "flag" in response.text:
            print("\033[92m" + response.text + "\033[0m")
            sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")

def scrape_website(root_addr, directory):
	"""
	This function recursively accesses all the links from the webpage
	and open each README file.
	"""
	url = root_addr + directory
	print(url)
	response = requests.get(url)

	if response.status_code == 200:
		# Parse the HTML content of the page
		soup = BeautifulSoup(response.content, 'html.parser')

		# Find all links on the page
		links = soup.find_all('a', href=True)

		# Extract and print file and directory URLs
		for link in links:
			href = link['href']
			full_url = urljoin(url, href)
			# We exclude the first link on each page that leads
			# to the previous directory 
			if href != "../":
				# If the link is not a README file we access the link
				# to get the included link set
				if href.lower() != "readme":
					print(full_url)
					scrape_website(url + "/", href)
				# If it's a README call print fille content 
				else: scrape_content(full_url)
	else:
		print('Failed to fetch the page:', response.status_code)

			
if __name__ == "__main__":
	scrape_website("http://localhost:8080/", ".hidden/")
