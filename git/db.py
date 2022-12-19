from sqlalchemy import connectors

class DatabaseConnection:
    def __init__(self, database_credentials): 
        self.database_credentials = database_credentials

    def do_work(self, do_work_bool = False):
        return do_work_bool