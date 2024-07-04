from pyscf import gto,dft
import dftd4.pyscf as d4
#from pyscf.geomopt.geometric_solver import optimize


mol=gto.Mole()
mol.atom="traj.xyz"
#mol.basis="def2-TZVP"
mol.basis="def2-TZVPP"
mol.build()

mf=dft.RKS(mol)
mf.xc="pbe0"
mf=mf.newton()
mf.kernel()

d4_r=d4.DFTD4Dispersion(mol,xc="r2SCAN")
print(d4_r.kernel()[0])


#mol.xc="pbe"
#mol.xc="PW6B95"

#d3_result=d4.DFTD3Dispersion(mol,xc="PW6B95",version="d3bj")
#####mf=d4.energy(mol.RHF()).run()#
#mf.kernel()


#print(d3_result.kernel()[0])
#mf=d3.energy(mol.RHF()).run()


#mf=scf.RHF(mol)
#mol_eq=optimize(mf)
#mf=mol.KS()
#mf=d3.energy(mol.RHF())
#mf.xc="PBE0"
#mf.kernel()


#mol_eq=optimize(mf)
#print(mf.kernel())
#mf.kernel()
#mf.Gradients()
#mf.kernel()
