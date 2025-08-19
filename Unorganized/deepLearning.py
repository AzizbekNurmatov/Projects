import torch.nn as nn
import torch
input_tensor = torch.tensor([[4.3, 6.1, 2.3]])

#linear_layer = nn.Linear(in_features=3, out_features=2)
#output = linear_layer(input_tensor)

#model = nn.Sequential(
#     nn.Linear(3, 15), 
#     nn.Linear(15, 20),
#     nn.Linear(20, 5),  
# )
#output_tensor = model(input_tensor)


probabilities = nn.Softmax(dim=-1)
output_tensor = probabilities(input_tensor)
print(output_tensor)
#-------------------------------------------------------------
# Using one-hot encoding to find entropy loss
import torch
import torch.nn.functional as F
from torch.nn import CrossEntropyLoss

y = [2]
scores = torch.tensor([[0.1, 6.0, -2.0, 3.2]])

# Create a one-hot encoded vector of the label y
one_hot_label = F.one_hot(torch.tensor(y), scores.shape[1])

# Create the cross entropy loss function
criterion = CrossEntropyLoss()

# Calculate the cross entropy loss
loss = criterion(scores.double(), one_hot_label.double())
print(loss)