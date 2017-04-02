def main():
    
    par_dict={}
    par_dict['subline'] =3
    par_dict['b'] =3
    par_dict['c'] =2
    par_dict['d'] ='ttr'
    par_dict['e'] ="\/ttr\/adsf"
    Kerma(par_dict)
    
def Kerma(par_dict):
    print ("a=",par_dict['subline'])
    print ("d=",par_dict['e'])
    
if __name__ == '__main__':
    main()
