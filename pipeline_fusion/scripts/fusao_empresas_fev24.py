
from processamento_dados import Dados

caminho_dados_json = 'data_raw/dados_empresaA.json'
caminho_dados_csv = 'data_raw/dados_empresaB.csv'
salvar_dados_processados = 'data_processed/dados_processados.csv'

#! EXTRACT
dadosEmpresaA = Dados(caminho_dados_json, 'json')
#print('Dados da empresa A:', dadosEmpresaA.dados)
print('Colunas da empresa A:', dadosEmpresaA.nome_colunas)
print('Tamanho dos dados da empresa A:', dadosEmpresaA.tamanho_dados)

dadosEmpresaB = Dados(caminho_dados_csv, 'csv')
#print('Dados da empresa B:', dadosEmpresaB.dados)
print('Colunas da empresa B:', dadosEmpresaB.nome_colunas)
print('Tamanho dos dados da empresa B:', dadosEmpresaB.tamanho_dados)


#! TREAT
keymapping = {
    'Nome do Item':'Nome do Produto',
    'Classificação do Produto':'Categoria do Produto',
    'Valor em Reais (R$)':'Preço do Produto (R$)',
    'Quantidade em Estoque':'Quantidade em Estoque',
    'Nome da Loja':'Filial',
    'Data da Venda':'Data da Venda'
}

dadosEmpresaB.renomeando_colunas(keymapping)
#print('new', dadosEmpresaB.nome_colunas)

fusao_dados = Dados.juntando_os_dados(dadosEmpresaA, dadosEmpresaB)
#print('Fusao dos dados', fusao_dados)
print('Fusao dos dados', fusao_dados.dados)
print('Colunas Fusao dos dados:', fusao_dados.nome_colunas)
print('Tamanho Fusao dos dados:', fusao_dados.tamanho_dados)


#! LOAD
dados_salvos = fusao_dados.salvar_dados(salvar_dados_processados)
print(dados_salvos)






