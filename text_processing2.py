#!/usr/bin/env python
# coding: utf-8

# In[24]:


def digits_to_words(input_string):
    num = ['zero','one','two','three','four','five','six','seven','eight','nine']
    temp = input_string.replace(' ', '')
    digit_string = ''
    
    for i in temp:
        if i.isdigit():
            digit_string = digit_string + num[int(i)] + ' '
            
    return digit_string.rstrip()


# In[94]:


def to_camel_case(underscore_str):
    underscore_str = underscore_str.strip('_')
    if '_' in underscore_str:
        temp = ' '.join(underscore_str.lower().split('_'))
        temp = temp.split()

        for i in range(1 ,len(temp)):
            temp[i] = list(temp[i])
            temp[i][0] = temp[i][0].upper()
            temp[i] = ''.join(temp[i])
        return ''.join(temp)
    else:
        return underscore_str

