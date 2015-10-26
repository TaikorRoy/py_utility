# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 10:23:52 2015

@author: Taikor
"""
import os
import time
import codecs
import json


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
            for i in range(len(s)):
                s[i] = s[i].strip("\n")
                s[i] = s[i].strip("\r")
                s[i] = s[i].strip(" ")
                s[i] = s[i].strip("\t")
    return s


def get_content_list(file):
    with codecs.open(file, "r", encoding="utf8") as f:
        s = f.readlines()
        for i in range(len(s)):
            s[i] = s[i].strip("\n")
            s[i] = s[i].strip("\r")
            s[i] = s[i].strip(" ")
            s[i] = s[i].strip("\t")
    return s


def to_string(_list, _sep):
    my_str = _sep.join(_list)
    return my_str


def write_content(file, content):
    with codecs.open(file, "w", encoding="utf8") as f:
        f.write(content)
    return 0


def json_loads(file):
    json_str = get_content(file)
    json_obj = json.loads(json_str)
    return json_obj


def json_dumps(file, json_obj):
    json_str = json.dumps(json_obj, ensure_ascii=False)
    write_content(file, json_str)
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

if __name__ == "__main__":
    file_path = r"C:\Users\Taikor\Desktop\test.txt"
    result = get_content_list(file_path)
    print(type(result[0]))
    print(result)