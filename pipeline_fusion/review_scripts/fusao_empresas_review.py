import csv
import json

path_json = './data_raw/dados_empresaA.json'
path_csv = './data_raw/dados_empresaB.csv'


#! Extract
def ler_json(dado):
    with open(dado, 'r') as file:
        dados_json = json.load(file)
    return dados_json

def ler_csv(dado):
    dados_csv = []
    with open(dado, 'r') as file:
        spamreader = csv.DictReader(file, delimiter=',')
        for dados in spamreader:
            dados_csv.append(dados)
    return dados_csv


'''def ler_dados(dado, tipo):
    todos_dados = []
    if tipo == 'csv':
        todos_dados = ler_csv(dado)
    elif tipo == 'json':
        todos_dados = ler_json(dado)
    
    return todos_dados'''


def tamanho_dados(dado):
    return len(dado)

def calcular_largura_total(dadoA, dadoB):
    soma = len(dadoA) + len(dadoB)
    return soma

def renomear_coluna(dado, chave_nova):
    coluna_nova = []
    
    for dados in dado:
        dict_temp = {}
        for coluna_original, dado_original in dados.items():
            dict_temp[chave_nova[coluna_original]] = dado_original
        coluna_nova.append(dict_temp)
    return coluna_nova



def get_colunas_novas(dado):
    colunas = dado[0].keys()
    return colunas

def juntar_dados(dadoA, dadoB):
    juncao_dados = []
    juncao_dados.extend(dadoA)
    juncao_dados.extend(dadoB)
    return juncao_dados

def gerando_tabela(todos_dados, nomes_colunas):
    dados_gerados = [nomes_colunas]
    for dados in todos_dados:
        linha = []
        for coluna in nomes_colunas:
            linha.append(dados.get(coluna, 'Indisponivel'))
        dados_gerados.append(linha)
    return dados_gerados



#empresaA_json = ler_dados(path_json, 'json')
empresaA_json = ler_json(path_json)
empresaB_csv = ler_csv(path_csv)

tamanho_dado_json = tamanho_dados(empresaA_json)
tamanho_dado_csv = tamanho_dados(empresaB_csv)

soma_largura_dados = calcular_largura_total(empresaA_json, empresaB_csv)



#! Transform
key_mapping = {
    'Nome do Item':'Nome do Produto',
    'Classificação do Produto':'Categoria do Produto',
    'Valor em Reais (R$)':'Preço do Produto (R$)',
    'Quantidade em Estoque':'Quantidade em Estoque',
    'Nome da Loja':'Filial',
    'Data da Venda':'Data da Venda'
}




empresaB_csv_colunas_renomeadas = renomear_coluna(empresaB_csv, key_mapping)


join_dados = juntar_dados(empresaB_csv_colunas_renomeadas, empresaA_json)
coluna_selecionada = get_colunas_novas(join_dados)
tamanho_dado_join = tamanho_dados(join_dados)





#! Load
tabela_dos_dados = gerando_tabela(join_dados, coluna_selecionada)
print(tabela_dos_dados[1])


'''caminho_salvar = './data_processed/dados_pipeline.csv'

def salvando_dados(dados, path):
    with open(path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(dados)

dados_salvos = salvando_dados(tabela_dos_dados, caminho_salvar)
print(tabela_dos_dados[2])
'''