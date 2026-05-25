"""
Porco Latino =  língua infantil inventada e difícil de entender para adultos

Tradução feita apatir da analise do padrão de vogais e consoantes no inicio de cada palavra 

Regra 1
Se uma palavra começa com uma vogal, ou começa com "xr""ou" "yt", 
adicione um "ay"som ao final da palavra.
Por exemplo:

"apple"-> "appleay"(começa com vogal)
"xray"-> "xrayay"(começa com "xr")
"yttria"-> "yttriaay"(começa com "yt")

Regra 2
Se uma palavra começa com uma ou mais consoantes, primeiro mova essas consoantes para o final da palavra e 
depois adicione um "ay"som ao final da palavra.

Por exemplo:

"pig"-> "igp"-> "igpay"(começa com uma única consoante)
"chair"-> "airch"-> "airchay"(começa com várias consoantes)
"thrush"-> "ushthr"-> "ushthray"(começa com várias consoantes)

Regra 3
Se uma palavra começa com zero ou mais consoantes seguidas de "qu", primeiro mova essas consoantes (se houver) e 
a "qu"parte para o final da palavra e, em seguida, adicione um "ay"som ao final da palavra.

Por exemplo:

"quick"-> "ickqu"-> "ickquay"(começa com "qu", sem consoantes precedentes)
"square"-> "aresqu"-> "aresquay"(começa com uma consoante seguida de "qu")

Regra 4
Se uma palavra começa com uma ou mais consoantes seguidas de um som "y", primeiro mova as consoantes que precedem o som "y"para o final da palavra e, em seguida, adicione um "ay"som ao final da palavra.

Alguns exemplos:

"my"-> "ym"-> "ymay"(começa com uma única consoante seguida de "y")
"rhythm"-> "ythmrh"-> "ythmrhay"(começa com várias consoantes seguidas de "y")
"""


texto = input("Informe o texto a ser traduzido: ").split()

def translate(texto):
    vogal = ['a','e','i','o','u']
    consoante = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    caractere_especial = ['xr','yt']

    for i, palavra in enumerate(texto):

        if palavra[0].lower() in vogal or palavra[:2].lower() in caractere_especial:
            # Regra 1
            palavra = palavra+'ay'
            texto[i] = palavra
        elif palavra[0].lower() in consoante:
            # Regra 2
            palavra = palavra+palavra[0]+'ay'
            texto[i] = palavra
        elif palavra[1].lower() in consoante and palavra[2].lower() in consoante:
            # Regra 2
            palavra = palavra+palavra[:2]+'ay'
            texto[i] = palavra
        elif palavra[1].lower() in consoante and palavra[2].lower() in consoante and palavra[3].lower() in consoante:
            # Regra 2
            palavra = palavra+palavra[:2]+'ay'
            texto[i] = palavra
        elif palavra[0] in consoante and palavra[1:3] in 'qu':
            # Regra 3
            palavra = palavra+palavra[:3]+'ay' ''' Revisar ''' 
            texto[i] = palavra
        elif palavra[:2] in 'qu':
            # Regra 3
            palavra = palavra+palavra[:2]+'ay' ''' Revisar ''' 
            texto[i] = palavra

        # Regra 4
        

        texto = " ".join(texto)
        print(" ")
        print("Texto traduzido ==> "+ texto)
        
