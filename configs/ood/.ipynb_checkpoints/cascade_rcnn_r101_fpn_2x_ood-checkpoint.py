_base_ = [
    './cascade_rcnn_r50_fpn_2x_ood.py'
]

model = dict(
    backbone=dict(
        depth=101,
        init_cfg=dict(type='Pretrained',
                      checkpoint='/hy-tmp/resnet101-63fe2227.pth')
    )
)