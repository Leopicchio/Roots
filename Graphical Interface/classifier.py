import numpy as np
import database_gestion as database 
import pandas as pd
from sklearn import neighbors

def get_classifiers(conn, n_neighbors = 4, weights = "uniform"):
    """Given a connection to database, for each object of the database it will create
    a classifier (KNN) and return a function to be called, which itself call the '.predict' 
    method of the classifier with the appropriated parameters. 

    Read the example to understand better how to use this function.

    Returns
    ------
    tuples (id, classifier): id of the object and the classification function to call in order to make a prediction

    """
    # 1. get all objects in the database
    objects = database.get_all_objects(conn)
    predictors = []
    for o in objects:
        df = pd.DataFrame()
        # get the locations associated with this object
        ids = database.get_locations_id_for_object(conn, o[0])
        # 2. for each location, get the measuremenets done there
        # and add them 'processed' to the training dataset
        for loc in ids:

            measurements = database.get_measurements_for_location(conn, loc[0])
            n_measurements = len(measurements)

            print("DEBUG: creating classifier for object {0}, processing {1} measurements of location: {2}".format(o, n_measurements, loc[0]))

            measurements = np.array(measurements).reshape(n_measurements,-1)

            df_loc = pd.DataFrame(data=np.zeros(shape = (len(measurements),2)), columns=["loc", "vals"])
            # add to the frame the features we care about 
            df_loc["loc"] = loc[0]
            df_loc["vals"] = measurements.tolist()
            # getting the min and the argmin over the first 50 elements
            df_loc["amin"] = df_loc.vals.apply(lambda x: np.array(x)[:50].argmin())
            df_loc["min"] = df_loc.vals.apply(lambda x: np.array(x)[:50].min())
            df = df.append(df_loc, ignore_index = True)


        # 3. normalize some features here
        min_mean = df["min"].mean() 
        min_std = df["min"].std()
        amin_mean = df["amin"].mean() 
        amin_std = df["amin"].std()
        df["min"] = (df["min"] - min_mean) / min_std 
        df["amin"] = (df["amin"] - amin_mean) / amin_std 
        X = df[["amin", "min"]].values
        y = df["loc"].values

        if np.count_nonzero(df["amin"].isna()):
            # --> object not valid
            predictors.append((o[0], None))
            continue 

        # --> object is valid
        # 4. make the classification AND the classifier
        # a. construct the classifier
        clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)    
        clf.fit(X, y)


        # b. make a function to call the classifier and add it to array of function to returns
        def predictor_function(x, obj_id = o[0], 
                min_mean = min_mean, min_std = min_std,
                amin_mean = amin_mean, amin_std = amin_std,
                clf = clf):
            """Given a list x, it will compute the predictors and run the prediction
            on the apprioated classifier for this object."""
            #print("Going to make prediction for object ", obj_id)
            x = np.array(x)
            m = (x[0:50].min() - min_mean) / min_std
            am = (x[0:50].argmin() - amin_mean ) / amin_std
            return clf.predict(np.array([[am, m]]))


        # add the created function to returned array
        predictors.append((o[0], predictor_function))
    return predictors
