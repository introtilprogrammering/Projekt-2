def dataFrame(data_a,tvec_a):
    import numpy as np
    import pandas as pd
    data_a = [x for x in data_a if x is not None] 
    tvec_a = [x for x in tvec_a if x is not None] 
    data_a = np.array(data_a)
    tvec_a = np.array(tvec_a)
    tvec_a = pd.DataFrame(tvec_a, columns = ['year','month','day','hour','minut','seconds'])
    data_a = pd.DataFrame(data_a, columns = ['zone1','zone2','zone3','zone4'])
    return (data_a,tvec_a)