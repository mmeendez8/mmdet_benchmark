env_cfg = dict(
    mp_cfg=dict(opencv_num_threads=0, mp_start_method='fork'),
    dist_cfg=dict(backend='nccl'))

dataset_type = 'CocoDataset'
data_root = 'coco/'
image_size = (640, 640)
backend_args = None

test_pipeline = [
    dict(type='LoadImageFromFile', backend_args=backend_args),
    dict(type='Resize', scale=image_size, keep_ratio=False),
    dict(
        type='PackDetInputs',
        meta_keys=('img_id', 'img_path', 'ori_shape', 'img_shape',
                   'scale_factor'))
]

test_dataloader = dict(
    batch_size=1,
    num_workers=2,
    persistent_workers=True,
    drop_last=False,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        ann_file='annotations/instances_val2017.json',
        data_prefix=dict(img='images/val2017/'),
        test_mode=True,
        pipeline=test_pipeline,
        backend_args=backend_args))

# test_evaluator = dict(
#     type='CocoMetric',
#     ann_file=data_root + 'annotations/instances_val2017.json',
#     metric='bbox',
#     format_only=False,
#     backend_args=backend_args)
