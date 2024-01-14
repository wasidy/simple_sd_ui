Simple Stable Diffusion UI built on hugging's face diffusers.
Requirements:
python 3.10
Installation:
pip install -r requirements.txt (venv recommended)

Usage:
Put your checkpoints to 'models' folder.
You can change default checkpoint's folder, size, steps and guidance scale in config.json
launch 'python simple_sd_ui.py'
Open browser and go to 127.0.0.1:7860
Select checkpoint from dropdown list, type positive and negative prompts and press "Generate"

Docker's usage:
Be sure you have Nvidia Container Toolkit
For WSL users additional info:
https://docs.nvidia.com/cuda/wsl-user-guide/
