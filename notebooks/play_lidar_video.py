import numpy as np
import open3d as o3d
import os
import time

# Point to the folder containing all the .bin files
velodyne_dir = r"C:\Sensor_Fusion_Project\data\kitti\training\velodyne"

# Create a visualizer window
vis = o3d.visualization.Visualizer()
vis.create_window(window_name="KITTI Lidar Playback")

pcd = o3d.geometry.PointCloud()
is_initialized = False

print("Starting playback... Close the window to stop.")

# Loop through the first 100 frames
for i in range(100):
    # This formats the number to have 6 digits (e.g., 0 -> 000000, 1 -> 000001)
    filename = f"{i:06d}.bin"
    filepath = os.path.join(velodyne_dir, filename)
    
    if not os.path.exists(filepath):
        continue
        
    # Load the points
    scan = np.fromfile(filepath, dtype=np.float32).reshape(-1, 4)
    points = scan[:, 0:3]
    pcd.points = o3d.utility.Vector3dVector(points)
    
    # Update the window
    if not is_initialized:
        vis.add_geometry(pcd)
        is_initialized = True
    else:
        vis.update_geometry(pcd)
        
    vis.poll_events()
    vis.update_renderer()
    
    # Wait a fraction of a second before loading the next frame
    time.sleep(0.1)

vis.destroy_window()