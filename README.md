# LineVulReplication

https://github.com/awsm-research/LineVul



06/13/2024 10:23:16 - WARNING - __main__ -   device: cpu, n_gpu: 0
/exports/eddie/scratch/s2291592/anaconda/envs/mypython/lib/python3.9/site-packages/huggingface_hub/file_download.py:1132: FutureWarning: `resume_download` is deprecated and will be removed in version 1.0.0. Downloads always resume when possible. If you want to force a new download, use `force_download=True`.
  warnings.warn(
Traceback (most recent call last):
  File "/exports/eddie/scratch/s2291592/LineVul/linevul/linevul_main.py", line 1253, in <module>
    main()
  File "/exports/eddie/scratch/s2291592/LineVul/linevul/linevul_main.py", line 1233, in main
    model = RobertaForSequenceClassification.from_pretrained(args.model_name_or_path, config=config, ignore_mismatched_sizes=True)    
  File "/exports/eddie/scratch/s2291592/anaconda/envs/mypython/lib/python3.9/site-packages/transformers/modeling_utils.py", line 3626, in from_pretrained
    model = cls(config, *model_args, **model_kwargs)
  File "/exports/eddie/scratch/s2291592/anaconda/envs/mypython/lib/python3.9/site-packages/transformers/models/roberta/modeling_roberta.py", line 1160, in __init__
    self.roberta = RobertaModel(config, add_pooling_layer=False)
  File "/exports/eddie/scratch/s2291592/anaconda/envs/mypython/lib/python3.9/site-packages/transformers/models/roberta/modeling_roberta.py", line 701, in __init__
    self.encoder = RobertaEncoder(config)
  File "/exports/eddie/scratch/s2291592/anaconda/envs/mypython/lib/python3.9/site-packages/transformers/models/roberta/modeling_roberta.py", line 474, in __init__
    self.layer = nn.ModuleList([RobertaLayer(config) for _ in range(config.num_hidden_layers)])
  File "/exports/eddie/scratch/s2291592/anaconda/envs/mypython/lib/python3.9/site-packages/transformers/models/roberta/modeling_roberta.py", line 474, in <listcomp>
    self.layer = nn.ModuleList([RobertaLayer(config) for _ in range(config.num_hidden_layers)])
  File "/exports/eddie/scratch/s2291592/anaconda/envs/mypython/lib/python3.9/site-packages/transformers/models/roberta/modeling_roberta.py", line 388, in __init__
    self.attention = RobertaAttention(config)
  File "/exports/eddie/scratch/s2291592/anaconda/envs/mypython/lib/python3.9/site-packages/transformers/models/roberta/modeling_roberta.py", line 303, in __init__
    self.self = ROBERTA_SELF_ATTENTION_CLASSES[config._attn_implementation](
  File "/exports/eddie/scratch/s2291592/anaconda/envs/mypython/lib/python3.9/site-packages/transformers/models/roberta/modeling_roberta.py", line 158, in __init__
    self.query = nn.Linear(config.hidden_size, self.all_head_size)
  File "/exports/eddie/scratch/s2291592/anaconda/envs/mypython/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 98, in __init__
    self.weight = Parameter(torch.empty((out_features, in_features), **factory_kwargs))
RuntimeError: [enforce fail at alloc_cpu.cpp:117] err == 0. DefaultCPUAllocator: can't allocate memory: you tried to allocate 2359296 bytes. Error code 12 (Cannot allocate memory)

