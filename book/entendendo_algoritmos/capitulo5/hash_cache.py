cache = {}

def pegar_pagina(url):
    if (cache.get(url)):
        print("CACHE")
        return cache[url]
    else:
        dados = pegar_dados(url)
        cache[url] = dados
        return dados
    

def pegar_dados(url):
    return f"https://{url}/teste"



print(pegar_pagina('facebook'))
print(pegar_pagina('facebook'))
print(pegar_pagina('kaedu'))