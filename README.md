# Exercise2

NST Part II Chemistry : Programming Option

INTRODUCTION
This program allows plotting of the energy surface of H2O/H2S using Gaussian output files.

REQUIREMENTS
This program also requires the following python libraries to work:

Numpy (https://pypi.org/project/numpy/)
pyutilib.math (if not already downloaded: https://pypi.org/project/pyutilib.math/#files includes wheel and zip)
Os
MATPLOTLIB (https://pypi.org/project/matplotlib/)
mplot3d from mpl_toolkits 
Scipy (https://www.scipy.org/scipylib/download.html)

RUNNING THE CODE
IMPORTANT: You need H2Ooutfiles and H2Soutfiles of the Gaussian output to run this code. AND in Functions.py you need to change the directory of the folders that contain YOUR files in order for the program to import data form the correct files.
">>>" Requires user input.

EXAMPLE CODE RUN (Visual Studio Code)
(Please view "Raw"/"Blame": for better presentation of example code)

Microsoft Windows [Version 10.0.17134.345]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Users\MinHyukChoi\Desktop\Programming\Part II_Chemistry>python -u "c:\Users\MinHyukChoi\Desktop\Programming\Part II_Chemistry\Exercise_2\Exercise_2.py"

Welcome to Energy Surface and Vibrational Frequency Program

==========================================================================

What is the molecule of your choice?
    1. H2O (water)
    2. H2S (hydrogen sulfide)
>>>1

==========================================================================

Equilibium Geometry of H2O :

O-H bond distance (Å) : 0.95
H-O-H Bond Angle, θ (°) : 105.0

==========================================================================

To what extent from the minimum would you like the optimisation to be done?
But. Be sensible. (for H2O <= 5 and H2S <= 10)
>>>3

==========================================================================

Result of Optimisation :

k_r :  4.582304222753023 in Hartree/Å^2
k_theta : 1.0161579740886828e-09 in Hartree/°^2

From your optimisation:
v1 =  2.3776440525237788 in sqrt(H/mu) per Å
v2 =  7.454042838899065e-05 in sqrt(H/mu) per degrees Å

==========================================================================

Please choose what to do next:
    1. Go back to the begining
    2. Exit
>>>1

==========================================================================
==========================================================================

Welcome to Energy Surface and Vibrational Frequency Program

==========================================================================

What is the molecule of your choice?
    1. H2O (water)
    2. H2S (hydrogen sulfide)
>>>2

==========================================================================

Equilibium Geometry of H2S :

O-H bond distance (Å) : 1.35
H-O-H Bond Angle, θ (°) : 94.0

==========================================================================

To what extent from the minimum would you like the optimisation to be done?
But. Be sensible. (for H2O <= 5 and H2S <= 10)
>>>4

==========================================================================

Result of Optimisation :

k_r :  2.291612575530947 in Hartree/Å^2
k_theta : 9.829560342796108e-10 in Hartree/°^2

From your optimisation:
v1 =  1.681417168679889 in sqrt(H/mu) per Å
v2 =  5.159031183175819e-05 in sqrt(H/mu) per degrees Å

==========================================================================

Please choose what to do next:
    1. Go back to the begining
    2. Exit
>>>2

==========================================================================
==========================================================================

C:\Users\MinHyukChoi\Desktop\Programming\Part II_Chemistry>
