import Functions as fc
import math

exit = 1
while(exit == 1):
    print(
        '''\nWelcome to Energy Surface and Vibrational Frequency Program'''
        )

    _molecule_dic ={
        1 : "H2O",
        2 : "H2S"
    }
    molecule = 0
    while(molecule not in [1,2]):
        print("\n==========================================================================\n")
        molecule = int(input(
'''What is the molecule of your choice?
    1. H2O (water)
    2. H2S (hydrogen sulfide)
>>>'''))
        if molecule not in [1,2]:
            print("Number you chose was not listed.\n")
    molecule = _molecule_dic[molecule]

    _dic = fc.makeDictionary(molecule)
    Eq_Geo = fc.EquilibriumGeometry(_dic)

    print("\n==========================================================================")
    print("\nEquilibium Geometry of", molecule,":")
    print("\nO-H bond distance (Å) :", Eq_Geo[0])
    print("H-O-H Bond Angle, θ (°) :", Eq_Geo[1])

    print("\n==========================================================================\n")
    how_far = int(input(
    '''To what extent from the minimum would you like the optimisation to be done?
But. Be sensible. (for H2O <= 5 and H2S <= 10)
>>>'''))
    print("\n==========================================================================")
    coeff = fc.Optimisation_Function(_dic,how_far)
    print("\nResult of Optimisation :")
    print("\nk_r : ", coeff[0], "in Hartree/Å^2")
    print("k_theta :", coeff[1], "in Hartree/°^2")
    
    print("\nFrom your optimisation:")
    v1 = math.sqrt(coeff[0]/2)/2*math.pi
    v2 = math.sqrt(coeff[1]/((Eq_Geo[0]**2)*0.5))/2*math.pi
    print("v1 = ", v1, "in sqrt(H/mu) per Å")
    print("v2 = ", v2, "in sqrt(H/mu) per degrees Å")
    fc.plotSurface(_dic, molecule)

    print("\n==========================================================================\n")
    exit = int(input(
'''Please choose what to do next:
    1. Go back to the begining
    2. Exit
>>>'''))
    print("\n==========================================================================")
    print("==========================================================================")

