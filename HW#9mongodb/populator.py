from pymongo import MongoClient
import csv


conn = MongoClient(host='localhost', port=27017)

if 'Test' in conn.list_database_names():
    conn.drop_database('Test')
database = conn['Test']

collection_p = database['Projects']
collection_t = database['Tasks']

col_types_p = [str, str, str]
col_types_t = [int, str, str, str, str, str]


def insert_from_csv(f_name, formats, collection_obj):
    with open(f'{f_name}', 'r') as f:
        csv_data = csv.reader(f, delimiter='|')
        headers = tuple(next(csv_data))
        for id_, row in enumerate(csv_data, start=1):
            row_typed = tuple(convert(value) for convert, value in zip(formats, row))
            dict_ = {"_id": id_}
            for head, body in zip(headers, row_typed):
                dict_[head] = body
            collection_obj.insert_one(dict_)
            dict_.clear()
        return id_


rows_inserted_p = insert_from_csv('Projects.csv', col_types_p, collection_p)
rows_inserted_t = insert_from_csv('Tasks.csv', col_types_t, collection_t)

canceled_projects = set(x['Project'] for x in collection_t.find({"Status": "Canceled"}))
print('Projects with canceled tasks:', *canceled_projects, sep='\n')

conn.close()

# print(f"\n{rows_inserted_p} documents were inserted into Projects collection\n"
#      f"{rows_inserted_t} documents were inserted into Tasks collection")


