units=int(input("enter units"))
gro_of_units=int(input("enter group of units"))
comp_gro=units//gro_of_units
remain_gro=units%gro_of_units
print("completed groups",comp_gro)
print("remaining group",remain_gro)