#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json 

# Opening the json file 
with open ('layer1.json' , 'r') as file:
    layer_data = json.load(file)


# In[1]:


for l in sub_layer:
    print(l.keys())


# In[498]:


# Looking at first value of the loaded json file 
stop_words = [] 
instr_list = []
for i in range(0 , len(sub_layer)):
  #  print(sub_layer[i])
    list_of_ingr = sub_layer[i]['ingredients']
    stop_words.append(list_of_ingr[-1]['text'])
    for elem in list_of_ingr:
        instr_list.append(elem['text'])

    
stop_words


# In[17]:


get_ipython().system('pip install tqdm')

from tqdm import tqdm


# In[18]:


def get_list_of_strings(key , json_file):
    stop_words = []
    key_list = []
    
    # Iterating to find out the stop words and adding all elements into a list 
    for i in range(0 , len(json_file)):
        list_of_key = json_file[i][key]
        
        # Getting the stop words 
        stop_words.append((list_of_key[-1]['text']))
        for elem in list_of_key:
            key_list.append(elem['text'])
            
    
    # Now we're adding a '#' character at every end of ingredients/instructions last value 
    updated_key_list = [] 
    for word in key_list:
        if word in stop_words:
            word += '#'
            updated_key_list.append(word)
            print(word)
            print('\n------\n')
        else:
            word +='/t'
            updated_key_list.append(word)
            print(word)
            print('\n------\n')
            
    
    # Converting the whole list of text into a big giant string
    big_string = ' '.join([str(word) for word in tqdm(updated_key_list)])
    #print(big_string)
    
    # Now returning the list of text for each ingredient/instructions (individual list of ingredients/instructions )
    indi_list = big_string.split('#')
    
    # We just really want the list 
    #print(indi_list)

    return indi_list


# In[ ]:


# Using our beautiful function to converting our instruction/ingredients to our desired list of strings
#instruction_list = get_list_of_strings(key = 'instructions' , json_file = layer_data)
ingr_list = get_list_of_strings(key = 'ingredients' , json_file = layer_data)


# In[ ]:


len(instruction_list) , len(ingredient_list)


# Perfect now we got the json file the next step would be is to decode them and store them in a dataframe for us. 
# 
# Why? 
# 
# Well so we can download the csv file and use it for loading the images from a directory! 
# 
# The attributes we care about: 
# - ingredients 
# - partition 
# - title
# - id 
# - instruction

# In[499]:


big_str = ''.join([str(word) for word in up_list])

p = big_str.split('#' , len(sub_layer))
len(p)

up_list = []
for word in instr_list:
    if word in stop_words:
        word += '#' 
        up_list.append(word)
    else:
        word += '/t'
        up_list.append(word)
        
up_list


# In[489]:


big_str = ''.join([str(word) for word in up_list])
big_str


# In[490]:


p = big_str.split('#' , len(sub_layer))
len(p)


# In[452]:


new1 = []
for word in up_list: 
    if word.endswith('#'):
        word


# In[3]:


# Using subset of the json file for experimentation 
sub_layer = layer_data[:10]


# In[266]:


for attr in sub_layer[:3]:
    print(f"ID: {attr['id']}\n")
    print(f"Ingredients: {attr['ingredients']}\n")
    print(f"Partition: {attr['partition']}\n")
    print('\n----Next Food----\n')

