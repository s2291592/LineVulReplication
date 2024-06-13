# LineVulReplication

https://github.com/awsm-research/LineVul


from transformers import RobertaForSequenceClassification

def load_model():
    model = RobertaForSequenceClassification.from_pretrained('roberta-base')
    return model

if __name__ == "__main__":
    load_model()

config.json: 100%|██████████████████████████████| 481/481 [00:00<00:00, 119kB/s]
model.safetensors: 100%|██████████████████████| 499M/499M [00:01<00:00, 317MB/s]
Traceback (most recent call last):
  File "/exports/eddie/scratch/s2291592/load_model.py", line 9, in <module>
    load_model()
  File "/exports/eddie/scratch/s2291592/load_model.py", line 4, in load_model
    model = RobertaForSequenceClassification.from_pretrained('roberta-base') 
  File "/exports/eddie/scratch/s2291592/anaconda/envs/mypython/lib/python3.9/site-packages/transformers/modeling_utils.py", line 3531, in from_pretrained
    with safe_open(resolved_archive_file, framework="pt") as f:
RuntimeError: unable to mmap 498818054 bytes from file </home/s2291592/.cache/huggingface/hub/models--roberta-base/snapshots/e2da8e2f811d1448a5b465c236feacd80ffbac7b/model.safetensors>: Cannot allocate memory (12)
