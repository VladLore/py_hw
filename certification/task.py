import pandas as pd
import numpy as np
import random

lst = ["robot"] * 10
lst += ["human"] * 10
random.shuffle(lst)
data = pd.DataFrame({"whoAmI": lst})
data.head()
unique_values = np.unique(data["whoAmI"].values)
one_hot_df = (
    data["whoAmI"]
    .apply(
        lambda x: {
            unique_values[i]: data.loc[
                data["whoAmI"] == unique_values[i], "whoAmI"
            ].count()
            for i in range(len(unique_values))
        }
        if x in unique_values
        else {}
    )
    .to_dict()
)
one_hot = pd.Series(one_hot_df).to_frame()
