<p align="center"><img width=30% src="src\assets\Logo.png" alt=""></p>
<p align="center"><img width=70% src="src\assets\smart-match.png" alt=""></p>

<div align="center">

![Python](https://img.shields.io/badge/PYTHON-v3.6.9-blue.svg)
![CUDA](https://img.shields.io/badge/CUDA-10.1-black)
![CUDNN](https://img.shields.io/badge/CUDNN-7.0-orange)
![TENSORFLOW](https://img.shields.io/badge/Tensorflow-2.1.0-green)

# **Myntra HackerRamp Submission Phase 2**
  
</div>

## Overview

**TheChibiTeam** from **Thapar Institute of Engineering and Technology** presents our submission for the Myntra HackerRamp Phase 2. We showcase how a Multi-Garment Network (MGN) can be fine-tuned on new images, and produce 3D garments and body parameters. These 3D-body parameters can then be layered on top of the Skinned Multi-Person Linear Model (SMPL) body. We also demonstrate how these 3D garments can be used to mix and match clothing on a model, and render this on a website in real-time using three.js.

## Team Members
- Khushnuma Grover
- Piyush Aggarwal
- Kartikey Tiwari

## Links
- Demo Site: https://khushgrover.github.io/smart-match/
- Video Explanation: https://drive.google.com/file/d/1QRDrG15-JAS8AP1cJY5Hg9Mgm1-XceyG/view
- Presentation: https://drive.google.com/file/d/1WFXqZGwt4ARoZs8HLbwpgdle7-PyiVSE/view
- Demo 1 (Machine Learning Model): https://drive.google.com/file/d/1eqPVxptgWA76aZt2NUSrmHBpPWXXzEDi/view
- Demo 2 (Website): https://drive.google.com/file/d/1juuHeB4G0OUVO6JLMe8celSGWUG561fk/view

## Approach

We show how a MGN network can be fine-tuned on new images. The network will produce 3d-garments of person and the 3d-body parameters. These 3d-body parameters can be layered on top of SMPL body.

We show how these 3d-garments can be used to mix and match clothing on a model. This can be rendered a website in real-time using **three.js**. For demo purposes we have used https://p3d.in.

## Colab notebooks

We have also shown our local changes on Colab Notebooks. However, Colab does not have a display, so we used SSH and ngrok on a local machine for visualization. Here are the links to the notebooks:
- MGN: https://github.com/khushgrover/smart-match/blob/main/MultiGarmentNetwork.ipynb
- PGN Segmentation: https://github.com/khushgrover/smart-match/blob/main/pgn_segmentation.ipynb
- Training U-NET: https://github.com/khushgrover/smart-match/blob/main/Train_UNET.ipynb
- Extracting Dresses using U-NET: https://github.com/khushgrover/smart-match/blob/main/Train_UNET.ipynb
- Extracting Dresses using GrabCut: https://github.com/khushgrover/smart-match/blob/main/OpenCv_GrabCut.ipynb
- Extracting Keypoints of Body OpenPose: https://github.com/khushgrover/smart-match/blob/main/Open

## References
### MultiGarmentNetwork
- GitHub Repository: Bharat, B., & Black, M. J. (2019). MultiGarmentNetwork. GitHub. https://github.com/bharat-b7/MultiGarmentNetwork
- Paper: Bharat, B., & Black, M. J. (2019). Multi-Garment Net: Learning to Dress 3D People from Images. Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2019, pp. 3303-3313. https://arxiv.org/abs/1908.06903
- In this, the trained model is provided and we plan to use the fine tuning of the network, which can be done using anywhere between 1-8 images of a person.

### Pre-requisites for running MGN
- Installed **DIRT**: https://github.com/pmh47/dirt (provides Fast Rendering for Tensorflow)
- Downloaded and installed **Mesh** packages for visualization: https://github.com/MPI-IS/mesh

### Preprocessing for Inputs
- Run **semantic segmentation** on images. PGN semantic segmentation used. https://github.com/Engineering-Course/CIHP_PGN
- Run **OpenPose** body_25 for 2D joints. https://github.com/CMU-Perceptual-Computing-Lab/openpose

### SMPL
- SMPL is a function M that maps pose θ and shape β to a mesh of V = 6890 vertices.
- Downloaded the neutral SMPL model from: http://smplify.is.tue.mpg.de/
- Paper: Loper, M., Mahmood, N., Romero, J., Pons-Moll, G., & Black, M. J. (2015). SMPL: A skinned multi-person linear model. ACM Transactions on Graphics, 34(6), 248:1-248:16. https://doi.org/10.1145/2818346.2820018
