from warnings import filterwarnings
from PIL import Image, ImageOps
from jikanpy import Jikan
from requests import get
from time import sleep
import re
import os

print('''Run this in your anime folder
For help, info and memes, check out
https://github.com/notdedsec/anicon
''')

sleep(1)
jikan = Jikan()
filterwarnings("ignore")
folderlist = next(os.walk('.'))[1]
automode = True if input('Use AutoMode? Y/N : ').upper() == 'Y' else False

def getname(name):

    lastwords = ['bd', 's0', '480p', '720p', '1080p']
    wordstoremove = ['bluray', 'x265', 'x264', 'hevc', 'hi10p', 'avc', '10bit', 'dual', 'audio', 'eng', 'english', 'subbed', 'sub', 'dubbed', 'dub']

    name = name.lower().replace('_', ' ').replace('.', ' ')
    
    for word in wordstoremove:
        name = name.replace(word, '')
    
    name = re.sub(r"(?<=\[)(.*?)(?=\])", '', name)
    name = re.sub(r"(?<=\()(.*?)(?=\))", '', name)
    name = name.replace('()', '').replace('[]', '')

    for word in lastwords:
        rexstr = "(?<=" + word + ")(?s)(.*$)"
        name = re.sub(rexstr, '', name).replace(word, '')

    return(name.strip())

def getartwork(name):
    
    results = jikan.search('anime', name, parameters={'type': 'tv'})

    print('\n' + name.title(), end = '')
    counter = 1
    for result in results['results']:
        if automode:
            print(' - ' + result['title'])
            ch = 1
            break
        else:
            print('\n' + str(counter) + ' - ' + result['title'], end = '')
            
        if counter == 5:
            break
        counter += 1

    if not automode:
        ch = input('\n>')
        if ch == '':
            ch = 1

    return(results['results'][int(ch)-1]['image_url'])

def createicon(folder, link):

    art = get(link)
    open(jpgfile, 'wb').write(art.content)

    img = Image.open(jpgfile)
    img = ImageOps.expand(img, (69, 0, 69, 0), fill=0)
    img = ImageOps.fit(img, (300,300)).convert("RGBA")
    
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            newData.append((0, 0, 0, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    os.remove(jpgfile)
    img.save(icofile)
    img.close()
    return(icofile)

for folder in folderlist:

    name = getname(folder)

    iconname = name.replace(' ', '_')
    jpgfile = folder + '\\' + iconname + '.jpg'
    icofile = folder + '\\' + iconname + '.ico'
    
    if os.path.isfile(icofile):
        continue

    link = getartwork(name)
    
    try:
        icon = createicon(folder, link)
    except:
        continue

    f= open(folder + "\\desktop.ini","w+")
    f.write("[.ShellClassInfo]\nIconResource={}\\{},0".format(os.getcwd(), icon))
    os.system('attrib +r \"{}\\{}\"'.format(os.getcwd(), folder))
    os.system('attrib +h +s \"{}\\desktop.ini\"'.format(folder))
    os.system('attrib +h \"{}\"'.format(icon))
