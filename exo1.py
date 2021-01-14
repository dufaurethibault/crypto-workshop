#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## test
## File description:
## test
##

import hashlib

i = 0;
file = open('file.txt', 'r');
tab = file.read()
toto = tab.split("\n")
for i in toto:
    m = hashlib.sha256(i.encode('utf-8')).hexdigest()
    if (m == "3ddcd95d2bff8e97d3ad817f718ae207b98c7f2c84c5519f89cd15d7f8ee1c3b"):
        print(i)