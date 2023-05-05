def don_limpio(url):    
    driver.get(url)
    lista = [word.text for word in driver.find_elements(By.TAG_NAME, "p")]
    
    indice = None
    for i, char in enumerate(texto):
        if char == "———":
            indice = i

    texto_final = texto[2:indice]
    cuerpo = []
    for str in texto_final:
        cuerpo.append(re.sub(r'[\[\]\{\}]', '', str))
    
    cuerpo
    obra = texto[1]
    
    return cuerpo, obra 