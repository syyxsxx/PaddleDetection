from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import paddle
import paddle.nn as nn
from ppdet.core.workspace import register

__all__ = ['BaseArch']


@register
class BaseArch(nn.Layer):
    def __init__(self):
        super(BaseArch, self).__init__()

    def forward(self, inputs, mode='infer'):
        self.inputs = inputs
        self.inputs['mode'] = mode
        self.model_arch()

        if mode == 'train':
            out = self.get_loss()
        elif mode == 'infer':
            out = self.get_pred()
        else:
            out = None
            raise "Now, only support train and infer mode!"
        return out

    def build_inputs(self, data, input_def):
        inputs = {}
        for i, k in enumerate(input_def):
            inputs[k] = data[i]
        return inputs

    def model_arch(self):
        raise NotImplementedError("Should implement model_arch method!")

    def get_loss(self, ):
        raise NotImplementedError("Should implement get_loss method!")

    def get_pred(self, ):
        raise NotImplementedError("Should implement get_pred method!")
