_base_ = [
    '../rtmdet_large/config.py',
]

checkpoint = 'https://download.openmmlab.com/mmdetection/v3.0/rtmdet/cspnext_rsb_pretrain/cspnext-s_imagenet_600e.pth'  # noqa
model = dict(
    backbone=dict(
        deepen_factor=0.33,
        widen_factor=0.5,
        init_cfg=dict(
            type='Pretrained', prefix='backbone.', checkpoint=checkpoint)),
    neck=dict(in_channels=[128, 256, 512], out_channels=128, num_csp_blocks=1),
    bbox_head=dict(in_channels=128, feat_channels=128, exp_on_reg=False))