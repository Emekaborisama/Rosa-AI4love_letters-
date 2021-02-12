import markovify as mk
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize as sent_tok


with open('./data/letter.txt') as f:
  data =f.readlines()


generator_a = mk.Text(data)
sonnets_model = mk.NewlineText(data, state_size=2)
modeljson = generator_a.to_json()
import json
# Writing a JSON file
with open('./model/model1.json', 'w') as f:
    json.dump(modeljson, f)

modeljson = sonnets_model.to_json()
import json
# Writing a JSON file
with open('./model/model2.json', 'w') as f:
    json.dump(modeljson, f)