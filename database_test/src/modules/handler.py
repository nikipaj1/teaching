import pandas as pd
import sqlite3

class Handler:
        
    def __init__(self, database_name: str):
        self.database_name = database_name

    def gen_task_1(self, table_name: str) -> None:
        conn = sqlite3.connect(self.database_name)
        tele = pd.read_csv('https://raw.githubusercontent.com/nikipaj1/teaching/main/Analytics/telecom_churn.csv')
        tele.to_csv("../data/telecom.csv")
        tele.to_sql(table_name, conn)