from pathlib import Path
import shutil
import json

with open(r"D:\Users\Dell\Documents\Web Projects\react\Plant Diseases\frontend\src\data\united.json","r") as f:
    data=json.loads(f.read())
    
    
DOWNLOADS_DIR = Path(r"C:\Users\Dell\Downloads")
IMAGE_DIR = Path(r"D:\Users\Dell\Documents\Web Projects\react\Plant Diseases\frontend\src\images")

for path in DOWNLOADS_DIR.glob('*jpg'):
    name=path.name.split(".")[0]
    try:
        data[name]['image']=path.name
        shutil.move(str(path), str(IMAGE_DIR/path.name))
        break
    except KeyError:
        for key,value in data.items():
            try:
                value[name]['image']=path.name
                shutil.move(str(path), str(IMAGE_DIR/path.name))
                break
            except KeyError:
                continue
                
with open(r"D:\Users\Dell\Documents\Web Projects\react\Plant Diseases\frontend\src\data\united.json","w") as f:
    json.dump(data,f, indent=4)                
       
                
        