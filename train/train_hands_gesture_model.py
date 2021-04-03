import torch
import numpy as np
from pathlib import Path
from torch import optim
from torch.utils.data import DataLoader
from torch.nn import CrossEntropyLoss
from constants.enum_keys import HG
from models.hands_recognition_model import HandsRecognitionModel
from hgdataset.s3_handcraft import HgdHandcraft
from constants import settings
from visdom import Visdom


class Trainer:
    def __init__(self, is_unittest=False):
        self.is_unittest = is_unittest
        self.batch_size = 2
        self.clip_len = 15 * 30
        hgd = HgdHandcraft(Path.home() / 'MeetingHands', True, (512, 512), clip_len=self.clip_len)
        self.data_loader = DataLoader(hgd, batch_size=self.batch_size, shuffle=False, num_workers=settings.num_workers)
        self.model = HandsRecognitionModel(batch=self.batch_size)
        self.model.train()
        self.epoch = 100000
        self.loss = CrossEntropyLoss()
        self.opt = optim.Adam(self.model.parameters(), lr=1e-3)
        self.vis = Visdom()
        self.loss_window = self.vis.line([0.], [0], win='train_loss', opts=dict(title='train_loss'))


    def train(self):
        step = 0
        self.model.load_ckpt()
        for epoch in range(self.epoch):
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
                loss_tensor = self.loss(class_out, target)
                self.opt.zero_grad()
                loss_tensor.backward()
                self.opt.step()
                self.vis.line([loss_tensor.item()], [epoch], win='train_loss', update='append')

                if step % 100 == 0:
                    print("step: %d, Loss: %f" %(step, loss_tensor.item()))
                if step % 5000 == 0 and step!=0:
                    self.model.save_ckpt()
                if self.is_unittest:
                    break
                step = step + 1
            if self.is_unittest:
                break


