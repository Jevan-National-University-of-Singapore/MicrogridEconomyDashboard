from abc import ABC, abstractmethod
from ..Database import Database

class Table(ABC):
    def __init__(self, database:Database):
        self._database = database
        self.init = self._database.create_table(query_string=self.create_string)
    
    @property
    @abstractmethod
    def name(self)->str: pass

    @property
    @abstractmethod
    def create_string(self)->str: pass

    @property
    @abstractmethod
    def fields(self)->set: pass    

    # records
    @abstractmethod
    def insert(self): pass

    def query(self, scenario: str):
        cursor = self._database.query(
            query_string = f'''
                SELECT * FROM {self.name}
                WHERE scenario={scenario}
            '''
        )
        return cursor.fetchall()
        

    # @abstractmethod #not implemented
    # def delete(self): pass

    def update_records(self, scenario: str, **kwargs): 
        set_string = ""
        query_arguments = []

        i = 0
        for key, value in kwargs.items():
            assert key in self.fields
            set_string += f"SET {key} = ? " #if i == len(kwargs) else f"SET {key} = ?\n"
            query_arguments.append(value)

        self._database.query(
            query_string = f''' UPDATE {self.name}
                                {set_string} WHERE scenario = {scenario}
                            ''',
            query_arguments = query_arguments
        )

    def update_record(self, scenario: str, field_name: str, field_value):
        assert field_name in self.fields
        self._database.query(
            query_string = f''' UPDATE {self.name}
                                SET {field_name} = ?
                                WHERE scenario = {scenario}
                            ''',
            query_arguments = (field_value,)
        )

    def insert_record(self, scenario: str, field_name: str, field_value):
        assert field_name in self.fields

        self._database.query(
            query_string = f'''
                                INSERT INTO {self.name}(scenario, {field_name})
                                VALUES ({scenario}, ?)
                            ''',
            query_arguments=(field_value,)
        )

    def insert_records(self, scenario: str, **kwargs):
        insert_string = "scenario" 
        query_arguments = [scenario]

        for key, value in kwargs.items():
            assert key in self.fields
            insert_string += f", {key}"
            query_arguments.append(value)

        self._database.query(
            query_string = f'''
                INSERT INTO {self.name}({insert_string})
                VALUES({"?" * len(kwargs)+1})
            ''',
            query_arguments=query_arguments
        )


        


