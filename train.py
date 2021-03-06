import os
from datetime import datetime
import argparse

from lib.utils import yaml2config
from networks import get_model

try:
    from torch.utils.tensorboard import SummaryWriter
except ModuleNotFoundError:
    from tensorboardX import SummaryWriter


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="config")
    parser.add_argument(
        "--config",
        nargs="?",
        type=str,
        default="/mydrive/MyDrive/khoa_luan/khoa_luan/configs/gan_iam.yml",
        help="Configuration file to use",
    )

    args = parser.parse_args()
    cfg = yaml2config(args.config)
    run_id = datetime.strftime(datetime.now(), '%m-%d-%H-%M')
    logdir = os.path.join("/mydrive/MyDrive/khoa_luan/khoa_luan/runs", os.path.basename(args.config)[:-4] + '-' + str(run_id))
    logdir = logdir.replace('\\', '/')
    model = get_model(cfg.model)(cfg, logdir)
    model.train()

