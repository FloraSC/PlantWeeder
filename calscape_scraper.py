import mysql.connector
import urllib.request
from bs4 import BeautifulSoup

hostname = 'mediaq.usc.edu'
username = 'cnp_app'
password = 'nLlfoblVj1vq'
database = 'native_plants'


def page_url_gen():
    for i in range(1,80):
        yield 'https://calscape.org/loc-California/cat-All-Plants/page-' + str(i)

def plant_info_url(plant_name, plant_species):
    return 'https://calscape.org/' + '-'.join(plant_species.split()) + '-(' + '-'.join(plant_name.split()) + ')'

def get_plant_entries(page_url):
    entries = []
    raw_html = urllib.request.urlopen(page_url).read()
    soup = BeautifulSoup(raw_html)
    plant_table = soup.find(
        "div", {"id": "page_main_content"}).find("div", {"class": "plants_view"}).find("div", {"class": "content view_grid"})
    for row in plant_table.find_all("div", {"class": "row"}):
        plant_info = row.find("div", {"class": "info"}).find("div", {"class": "pad"}).find("a")
        plant_name = plant_info.find("span", {"class": "common_name"}).text
        plant_species = plant_info.find("span", {"class": "species_text"}).text
        entries.append((plant_species, plant_name, plant_info_url(plant_name, plant_species)))

    return entries

if __name__ == '__main__':
	conn = mysql.connector.connect(host=hostname, user=username, passwd=password, database=database)
	curr = conn.cursor()

	sql = "INSERT INTO native_plants (scientific_name, common_name, url) VALUES (%s,%s,%s)"
    for page_url in page_url_gen():
        print("\n\n" + page_url)
		plant_entries = get_plant_entries(page_url)
		curr.executemany(sql, plant_entries)
		conn.commit()
        print(plant_entries)
	conn.close()
