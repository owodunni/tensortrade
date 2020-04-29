# Copyright 2019 The TensorTrade Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License

import os
import pandas as pd
import datetime
import tensorflow as tf

from tensortrade.environments.render import BaseRenderer
from tensortrade.environments.utils.helpers import create_auto_file_name, check_path

DEFAULT_LOG_FORMAT = '[%(asctime)-15s] %(message)s'
DEFAULT_TIMESTAMP_FORMAT = '%Y-%m-%d %H:%M:%S'


class TensorBoardLogger(BaseRenderer):
    def __init__(self, log_path: str = "logs"):

        current_time = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        train_log_dir = f"{log_path}/gradient_tape/{current_time}/train"
        test_log_dir = f"{log_path}/gradient_tape/{current_time}/test"
        self.train_summary_writer = tf.summary.create_file_writer(train_log_dir)
        self.test_summary_writer = tf.summary.create_file_writer(test_log_dir)

    def render(self, episode: int = None, max_episodes: int = None,
               step: int = None, max_steps: int = None,
               price_history: pd.DataFrame = None, net_worth: pd.Series = None,
               performance: pd.DataFrame = None, trades: 'OrderedDict' = None
               ):
        with self.test_summary_writer.as_default():
            tf.summary.scalar('net_worth', net_worth[step], step=step)
