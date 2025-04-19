import torch
print(torch.cuda.is_available())
#print(torch.cuda.get_device_name(0)) #This is the corrected line.
if torch.cuda.is_available():
    print(torch.cuda.get_device_name(0))