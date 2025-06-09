valores = list(map(float, input() .split()))
a, g, ra, rg = map("{:.2f}".format, valores)
custo_km_a = float(a)/float(ra)
custo_km_g = float(g)/float(rg)

if custo_km_g <= custo_km_a:
    print ("G")

else:
    print ("A")