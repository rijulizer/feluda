import pandas as pd
import numpy as np
import pyspark.sql.functions as sf


def des(sdf_in,v_allowed_category):
    """
    Input: Input saprk dataframe, allowed number of categories less than which will be considered as categorical columns
    Output: Sparkdf with column level analysis
    """

    sdf_in.persist()
    # Count total number of rows
    n_rows = sdf_in.count()

    columns = []
    unique_values = []
    fraction_nulls = []
    unique_value_fracs = []
    # Iterate through Columns
    for c in sdf_in.columns:
        print(c)
        sdf_in_c = sdf_in.select(c)
        columns.append(c)
        un_v = sdf_in_c.distinct().count()
        unique_values.append(un_v)
        fraction_nulls.append(sdf_in_c.filter(sf.col(c).isNull().count()/n_rows))
        if un_v <= v_allowed_category:
            list_num_uv = sdf_in_c.groupBy(c).count().select('count')\
                                .rdd.flatMap(lambda x:x).colect()
            list_num_uv = list(np.round(np.array(list_num_uv)/sum(list_num_uv),3))
            unique_value_fracs.append(list_num_uv)
        else:
            unique_value_fracs.append([100])

    df = pd.DataFrame(list(zip(columns,fraction_nulls, unique_values, unique_value_fracs)),
                    columns=['columns','fraction_nulls', 'unique_values', 'unique_value_fracs'])

    #sdf = spark.createDataFrame(df)
    sdf_in.unpersist()

    return (df)

