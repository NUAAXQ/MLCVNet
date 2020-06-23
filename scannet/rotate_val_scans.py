# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 11:03:21 2019

@author: QIAN
"""
import os
import sys
import numpy as np
BASE_DIR = os.path.dirname(os.path.abspath('__file__'))
ROOT_DIR = os.path.dirname(BASE_DIR)
sys.path.append(os.path.join(ROOT_DIR, 'utils'))
from plyfile import PlyData

def transform(file_name, mesh_file,meta_file,new_dir):
    
    #1.load point cloud
    with open(mesh_file, 'rb') as f:
        plydata = PlyData.read(f)
        num_verts = plydata['vertex'].count
        mesh_vertices = np.zeros(shape=[num_verts, 6], dtype=np.float32)
        mesh_vertices[:,0] = plydata['vertex'].data['x']
        mesh_vertices[:,1] = plydata['vertex'].data['y']
        mesh_vertices[:,2] = plydata['vertex'].data['z']

    #2.apply transformation
    ## Load scene axis alignment matrix
    lines = open(meta_file).readlines()
    for line in lines:
        if 'axisAlignment' in line:
            axis_align_matrix = [float(x) \
                for x in line.rstrip().strip('axisAlignment = ').split(' ')]
    axis_align_matrix = np.array(axis_align_matrix).reshape((4,4))
    pts = np.ones((mesh_vertices.shape[0], 4))
    pts[:,0:3] = mesh_vertices[:,0:3]
    pts = np.dot(pts, axis_align_matrix.transpose()) # Nx4
    
    plydata['vertex'].data['x'] = pts[:,0]
    plydata['vertex'].data['y'] = pts[:,1]
    plydata['vertex'].data['z'] = pts[:,2]
    
    #3.save transformed meshes
    plydata.write(os.path.join(new_dir,file_name))
    
    
def main():
    ## you need first put all the val meshes into "base_dir"
    base_dir = 'D:/MLCVNet/scannet/scans'
    new_dir = 'D:/MLCVNet/scannet/scans_val_transformed'
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    
    file_val = "D:/MLCVNet/scannet/meta_data/scannetv2_val.txt"
    lines = open(file_val).readlines()
    
    ## transform meshes one by one
    for line in lines:
        line = line.strip('\n')
        print(line)
        file_name = line + '_vh_clean_2.ply'
        meta_file = line + '.txt'
        file_path = os.path.join(base_dir,line,file_name)
        meta_file = os.path.join(base_dir,line,meta_file)
        transform(file_name, file_path, meta_file, new_dir)

if __name__ == '__main__':
    main()