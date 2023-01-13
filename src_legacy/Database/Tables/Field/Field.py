# from abc import ABCMeta, abstractmethod


# class Field(metaclass=ABCMeta):
#     @abstractmethod
#     def __init__(self): pass

#     @property
#     @abstractmethod
#     def name(self)->str: pass

#     @property
#     @abstractmethod
#     def data_type(self)->type: pass

#     @property
#     @abstractmethod
#     def insert_query_string(self)->str: pass

#     @property
#     @abstractmethod
#     def delete_query_string(self)->str: pass

#     @property
#     @abstractmethod
#     def update_query_string(self)->str: pass

#     @abstractmethod
#     def insert(self): pass

#     @abstractmethod
#     def delete(self): pass

#     @abstractmethod
#     def update(self): pass

from functools import partialmethod

class Field():
    
    # @staticmethod
    # def get_insert_string(field_name:str, table_name:str, **kargs):
    #     return  f'''
    #             INSERT INTO {table_name}({field_name},begin_date,end_date)
    #                     VALUES(?,?,?)
    #             '''

    def __init__(self,
        name:str,
        data_type: type,
        insert_query_string: str = None,
        delete_query_string: str = None,
        update_query_string: str = None
    ):
        self.name: str =  name
        self.data_type: type = data_type
        self.insert_query_string: str = insert_query_string
        self.delete_query_string: str = delete_query_string
        self.update_query_string: str = update_query_string

    def insert(self):
        NotImplemented

    def delete(self):
        NotImplemented

    def update(self):
        NotImplemented