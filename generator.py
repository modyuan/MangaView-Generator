#!/usr/bin/env python3

import os


def generate_section(name :str, pages_dir: list):
    name = name.replace("<","").replace(">","").replace("\"","").replace("&","")
    tamplate_prefix = f"<div id='{name}' style='border-top: 10px skyblue solid'>\n<h2>{name}</h2>\n"
    tamplate_mid = "<h5>{0}</h5><img src='{1}' />\n"
    tamplate_suffix = "</div>\n\n"

    mid_text = ""
    for i,v in enumerate(pages_dir):
        mid_text += tamplate_mid.format(i,v)
    
    return tamplate_prefix + mid_text + tamplate_suffix



if __name__ == "__main__":
    cwd = os.getcwd()
    subfiles = os.listdir(cwd)
    dirs = list(filter(lambda x: os.path.isdir(x), subfiles))

    dirs.sort()
    
    title = cwd.split(os.sep)[-1]

    htmls_prefix = f"<!DOCTYPE html>\n" +  \
    f"<html><head><meta charset=\"UTF-8\" /><title>{title}</title></head>\n<body>\n"

    htmls_prefix += '''
    <style>
    img{
        display: block;
        margin: auto
    }
    h1,h2,h5{
        text-align: center;
    }
    </style>
    '''

    htmls_suffix = "\n</body></html>"

    htmls_mid = ""
    img_exts = ["jpg","jpeg","png","bmp"]

    for dir in dirs:
        subfiles2 = os.listdir(dir)
        imgs = list(filter(lambda x : x.split(".")[-1].lower() in img_exts, subfiles2))
        imgs.sort()
        imgs2 = []
        imgs_len = len(imgs)
        print(f"找到子文件夹: {dir}, 找到图片{imgs_len}张。 ")
        for img in imgs:
            imgs2.append( os.path.join(dir, img))
        
        htmls_mid += generate_section(dir,imgs2)
    
    final = htmls_prefix + htmls_mid + htmls_suffix

    file = open(title+".html","w",encoding="utf-8")
    file.write(final)
    file.close()
    print(f"\n写入HTML文件: {title}.html")
    print("\n>>>>>>>>>>> OK! >>>>>>>>>>>\n")




