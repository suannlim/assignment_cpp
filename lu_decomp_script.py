# -*- coding: utf-8 -*-

import lu_decomp_q2 as lu

A=[[3,1,0,0,0],[3,9,4,0,0],[0,8,20,10,0],[0,0,-22,31,-25],[0,0,0,-35,61]]
b=[[2],[5],[-4],[8],[9]]

#taking the upper matrix produced by lu_decomp
U=lu.lud(A)[0]
L=lu.lud(A)[1]

lu.determinant(U)

lu.substitution(U,L,b)