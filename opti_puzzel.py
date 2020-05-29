import time
'''170387F M.W.G.V.Melaka '''
'''a class that holds every detail about a node'''
class node:

    def __init__(self,g_score,data,g_m,move,parent,character):

        self.g_score=g_score
        self.data=data
        self.g_m=g_m
        self.move=move
        self.h_score=self.h_value()
        self.f_score=self.g_score+self.h_score
        self.parent=parent
        self.character=character
    '''functions that calculates the h_score of the node'''

    '''this function calculates h_score using misplaced tiles heuristics'''
##    def h_value(self):
##        h_s=0
##        for i in range(0,len(self.data)):
##            for j in range(0,len(self.g_m)):
##                if self.data[i][j]=='-':
##                    continue
##                else:
##                    if self.data[i][j]!=self.g_m[i][j]:
##                        h_s = h_s+1
##        return h_s
    '''this function calculates h_score using manhattan distance heuristics'''
    def h_value(self):
        s_m=self.data
        g_m=self.g_m
        h_s=0
        for i in range(0,len(s_m)):
            for j in range(0,len(s_m)):
                item=s_m[i][j]
                if item=='-':
                    continue
                else:
                    for x in range(0,len(g_m)):
                        for y in range(0,len(g_m)):
                            if item==g_m[x][y]:
                                h_s=h_s+(abs(i-x)+abs(j-y))
               
        return h_s

    '''function to update the g_score of the node'''
    def update(self,g_s):
        self.g_score=g_s
        self.f_score=self.g_score+self.h_score

'''function that returns all possible moves(nodes) of a node'''
def get_moves (n):
    s_m=n.data
    g_m=n.g_m
    g_score=n.g_score
    moves=[]
    for i in range(0,len(s_m)):
        for j in range(0,len(g_m)):
            if s_m[i][j]=='-':
                if i<(len(s_m)-1):
                    s_m[i][j]=s_m[i+1][j]
                    s_m[i+1][j]='-'
                    d1=[]
                    char=s_m[i][j]
                    for x in range(0,len(s_m)):
                        r=[]
                        for y in range(0,len(s_m)):
                            v=s_m[x][y]
                            r.append(v)
                        d1.append(r)
                    child=node(g_score+1,d1,g_m,'up',n,char)
                    moves.append(child)
                    s_m[i+1][j]=s_m[i][j]
                    s_m[i][j]='-'
                if i>0:
                    s_m[i][j]=s_m[i-1][j]
                    s_m[i-1][j]='-'
                    d1=[]
                    char=s_m[i][j]
                    for x in range(0,len(s_m)):
                        r=[]
                        for y in range(0,len(s_m)):
                            v=s_m[x][y]
                            r.append(v)
                        d1.append(r)
                    child=node(g_score+1,d1,g_m,'down',n,char)
                    moves.append(child)
                    s_m[i-1][j]=s_m[i][j]
                    s_m[i][j]='-'
                if j<len(s_m)-1:
                    s_m[i][j]=s_m[i][j+1]
                    s_m[i][j+1]='-'
                    d1=[]
                    char=s_m[i][j]
                    for x in range(0,len(s_m)):
                        r=[]
                        for y in range(0,len(s_m)):
                            v=s_m[x][y]
                            r.append(v)
                        d1.append(r)
                    child=node(g_score+1,d1,g_m,'left',n,char)
                    moves.append(child)
                    s_m[i][j+1]=s_m[i][j]
                    s_m[i][j]='-'
                if j>0:
                    s_m[i][j]=s_m[i][j-1]
                    s_m[i][j-1]='-'
                    d1=[]
                    char=s_m[i][j]
                    for x in range(0,len(s_m)):
                        r=[]
                        for y in range(0,len(s_m)):
                            v=s_m[x][y]
                            r.append(v)
                        d1.append(r)
                    child=node(g_score+1,d1,g_m,'right',n,char)
                    moves.append(child)
                    s_m[i][j-1]=s_m[i][j]
                    s_m[i][j]='-'

                    
    
    return moves


'''main function'''
if __name__ == "__main__":
    start=input("start configuration file :")
    goal=input("goal configuration file :")

    f=open(start,'r')
    s_d=f.read().split('\n')
    f.close()

    s_matrix=[]
    for each in s_d:
        if len(each)>1:
            s_matrix.append(each.split('\t'))

    f=open(goal,'r')
    g_d=f.read().split('\n')
    f.close()

    g_matrix=[]
    for each in g_d:
        if len(each)>1:
            g_matrix.append(each.split('\t'))


    open_list=[]
    closed_list=[]
    closed_data=[]
    parent=node(0,s_matrix,g_matrix,'parent',None,None)
    open_list.append(parent)
    configurations=0
    '''A* algorithm'''
    start_time=time.time()
    while len(open_list) != 0:
        configurations=configurations+1
        f_values=[]
        h_values=[]
        for each in open_list:
            f_values.append(each.f_score)
            h_values.append(each.h_score)
        n=min(f_values)
        r=min(h_values)
        '''breaking condition'''
        if r==0:
            end_time=time.time()
            t=end_time-start_time
            result=open_list[h_values.index(0)]
            if result.move=='parent':
                f=open("results.txt",'w')
                f.write("no moves")
                f.close()
                
            else:
                top=result.parent
                m=[]
                m.append((result.character,result.move))
                '''getting moves up to the solution'''
                while top.move != 'parent':
                    result=top
                    top=result.parent
                    m.append([result.character,result.move])
                answer=''
                for i in range(len(m)-1,-1,-1):
                    if i==0:
                        answer=answer+'('+str(m[i][0])+","+str(m[i][1])+")"
                    else:
                        answer=answer+'('+str(m[i][0])+","+str(m[i][1])+"),"
                f=open("results.txt",'w')
                f.write(answer)
                f.close()
                
            break
        else:
            to_add=[]
            '''get index of the lowest f score'''
            index_of_parent=f_values.index(n)
            '''get the relevent object remove it from open set'''
            parent=open_list.pop(index_of_parent)
            '''get children objects'''
            children= get_moves(parent)
            '''add the parent to the closed set'''
            closed_list.append(parent)
            '''analysing children nodes'''
            
            for each in children:
                '''checking weather child is in closed set'''
                for visited in closed_list:
                    if visited.data==each.data:
                        break
                    else:
                        continue
                else:
                    '''checking weather child in open set'''
                    for not_visited in open_list:
                        '''match found in open set'''
                        if not_visited.data==each.data:
                            child_g=each.g_score
                            open_g=not_visited.g_score
                            '''comparing two g_scores (cost) of the two objects'''
                            if child_g<open_g:
                                '''update cost of the node in open list with new
                                    cost if the cost of the child is lower'''
                                not_visited.update(child_g)
                                break
                            else:
                                break
                    else:
                        '''if not in open set add it to the list that holds nodes that has to
                    be added to the open set in next iteration''' 
                        to_add.append(each)
            '''adding new children to the open set'''           
            for new in to_add:
                open_list.append(new)

    
                        
                            

                    

                            

            
                
            


                        
                            
                        


        
                        
                            

                    

                            

            
                
            

