import numpy as np
from numpy import sin, cos, tan
from math import acos, atan2

def euler_to_quaternion( alpha, beta, gamma ):
    diff = (alpha - gamma) / 2.0
    summ = (alpha + gamma) / 2.0
    return np.array([ cos(diff)*sin(beta/2.0),
                      sin(diff)*sin(beta/2.0),
                      sin(summ)*cos(beta/2.0),
                      cos(summ)*cos(beta/2.0)
                   ])

def mult( q1, q2):
    res = np.array([ 0.0, 0.0, 0.0, 0.0 ])
    res[0] = q1[0] * q2[0] - q1[1] * q2[1] - q1[2] * q2[2] - q1[3] * q2[3]
    res[1] = q1[0] * q2[1] + q1[1] * q2[0] + q1[2] * q2[3] - q1[3] * q2[2]
    res[2] = q1[0] * q2[2] - q1[1] * q2[3] + q1[2] * q2[0] + q1[3] * q2[1]
    res[3] = q1[0] * q2[3] + q1[1] * q2[2] - q1[2] * q2[1] + q1[3] * q2[0]
    return res

def quaternion_to_euler( q ):
    phi = atan2( q[1]*q[3] + q[0]*q[2], q[0]*q[1] - q[2]*q[3] )
    theta = acos( -q[1]*q[1] - q[2]*q[2] + q[3]*q[3] + q[0]*q[0])
    psi = atan2( q[1]*q[3] - q[0]*q[2], q[2]*q[3] + q[0]*q[1] )
    return phi, theta, psi

alpha1 = 0.12;
beta1 = 0.26;
gamma1 = 0.231;

alpha2 = 0.678;
beta2 = 0.45;
gamma2 = 1.345;

q1 = euler_to_quaternion( alpha1, beta1, gamma1 )
print('q1: {0}'.format(q1))
q2 = euler_to_quaternion( alpha2, beta2, gamma2 )
print('q2: {0}'.format(q2))
q3 = mult(q1, q2)
print('q3: {0}'.format(q3))

alpha3, beta3, gamma3 = quaternion_to_euler( q3 )
print('(numerical) alpha3 = {0}; tan(alpha3): {1}'.format(alpha3, tan(alpha3)))
print('(numerical) beta3 = {0}; cos(beta3): {1}'.format(beta3, cos(beta3)))
print('(numerical) gamma3 = {0}; tan(gamma3): {1}'.format(gamma3, tan(gamma3)))

def calc_cos_beta3( alpha1, beta1, gamma1, alpha2, beta2, gamma2 ):
    return - sin(gamma1) * sin(alpha2) * sin(beta1) * sin(beta2) + \
          (sin(gamma1)*sin(alpha2)*cos(beta1)*cos(beta2) + cos(gamma1)*cos(alpha2))*cos(alpha1-gamma2) + \
          (sin(alpha2)*cos(beta2)*cos(gamma1) - sin(gamma1)*cos(alpha2)*cos(beta1))*sin(alpha1-gamma2)

def calc_tan_alpha3( alpha1, beta1, gamma1, alpha2, beta2, gamma2 ):
    numerator = (sin(beta1)*cos(beta2)*cos(alpha1)*cos(gamma2) + sin(beta1)*cos(beta2)*sin(gamma2)*sin(alpha1) + cos(beta1)*sin(beta2))*sin(alpha2) + sin(beta1)*cos(alpha2)*sin(gamma2 - alpha1)
    denumerator = ( -cos(beta2) * (sin(gamma1)*sin(gamma2) + cos(beta1)*cos(gamma1)*cos(gamma2))*cos(alpha1) + cos(beta2)*cos(gamma2)*sin(alpha1)*sin(gamma1) + \
                   cos(gamma1) * (sin(beta1)*sin(beta2) - cos(beta1)*cos(beta2)*sin(gamma2)*sin(alpha1)) ) * sin(alpha2) - \
                  ( (sin(gamma2)*cos(beta1)*cos(gamma1) - sin(gamma1)*cos(gamma2)) * cos(alpha1) - \
                   sin(alpha1) * (sin(gamma1)*sin(gamma2) + cos(gamma1)*cos(gamma2)*cos(beta1))*cos(alpha2) )
    return numerator / denumerator

def calc_tan_gamma3( alpha1, beta1, gamma1, alpha2, beta2, gamma2 ):
    numerator = (cos(beta2)*sin(beta1) + cos(beta1)*sin(beta2)*cos(alpha1)*cos(gamma2) + cos(beta1)*sin(beta2)*sin(gamma2)*sin(alpha1))*sin(gamma1) - \
            sin(beta2)*cos(gamma1)*sin(gamma2 - alpha1)
    denumerator = ( -cos(beta1)*( -sin(gamma2)*sin(alpha2) + cos(beta2)*cos(alpha2)*cos(gamma2))*cos(alpha1) - sin(alpha2)*sin(alpha1)*cos(beta1)*cos(gamma2) + \
            cos(alpha2)*(sin(beta2)*sin(beta1) - cos(beta1)*cos(beta2)*sin(gamma2)*sin(alpha1))) * sin(gamma1) + \
            cos(gamma1) * ((sin(gamma2)*cos(beta2)*cos(alpha2) + sin(alpha2)*cos(gamma2)) * cos(alpha1) - sin(alpha1)*(-sin(gamma2)*sin(alpha2) + cos(beta2)*cos(alpha2)*cos(gamma2)))
    return numerator / denumerator

cos_beta3 = calc_cos_beta3( alpha1, beta1, gamma1, alpha2, beta2, gamma2 )
print('(analytical) cos(beta3) = {0}'.format(cos_beta3)) 
tan_alpha3 = calc_tan_alpha3( alpha1, beta1, gamma1, alpha2, beta2, gamma2 )
print('(analytical) tan(alpha3) = {0}'.format(tan_alpha3))
tan_gamma3 = calc_tan_gamma3( alpha1, beta1, gamma1, alpha2, beta2, gamma2 )
print('(analytical) tan(gamma3) = {0}'.format(tan_gamma3))
