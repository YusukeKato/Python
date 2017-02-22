# 2016.4.23
# Python
# TryToException
# エラーの名前を覚えよう！！

# !/usr/bin/env python

import sys

for fn in sys.argv[1:]:
    try:# I want do
        f = open(fn)
    except FileNotFoundError:# muri
        print("{}というファイルは存在しない".format(fn))
    else:
        try:# FilelengthPrint
            print(fn,len(f.read()))
        finally:# FileClose
            f.close()
