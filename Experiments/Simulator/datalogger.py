from pandas import DataFrame
from sqlalchemy import create_engine, types

import pymysql
import configuration
import uuid

pymysql.install_as_MySQLdb()

my_conn = create_engine("mysql+mysqldb://root:root@localhost:3008/ACL_Extension")  # fill details
my_conn = my_conn.connect()


class DataLogger:
    def __init__(self):
        self.data = []
        self.nodelist = None
        self.service = None
        self.experiment_id = str(uuid.uuid4())

    def log(self, nodelist, node, service, metric):
        self.data.append(
            {
                'experiment_id': self.experiment_id,
                'window_id': str(configuration.WINDOW_ID),
                'node': str(nodelist),
                'service': str(node) + str(service),
                'metric': metric
            }
        )

    def store(self, filename):
        #print(self.data)
        df = (DataFrame(
            self.data,
            columns=['experiment_id',
                     'window_id',
                     'node',
                     'service',
                     'metric'])
              .sort_values(by=["metric"], ascending=True))

        df.to_csv(f"{configuration.OUTPUT_FOLDER}/{filename}",
                  index=True,
                  index_label="id",
                  encoding='utf-8'
                  )

        sql_types = {
            'node': types.VARCHAR(255),
            'service': types.VARCHAR(255),
            'metric': types.Float()
        }

        df.to_sql(filename.replace('.csv', ''),
                  con=my_conn,
                  if_exists='replace',
                  index=True,
                  index_label="id",
                  dtype=sql_types
                  )

        df.to_sql("latest",
                  con=my_conn,
                  if_exists='replace',
                  index=True,
                  index_label="id",
                  dtype=sql_types
                  )
