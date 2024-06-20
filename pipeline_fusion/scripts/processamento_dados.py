import json
import csv

class Dados():
    def __init__(self, path, tipo_dados):
        self.path = path
        self.tipo_dados = tipo_dados
        self.dados = self.ler_todos_dados()
        self.nome_colunas = self.get_columns()
        self.tamanho_dados = self.size_dados()
    
    def ler_json(self):
        with open(self.path, 'r') as file:
            base_json = json.load(file)
        return base_json


    def ler_csv(self):
        dados_csv = []
        with open(self.path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for dicionario_csv in spamreader:
                dados_csv.append(dicionario_csv)
        return dados_csv


    def ler_todos_dados(self):
        dados = []
        if self.tipo_dados == 'csv':
            dados = self.ler_csv()

        elif self.tipo_dados == 'json':
            dados = self.ler_json()
        
        elif self.tipo_dados == 'list':
            dados = self.path
            self.path = 'Lista em memória'

        return dados
    
    def get_columns(self):
        return list(self.dados[-1].keys())
    

    def renomeando_colunas(self, keymapping):
        novos_dados = []
        for dict_antigo in self.dados:
            dict_vazio = {}
            for coluna_antiga, valor_original in dict_antigo.items():
                dict_vazio[keymapping[coluna_antiga]] = valor_original
            novos_dados.append(dict_vazio)

        self.dados = novos_dados
        self.nome_colunas = self.get_columns()

    def size_dados(self):
        return len(self.dados)
    
    def juntando_os_dados(dadoA, dadoB):
        todos_dados = []
        todos_dados.extend(dadoA.dados)
        todos_dados.extend(dadoB.dados)

        return Dados(todos_dados, 'list')

    def gerando_tabela(self):
        dados_gerados = [self.nome_colunas]
        for dados in self.dados:
            linha = []
            for coluna in self.nome_colunas:
                linha.append(dados.get(coluna, 'Indisponivel'))
            dados_gerados.append(linha)
        return dados_gerados
    
    def salvar_dados(self, path):

        dados_gerados = self.gerando_tabela()
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(dados_gerados)