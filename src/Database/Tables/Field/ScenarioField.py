from Field import Field
class ScenarioField(Field):
    
    def __init__(self,
        insert_query_string: str = None,
        delete_query_string: str = None,
        update_query_string: str = None
    ):
        super().__init__(
            name = "scenario",
            data_type=str,
            insert_query_string= insert_query_string,
            delete_query_string= delete_query_string,
            update_query_string= update_query_string
        )
