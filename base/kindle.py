#!/usr/bin/env/ python

# -*- coding: utf-8 -*-

import sys,os,codecs
from collections import defaultdict

fileName = 'kindle.txt';

def procee_clipping(clipping):

    clipping_lines = clipping.split('\r\n');

    if not len(clipping_lines) >= 4:
        return ('','')
    title = clipping_lines[0].split('(')[0];

    content = "\r\n".join(clipping_lines[3:])

    print(title)
    return title,content

def process_file():

    fh = codecs.open(fileName,'r','utf-8');
    text = fh.read();
    clippings = text.split('\r\n=======\r\n')

    ebooks = defaultdict(list);

    for c in clippings:
        title,content = procee_clipping(c);
        if title and content:
            ebooks[title].append(content);

    if not os.path.isdir('clipings'):
        os.mkdir('clippings')

    for ebook in ebooks.keys():

        ebook = ebook.replace('/','')
        ebook = ebook.replace('\\','')

        fh = codecs.open('clippings/'+ebook+'.txt','w','utf-8');

        for content in ebook[ebooks]:
            fh.write(content+'\n\n');

        fh.close()

if __name__ == '__main__':

    process_file();