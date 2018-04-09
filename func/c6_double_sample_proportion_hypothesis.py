#Author : JUNHO LEE
#Required : n1p1>=5, n2p2>=5 and also, n1(1-p1)>=5, n2(1-p2)>=5
from matplotlib import pyplot as plt
import numpy as np
import math
import sys,os
from sympy import exp,sqrt,pi,Integral
sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/func/")
from c1_basic_statistic import *



def bothSide_hypothesis(proportion1=0.1,event_num1=100,proportion2=0.5,event_num2=100):
    # H0 : P1 = P2
    # H1 : P1 != P2
    pbar = (event_num1*proportion1+event_num2*proportion2)/(event_num1+event_num2)
    Zc = (proportion1-proportion2) / math.sqrt(pbar*(1-pbar)/event_num1 + pbar*(1-pbar)/event_num2)
    return Zc



def main():
#    twoSigma_region = bothSide_hypothesis(proportion1=0.031, event_num1 = 7000, proportion2=0.0175, event_num2 = 22000)
    twoSigma_region = bothSide_hypothesis(proportion1=0.0315, event_num1 = 7000, proportion2=0.022, event_num2 = 10000)
    print(twoSigma_region)    

if __name__ == "__main__":
    main()

