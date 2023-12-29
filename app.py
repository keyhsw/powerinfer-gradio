import os
os.system('bash install.sh')
os.system('PYTHONUNBUFFERED=1         GRADIO_ALLOW_FLAGGING=never         GRADIO_NUM_PORTS= 1         GRADIO_SERVER_NAME=0.0.0.0         GRADIO_THEME=huggingface         SYSTEM=spaces N_OFFLOAD_ATTN=60 N_OFFLOAD_MLP=60 MODEL_PATH=/root /autodl-tmp/falcon-40b-relu.mlp_q4.powerinfer.gguf IDX_PATH=/root/autodl-tmp/gpu-idx-falcon.gguf python3 app.py')
