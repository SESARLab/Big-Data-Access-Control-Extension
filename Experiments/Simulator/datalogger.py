import os

import pymysql
from pandas import DataFrame
from sqlalchemy import create_engine, types

import configuration

pymysql.install_as_MySQLdb()

my_conn = create_engine("mysql+mysqldb://root:root@localhost:3008/ACL_Extension")  # fill details
my_conn = my_conn.connect()


class DataLogger:
    def __init__(self):
        self.data = []
        self.combination = None
        self.nodelist = None
        self.service = None

    def log(self, nodelist, node, service, metric):
        self.data.append(
            {
                'window_id': str(configuration.WINDOW_ID),
                'node': str(nodelist),
                'service': str(node) + str(service),
                'metric': metric
            }
        )

    def logAddCombination(self, combination, metric, percentage,
                        number_of_nodes=configuration.NUMBER_OF_NODES,
                        experiment_id=configuration.EXPERIMENT_ID,
                        window_size=configuration.WINDOW_SIZE,
                        number_of_services=configuration.NUMBER_OF_SERVICES
                          ):
        if self.combination is None:
            self.combination = {
                'number_of_nodes': number_of_nodes,
                'experiment_id': experiment_id,
                'window_size': window_size,
                'number_of_services': number_of_services,
                'combination': combination,
                'metric': metric,
                'metric_count': 1,
                'percentage': percentage,
                'execution_time': ""
            }
        else:
            self.combination['combination'] += combination
            self.combination['metric'] += metric
            self.combination['metric_count'] += 1
            self.combination['percentage'] *= percentage

    def logAddExecutionTime(self, execution_time):
        self.combination['metric'] = self.combination['metric'] / self.combination['metric_count']
        # self.combination['percentage'] = self.combination['percentage'] / self.combination['metric_count']
        self.combination['execution_time'] = execution_time
        DataFrame(self.combination, index=[0]).to_sql("combinations",
                                                    con=my_conn,
                                                    if_exists='append',
                                                    index_label="id")
        self.combination = None

    def store(self, filename):
        df = (DataFrame(
            self.data,
            columns=['experiment_id',
                    'window_id',
                    'node',
                    'service',
                    'metric'])
              .sort_values(by=["metric"], ascending=True))

        os.makedirs(configuration.OUTPUT_FOLDER, exist_ok=True)

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


if __name__ == '__main__':
    data_logger = DataLogger()
    data_logger.logAddCombination(1, 1, 1, 1, "a", 1, 1)
    data_logger.logAddCombination(1, 1, 1, 1, "b", 0, 0)
    data_logger.logAddCombination(1, 1, 1, 1, "c", 0.5, 0.5)
    data_logger.logAddExecutionTime(0.5)
