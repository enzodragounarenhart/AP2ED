##def recursao(n: int):
#    if n <= 10:
#        return n*2
#    else:
#        print(recursao(n/3))
#        return recursao(recursao(n/3))
    
#print(recursao(27))

#caminhoneiros = ["João", "Jorge", "Enzo", "Lucas", "Paulo", "Gabriel", "Leonardo", "Kaynã", "Kauã", "Enrico"]
#total = 0
#
#def esta_vazia():
#    if total == 0:
#        return True
#    else:
#        return False
#
#def esta_cheia():
#    if total >=10:
#        return True
#    else:
#        return False
#    
#def enfileirar(nome: str):
#    if esta_cheia() == False:
#        total + 1
#        caminhoneiros[total] = nome
#        return f"{nome} enfileirado."
#    else:
#        print("Fila cheia")
#        
#def desenfileirar(index: int):
#    if esta_vazia == True:
#        print("Fila Vazia")
#    else:
#        deixou = caminhoneiros.pop(index)
#        total - 1
#        return f"{deixou} desenfileirado"
#    
#def mostrar_fila():
#    for nome in caminhoneiros:
#        print(nome)
#
#print(desenfileirar(4))
#print(enfileirar("Ricardo"))
#mostrar_fila()

pilha = []
i = topo = 0
palavra = ""

def push(valor):
    if len(pilha) == 0:
        pilha.append(valor)
        topo + 1
        
        
    else:
        pilha.insert(0, valor)
        topo + 1

    
def pop():
    topo - 1
    top = pilha.pop(0)
    return top
    
def inverter_palavra(word):
    word2 = ""
    for char in word:
        push(char)
    
    return palavra.join(pilha)
    
print(inverter_palavra("""What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little "clever" comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo."""))


print(27/3)