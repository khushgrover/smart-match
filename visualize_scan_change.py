'''
This loads scan and visualizes segmentation and texture on it
'''
import os
from os.path import split, join, exists
from glob import glob
import pickle as pkl  # Python 3 change
from shutil import copyfile
from psbody.mesh import Mesh, MeshViewers
import numpy as np
import cv2

if __name__ == '__main__':
    path = './Multi-Garment_dataset/125611499279708'

    scan1 = Mesh(filename=join(path, 'smpl_registered.obj'))
    tex_file = join(path, 'registered_tex.jpg')
    scan1.set_texture_image(tex_file)

    scan2 = Mesh(filename=join(path, 'scan.obj'))
    tex_file1 = join(path, 'scan_tex.jpg')
    scan2.set_texture_image(tex_file1)

    scan3 = Mesh(filename=join(path, 'scan.obj'))
    seg = np.load(join(path, 'scan_labels.npy'))
    scan3.set_vertex_colors_from_weights(seg.reshape(-1,))

    fts_file = 'assets/garment_fts.pkl'
    vert_indices, _ = pkl.load(open(fts_file, "rb"), encoding="latin1")

    garment_type_upper = 'TShirtNoCoat'
    garment_type_lower = 'ShortPants'
    garment_unposed_upper = Mesh(
        filename=join(path, garment_type_upper + '.obj'))
    garment_unposed_lower = Mesh(
        filename=join(path, garment_type_lower + '.obj'))

    vert_inds_upper = vert_indices[garment_type_upper]
    garment_tex_upper = join(path, 'multi_tex.jpg')
    garment_unposed_upper.set_texture_image(garment_tex_upper)

    vert_inds_lower = vert_indices[garment_type_lower]
    garment_tex_lower = join(path, 'multi_tex.jpg')
    garment_unposed_lower.set_texture_image(garment_tex_lower)

    mvs = MeshViewers((2, 3))
    mvs[0][0].set_static_meshes([scan1])
    mvs[0][1].set_static_meshes([scan2])
    mvs[0][2].set_static_meshes([scan3])
    mvs[1][0].set_static_meshes([garment_unposed_upper])
    mvs[1][1].set_static_meshes([garment_unposed_lower])
    garment_unposed_upper.write_obj('upper.obj')
    garment_unposed_lower.write_obj('lower.obj')

    print('Done')
