import sqlite3
from sqlite3 import Error
from time import gmtime, strftime




def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn




# first, let's define 4 functions to interact with the database

def create_obj(conn, new_object):
    """
    Create a new object into the allObjects table.

    Parametesr
    new_object (tuple): a tuple containing (name, )

    Returns
    obj_id (int): idea of the new created object in the database
    """
    sql = ''' INSERT INTO allObjects(name)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, new_object)
    conn.commit()
    return cur.lastrowid



def create_location(conn, location):
    sql = ''' INSERT INTO locations(name, object_id, trained)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    name, object_id = location
    cur.execute(sql, (name, object_id, "FALSE"))
    conn.commit()
    return cur.lastrowid


def create_measurement(conn, measurement):
    sql = ''' INSERT INTO measurements(location_id, date)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, measurement)
    conn.commit()
    return cur.lastrowid

def create_datapoint(conn, datapoint):
    sql = ''' INSERT INTO datapoints(value, measurement_id)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, datapoint)
    conn.commit()
    return cur.lastrowid


### API functions

# let's add a function function takes a serie of datapoints and create a measurements

def save_points(conn, points, location_id):
    """Given an array of points, it will generate the SQL records to save it.

    Parameters
    conn: connection to the database
    points ([float]): array of points to be saved 
    location_id (int): id of the location to which add those points

    Returns 
    the id of the measurement created
    """
    time_str = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
    m_id = create_measurement(conn, (location_id, time_str))
    for p in points:
        create_datapoint(conn, (p, m_id))

    set_location_trained(conn, location_id, "TRUE")


def set_location_trained(conn, location_id, value):

    sql = 'UPDATE locations SET trained = ? WHERE id = ?'
    cur = conn.cursor()

    if value == "TRUE":
        cur.execute(sql, ("TRUE", location_id,))
    elif value == "FALSE":
        cur.execute(sql, ("TRUE", location_id,))
    else:
        return
    conn.commit()


def create_object(conn, name):
    """
    Creates an Object by the UI. 
    It will creates 4 locations associated to this object and return all the created IDs
    """
    # 1. create object
    obj = (name, )
    obj_id = create_obj(conn, obj)

    # 2. create 4 locations
    names = ["Untouched", "Point 1", "Point 2" , "Point 3"]
    loc_ids = []
    for n in names: 
        loc = (n, obj_id)
        loc_id = create_location(conn, loc)
        loc_ids.append(loc_id)


    # 3. return the created IDs
    return obj_id, loc_ids

def rename_object(conn, obj_id, new_name):
    """Change the name of a given object"""
    sql = 'UPDATE allObjects SET name = ? WHERE id = ?'
    cur = conn.cursor()
    cur.execute(sql, (new_name, obj_id,))
    conn.commit()

def delete_object(conn, obj_id):
    """Delete the given object"""
    sql = 'DELETE FROM allObjects WHERE id=?'
    conn.execute("PRAGMA foreign_keys = ON")
    cur = conn.cursor()
    cur.execute(sql, (obj_id,))
    conn.commit()

def reset_db(conn):
    """Will delete everything within the database"""
    all_objs = get_all_objects(conn)
    for obj in all_objs:
        delete_object(conn, obj[0])

def get_measurements_for_location(conn, location_id):
    """
    Returns all measurements for a given location_id.  

    Note: a measurement is an array of datapoints
    """
    cur = conn.cursor()
    cur.execute("SELECT id FROM measurements where location_id == ?", (location_id,))
    # this gives the ids of the measurements taken at this place
    ids = cur.fetchall()
    points = []
    for i in ids:
        cur.execute("SELECT value FROM datapoints where measurement_id == ?", (i[0],))
        values = cur.fetchall()
        points.append(values)
    return points

def get_all_objects(conn):
    """Returns all saved objects as tuples (id, name)
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM allObjects")
    # this gives the ids of the measurements taken at this place
    results = cur.fetchall()
    return results

def get_locations_id_for_object(conn, obj_id):
    """Given an object_id, it returns the id of all of the locations associated to it"""
    cur = conn.cursor()
    cur.execute("SELECT id FROM locations WHERE object_id == ?;", (obj_id,))
    # this gives the ids of the measurements taken at this place
    results = cur.fetchall()

    return results



def delete_measurements_from_location(conn, location_id):
    """Delete the given object"""
    sql = 'DELETE FROM measurements WHERE location_id=?'
    conn.execute("PRAGMA foreign_keys = ON")
    cur = conn.cursor()
    cur.execute(sql, (location_id,))
    conn.commit()

    sql = 'UPDATE locations SET trained = ? WHERE id = ?'
    cur = conn.cursor()
    cur.execute(sql, ("FALSE", location_id,))
    conn.commit()



def is_location_trained(connection, location_id):
    cursor = connection.cursor()
    cursor.execute("SELECT trained FROM locations WHERE id == ?;", (location_id,))
    # this gives the ids of the measurements taken at this place
    result = cursor.fetchall()

    return (result[0])[0]



# function written by Leo to initialize a database
def create_tables(connection):
    c = connection.cursor()

    # Create table - allObjects
    c.execute('''CREATE TABLE allObjects ([id] INTEGER PRIMARY KEY,[name] text)''')

    # Create table - locations
    c.execute('''CREATE TABLE locations ([id] INTEGER PRIMARY KEY,[name] text, [object_id] integer, [trained] text)''')

    # Create table - measurements
    c.execute('''CREATE TABLE measurements ([id] INTEGER PRIMARY KEY, [date] text, [location_id] integer)''')

    # Create table - datapoints
    c.execute('''CREATE TABLE datapoints ([id] INTEGER PRIMARY KEY, [value] float, [measurement_id] integer)''')

    connection.commit()
    return


def main():
    database = "chic.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        obj = ('Plant of the leaving room', );
        obj_id = create_obj(conn, obj)
        # let's add a new location
        loc = ('Leaf 1', 1)
        loc_id = create_location(conn, loc)
        # add some measures collected by ESP
        points = [1,2,3,4,5,7,8]
        save_points(conn, points, loc_id)
        save_points(conn, points, loc_id)
        # finally let's try to inspect some points
        points = get_measurements_for_location(conn, loc_id - 1)
        print(points)


if __name__ == '__main__':
    main()
