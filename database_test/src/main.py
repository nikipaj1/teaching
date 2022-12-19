from modules.handler import Handler

if __name__ == "__main__":
    h = Handler("task1.db")
    h.gen_task_1(table_name="telecom")
    