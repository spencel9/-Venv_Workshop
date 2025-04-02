import numpy as np

#Tell user what this program is doing
print("Calculator for the dust-corrected absolute magnitude of a galaxy! ")

#Ask for user inputs
app_mag = float(input("Please enter the apparent magnitude (m) of the galaxy: "))
distance = float(input('Please enter the distance (D) of the galaxy in Mpc: ')) #in Mpc
dust_cor = float(input('Please enter the dust correction factor (A) for the galaxy: '))
redshift = float(input('Please enter the redshift (z) of the galaxy: '))

#Make actual calc, modify the distance modulus
abs_mag = app_mag - 5*np.log10(distance * 10**6) + 5 -2.5*np.log((1 + redshift)**4) - dust_cor

#Print results and input
print()
print("The dust and cosmology corrected absolute magnitude of the galaxy is " + str(abs_mag))
print('The apparent magnitude is ' + str(app_mag))
print('The distance in pc is ' + str(distance))
print('The redshift (z) is ' + str(redshift))
print('The dust correction factor is ' + str(dust_cor))

