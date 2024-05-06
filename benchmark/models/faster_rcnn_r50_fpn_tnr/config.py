_base_ = [
    '../faster_rcnn_r50_fpn_orig/config.py',
]

checkpoint = 'https://download.pytorch.org/models/resnet50-11ad3fa6.pth'
model = dict(
    backbone=dict(init_cfg=dict(type='Pretrained', checkpoint=checkpoint)))