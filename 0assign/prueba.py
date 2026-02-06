import torch
x = torch.rand(5, 3)
print(x)
print("Pytorch works correctly")
print("Is CUDA available?", torch.cuda.is_available())
if torch.cuda.is_available():
 print("CUDA device:", torch.cuda.get_device_name(0))
else:
 print("running on CPU")
