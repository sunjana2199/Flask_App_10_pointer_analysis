import numpy as np
import pandas as pd
from flask import Flask, render_template,request
import pickle



model = pickle.load(open('model.pkl', 'rb'));

print(model.predict([[10.00,10.00 ,10.00,10.00, 10.00 ,10.00 ,10.00 ,10.00 ,10.00 ,10.00]]));

