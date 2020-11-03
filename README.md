<p align="center"><img width=30% src="assets\Logo.png"></p>
<p align="center"><img width=70% src="assets\smart-match.png"></p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/PYTHON-v3.6.9-blue.svg)
![CUDA](https://img.shields.io/badge/CUDA-10.1-black)
![CUDNN](https://img.shields.io/badge/CUDNN-7.0-orange)
![TENSORFLOW](https://img.shields.io/badge/Tensorflow-2.1.0-green)

## **Myntra HackerRamp Submission Phase 2**

**Team**: TheChibiTeam

**Members**: Piyush Aggarwal, Kartikey Tiwari, Khushnuma Grover

**University**: Thapar Institute of Engineering and Technology

### The demo site has been published to : https://khushgrover.github.io/smart-match/

This repository is implemented using:

- Tensorflow 2.1.0
- Python 3.6.9
- CUDA 10.1
- CUDNN 7

## **Phase 2 Explaination to approach taken:**

We show how a MGN network can be fine-tuned on new images. The network will produce 3d-garments of person and the 3d-body parameters. These 3d-body parameters can be layered on top of SMPL body.

We show how these 3d-garments can be used to mix and match clothing on a model. This can be rendered a website in real-time using **three.js**. For demo purposes we have used https://p3d.in.

### VIDEO EXPLAINATION

https://drive.google.com/file/d/1QRDrG15-JAS8AP1cJY5Hg9Mgm1-XceyG/view

### PPT

https://drive.google.com/file/d/1WFXqZGwt4ARoZs8HLbwpgdle7-PyiVSE/view

### DEMO-1 (ML MODEL)

https://drive.google.com/file/d/1eqPVxptgWA76aZt2NUSrmHBpPWXXzEDi/view

### DEMO-2 (WEB SITE)

https://drive.google.com/file/d/1juuHeB4G0OUVO6JLMe8celSGWUG561fk/view

## Colab notebooks

The local changes have also been shown on Colab Notebooks: (Colab doesn't have a display so we could not display out the resulta and have used SSH and ngrok int local machine for visualization.)

**MGN**: https://github.com/khushgrover/smart-match/blob/main/MultiGarmentNetwork.ipynb

**PGN Segmentation**: https://github.com/khushgrover/smart-match/blob/main/pgn_segmentation.ipynb

**Training U-NET**: https://github.com/khushgrover/smart-match/blob/main/Train_UNET.ipynb

**Extracting dresses using U-NET**: https://github.com/khushgrover/smart-match/blob/main/Train_UNET.ipynb

**Extracting dresses using GrabCut**: https://github.com/khushgrover/smart-match/blob/main/OpenCv_GrabCut.ipynb

**OpenPose**: https://github.com/khushgrover/smart-match/blob/main/Openpose1_6_0.ipynb

## **References**

### **MultiGarmentNetwork**

https://github.com/bharat-b7/MultiGarmentNetwork.git

This repository is the official implementation for the paper **"Multi-Garment Net: Learning to Dress 3D People from Images, ICCV'19"** in Python 2.7 and Tensorflow 1.13.

Link to paper: https://arxiv.org/abs/1908.06903

In this, the trained model is provided and we plan to use the fine tuning of the network, which can be done using anywhere between 1-8 images of a person.

### Pre-requisites for running MGN

- Installed **DIRT**: https://github.com/pmh47/dirt (provides Fast Rendering for Tensorflow)
- Downloaded and installed **Mesh** packages for visualization: https://github.com/MPI-IS/mesh

_Preprocessing for Inputs_

- Run **semantic segmentation** on images. PGN semantic segmentation used. https://github.com/Engineering-Course/CIHP_PGN
- Run **OpenPose** body_25 for 2D joints. https://github.com/CMU-Perceptual-Computing-Lab/openpose

### **SMPL: A Skinned Multi-Person Linear Model**

Downloaded the neutral SMPL model from http://smplify.is.tue.mpg.de/
