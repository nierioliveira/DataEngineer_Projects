import json
import csv

class Dados():
    def __init__(self, path, tipo_dados):
        self.__path = path
        self.__tipo_dados = tipo_dados
        self.dados = self.__ler_todos_dados()
        self.nome_colunas = self.__get_columns()
        self.tamanho_dados = self.__size_dados()
    
    def __ler_json(self):
        with open(self.__path, 'r') as file:
            base_json = json.load(file)
        return base_json


    def __ler_csv(self):
        dados_csv = []
        with open(self.__path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for dicionario_csv in spamreader:
                dados_csv.append(dicionario_csv)
        return dados_csv


    def __ler_todos_dados(self):
        dados = []
        if self.__tipo_dados == 'csv':
            dados = self.__ler_csv()

        elif self.__tipo_dados == 'json':
            dados = self.__ler_json()
        
        elif self.__tipo_dados == 'list':
            dados = self.__path
            self.__path = 'Lista em memória'

        return dados
    
    def __get_columns(self):
        return list(self.dados[-1].keys())
    

    def renomeando_colunas(self, keymapping):
        novos_dados = []
        for dict_antigo in self.dados:
            dict_vazio = {}
            for coluna_antiga, valor_original in dict_antigo.items():
                dict_vazio[keymapping[coluna_antiga]] = valor_original
            novos_dados.append(dict_vazio)

        self.dados = novos_dados
        self.nome_colunas = self.__get_columns()

    def __size_dados(self):
        return len(self.dados)
    
    def juntando_os_dados(dadoA, dadoB):
        todos_dados = []
        todos_dados.extend(dadoA.dados)
        todos_dados.extend(dadoB.dados)

        return Dados(todos_dados, 'list')

    def __gerando_tabela(self):
        dados_gerados = [self.nome_colunas]
        for dados in self.dados:
            linha = []
            for coluna in self.nome_colunas:
                linha.append(dados.get(coluna, 'Indisponivel'))
            dados_gerados.append(linha)
        return dados_gerados
    
    def salvar_dados(self, path):

        dados_gerados = self.__gerando_tabela()
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(dados_gerados)