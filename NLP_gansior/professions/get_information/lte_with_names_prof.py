""" 
This servis module for work names of professionals
results - names dieferent of forms names and first:forma and two vorbs first forma and two words

"""
import pymorphy2
import pickle

morph = pymorphy2.MorphAnalyzer()

def creater_words_forms_voc(name_i_f, name_f_r):
    f_r = open(name_f_r, 'w')
    arr_name = {}
    with open(name_i_f, 'r') as i_f:
        for line in i_f:
            s_l = line.strip().lower().replace('(', '').replace(')', '').replace('-', ' ').replace(',', ' ').split()
            if s_l[0] not in arr_name:
                arr_name[s_l[0]] = {}
            else:
                
    for nn in arr_name:
        f_r.write(nn + '\n')
    
    
if __name__ == "__main__":
    n_f_i = '/home/al/Projects_My/NLP-russian-language/NLP_gansior/professions/get_information/list_prof_slug_com.csv'
    n_f_r = '/home/al/Projects_My/NLP-russian-language/NLP_gansior/professions/get_information/first_names_prof.csv'
    creater_words_forms_voc(n_f_i, n_f_r)