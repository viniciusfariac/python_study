def domain_name(url: str):
    ponto = url.find(".")
    barra = url.find("//")
    www = url.find("www")
    co = url.find(".co")
    us = url.find(".us")
    ultimo_ponto = url.rfind(".")
    if (ponto > -1 and barra > -1 and www == -1):
        return url[barra + 2:ponto]
    if (www > -1 and ultimo_ponto > -1):
        return url[www + 4:ultimo_ponto]
    if (co > -1):
        return url[www + 4:co]
    if (us > -1):
        return url[www + 4:us]

    return url [0:ponto]
    
print(domain_name("http://www.543hubrhpauy60ugz2.us/default.html"))