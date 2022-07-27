import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy as np
import tflearn
import tensorflow as tf
import random
import json 
import pickle
import sys



with open("Chat_Bot\\intents.json") as  file:
    data  = json.load(file)

with open("Chat_Bot\\Model_Data\\data.pickle", "rb") as f:
    words, labels, training, output = pickle.load(f)

tf.compat.v1.reset_default_graph()
# tf.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8,)
net = tflearn.fully_connected(net, 8,)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)



model.load("Chat_Bot\\Model_Data\\model.tflearn")

# model.fit(training,output, n_epoch=2000, batch_size=5, show_metric=True)
# model.save("Python-Learn/Projects/Ai learn/model.tflearn")
    
    
def bag_of_words(s, words):
    bag = [0] * len(words)
    
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]
    
    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
    return np.array(bag)

def tags(message):
    inp = message
    results = model.predict([bag_of_words(inp, words)])
    
    results_index = np.argmax(results)
    tag = labels[results_index]
    return tag

def chat(message):
    print("Bot Is Active")
    while True:
        inp = message
        if inp.lower() == "quit":
            break
        results = model.predict([bag_of_words(inp, words)])
        
        results_index = np.argmax(results)
        tag = labels[results_index]

        
        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']

        return random.choice(responses)
    