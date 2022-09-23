import torch
import torch.nn as nn
import transformers
from config import modelpath

DEVICE = "cpu"
BERT_PATH = "bert-base-uncased"

class BERTBaseUncased(nn.Module):
    def __init__(self):
        super(BERTBaseUncased, self).__init__()
        self.bert = transformers.BertModel.from_pretrained(BERT_PATH)
        self.bert_drop = nn.Dropout(0.3)
        self.out = nn.Linear(768, 1)

    def forward(self, ids, mask, token_type_ids):
        _, o2 = self.bert(ids, attention_mask=mask,
                          token_type_ids=token_type_ids, return_dict=False)
        bo = self.bert_drop(o2)
        output = self.out(bo)
        return output

MODEL = BERTBaseUncased()
    
TOKENIZER = transformers.BertTokenizer.from_pretrained(
    BERT_PATH, do_lower_case=True)

def sentence_prediction(sentence):
    tokenizer = TOKENIZER #bertfasttokenizer
    max_len = 64 #change to 212
    review = str(sentence)
    review = " ".join(review.split())

    inputs = tokenizer.encode_plus(
        review, None, add_special_tokens=True, max_length=max_len
    )

    ids = inputs["input_ids"] #getting 3 input for bert
    mask = inputs["attention_mask"]
    token_type_ids = inputs["token_type_ids"]

    padding_length = max_len - len(ids)
    ids = ids + ([0] * padding_length)
    mask = mask + ([0] * padding_length)
    token_type_ids = token_type_ids + ([0] * padding_length) #adding padding

    ids = torch.tensor(ids, dtype=torch.long).unsqueeze(0) #adding to tensors
    mask = torch.tensor(mask, dtype=torch.long).unsqueeze(0)
    token_type_ids = torch.tensor(
        token_type_ids, dtype=torch.long).unsqueeze(0)

    ids = ids.to(DEVICE, dtype=torch.long)
    token_type_ids = token_type_ids.to(DEVICE, dtype=torch.long)
    mask = mask.to(DEVICE, dtype=torch.long)

    outputs = MODEL(ids=ids, mask=mask, token_type_ids=token_type_ids) #eval command
    MODEL.load_state_dict(torch.load(modelpath,map_location=torch.device(DEVICE)))
    MODEL.to(DEVICE)
    MODEL.eval()
    print("\nBERT MODEL LOADDED - 1\n")
    
    outputs = torch.sigmoid(outputs).cpu().detach().numpy()
    return outputs[0][0]