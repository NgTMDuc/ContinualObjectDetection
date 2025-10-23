# Copyright (c) Facebook, Inc. and its affiliates.
from .build import build_backbone, BACKBONE_REGISTRY  # noqa F401 isort:skip

from .backbone import Backbone
from .fpn import FPN
from .regnet import RegNet
from .resnet import (
    BasicStem,
    ResNet,
    ResNetBlockBase,
    build_resnet_backbone,
    make_stage,
    BottleneckBlock,
)
from .vit import ViT, SimpleFeaturePyramid, get_vit_lr_decay_rate
from .mvit import MViT
try:
    from .swin import SwinTransformer, build_swint_backbone, build_swint_fpn_backbone, add_swint_config
except Exception:
    SwinTransformer = None
    build_swint_backbone = None
    build_swint_fpn_backbone = None
    def add_swint_config(cfg): pass


__all__ = [k for k in globals().keys() if not k.startswith("_")]
# TODO can expose more resnet blocks after careful consideration
