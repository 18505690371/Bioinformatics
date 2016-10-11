# -*- coding: cp936 -*-
import numpy as np
#################################����ȫ�ֱȶԺ���Global_align############################
def Global_align(se1,se2,tab):
#####################����2��2ά����ȫ��Ϊ0��Ȼ���ʼ����һ�к͵�һ��#########################
#####################tab1�洢������tab2�洢������Դ#######################################
    tab1=np.zeros((len(se1)+1,len(se2)+1),np.int)
    tab2=np.zeros((len(se1)+1,len(se2)+1),np.string_)
    for i in range(len(se2)+1):
        tab1[0][i],tab2[0][i]=i*(-4),'-'
    for i in range(len(se1)+1):
        tab1[i][0],tab2[i][0]=i*(-4),'|'
#################################����˫����ȫ�ֱȶ�######################################
    for i in range(len(se1)):
        aa1=se1[i]
        for j in range(len(se2)):
            aa2=se2[j]
            score1=int(tab[aa1][aa2])
            tab1[i+1][j+1]=max(tab1[i][j]+score1,tab1[i+1][j]-4,tab1[i][j+1]-4)            
            if tab1[i+1][j+1]==tab1[i][j]+score1:
                tab2[i+1][j+1]='*'
            elif tab1[i+1][j+1]==tab1[i+1][j]-4:
                tab2[i+1][j+1]='-'
            else:
                tab2[i+1][j+1]='|'
#################################����·������######################################
    seq1,seq2=[],[]
    i,j=len(se1),len(se2)
    Score1=tab1[i][j]   #ȫ�ֱȶԵ��ܷ�
    while i+j>0:
        if tab2[i][j]=='*':
            i,j=i-1,j-1
            seq1.append(se1[i])
            seq2.append(se2[j])
        elif tab2[i][j]=='|':
            i=i-1
            seq1.append(se1[i])
            seq2.append('*')
        elif tab2[i][j]=='-':
            j=j-1
            seq1.append('*')
            seq2.append(se2[j])
    seq1.reverse()
    seq2.reverse()
    seq1,seq2=''.join(seq1),''.join(seq2)
    return seq1,seq2,tab1,tab2  #���ص�4������������1������2����ֱ�·����
#################################����ȫ�ֱȶԺ���Global_align############################
def Local_align(se1,se2,tab):
#####################����2��2ά����ȫ��Ϊ0��Ȼ���ʼ����һ�к͵�һ��#########################
#####################tab1�洢������tab2�洢������Դ#######################################
    tab1=np.zeros((len(se1)+1,len(se2)+1),np.int)
    tab2=np.zeros((len(se1)+1,len(se2)+1),np.string_)
    for i in range(len(se2)+1):
        tab2[0][i]='-'
    for i in range(len(se1)+1):
        tab2[i][0]='|'
#################################����˫���оֲ��ȶ�######################################
    for i in range(len(se1)):
        aa1=se1[i]
        for j in range(len(se2)):
            aa2=se2[j]
            score1=int(tab[aa1][aa2])
            tab1[i+1][j+1]=max(tab1[i][j]+score1,tab1[i+1][j]-4,tab1[i][j+1]-4,0)
            if tab1[i+1][j+1]==0:
                tab2[i+1][j+1]='X'
            elif tab1[i+1][j+1]==tab1[i][j]+score1:
                tab2[i+1][j+1]='*'
            elif tab1[i+1][j+1]==tab1[i+1][j]-4:
                tab2[i+1][j+1]='-'
            else:
                tab2[i+1][j+1]='|'
#################################����·������###########################################
    seq1,seq2=[],[]
    a=np.argmax(tab1)
    i,j=a/(len(se2)+1),a%(len(se2)+1)
    Score1=np.max(tab1)   #�ֲ��ȶԵ��ܷ�
    while tab1[i][j]>0:
        if tab2[i][j]=='*':
            i,j=i-1,j-1
            seq1.append(se1[i])
            seq2.append(se2[j])
        elif tab2[i][j]=='|':
            i=i-1
            seq1.append(se1[i])
            seq2.append('*')
        elif tab2[i][j]=='-':
            j=j-1
            seq1.append('*')
            seq2.append(se2[j])
    seq1.reverse()
    seq2.reverse()
    seq1,seq2=''.join(seq1),''.join(seq2)
    return seq1,seq2,tab1,tab2  #���ص�4������������1������2����ֱ�·����'''
