from requests_html import HTMLSession
from bs4 import BeautifulSoup
import re
from pathlib import Path

BASE_STORAGE_PATH=Path(r"D:\Users\Dell\Documents\Web Projects\react\Plant Diseases\web-scraping\initial-extract")



BASE_URL="https://vikaspedia.in/agriculture/crop-production/integrated-pest-managment/"

session = HTMLSession(verify=False)
r1 =session.get(BASE_URL,timeout=20)
r1.html.render()

not_extracted=[]

for i in r1.html.find("#texttospeak",first=True).find("a"):
	category_text=i.text.strip().lower()
	if category_text.startswith("ipm for"):

		r2 =session.get(list(i.absolute_links)[0],timeout=20)
		r2.html.render()
		category_name=re.findall(r'(?<=for).*',category_text)[0].strip().replace("/"," ").replace("\\"," ")  #r'(?<=for-)[A-z-]+$'

		for j in r2.html.find("#texttospeak",first=True).find("a"):
			next_text=j.text.strip().lower()

			if next_text.startswith("ipm strategies for"):
				print(next_text)
				file_name=re.findall(r'(?<=for).*',next_text)[0].strip().replace("/"," ").replace("\\"," ")
				not_extracted.append(file_name)
				
				r3 =session.get(list(j.absolute_links)[0],timeout=20)
				r3.html.render()

				for k in r3.html.find("#texttospeak",first=True).find("a"):
					if re.search("disease",k.text.strip().lower()):
						absolute_link_k=list(k.absolute_links)[0]
						r4 =session.get(absolute_link_k)
						r4.html.render()
						output_path=BASE_STORAGE_PATH/category_name
						output_path.mkdir(exist_ok=True)
						
						with open(f"{str(output_path)}/{file_name}.html","w", encoding="utf-8") as fh:
							not_extracted.pop()
							fh.write(r4.html.find("#texttospeak",first=True).html)


session.close()

print(not_extracted) #['walnut', 'peach', 'oilpalm', 'sunflower', 'brinjal', 'okra']