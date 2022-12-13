import logging
import os
import os.path as osp

from mmengine.config import Config, DictAction
from mmengine.runner import Runner

def main(): 
    # load config
    config = os.path.join("./config", "deep3dbox", "debug_train_config.py")
    cfg = Config.fromfile(config)
    # create work_dir
    cfg.work_dir = osp.join('./work_dirs',
                            osp.splitext(osp.basename(config))[0])
    runner = Runner.from_cfg(cfg)
    # start training
    runner.train()

if __name__ == "__main__": 
    main()