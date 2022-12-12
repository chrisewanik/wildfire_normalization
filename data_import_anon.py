# Connecting to Postgres
from sqlalchemy import create_engine
import geopandas as gpd
import geoalchemy2

# Get connected
try:
    # Note that the below needs to be updated with your username, password, hostname (localhost if local), port number
    # (5432 or 9999) and the database name
    connection_uri = 'postgresql://username:password@hostname:port_num/db_name'
    engine = create_engine(connection_uri)
except Exception as e:
    print("Unable to connect to the database")
    raise Exception(e)
else:
    print("Database connected")


# Read Data
try:
    # Insert the Path to your data here
    gdf = gpd.read_file('C:/Users/you/OneDrive/Documents/data/data.shp')
except Exception as e:
    print("Unable to load data")
    raise Exception(e)
else:
    print("Data loaded")


# Push the geodataframe to postgresql
try:
    # Arguments specify the table to create, the connection, the scheme
    gdf.to_postgis("ignitions", engine, schema="final_project", index=False, if_exists='replace')
except Exception as e:
    print("Unable to push data")
    raise Exception(e)
else:
    print("Data pushed")