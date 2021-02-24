import classifier
import database_gestion as database 

# create connection
conn = database.create_connection("roots.db")

# get the classifiers for this training set 
classifiers = classifier.get_classifiers(conn)

# select one classifier (depending on the object)
object_id, classifier = classifiers[2]

# try to predict something given a new measurement
measurements = [1.0, 1.0, 1.0, 1.0, 0.99, 0.98, 0.98, 0.98, 0.97, 0.95, 0.93, 0.9, 0.86, 0.81, 0.76, 0.71, 0.67, 0.65, 0.65, 0.67, 0.71, 0.75, 0.79, 0.83, 0.86, 0.89, 0.92, 0.93, 0.95, 0.97, 0.98, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.99, 0.98, 0.97, 0.97, 0.96, 0.95, 0.94, 0.93, 0.92, 0.91, 0.9, 0.89, 0.88, 0.86, 0.85, 0.83, 0.82, 0.8, 0.79, 0.78, 0.77, 0.75, 0.74, 0.73, 0.72, 0.71, 0.71, 0.7, 0.69, 0.68, 0.67, 0.66, 0.66, 0.65, 0.64, 0.63, 0.62, 0.61, 0.6, 0.59, 0.59, 0.58, 0.58, 0.58, 0.57, 0.57, 0.56, 0.56, 0.56, 0.56, 0.55, 0.55]

# and make the prediction
if classifier is not None: 
    predicted_location_id = classifier(measurements)
    print("Predicted location : ", predicted_location_id)
