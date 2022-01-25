from omegaconf import OmegaConf

from libai.data.datasets import ImageNetDataset
from libai.data.build import build_image_train_loader, build_image_test_loader
from libai.config import LazyCall

from .transform import default_train_transform as train_aug_cfg
from .transform import default_test_transform as test_aug_cfg


dataloader = OmegaConf.create()

dataloader.train = LazyCall(build_image_train_loader)(
    dataset=[
        LazyCall(ImageNetDataset)(
            root="/DATA/disk1/ImageNet/extract/", train=True, transform=train_aug_cfg
        ),
    ],
)


dataloader.test = [
    LazyCall(build_image_test_loader)(
        dataset=LazyCall(ImageNetDataset)(
            root="/DATA/disk1/ImageNet/extract/", train=False, transform=test_aug_cfg
        ),
    )
]