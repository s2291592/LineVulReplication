# LineVulReplication

https://github.com/awsm-research/LineVul



>>> from transformers import RobertaForSequenceClassification
>>> model = RobertaForSequenceClassification.from_pretrained('distilroberta-base')
config.json: 100%|██████████████████████████████| 480/480 [00:00<00:00, 116kB/s]
model.safetensors: 100%|██████████████████████| 331M/331M [00:00<00:00, 434MB/s]
Some weights of RobertaForSequenceClassification were not initialized from the model checkpoint at distilroberta-base and are newly initialized: ['classifier.dense.bias', 'classifier.dense.weight', 'classifier.out_proj.bias', 'classifier.out_proj.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.

