#Coordinates Reference System (CRS)

#Load a GeoDataFrame
regions = gpd.read_file("../input/..Map_of_Regions_inGhana.shp")
print(regions.crs)

#Health Facilities
facilities_df = pd.read_csv("../input/geospatial-learn-../ghana/health_facilities.csv")

#Convert dataframe to GeoDataFrame
facilities = gpd.GeoDataFrame(facilities_df, geometry = gpd.points_from_xy(facilities_df.Longitude, facilites_df.Latitude))

#Set the CRS to EPSG 4326
facilities.crs = {'init': 'epsg:4326'}

#View the first five rows of GeoDataFrame
facilities.head()

#Re-projecting
# Create a Map
ax = regions.plot(figsize=(8,8),color='whitesmoke',linestyle=':',edgecolor='black')
facilities.to_crs(epsg=32630).plot(markersize=1,ax=ax)

#if EPSG not available
+prj=longlat +ellps=WGS84 +datum=WGS84 +no_defs

regions.to_crs("+proj=longlat +ellps=WGS84 +Datum=WGS84 +no_defs").head()

# Calculate Area
regions.loc[:, "AREA"] = regions.geometry.area / 10**6

print("Area of Ghana: {} square kilometers".format(regions.AREA.sum()))
print("CRS:", regions.crs)
regions.head()


#Exercise
import pandas as pd 

#load data
birds_df = pd.read_csv("../input/purple_martin.csv", parse_dates=['timestamp'])
print("There are {} different birds in the dataset.".format(brids_df["tag-local-identifier"].nunique()))
birds_df.head()

#Create dataframe
birds = gpd.GeoDataFrame(birds_df, geometry = gpd.points_from_xy(birds_df["location-long"],birds_df["location-lat"]))

#Set CRS to 4326
birds.crs = {'init':'epsg:4326'}

#Plotting
#Load GeoDataFrame with country boundaries
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
americas = world.loc[world['continent'].isin(['North America', 'South America'])]
americas.head()

ax = americas.plot(figsize=(20,20),color='whitesmoke',linestyle=':', edgecolor='black')
birds.plot(color='lightgreen', ax=ax)

#Start and Ending Journey
# GeoDataFrame showing path for each birds_df
path_df = birds.groupby("tag-local-identifier")['geometry'].apply(list).apply(lambda x: LineString(x)).reset_index()
path_gdf = gpd.GeoDataFrame(path_df, geometry=path_df.geometry)
path_gdf.crs = {'init':'epsg:4326'}

# GeoDataFrame showing starting point for each bird
start_df = birds.groupby("tag-local-identifier")['geometry'].apply(list).apply(lambda x: x[0]).reset_index()
start_gdf = gpd.GeoDataFrame(start_df, geometry=start_df.geometry)
start_gdf.crs = {'init' :'epsg:4326'}

end_df = birds.groupby("tag-local-identifier")['geometry'].apply(list).apply(lambda x: x[-1]).reset_index()
end_gdf = gpd.GeoDataFrame(end_df, geometry=end_df.geometry)
end_gdf.crs = {'init' :'epsg:4326'}

# Path of the shapefile to load
protected_filepath = "../input/geospatial-learn-course-data/SAPA_Aug2019-shapefile/SAPA_Aug2019-shapefile/SAPA_Aug2019-shapefile-polygons.shp"

# Your code here
protected_areas = gpd.read_file(protected_filepath)
print(protected_areas.crs)

# Country boundaries in South America
south_america = americas.loc[americas['continent']=='South America']

# Your code here: plot protected areas in South America
ax = south_america.plot(figsize=(10,10),color='whitesmoke',linestyle=':',edgecolor='black')
protected_areas.plot(ax=ax,alpha=0.4)

#Calculate the total area of South America (in square kilometers)

totalArea = sum(south_america.geometry.to_crs(epsg=3035).area / 10**6)

# What percentage of South America is protected?
percentage_protected = P_Area/totalArea
print('Approximately {}% of South America is protected.'.format(round(percentage_protected*100, 2)))

#Overlap Mapping
ax = south_america.plot(figsize=(10,10),color='whitesmoke',linestyle=':',edgecolor='black')
protected_areas[protected_areas['MARINE']!='2'].plot(ax=ax,alpha=0.4)
birds[birds.geometry.y < 0].plot(ax=ax, color='red', alpha=0.6, markersize=10, zorder=2)