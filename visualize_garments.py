'''
This code visualises registered garment on the original smpl body
If you use this code please cite:
"Multi-Garment Net: Learning to Dress 3D People from Images", ICCV 2019

Code author: Bharat
'''
import os
from os.path import exists, join, split
from glob import glob
import numpy as np
import pickle as pkl  # Python 3 change
from psbody.mesh import Mesh, MeshViewer, MeshViewers

from utils.smpl_paths import SmplPaths
from lib.ch_smpl import Smpl
from dress_SMPL import load_smpl_from_file, pose_garment
from utils.interpenetration_ind import remove_interpenetration_fast

if __name__ == '__main__':
    # path to dataset
    path = './Multi-Garment_dataset/'

    # types of garments
    garment_classes = ['Pants', 'ShortPants',
                       'ShirtNoCoat', 'TShirtNoCoat', 'LongCoat']

    # dictionary containing
    # keys: garments
    # values: list of paths to garments
    gar_dict = {}
    for gar in garment_classes:
        gar_dict[gar] = glob(join(path, '*', gar + '.obj'))

    # define smpl body
    dp = SmplPaths()
    vt, ft = dp.get_vt_ft_hres()
    smpl = Smpl(dp.get_hres_smpl_model_data())

    # This file contains correspondances between garment vertices and smpl body
    fts_file = 'assets/garment_fts.pkl'
    vert_indices, fts = pkl.load(open(fts_file, "rb"), encoding="latin1")
    fts['naked'] = ft

    # Choose any garment type
    type_upper = 'TShirtNoCoat'
    type_lower = 'ShortPants'

    # # Randomly pick from the digital wardrobe
    # index_upper = np.random.randint(0, len(gar_dict[type_upper]))
    # index_lower = np.random.randint(0, len(gar_dict[type_lower]))

    # store their paths
    path_upper = './Multi-Garment_dataset/125611499279708'
    path_lower = './Multi-Garment_dataset/125611499279708'

    # Load SMPL body for the upper garment
    upper_garment_org_body = load_smpl_from_file(
        join(path_upper, 'registration.pkl'))
    upper_garment_org_body = Mesh(
        upper_garment_org_body.v, upper_garment_org_body.f)

    # Load SMPL body for the lower garment
    lower_garment_org_body = load_smpl_from_file(
        join(path_lower, 'registration.pkl'))
    lower_garment_org_body = Mesh(
        lower_garment_org_body.v, lower_garment_org_body.f)

    # Load unposed garment
    garment_unposed_upper = Mesh(
        filename='./Multi-Garment_dataset/125611499279708/TShirtNoCoat.obj')
    garment_unposed_upper.set_texture_image(join(path_upper, 'multi_tex.jpg'))

    garment_unposed_lower = Mesh(
        filename='./Multi-Garment_dataset/125611499279708/ShortPants.obj')
    garment_unposed_lower.set_texture_image(join(path_lower, 'multi_tex.jpg'))

    # Pose garments
    # upper
    dat_upper = pkl.load(
        open(join(path_upper, 'registration.pkl'), "rb"), encoding="latin1")
    dat_upper['gender'] = 'neutral'
    garment_posed_upper = pose_garment(
        garment_unposed_upper, vert_indices[type_upper], dat_upper)
    garment_posed_upper = remove_interpenetration_fast(
        garment_posed_upper, upper_garment_org_body)
    # loading textures on posed garments
    garment_posed_upper.vt = garment_unposed_upper.vt
    garment_posed_upper.ft = garment_unposed_upper.ft
    garment_posed_upper.set_texture_image(join(path_upper, 'multi_tex.jpg'))

    # lower
    dat_lower = pkl.load(
        open(join(path_lower, 'registration.pkl'), "rb"), encoding="latin1")
    dat_lower['gender'] = 'neutral'
    garment_posed_lower = pose_garment(
        garment_unposed_lower, vert_indices[type_lower], dat_lower)
    garment_posed_lower = remove_interpenetration_fast(
        garment_posed_lower, lower_garment_org_body)
    # loading textures on posed garments
    garment_posed_lower.vt = garment_unposed_lower.vt
    garment_posed_lower.ft = garment_unposed_lower.ft
    garment_posed_lower.set_texture_image(join(path_lower, 'multi_tex.jpg'))

    # visualizing
    mvs = MeshViewers((2, 4), keepalive=True)

    # smpl
    mvs[1][0].set_static_meshes([upper_garment_org_body])
    mvs[0][0].set_static_meshes([lower_garment_org_body])

    # unposed garments
    mvs[1][1].set_static_meshes([garment_unposed_upper])
    mvs[0][1].set_static_meshes([garment_unposed_lower])

    # posed garments
    mvs[1][2].set_static_meshes([garment_posed_upper])
    mvs[0][2].set_static_meshes([garment_posed_lower])

    # posed body
    mvs[1][3].set_static_meshes([upper_garment_org_body, garment_posed_upper])
    mvs[0][3].set_static_meshes([lower_garment_org_body, garment_posed_lower])

    print('Done')
