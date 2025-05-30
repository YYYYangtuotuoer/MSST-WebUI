import torch.nn as nn


class BiGRU(nn.Module):
	def __init__(self, input_features, hidden_features, num_layers):
		super(BiGRU, self).__init__()
		self.gru = nn.GRU(input_features, hidden_features, num_layers=num_layers, batch_first=True, bidirectional=True)

	def forward(self, x):
		return self.gru(x)[0]
