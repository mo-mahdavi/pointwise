import numpy as np
import open3d as o3d

if __name__ == "__main__":

    print("Load a ply point cloud, print it, and render it")
    pcd = o3d.io.read_point_cloud('./points.xyzrgb')
    print(pcd)
    print(np.asarray(pcd.points))
    o3d.visualization.draw_geometries([pcd])

    l = np.loadtxt('labels.txt')
    pred_l = np.loadtxt('pred_label.txt')
    print(l)
    palet = [[1, 0, 0],
             [0, 1, 0],
             [0, 0, 1],
             [1, 1, 0],
             [1, 0, 1],
             [0, 1, 1],
             [0, 0, 0],
             [1, 0.5, 0],
             [1, 1, 0.5],
             [0.5, 0, 1],
             [0.5, 1, 0],
             [0, 0.5, 1],
             [1, 0, 0.5]]

    colors = [[0, 0, 0] for x in range(len(l))]
    for i in range(len(l)):
        colors[i] = palet[int(l[i]) - 1]

    pcd.colors = o3d.utility.Vector3dVector(colors)
    o3d.visualization.draw_geometries([pcd])

    for i in range(len(l)):
        colors[i] = palet[int(pred_l[i]) - 1]

    pcd.colors = o3d.utility.Vector3dVector(colors)
    o3d.visualization.draw_geometries([pcd])
