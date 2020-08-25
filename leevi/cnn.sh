#!/bin/bash
#SBATCH --gres=gpu:1
#SBATCH --time=04:00:00
#SBATCH --mem-per-cpu=5G

module load anaconda/2020-02-tf2
python cnn_keras.py
