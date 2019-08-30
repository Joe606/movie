# -*- coding: utf-8 -*-
import json

def after_deal(file):
    f = open(file,'r+',encoding='utf-8')
    content = list()
    for line in f:
        middle = json.loads(line)
        content.append(middle)
    print(len(content))        
    print(content[2].keys())
    print(content[2].items())
    f.close()
    pass

if __name__ == '__main__':
    file_1 = 'movie_message.json'
    file_2 = 'movie_list.json'
    
    #after_deal(file_1)
    after_deal(file_2)
    
    

    
    
    