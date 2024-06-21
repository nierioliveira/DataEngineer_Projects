import csv
import json


class Dados():
    def __init__(self, path, type):
        self.__path = path
        self.__type = type
        self.data = self.__read_all_data()
        self.columns = self.__get_columns()
        self.size = self.__size_data()


    def __read_json(self):
        with open(self.__path, 'r') as file:
            json_data = json.load(file)
        return json_data
    
    def __read_csv(self):
        list = []
        with open(self.__path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')

            for csv_data in spamreader:
                list.append(csv_data)
        return list
    
    def __read_all_data(self):
        data = []

        if self.__type == 'json':
            data = self.__read_json()
        
        elif self.__type == 'csv':
            data = self.__read_csv()
            
        elif self.__type == 'list':
            data = self.__path
            self.__path = 'Internal List passed'

        return data
    
    def __get_columns(self):
        return list(self.data[-1].keys())
    
    def __size_data(self):
        return len(self.data)
    
    def rename_columns(self, keymapping):
        new_data = []
        for all_data in self.data:
            dict = {}
            for old_key, old_value in all_data.items():
                dict[keymapping[old_key]] = old_value
            new_data.append(dict)
        
        self.data = new_data
        self.columns = self.__get_columns()

    def data_fusion(dataA, dataB):
        all_new_data = []
        all_new_data.extend(dataA.data)
        all_new_data.extend(dataB.data)

        return Dados(all_new_data, 'list')

    
 
    def __data_table(self):
        original_columns = [self.columns]
        for all_data in self.data:
            row = []
            for all_columns in self.columns:
                row.append(all_data.get(all_columns, 'Coluna Indisponivel'))
            original_columns.append(row)

        return original_columns
    
    def save_data(self, path):
        data_toBe_saved = self.__data_table()

        try:
            with open(path, 'w') as file:
                writer = csv.writer(file)
                writer.writerows(data_toBe_saved)
                print('All data saved with success')
        except:
            print('Error trying to save the data')