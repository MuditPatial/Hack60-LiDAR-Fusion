import numpy as np
import open3d as o3d
import os

# 1. Path to the very first Lidar scan in your training set
bin_path = r"C:\Sensor_Fusion_Project\data\kitti\training\velodyne\000001.bin"

if not os.path.exists(bin_path):
    print(f"Error: Could not find the file at {bin_path}")
    print("Check your folder structure!")
else:
    print("Loading point cloud...")
    # 2. KITTI point clouds are saved as float32 arrays (x, y, z, reflectance)
    scan = np.fromfile(bin_path, dtype=np.float32).reshape(-1, 4)

    # 3. We only need the X, Y, and Z coordinates to draw the 3D map
    points = scan[:, 0:3]

    # 4. Create an Open3D point cloud object
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)

    # Optional: Paint it a solid color (e.g., light blue) to see it better
    pcd.paint_uniform_color([0.1, 0.7, 0.7])

    print("Opening 3D viewer! You can rotate with your mouse.")
    # 5. Visualize it
    o3d.visualization.draw_geometries([pcd], window_name="KITTI Lidar Scan 000000")