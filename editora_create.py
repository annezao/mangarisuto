# -*- coding: utf-8 -*-
"""
id: string
nome: string
autor: string
status: string (Opções: Completo, Andamento, Cancelado e Hiato)
ano_inicio: int
ano_fim: int
sinopse: string
num_de_volumes: int
publico: string (Opções: Shojo, Josei, Shonen e Seinen)
genero: lista de string
impressao: string
revista: string
venda_mensal: [ [ano, mes, quantidade], [ano, mes, quantidade], ..., [ano, mes, quantidade] lista de lista de int
"""
# ----------------------------------------------------------------------------#
# -------------------------------------ID-------------------------------------#
# ----------------------------------------------------------------------------#
# checa se o ID recebido já foi utilizado
def checar_id(id, dic_mangas):
    
    for chaves_manga in dic_mangas.keys():
        if id == chaves_manga:
            print(f"ID repetido, por favor insira outro ID.")
            return True
    
    return False
# ------------------------------------ID--------------------------------------#
# pede um novo ID ao usuário para cadastro e checa o valor desse ID
def adicionar_id(dic_mangas):
    
    flag_id_repetido = True
    while flag_id_repetido == True:
        id = input(("Entre com o ID do novo mangá que você deseja cadastrar: "))
        flag_id_repetido = checar_id(id, dic_mangas)
        
    return id


# ----------------------------------------------------------------------------#
# ----------------------------------STATUS------------------------------------#
# ----------------------------------------------------------------------------#
# checa se o status recebido é válido: Completo ou Andamento ou Cancelado ou Hiato
def checar_status(status):

    if status == "Completo" or status == "Andamento" or status == "Cancelado" or status == "Hiato":
        return True
    
    print(f"Status incorreto, por favor insira um status válido.")   
    return False
# ----------------------------------STATUS------------------------------------#
# pede o status do mangá ao usuário e checa se é válido
def adicionar_status():
    
    flag_status_valido = False
    while flag_status_valido == False:
        status = input(("Entre com o status do mangá que você deseja cadastrar - Completo ou Andamento ou Cancelado ou Hiato - : "))
        flag_status_valido = checar_status(status)
        
    return status


# ----------------------------------------------------------------------------#
# -------------------------------ANO DE INICIO--------------------------------#
# ----------------------------------------------------------------------------#
# checa se o ano recebido é válido
def checar_ano_inicio(ano_inicio):

    if ano_inicio >= 0:
        return True
    
    print(f"O ano do início da publicação não é válido, por favor insira um ano válido.")   
    return False
# -------------------------------ANO DE INICIO--------------------------------#
# pede o ano que o mangá começou a ser publicado e checa se é válido
def adicionar_ano_inicio():
    
    flag_ano_inicio_valido = False
    while flag_ano_inicio_valido == False:
        ano_inicio = int(input(("Entre com o ano que o mangá começou a ser publicado: ")))
        flag_ano_inicio_valido = checar_ano_inicio(ano_inicio)
        
    return int(ano_inicio)


# ----------------------------------------------------------------------------#
# --------------------------------ANO DE FIM----------------------------------#
# ----------------------------------------------------------------------------#
# checa se o ano recebido é válido
def checar_ano_fim(ano_fim, ano_inicio):

    if ano_fim >= ano_inicio:
        return True
    
    print(f"O ano do termino da publicação não é válido, por favor insira um ano válido.")   
    return False
# --------------------------------ANO DE FIM----------------------------------#
# pede o ano que o mangá terminou de ser publicado e checa se é válido
def adicionar_ano_fim(status, ano_inicio):
    
    # Se o mangá estiver em Andamento ou em Hiato,
    # ele ainda não terminou de ser publicado
    if status == "Andamento" or status == "Hiato":
        return None
    
    # status == "Completo" or status == "Cancelado"
    flag_ano_fim_valido = False
    while flag_ano_fim_valido == False:
        ano_fim = int(input(("Entre com o ano que o mangá terminou de ser publicado: ")))
        flag_ano_fim_valido = checar_ano_fim(ano_fim, ano_inicio)
        
    return int(ano_fim)


# ----------------------------------------------------------------------------#
# -----------------------------NUMERO DE VOLUMES------------------------------#
# ----------------------------------------------------------------------------#
# checa se o número de volumes é válido
def checar_num_volumes(num_de_volumes):

    if num_de_volumes >= 1:
        return True
    
    print(f"O número de volumes não é válido, por favor insira um valor válido.")   
    return False
# -----------------------------NUMERO DE VOLUMES------------------------------#
# pede o número de volumes do mangá e checa se é esse número é válido
def adicionar_num_volumes():
    
    flag_num_volumes_valido = False
    while flag_num_volumes_valido == False:
        num_de_volumes = int(input(("Entre com a quantidade de volumes que o mangá possui: ")))
        flag_num_volumes_valido = checar_num_volumes(num_de_volumes)
        
    return int(num_de_volumes)


# ----------------------------------------------------------------------------#
# ---------------------------------PUBLICO------------------------------------#
# ----------------------------------------------------------------------------#
# checa se o publico recebido é válido: Shojo ou Josei ou Shonen ou Seinen
def checar_publico(publico):

    if publico == "Shojo" or publico == "Josei" or publico == "Shonen" or publico == "Seinen":
        return True
    
    print(f"Publico incorreto, por favor insira o publico correto.")   
    return False
# ---------------------------------PUBLICO------------------------------------#
# pede o publico do mangá ao usuário e checa se é válido
def adicionar_publico():
    
    flag_publico_valido = False
    while flag_publico_valido == False:
        publico = input(("Entre com o público alvo do mangá que você deseja cadastrar - Shojo ou Josei ou Shonen ou Seinen - : "))
        flag_publico_valido = checar_publico(publico)
        
    return publico


# ----------------------------------------------------------------------------#
# ----------------------------------GENERO------------------------------------#
# ----------------------------------------------------------------------------#
# pede o genero do mangá ao usuário
def adicionar_genero(genero):
    
    flag_adicionar_genero = True
    while flag_adicionar_genero == True:
        gen = input(("Entre com o genero do mangá que você deseja cadastrar: "))
        genero.append(gen)
        
        continua = input(("Você deseja cadastrar um novo genero? s/n: "))
        if continua == "n":
            flag_adicionar_genero = False


# ----------------------------------------------------------------------------#
# ------------------------------VENDAS MENSAIS--------------------------------#
# ----------------------------------------------------------------------------#
# Adiciona as vendas mensais
def adicionar_vendas_mensais(venda_mensal, ano_inicio):
    
    print(f"\nInício do cadastro de vendas mensais do mangá.")

    flag_cadastrar_venda = True
    while flag_cadastrar_venda == True:
        ano_venda = int(input("Entre com o ano: "))
        
        while ano_venda < ano_inicio:
            ano_venda = int(input("Ano inválido. Entre com um ano válido: "))
        
        mes_venda = int(input("Entre com o mês: "))
        
        while mes_venda < 1 or mes_venda > 12:
            mes_venda = int(input("Mês inválido. Entre com um mês válido: "))
        
        quantidade = int(input("Entre com a quantidade de vendas: "))

        while quantidade < 0 :
            quantidade = int(input("Número de vendas mensal inválido. Entre com um valor válido: "))
        
        continua = input(("Você deseja cadastrar outra venda? s/n: "))
        if continua == "n":
            flag_cadastrar_venda = False
            
        venda_mensal.append([ano_venda, mes_venda, quantidade])
        
    venda_mensal.sort()


# ----------------------------------------------------------------------------#
# ------------------------------ADICIONAR MANGÁ-------------------------------#
# ----------------------------------------------------------------------------#
def adicionar_manga(dic_mangas):

    id = adicionar_id(dic_mangas)
    nome = input(("Entre com o nome do novo mangá que você deseja cadastrar: "))
    autor = input(("Entre com o nome do autor do mangá que você deseja cadastrar: "))
    status = adicionar_status()
    ano_inicio = adicionar_ano_inicio()
    ano_fim = adicionar_ano_fim(status, ano_inicio)
    sinopse = input(("Entre com a sinopse do mangá que você deseja cadastrar: "))
    num_de_volumes = adicionar_num_volumes()
    publico = adicionar_publico()
    genero = []
    adicionar_genero(genero)
    impressao = input(("Entre com a gráfica de impressão do mangá: "))
    revista = input(("Entre com a revista de publicação do mangá: "))
    venda_mensal = []
    adicionar_vendas_mensais(venda_mensal, ano_inicio)

    dic_mangas[id] = [nome, autor, status, ano_inicio, ano_fim, sinopse, num_de_volumes, publico, genero, impressao, revista, venda_mensal]
    print(f"Cadastro efetuado com sucesso.")
    
    #atualizar o arquivo

n = 1
dic_mangas = {}
for i in range(n):
    adicionar_manga(dic_mangas)
print(dic_mangas)