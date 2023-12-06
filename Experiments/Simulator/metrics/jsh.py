from scipy.spatial import distance
import warnings
warnings.filterwarnings("error")

def calculate(df1, df2):

  dis1 = {}
  dis2 = {}
  ds = []

  for col in df1.columns:
    try:
      coln = col.lower().replace(" ", "_")
      dis1[coln] = df1[col].value_counts(normalize=True).to_dict()
      dis2[coln] = df2[col].value_counts(normalize=True).reindex(df1[col],fill_value=0.0).to_dict()
      p = list(dict(sorted(dis1[coln].items())).values())
      q = list(dict(sorted(dis2[coln].items())).values())
      ds.append(distance.jensenshannon(p, q))
    except Exception as e:
      print(e)
      ds.append(1.0)

  return sum(ds)/len(ds)