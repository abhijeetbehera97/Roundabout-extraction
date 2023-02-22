# Function to extract roundabout crossings from NDD

# Input 1: Vehicle's GPS coordinates: tc["x"]["y"] and 
# Input 2: Roundabout boundaries (rb_boundary): ["x1"]["y1"], ["x2"]["y1"], ["x1"]["y2"], ["x2"]["y2"]
# Output: Interval in the vehicle coordinates where the vehicle is within roundabout boundaries

import numpy as np

def roundabout_crossing_interval(tc, rb_boundary):
    vehicle_not_in_roundabout = 1 # 1 when vehicle is roundabout, 0 when vehicle is in roundabout
    k = 1
    interval = []

    for i in rb_boundary(len(tc["x"])):
        if vehicle_not_in_roundabout == 1:
            for j in rb_boundary(rb_boundary["x"].shape[0]):
                # The rectangular boundary is discretized
                if (np.digitize(tc["x"][i], [rb_boundary["x"][j, 0], rb_boundary["x"][j, 1]]) == 1
                    and np.digitize(tc["y"][i], [rb_boundary["y"][j, 0], rb_boundary["y"][j, 1]]) == 1):
                    interval.append([i])
                    vehicle_not_in_roundabout = 0
                    break
        else:
            if (np.isnan(np.digitize(tc["x"][i], [rb_boundary["x"][j, 0], rb_boundary["x"][j, 1]]))== 1
                or np.isnan(np.digitize(tc["y"][i], [rb_boundary["y"][j, 0], rb_boundary["y"][j, 1]]))== 1):
                interval[k - 1].append(i)
                k += 1
                vehicle_not_in_roundabout = 1

    return interval
