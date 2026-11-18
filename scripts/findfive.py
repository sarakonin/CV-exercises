# script to find directories with most species

import json, re
import operator

f=open("/home/s/projects/cv-practice/data/metadata/wsu-lynx.json")
data=json.load(f)
for i in data:
    print(i)
print(data["categories"])
camera_number_species={}
path=''
for i in data["annotations"]:
    path=i["id"]
    cat_id=str(i["category_id"])
    dir=re.search(".*/(.*)/.*",path)
    if dir is not None:
        if dir.group(1) in camera_number_species:
            if cat_id in camera_number_species[dir.group(1)]:
                camera_number_species[dir.group(1)][cat_id]+=1
            else:
                camera_number_species[dir.group(1)][cat_id]=1
        else:
            camera_number_species[dir.group(1)]={}
            camera_number_species[dir.group(1)][cat_id]=1

# for i in camera_number_species:
#     print(i, camera_number_species[i])

camera_species={}
for i in camera_number_species:
    camera_species[i]=len(camera_number_species[i])

# for i in camera_species:
#     print(i, camera_species[i])

camera_species_sorted = dict(sorted(camera_species.items(), key=operator.itemgetter(1), reverse=True))

# for i in camera_species_sorted:
#     print(i, camera_species_sorted[i])

to_download=list(camera_species_sorted.keys())[:5]

# print(to_download)

# ['Cell221Camera2', 'Cell221Camera4', 'Cell37Camera4K', 'Cell47Camera3', 'Cell57Camera2']

f.close()
