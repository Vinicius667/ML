import torch

cuda_available = torch.cuda.is_available()

if cuda_available:
    device = 'cuda'
    print(f'device name: {torch.cuda.get_device_name(0)}')
else:
    device = 'cpu'

print(f'device = {device}')