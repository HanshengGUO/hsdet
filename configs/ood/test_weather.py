_base_ = [
    './cascade_rcnn_r50_fpn_2x_ood.py'
]

data = dict(
    test=dict(
        ann_file=data_root + 'annotations/instances_weather_val2017.json'
    )
)