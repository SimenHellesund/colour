#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" A simple module for printing coloured strings  in Python"""

fg_map = {
    "k": "30",
    "r": "91",
    "g": "92",
    "y": "93",
    "b": "94",
    "p": "95",
    "c": "96",
    "w": "97"}

bg_map = {
    "k": "",
    "r": "101",
    "g": "102",
    "y": "103",
    "b": "104",
    "p": "105",
    "c": "106",
    "w": "107"}

colour_map = {"black": "k", "bck": "k", "bla": "k", "bk": "k",
              "red": "r", "rd": "r",
              "green": "g", "grn": "g", "gre": "g", "gn": "g",
              "yellow": "y", "ylo": "y", "yel": "y", "yl": "y", "yo": "y",
              "blue": "b", "blu": "b", "bu": "b", 
              "purple": "p", "prp": "p", "ppl": "p", "pur": "p", "pl": "p", 
              "cyan": "c", "cyn": "c", "can": "c", "cn": "c", "cy": "c",
              "white": "w", "wht": "w", "whi": "w", "wte": "w", "wh": "w", "wi": "w", "wt": "w"}


def colour(string, fg="k", bg="r", bold="0"):
    """ Decorates the input string with text and background colour 

    keyword arguments:
    (str) fg -- text colour
    (str) bg -- background colour
    (str) bold -- bold text
    """
    string = str(string)

    if fg in fg_map.keys():
        pass
    elif fg in colour_map.keys():
        fg = colour_map(fg)
    else:
        raise ValueError("invalid foreground value fg")
    
    if bg in bg_map.keys():
        pass
    elif bg in colour_map.keys():
        bg = colour_map(bg)
    else:
        raise ValueError("invalid background value bg")
    
    if type(bold) == "str" and bold == "1" or bold == "0":
        pass
    elif type(bold) == bool:
        bold = str(int(bold))
    elif type(bold) == int:
        bold = str(bold)
       
    outstr = "\33[{};{};{}m".format(bold, fg_map[fg], bg_map[bg]) + string + "\33[m"
    return outstr

if __name__ == '__main__':
    pass




    
