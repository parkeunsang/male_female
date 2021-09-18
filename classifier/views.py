from django.shortcuts import render
from django.http import JsonResponse
from tensorflow import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences
import os
from konlpy.tag import Okt
import pickle
import time
# Create your views here.
model = keras.models.load_model("./data/lstm_model.h5")
with open('./data/tokenizer.pickle', 'rb') as f:
    tokenizer = pickle.load(f)

def index(request):
    return render(request, 'classifier/index.html')


def clf(request, sentence):
    ratio = sentences_to_seq(sentence, tokenizer)
    if ratio == -1:
        return JsonResponse({
            'value': -1
        })
    else:
        ratio = ratio[0][0]
    ratio *= 100
    ratio = str(round(ratio, 1))
    return JsonResponse({
        'value': ratio
    })
    

def sentences_to_seq(sentences, tokenizer):
    if type(sentences) == str:
        sentences = [sentences]
    
    morphs_list = to_morph(sentences)
    sequences = tokenizer.texts_to_sequences(morphs_list)
    if not sequences[0]:  # 빈 값이면
        return -1
    # empty = [idx for idx, x in enumerate(sequences) if not x]
    X_test = pad_sequences(sequences, padding='post', maxlen=15)
    pred = model.predict(X_test)
    # for i in empty:
    #     pred[i] = [None]
    return pred


def to_morph(sentences):
    okt = Okt()
    morphs = []
    for comment in sentences:
        m = okt.pos(comment)
        m = [x[0] for x in m if x not in  ['\n', '.', ','] and x[1] not in ['Josa', 'Suffix']]
        morphs.append(m)
    return morphs
