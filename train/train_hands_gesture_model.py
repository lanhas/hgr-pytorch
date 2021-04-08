import torch
import numpy as np
from pathlib import Path
from torch import optim
from torch.utils.data import DataLoader
from torch.nn import CrossEntropyLoss
from constants.enum_keys import HG
from models.hands_recognition_model import HandsRecognitionModel
from torch.optim.lr_scheduler import CosineAnnealingLR
from hgdataset.s3_handcraft import HgdHandcraft
from constants import settings

from visdom import Visdom


class Trainer:
    def __init__(self, is_unittest=False):
        self.is_unittest = is_unittest
        self.batch_size = 1
        self.clip_len = -1
        hgd = HgdHandcraft(Path.home() / 'MeetingHands', True, (512, 512), clip_len=self.clip_len)
        self.data_loader = DataLoader(hgd, batch_size=self.batch_size, shuffle=False, num_workers=settings.num_workers)
        self.model = HandsRecognitionModel(batch=self.batch_size)
        self.model.train()
        self.model_folder = Path.cwd() / 'checkpoints'
        self.loss_his_train = []
        self.epochs = 3000
        self.loss = CrossEntropyLoss()
        self.opt = optim.Adam(self.model.parameters(), lr=1e-3)
        self.scheduler = CosineAnnealingLR(self.opt, T_max=self.epochs, eta_min=1e-10)
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.vis = Visdom()

    def set_train(self):
        """Convert models to training mode
        """
        self.model.train()

    def set_eval(self):
        """Convert models to testing/evaluation mode
        """
        self.model.eval()

    def train(self):
        self.epoch = 0
        for epoch in range(self.epochs):
            loss_trained = self.run_epoch()
            self.loss_his_train.append(loss_trained)
            self.vis.line([loss_trained.item()], [epoch], win='train_loss', update='append', opts=dict(title='losses'))

            print("Epoch:{}".format(epoch))
            print("train loss: {}".format(loss_trained))
            model_path = self.model_folder / Path('lstm_model_epoch_' + str(epoch) + '_trainloss_' + str(round(loss_trained, 2)) + '.pt')
            if epoch != 0 and epoch % 500 == 0:
                torch.save(self.model.state_dict(), model_path)
        self.model.save_ckpt()

    def run_epoch(self):
        loss_train = torch.tensor(.0).to(self.device)
        train_count = 0
        self.set_train()
        for ges_data in self.data_loader:
            features = torch.cat((ges_data[HG.BONE_LENGTH], ges_data[HG.BONE_ANGLE_COS],
                                    ges_data[HG.BONE_ANGLE_SIN], ges_data[HG.BONE_DEPTH]), dim=2)
            features = features.permute(1, 0, 2)
            features = features.to(self.model.device, dtype=torch.float32)
            h0, c0 = self.model.h0(), self.model.c0()
            _, h, c, class_out = self.model(features, h0, c0)
            target = ges_data[HG.GESTURE_LABEL]
            target = target.to(self.model.device, dtype=torch.long)
            target = target.permute(1, 0)
            target = target.reshape((-1))
            loss_step = self.loss(class_out, target)
            self.opt.zero_grad()
            loss_step.backward()
            self.opt.step()
            loss_train += loss_step
            train_count += 1
            self.scheduler.step()
        
        loss_trained = loss_train.cpu().detach().numpy() / train_count
        return loss_trained


if __name__ == "__main__":
    tr = Trainer()
    tr.train()

