import numpy as np
import os
# importing the required libraries and modules  
from tkinter import *
import tkinter as tk           # importing all methods, classes and widgets from the tkinter library  
from PIL import ImageTk, Image  # importing the ImageTk and Image modules from the PIL library  
import calendar                 # importing the calendar module  
from datetime import date       # importing the date module from the datetime library  
from tkcalendar import *        # importing the tkcalendar module
import pandas as pd
import csv 

weird_literal = 'þ'
weird_name = '\N{LATIN SMALL LETTER THORN}'
weird_char = '\xfe'  # hex representation
weird_literal == weird_name == weird_char  # True
