# LineVulReplication

https://github.com/awsm-research/LineVul


from transformers import RobertaForSequenceClassification

def load_model():
    model = RobertaForSequenceClassification.from_pretrained('roberta-base')
    return model

if __name__ == "__main__":
    load_model()


