import sympy as sp
sp.init_printing()

p, V, T = sp.symbols("p V T", positive=True, real=True)
n, R, a, b = sp.symbols("n R a b", positive=True, real=True)

ideal_p = n * R * T / V

vdw_eos = (R * T / (V - b)) - (a / V**2)

van_der_walls_solved_for_volume = sp.solve(vdw_eos, V)
van_der_walls_solved_for_temperature = sp.solve(vdw_eos, T)

sp.pprint(van_der_walls_solved_for_volume)

sp.pprint(van_der_walls_solved_for_temperature)

dp = sp.diff(vdw_eos, V)
ddp = sp.diff(vdw_eos, V, 2)

sp.pprint(dp)
sp.pprint(ddp)

pressure_eq = sp.Eq(p, vdw_eos)

dp_eq = sp.Eq(0, dp)
ddp_eq = sp.Eq(0, ddp)

sp.pprint(pressure_eq)
sp.pprint(dp_eq)
sp.pprint(ddp_eq)

pc, Vc, Tc = sp.symbols("p_c V_c T_c")

critpoint = sp.solve([pressure_eq, dp_eq, ddp_eq], [p, V, T])

pcr, Vcr, Tcr = [critpoint[i] for i in range(len(critpoint))]

sp.pprint(sp.Eq(pc, pcr))
sp.pprint(sp.Eq(Vc, Vcr))
sp.pprint(sp.Eq(Tc, Tcr))