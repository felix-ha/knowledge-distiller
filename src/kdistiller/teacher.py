import os
from pathlib import Path
import datetime
import logging

import torch
from torch.utils.data import DataLoader
from dataclasses import dataclass


CHECKPOINT_FILE = "model.pt"
LOG_FILE = "info.log"

@dataclass
class TrainingConfig:
    model: any
    loss_func: any
    training_loader: DataLoader
    validation_loader: DataLoader = None
    lr: float = 0.001
    optimizer: str = "SGD"
    epochs: int = 2
    device: str = "cpu"
    save_model: bool = False
    zip_result: bool = False
    save_path: str = None
    model_name: str = None
    classification_metrics: dict = False
    class_names: list = None
    progress_bar: bool = True
    checkpoint_epochs: list[int] = None

    def __post_init__(self):
        if self.optimizer == "SGD": 
            self.optimizer = torch.optim.SGD(self.model.parameters(), lr=self.lr)
        elif self.optimizer == "AdamW": 
            self.optimizer = torch.optim.AdamW(self.model.parameters(), lr=self.lr)

        if self.save_model:
            current_time = datetime.datetime.now()
            timestamp = current_time.strftime("%Y%m%d_%H%M%S")
            # TODO fix naming or general handling of saving
            self.save_path_final = Path(self.save_path).joinpath(f"{timestamp}_{self.model_name}")
            self.save_path_final.mkdir(parents=True, exist_ok=False)
            logfile = os.path.join(self.save_path_final, LOG_FILE)
        else:
            logfile = LOG_FILE

        logging.basicConfig(
            format='%(asctime)s - %(message)s',
            level=logging.INFO,
            handlers=[logging.FileHandler(logfile, mode='w')],
            force=True
            )

        if self.device == "gpu" or self.device == torch.device("cuda:0"):
            self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
            logging.info(f"using device {self.device}")
        elif self.device == "cpu" or torch.device("cpu"):
            self.device = torch.device("cpu")
            logging.info(f"using device {self.device}")
        else:
            logging.info(f"device {self.device} is not available, using cpu instead")


def train(config):
    return 1
