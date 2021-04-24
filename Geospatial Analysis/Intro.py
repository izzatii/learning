import geopandas as pd

full_data = gpd.read_file(".../input/geospatial-learn-course-data/DEC_lands/DEC_lands/DEC_lands.shp")
full_data.head()

#select columns
data = full_data.loc[:, ["CLASS", "COUNTY", "geometry"]].copy()

#how many lands of each type are there?
data.CLASS.value_counts()

#Select lands that fall under the "WILD FOREST" or "WILDERNESS" category
wild_lands = data.loc[data.CLASS.isin(['WILD FOREST', 'WILDERNESS'])].copy()
wild_lands.head()

#Plotting
wild_lands.plot()

# Campsite (Point)
POI_data = gpd.read_file("../Decptsofinterest.shp")
campsites = POI_data.loc[POI_data.ASSET=='PRIMIpipTIVE CAMPSITE'].copy()

#Foor trails (LineString)
roads_trails = gpd.read_file("/input/Decroadstrails.shp")
trails = roads_trails.loc[roads_trails.ASSET=='FOOT TRAIL'].copy()

#County Boundaries (Polygon)
counties = gpd.read_file("../input/NY_county_boundaries.shp")

#Define base map
ax = counties.plot(figsize=(10,10),color='none', edgecolor='gainsboro', zorder=3)

#Add wild lands, campsites, and foot trails to the base map
wild_lands.plot(color = 'lightgreen', ax=ax)
campsites.plot(color='maroon', markersize=2, ax=ax)
trails.plot(color='black', markersize=1, ax=ax)

#Alternative
ax = world.plot(figsize=(20,20), color='whitesmoke', linestyle=':',edgecolor='black')
world_loans.plot(ax=ax, markersize=2)

#Select loans based on country
PHL_loans = world_loans.loc[world_loans.country=="Philippines"].copy()

#Load KML file containing island Boundaries (KML file)
gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'
PHL = gpd.read_file("../input/../Philippines_AL258.kml", driver = 'KML')
PHL.head()