import xml.etree.ElementTree as ET
from shapely.geometry import LineString
import matplotlib.pyplot as plt

# Loading the .osm file and parsing
tree = ET.parse('test_file.osm')
root = tree.getroot()

# Extract Roundabout from .osm
roundabouts = []
for way in root.findall("./way/tag[@k='junction'][@v='roundabout']/.."):
    nodes = []
    for nd in way.findall('nd'):
        node_id = nd.get('ref')
        node = root.find("node[@id='{}']".format(node_id))
        lon = float(node.get('lon'))
        lat = float(node.get('lat'))
        nodes.append((lon, lat))
    roundabout = LineString(nodes)
    roundabouts.append({'geometry': roundabout})

# Display the roundabouts on a map
fig, ax = plt.subplots(figsize=(10, 10))
for roundabout in roundabouts:
    ax.plot(*roundabout['geometry'].xy, color='red', linewidth=2)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)    
plt.show()