def norm(value):
    return value.lower().replace("/","___")

with open("dokubase.html","r") as base:
    with open("doctemplate.html","r") as tmpl:
        with open("index.html","w") as oux:
            topdata = ""
            navdata = ""
            element_config = ""
            element_descr = ""
            element_content = ""
            for line in base.readlines():
                if line.startswith("#"):
                    if element_config != "":
                        navdata += f"<li><a href='#{norm(element_config.split('#')[1])}'>{element_config.split('#')[1]}</a></li>"
                        topdata += (f"<article id='{norm(element_config.split('#')[1])}'><h2>{element_config.split('#')[1]}@{element_config.split('#')[3]}</h2><a href='#top'>Go to top</a><br><p>{element_descr}</p><br><div class='codecont'><code>{element_content.replace("<","&lt;").replace(">","&gt;").replace("\n","<br>").replace(" ","&nbsp;")}</code></div><br>")
                        if "UGEN" in element_config.split('#')[2].split(' '):
                            topdata += (f"<div class='examplecont'>{element_content.replace("\n","")}</div><br>")
                        topdata += "</article>"
                        element_config = ""
                        element_content = ""
                    element_config = line
                elif line.startswith("!"):
                   element_descr = line[1:]
                else:
                    if line != "\n" and line != "":
                        element_content += line
            if element_config != "":
                topdata += (f"<h2>{element_config.split('#')[1]}@{element_config.split('#')[3]}</h2><br><div class='codecont'><code>{element_content.replace("<","&lt;").replace(">","&gt;").replace("\n","<br>").replace(" ","&nbsp;")}</code></div><br>")
                print(element_config.split('#')[2].replace("\n","").split(' '))
                if "UGEN" in element_config.split('#')[2].replace("\n","").split(' '):
                    topdata += (f"<div class='examplecont'>{element_content.replace("\n","")}</div><br>")
                element_config = ""
            oux.write(tmpl.read().replace("&&CONTENT&&",topdata.replace(">",">\n")).replace("&&NAV&&",f"<article id='top'><ul>{navdata}</ul></article>").replace("'","\""))