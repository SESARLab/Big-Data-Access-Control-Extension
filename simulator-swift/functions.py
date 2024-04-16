from scipy.spatial import distance
import numpy as np

from pandas import DataFrame
from sqlalchemy import create_engine, types
my_conn = create_engine("mysql+mysqldb://root:r00t@mysql:3306/pippo")  # fill details
my_conn = my_conn.connect()
def mydistance(df1, df2):
    ds = []

    for col in df1.columns:
        try:
            p = df1[col].value_counts(normalize=True).sort_index()
            q = df2[col].value_counts(normalize=True).reindex(p.index, fill_value=0.0).sort_index()
            if np.sum(np.asarray(q), axis=0, keepdims=True) != 0:
                ds.append(distance.jensenshannon(p, q))
            else:
                ds.append(1.0)
        except Exception as e:
            print(e)
            ds.append(1.0)

    return sum(ds) / len(ds)


def store(item):

    DataFrame(item, index=[0]).to_sql('n7_s7_70_100', my_conn, if_exists='append', index=False)
