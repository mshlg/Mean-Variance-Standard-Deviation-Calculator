import numpy as np

def calculate(list):
    #import numpy
    import numpy as np
    if len(list) < 9:
      raise ValueError("List must contain nine numbers.")
  
    else: 
        my_array = np.asarray(list).reshape(3,3)
        #calculate means
        mean0 = np.mean(my_array, axis=0).tolist()
        mean1 = np.mean(my_array, axis=1).tolist()
        mean_ = np.mean(my_array).tolist()
        #calculate variance
        var0 = np.var(my_array, axis=0).tolist()
        var1 = np.var(my_array, axis=1).tolist()
        var_ = np.var(my_array).tolist()
        #calculate stdev
        std0 = np.std(my_array, axis=0).tolist()
        std1 = np.std(my_array, axis=1).tolist()
        std_ = np.std(my_array).tolist()
        #calculate max
        max0 = np.max(my_array, axis=0).tolist()
        max1 = np.max(my_array, axis=1).tolist()
        max_ = np.max(my_array).tolist()
        #calculate min
        min0 = np.min(my_array, axis=0).tolist()
        min1 = np.min(my_array, axis=1).tolist()
        min_ = np.min(my_array).tolist()
        #calculate sum
        sum0 = np.sum(my_array, axis=0).tolist()
        sum1 = np.sum(my_array, axis=1).tolist()
        sum_ = np.sum(my_array).tolist()
        
        #create dictionary
        calculations = {'mean':[mean0,mean1,mean_],
                        'variance':[var0,var1,var_],
                        'standard deviation':[std0,std1,std_],
                        'max':[max0,max1,max_],
                        'min':[min0,min1,min_],
                        'sum':[sum0,sum1,sum_]
               }
        return calculations