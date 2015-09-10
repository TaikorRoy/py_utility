# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 10:23:52 2015

@author: Taikor
"""
import os
import time
import codecs

def listdir_enchanced(folder):
    files = os.listdir(folder)
    myfiles = list()

    for file in files:
        myfiles.append(os.path.join(folder, file))
    myfiles = sorted(myfiles)
    return myfiles

def get_content(file, mode="read"):
    if mode == "read":
        with codecs.open(file, "r", encoding="utf8") as f:
            s = f.read()
    if mode == "readlines":
        with codecs.open(file, "r", encoding="utf8") as f:
            s = f.readlines()
    return s

def get_content_list(file):
    with codecs.open(file, "r", encoding="utf8") as f:
        s = f.readlines()
        for i in range(len(s)):
            s[i] = s[i].strip("\n")
    return s
    
def write_content(file, content):
    with codecs.open(file, "w", encoding="utf8") as f:
        f.write(content)
    return 0

class running_timer:
    def __init__(self):
        self.start_time = time.time()
        self.end_time = 0

    def end(self):
        self.end_time = time.time()
        running_time = self.end_time - self.start_time
        return running_time

class RunningTimer:
    def __init__(self):
        self.start_time = time.time()
        self.end_time = 0

    def end(self):
        self.end_time = time.time()
        running_time = self.end_time - self.start_time
        return running_time

