# MLCVNet
## Introduction
This repository is the MLCVNet code implementation on ScanNet dataset. The main parts of the code are based on [VoteNet](https://github.com/facebookresearch/votenet).

![teaser](https://github.com/NUAAXQ/MLCVNet/blob/master/images/teaser.jpg)

## Installation
Follow the [Installation](https://github.com/facebookresearch/votenet#installation) and [Data preparation](https://github.com/facebookresearch/votenet#data-preparation) structions in VoteNet.

## Train and Test
To train a MLCVNet model on Scannet data, you can simply run (it takes around 4 hours to convergence with one 1080ti GPU):
```
	CUDA_VISIBLE_DEVICES=0 python train.py
```
To test the trained model with its checkpoint:
```
	python eval.py --checkpoint_path demo_files/pretrained_mlcvnet_on_scannet.tar --dump_dir eval_scannet --use_3d_nms --use_cls_nms --per_class_proposal
```

## Run demo
You can simply run the following command to use the pretrained model on a ScanNet:
```
    python demo.py
```
The default scene ID used here is `scene0609_02_vh_clean_2` in `demo_files`. Detection results will be dumped to `demo_files/scene0609_02_vh_clean_2`. The data structure should be:
```
demo_files/scene0609_02_vh_clean_2
├── 2_pred_confident_nms_bbox.ply
├── 4_pred_confident_nms_bbox.ply
├── ...
```
You can use 3D visualization software such as the [MeshLab](http://www.meshlab.net/) to open the dumped file under `demo_files/scene0609_02_vh_clean_2` to see the 3D detection output. 


## Detections Visualization
### Step 1: generate the results
Run `python demo.py` to get the output results for a specific scene `scene0609_02_vh_clean_2.ply`.

(If you want to see results of another scene: Since the output boxes are in different coordination with the original scene, so you need first run `rotate_val_scans.py` in the `scannet` folder to tranform the original scenes into the boxes' coordination, for the proper visualization. Then, choose a scene ID, for instance `scene0575_00`, and find `scene0575_00_vh_clean_2.ply` in `scans_val_transformed` folder. Move it to the `demo_files` and run `python demo.py scene0575_00_vh_clean_2.ply`)

### Step 2: visualization mode
Import the `scene0609_02_vh_clean_2.ply` and `*_pred_confident_nms_bbox.ply` to Meshlab. Set the correct visualization mode for the scene and all imported boxes, as shown in the below picture.

<img src="https://github.com/NUAAXQ/MLCVNet/blob/master/images/0-import.jpg" width = 80% height = 80% div align=center />

### Step 3: Quad-mesh
Turn the boxes into Quad mode as shown in the following figure. Choose the box one by one in the Layer Dialog. Follow the operations by "Filters"->"Polygonal and Quad Mesh"->"Turn into Quad-Dominant mesh"->"Apply".

<img src="https://github.com/NUAAXQ/MLCVNet/blob/master/images/1-mesh.jpg" width = 80% height = 80% div align=center />

### Setp 4: colorization
Choose one type of objects and change the color under the "Wireframe" visualization mode, in the Layer Dialog.
<img src="https://github.com/NUAAXQ/MLCVNet/blob/master/images/2-color.jpg" width = 80% height = 80% div align=center />

See more results in `visualization examples`.

## Citation
If our work is useful for your research, please consider cite:

```
@inproceedings{xie2020mlcvnet,
	title={MLCVNet: Multi-Level Context VoteNet for 3D Object Detection},
	author={Qian, Xie and Yu-kun, Lai and Jing, Wu and Zhoutao, Wang and Yiming, Zhang and Kai, Xu and Jun, Wang},
	booktitle={The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
	year={2020}
}
```


## Acknowledgemets
This code largely benefits from excellent works [VoteNet](https://github.com/facebookresearch/votenet) and [cgnl-network.pytorch](https://github.com/KaiyuYue/cgnl-network.pytorch) repositories, please also consider cite [VoteNet](https://arxiv.org/pdf/1904.09664.pdf) and [CGNL](https://arxiv.org/pdf/1810.13125.pdf) if you use this code.
