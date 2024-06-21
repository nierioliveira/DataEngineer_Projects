
from data_processing import Dados

path_json = './data_raw/dados_empresaA.json'
path_csv = './data_raw/dados_empresaB.csv'
path_to_save = './data_processed/data_processed.csv'


#? Extract
empresaA = Dados(path_json, 'json')

empresaB = Dados(path_csv, 'csv')


#? Treat
keymapping = {
    'Nome do Item': 'Nome do Produto',
    'Classificação do Produto': 'Categoria do Produto',
    'Valor em Reais (R$)': 'Preço do Produto (R$)',
    'Quantidade em Estoque': 'Quantidade em Estoque',
    'Nome da Loja': 'Filial',
    'Data da Venda': 'Data da Venda',
}
empresaB.rename_columns(keymapping)

data_fusioned = Dados.data_fusion(empresaA, empresaB)


#? Load
data_fusioned.save_data(path_to_save)





