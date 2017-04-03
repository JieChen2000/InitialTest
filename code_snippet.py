def main():
    #    global n,g_name,subline,xlmin,xlmax,process_stk
    n=3  #automatically in global
    g_name ='ttttt'
    process_stk = 1 
    if process_stk == 1: 
        stk()
    
    #generating a dictionary
    #method 1 
    #par_dict={}
    #par_dict['subline'] =3
    #par_dict['b'] =3
    #par_dict['c'] =2
    
    par_dict = {'Name':'Zara', 'Age': 7}
    par_dict['subline'] =3 
    par_dict['Age'] = 8; # update existing entry
    par_dict['School'] = "DPS School"; # Add new entry
    par_dict['b'] =3
    par_dict['c'] =2
    par_dict['d'] ='ttr'
    par_dict['e'] ="\/ttr\/adsf"
    #print(str(par_dict))
    par_stk_dict ={'nsw':16,'cmbmst':'tt.mjs'}
    par_dict.update(par_stk_dict)  #Append new dictionary to exisiting dict
    #print(str(par_dict))
    Kerma(par_dict)
    del par_dict
    
def stk():
    print('here in stack')
#    g_name='3t'  #assigment make it local
#    print (g_name)   # treat as local variable
    global g_name
    g_name = '4t'
    print(g_name)
def Kerma(par_dict):
    print (g_name)  #treat as global
    print ("Name=",par_dict['Name'])
    print ("subline=",par_dict['subline'])
    print ("d=",par_dict['e'])
    par_dict['e'] = 'updated'
    print ("d=",par_dict['e'])
    print ("school=",par_dict['School'])
    print ("nsw=",par_dict['nsw'])
if __name__ == '__main__':
    main()
