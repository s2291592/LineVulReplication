# LineVulReplication

https://github.com/awsm-research/LineVul


from transformers import RobertaForSequenceClassification

def load_model():
    model = RobertaForSequenceClassification.from_pretrained('roberta-base')
    return model

if __name__ == "__main__":
    load_model()

cd linevul
python linevul_main.py \
  --model_name=12heads_linevul_model.bin \
  --output_dir=./saved_models \
  --model_type=roberta \
  --tokenizer_name=microsoft/codebert-base \
  --model_name_or_path=microsoft/codebert-base \
  --do_test \
  --train_data_file=../data/big-vul_dataset/train.csv \
  --eval_data_file=../data/big-vul_dataset/val.csv \
  --test_data_file=../data/big-vul_dataset/test.csv \
  --block_size 512 \
  --eval_batch_size 512 \
  --num_train_epochs 1

