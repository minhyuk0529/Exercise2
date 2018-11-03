import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import scipy.optimize as s_op

def makeDictionary(molecule):
    if molecule == "H2O":
        files = os.listdir(path="C:\\Users\\MinHyukChoi\\Desktop\\Programming\\Part II_Chemistry\\Exercise_2\\H2Ooutfiles")
        folder = os.chdir("C:\\Users\\MinHyukChoi\Desktop\\Programming\\Part II_Chemistry\\Exercise_2\\H2Ooutfiles")
    elif molecule == "H2S":
        files = os.listdir(path="C:\\Users\\MinHyukChoi\\Desktop\\Programming\\Part II_Chemistry\\Exercise_2\\H2Soutfiles")
        folder = os.chdir("C:\\Users\\MinHyukChoi\Desktop\\Programming\\Part II_Chemistry\\Exercise_2\\H2Soutfiles")
    _dic = {}
    for file in files:      
        f = open(file,"r")
        for line in f:
            if 'SCF Done:' in line:
                l = line.split()
                Energy = l[4]
        name = os.path.splitext(file)[0]                #Could calculate r and theta from the coordinates but they are on the file name.
        r_theta = (float(name[5:9]),float(name[14:18]))    
        _dic[r_theta] = float(Energy)
    return _dic         #Dictionary containing all the (r, theta) = Energy extracted from the files
    

def plotSurface(_dic, molecule):
    r =[]
    theta = []
    for i in _dic.keys():
        r.append(i[0])
        theta.append(i[1])

    x = np.arange(min(r),max(r)+0.05,0.05)
    y = np.arange(min(theta),max(theta),1)

    X,Y = np.meshgrid(x,y)
    Z = np.ndarray(X.shape)

    for i in range(0,len(y),1):         #rows of the matrix
        for j in range(0,len(x),1):     #columns of the matrix
            Z[i][j] = _dic[(round(X[i][j],2),round(Y[i][j],1))]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    if molecule == "H2O":
        ax.set_title("H2O Plot")
        ax.set_xlabel('distance O-H, r (Å)')
        ax.set_ylabel('H-O-H Bond Angle, θ (degrees)')
    elif molecule == "H2S":
        ax.set_title("H2S Plot")
        ax.set_xlabel('distance S-H, r (Å)')
        ax.set_ylabel('H-S-H Bond Angle, θ (degrees)')
    
    ax.plot_surface(X,Y,Z,cmap="CMRmap")
    ax.set_zlabel('E(RHF), (Hartree)')

    plt.show()
    save = molecule+".png"
    plt.savefig(save)
    

def EquilibriumGeometry(_dic):     
    for key in _dic.keys():
        if _dic[key] == min(_dic.values()):
            return key

def Optimisation_Function(_dic,how_far):    #This function fits the curve Estimated graph to our data.
    r_theta = EquilibriumGeometry(_dic)
    r0 = r_theta[0]
    theta0 = r_theta[1]
    E0 = _dic[r_theta]

    def Estimated_Graph(coeff, data):   #The function that we want to fit around the minimum
        nonlocal r0, theta0, E0         #These values are nonlocal to the function Estimated_Graph

        k_r, k_theta = coeff
        X = data[0]
        Y = data[1]

        return E0 + np.divide(k_r*(X - r0)**2,2) + np.divide(k_theta*(Y - theta0)**2,2)

    p = np.arange(r0 - 0.05*how_far, r0 + 0.05*how_far, 0.05)
    q = np.arange(theta0-1*how_far,theta0+1*how_far,1)
    P,Q = np.meshgrid(p,q)
    data = [P,Q]

    target = np.ndarray(P.shape)        #The target matrix of values = the values in the dictionary
    for i in range(0,len(q),1):        
            for j in range(0,len(p),1):    
                target[i][j] = _dic[(round(P[i][j],2),round(Q[i][j],1))]

    num_coeff = 2
    coeff_0 = np.ones(num_coeff)            #We want to minimise the difference in values between 
                                            #the target matrix and the Estimated_Graph return matrix.
    def fMinimising(coeff, data, target):  
        if np.any(coeff < 0):               #We don't want negative coefficients.  
            return np.inf
        prediction = Estimated_Graph(coeff, data)
        losses = (prediction - target) ** 2
        loss = losses.sum()
        return loss

    Result_of_Optimisation = s_op.minimize(fMinimising, coeff_0, method='Nelder-Mead', args=(data, target))
    coeff = Result_of_Optimisation.x

    return coeff



