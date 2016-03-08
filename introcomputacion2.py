nombre = input("nombre del paciente:")
TipoDoctor = input("ingrese el tipo de doctor:")
tipo = input("tipo de consulta:")
honorarios = float(input("ingrese los honorarios:"))

if TipoDoctor == "dermatologo":
	if tipo == "consulta":
		visita = 500
	else:
		visita = 15000

elif TipoDoctor == "pediatra":
	if tipo == "consulta":
		visita = 800
	else:
		visita = 20000

elif TipoDoctor == "cardiologia":
	if tipo =="consulta":
		visita = 900
	else:
		visita = 25000
else:
	if tipo == "consulta":
		visita = 700
	else:
		visita =10000

subtotal = honorarios + visita
impuesto = 0.15* subtotal
total = impuesto + subtotal

print ("subtotal",subtotal)
print("impuesto",impuesto)
print("total",total)