import numpy as np
import database_gestion as database 
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.colors import ListedColormap
from sklearn import neighbors

#%load_ext autoreload
#%autoreload 2
#%matplotlib qt

#%% Read the database a first time and get all the locations

# this variable must be set to have access to the database
conn = database.create_connection("roots.db")
objects = database.get_all_objects(conn)

# the locations are the label of the classification, for each object of course 

#%% I. Plot 1
dfs_long = []
for o in objects:
    print("Object: ", o)
    # array containing the data for this object
    df = pd.DataFrame()
    # get the locations associated with this object
    ids = database.get_locations_id_for_object(conn, o[0])
    # for each location, get the measuremenets done there
    for loc in ids:
        measurements = database.get_measurements_for_location(conn, loc[0])
        measurements = np.array(measurements).reshape(11,-1)
        df_loc = pd.DataFrame(data=measurements)
        df = df.append(df_loc, ignore_index = True)
    dfs_long.append(df)

df = dfs_long[0]
df.T.plot(legend = False, title="Measurements done over 1 object", xlim=(0, 100), ylim = (0, 3))
# observing this plot, it feels like we can use 2 features that matters: min_x and min_y of the first minimum.

#%% II. Create classifier (and dataset for plotting)
# and train knn classifier for each model
# HYPOTHESIS 1 (to check with Leo): the first minimum is always clear in the first 50 points

n_neighbors = 4
weights = "uniform"

dfs, clfs = [], []
for o in objects:
    print("Object: ", o)
    # array containing the data for this object
    df = pd.DataFrame()
    # get the locations associated with this object
    ids = database.get_locations_id_for_object(conn, o[0])
    # for each location, get the measuremenets done there
    for loc in ids:
        measurements = database.get_measurements_for_location(conn, loc[0])
        measurements = np.array(measurements).reshape(11,-1)
        df_loc = pd.DataFrame(data=np.zeros(shape = (len(measurements),2)), columns=["loc", "vals"])
        # add to the frame the features we care about 
        df_loc["loc"] = loc[0]
        df_loc["vals"] = measurements.tolist()
        # getting the min and the argmin over the first 50 elements
        df_loc["amin"] = df_loc.vals.apply(lambda x: np.array(x)[:50].argmin())
        df_loc["min"] = df_loc.vals.apply(lambda x: np.array(x)[:50].min())
        df = df.append(df_loc, ignore_index = True)
    # normalize some features here
    df["min"] = (df["min"] - df["min"].mean()) / df["min"].std()
    df["amin"] = (df["amin"] - df["amin"].mean()) / df["amin"].std()
    # training daa
    X = df[["amin", "min"]].values
    y = df["loc"].values
    # make the classification
    if np.count_nonzero(df["amin"].isna()):
        clfs.append((o[0], None))
    else:
        clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)    
        clf.fit(X, y)
        clfs.append(clf)
    # save this for next plots
    dfs.append(df)

df = dfs[2]

#%% III. Plot 2
plt.plot(df.head(1).vals.values[0])

#%% IV. Plot 3
sns.catplot(data=df, x = "amin", y = "min", hue = "loc") 

#%% KNN Plot
h = 0.02
cmap_light = ListedColormap(['orange', 'cyan', 'cornflowerblue', 'yellow'])
cmap_bold = ['darkorange', 'c', 'darkblue', 'yellow']

def knn_plot(df, clf, ax):
    """Make a nice plot for KNN classification

    Parameters
    df: dataframe containing 'min' and 'amin' for drawing points  
    clf: classifier already trained
    """
    X = df[["amin", "min"]].values
    y = df["loc"].values

    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    ax.contourf(xx, yy, Z, cmap=cmap_light)

    # Plot also the training points
    sns.scatterplot(data=df, x = "amin", y="min", hue="loc",
                    palette=cmap_bold, alpha=1.0, edgecolor="black", ax=ax)
    ax.set_xlim(xx.min(), xx.max())
    ax.set_ylim(yy.min(), yy.max())
    ax.set_title("Classification Results (k = %i, weights = '%s', accuracy = %.2f')"
              % (n_neighbors, weights, clf.score(X,y)))
    ax.set_xlabel("argmin normalized")
    ax.set_ylabel("min noralized")

plt.figure()
ax = plt.gca()
knn_plot(dfs[2],clf,ax)

#%% Plot for the report

indices = [0, 2] 
fig, axs = plt.subplots(len(indices), 2)

for i, idx in enumerate(indices):
    df = dfs_long[idx]
    # 1. make the plot with the grahpsi
    df.T.plot(legend = False, title="Measurements done over 1 object", xlim=(0, 50), ylim = (0, 3), ax=axs[i,0])

    # 2. knn plot
    knn_plot(dfs[idx], clfs[idx], axs[i,1])

plt.show()

