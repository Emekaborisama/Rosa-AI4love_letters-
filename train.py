import markovify as mk
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize as sent_tok


with open('letter.txt') as f:
  data =f.readlines()


generator_a = mk.Text(data)
sonnets_model = mk.NewlineText(data, state_size=2)
modeljson = generator_a.to_json()
import json
# Writing a JSON file
with open('model1.json', 'w') as f:
    json.dump(modeljson, f)

modeljson = sonnets_model.to_json()
import json
# Writing a JSON file
with open('model2.json', 'w') as f:
    json.dump(modeljson, f)