#!/usr/bin/env python3
import sys

files = []
options = ""
if len(sys.argv) > 2:
    string = sys.argv[1].lower()
    if string[0] == "-":
        options = string
    else:
        files.append(sys.argv[1])
    for index in range(2, len(sys.argv)):
        files.append(sys.argv[index])
else:
    files.append(sys.argv[1])


def main():
    totals = {"l": 0, "c": 0, "w": 0, "m": 0}
    for file in files:
        file_totals = sub(file)
        for key in file_totals:
            totals[key] += file_totals[key]
    res = ""
    # totals["f"] = "Totals"
    for key in totals:
        if totals[key] > 0:
            res += f" {totals[key]}"
    print(res, "Totals")


def byte_count(file):
    # -c
    text = open(file, "rb").read()
    return len(text)


def line_count(file):
    # -l
    lines = open(file, "r")
    line_count = 0
    for _ in lines:
        line_count += 1
    return line_count


def word_count(file):
    # -w
    text = open(file, "r").read()
    words = text.split()
    word_count = 0
    word_count += len(words)
    return word_count


def char_count(file):
    #  -m
    lines = open(file, "rb")
    char_count = 0
    for word in lines:
        char_count += len(word.decode())
    return char_count


def sub(file):
    res = {}
    if "l" in options:
        res["l"] = line_count(file)
    if "w" in options:
        res["w"] = word_count(file)
    if "c" in options:
        res["c"] = byte_count(file)
    if "m" in options:
        res["m"] = char_count(file)
    if options == "":
        res["l"], res["w"], res["c"] = (
            line_count(file),
            word_count(file),
            byte_count(file),
        )
    totals = ""
    for key in res:
        totals += f" {res[key]}"
    print(totals, file)
    return res


main()
