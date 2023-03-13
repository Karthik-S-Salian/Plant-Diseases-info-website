from bs4 import BeautifulSoup,Tag, NavigableString
import re
from bs4.formatter import HTMLFormatter
import pathlib
import json


def clone_soup(el):
    if isinstance(el, NavigableString):
        return type(el)(el)

    copy = Tag(None, el.builder, el.name, el.namespace, el.nsprefix)
    # work around bug where there is no builder set
    # https://bugs.launchpad.net/beautifulsoup/+bug/1307471
    copy.attrs = dict(el.attrs)
    for attr in ('can_be_empty_element', 'hidden'):
        setattr(copy, attr, getattr(el, attr))
    for child in el.contents:
        copy.append(clone_soup(child))
    return copy


def CleanSoup(soup):
    content=clone_soup(soup)
    for tag in content.findAll(True): 
        if tag.name=='a':
            if tag.attrs.get("name",None):
                tag.attrs = {"name":tag.attrs["name"]}
            elif tag.attrs.get("href",None):
                tag.attrs = {"href":tag.attrs["href"]}
            else:
                tag.decompose()
        elif tag.name=='img':
            attrs=dict()
            for prop in ["width","height","alt","src"]:
                value=tag.attrs.get(prop,None)
                if value:
                    attrs[prop]=value
            tag.attrs=attrs
        else:
            tag.attrs = {}
    return content


def write_html(soup,file_name="test"):
    with open(f"{file_name}.html","w",encoding="UTF-8") as fh:
        fh.write(str(soup.prettify(formatter=HTMLFormatter(indent=4))))


def get_next_tag(soup):
    next_ele=soup
    while next_ele is not None:
        next_ele=next_ele.next_element
        if isinstance(next_ele,Tag):
            return next_ele
    
    return None


def get_previous_tag(soup):
    next_ele=soup
    while next_ele is not None:
        next_ele=next_ele.previous_element
        if isinstance(next_ele,Tag):
            return next_ele
    return None


def jsonify_data_in_soup(soup):
    main_dict={}
    for section in soup.findAll("section")[1:]:
        disease=str(section.find("h3").text)
        d=dict(dict())
        for h4 in section.findAll("h4"):
            content={}

            content_list=list()

            for next_ele in h4.findNextSiblings():
                
                if  next_ele.name in ["h4","section"]:
                    break

                if next_ele.name=="img":
                    update=True
                    content["img"]={
                        "src":next_ele.attrs["src"],
                        "alt":next_ele.attrs.get("alt",disease)
                }
                elif next_ele.name=="ul":
                    update=True
                    content_list.extend(map(lambda x:x.text.strip(),next_ele.find_all("li")))
                elif next_ele.text.strip():
                    update=True
                    content_list.append(next_ele.text.strip())
                         
            content["content"]=content_list
            d[str(h4.text)]=content

        main_dict[disease]=d

    return main_dict

    
def write_json(data,path,file_name):
    with open(f"{path}/{file_name}.json", "w") as outfile:
        json.dump(data, outfile,indent=4)


def beautifySoup(soup):
    # removing unnecessary tag groups [tag+content]
    removable=soup.find_all("p")[-3:]
    removable.append(soup.find_all("h3")[-1])
    removable.append(soup.find("div",{"class":"col text-right"}))

    for tag in removable:
        tag.decompose()
    
    #************************************************

    # removing classes and unnecessary id and other tag props
    soup1=CleanSoup(soup)

    #*************************************************

    # in order to make container for each disease detail add wording 
    # REPLACE at selected location to after replace using regex
    # with section tags

    for tag in soup1.findAll(True): 
        if tag.name=='a':
            if tag.attrs.get("name",None):
                tag.attrs = {"name":tag.attrs["name"]}
                tag.insert_before(soup.new_string("REPLACE"))

    #**************************************************

    #replacing REPLACE with section Tags 
    # here soup is converted into text

    REPLACE_PATTERN=r'REPLACE(?=<a.*?name="section.*?(?=a>))'
    new_text=re.sub(REPLACE_PATTERN,"\n</section>\n<section>\n",str(soup1))

    # converting text to soup it also removes extra section tags added
    #specifically </section> at top and <section> at bottom

    soup2=BeautifulSoup(new_text,"html.parser")

    # removing last section
    soup2.find_all("section")[-1].decompose()

    #**************************************************

    # removing reductant div 
    soup2.div.unwrap()
    soup2.div.unwrap()

    for tag in soup2.div.find_all("div",recursive=False):
        tag.div.unwrap()

    soup2.div.find_all("div",recursive=False)[0].div.unwrap()

    # converting first div to section
    soup2.div.div.name="section"
    #********************************************

    # moving image to before unordered list if it is in ul or para after ul
    for section in soup2.findAll("section"):
        image=section.find("img")
        if image:
            image.attrs["alt"]=image.attrs.get("alt",image.find_previous("h3").text)
            parent=image.find_parent()
            if parent.name in ['p','li']:
                ul=image.find_previous("ul")
                if ul:
                    ul.insert_before(image.extract())
                    if parent.text:
                        new_li=soup2.new_tag('li')
                        new_li.append(soup2.new_string(str(parent.text)))
                        ul.insert(0,new_li)
                    parent.decompose()
                

    #*************************************************************

    #converting all strong and b tags to h4
    for tag in soup2.findAll(["strong","b"]):
        if tag.name=="b":
            if tag.parent.name=="li":
                continue
        tag.name="h4"

    #*************************************************************

    # removing additional h4 tags for 'primary' and "secondary" to maintain 
    # symmetry in all pages and not to add any html tags in jsonified data
    for li in soup2.findAll("li"):
        for h4 in li.find_all("h4"):
            h4.extract()
            li.string=str(h4.text+" "+li.text)
    
    #**************************************************************

    # removing problematic sections formed in fennel.html
    for section in soup2.findAll("section")[1:]:
        if section.find("h3") is None:
            section.decompose()

    #**************************************************************

    #removing empty tags
    
    for tag in soup2.findAll(True):
        if tag.name in ['a','img']:
            continue
        if not re.sub(" +","",tag.text):
            tag.decompose()

    #******************************************************************
    #removing last section link in table of content
    soup2.find("section").find_all("li")[-1].decompose()
    #**************************************************************

    for tag in soup2.findAll(["h4","ul"]):
        while not tag.parent.name == "section":
            tag.parent.unwrap()

    return soup2


def main():
    united_data=dict()
    html_folder_path=pathlib.Path(r"D:\Users\Dell\Documents\Web Projects\react\Plant Diseases\web-scraping\initial-extract")
    for file in html_folder_path.glob("*/*.html"):
        with open(str(file),"r",encoding="UTF-8") as fh:

            file_name=file.name.replace(".html", "")
            print(file_name)

            soup=BeautifulSoup(fh.read(),"html.parser")

            formated_soup=beautifySoup(soup)

            write_html(formated_soup,f'D:/Users/Dell/Documents/Web Projects/react\Plant Diseases/web-scraping/filtered-html-files\{file_name}')
            jsonifed_data=jsonify_data_in_soup(formated_soup)

            united_data[file.parent.name]=united_data.get(file.parent.name,dict())
            d=dict()
            d["image"]=""
            d["diseases"]=jsonifed_data
            united_data[file.parent.name][file_name]=d
            united_data[file.parent.name]["image"]=""

            write_json(jsonifed_data, 'D:/Users/Dell/Documents/Web Projects/react\Plant Diseases/web-scraping/jsonified-data', file_name)

            print(f"{file_name}  Completed")

    write_json(united_data, 'D:/Users/Dell/Documents/Web Projects/react\Plant Diseases/web-scraping/jsonified-data', "united")

    print("united completed")

    print("\n\n",'*'*20,"EXTRACTION COMPLETED",'*'*20,"\n\n")

if __name__=="__main__":
    main()



