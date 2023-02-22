# Roundabout-extraction
Codes to extract roundabout crossings from Naturalistic Driving Data using Open Street Map

There are two codes "OSM_Roundabout" and "NDD_Roundabout"

OSM_Roundabout: A code that takes input ".osm" file for an area and extracts all the roundabouts in that area.
NDD_Roundabout: A function that takes input vehicle GPS coordinates and location of roundabouts (roundabout boundaries) and provides with interval when vehicle is within the roundabout boundaries. The roundabout boundaries denote a rectangular bounding box around a roundabout. Once the roundabout is obtained from OSM_Roundabout function, a bounding box can be created around it.    
