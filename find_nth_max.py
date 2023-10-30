# FUNCTION FOR DEFINING THE nth MAX NUMBER IN ALIST
def max_of_number(my_list,n):
    m=[]
    #DEFINIG EMPTY LIST
    if(len(set(my_list))<n):
        return ValueError("error")
    #CHECKING FOR THE LENGTH ERROR 

    #GETTING THE MAXIMUM NUMBER IN LIST.
    for i in range(n):
        lar=0
        for j in range(len(my_list)):
            #CHECKING THE NUMBER IS ALREADY PRESENT OR NOT
            if my_list[j]>lar and my_list[j] not in m :
                lar=my_list[j]
        m.append(lar)            
              
    return lar            
    #RETURNING THE NUMBER.                        