def promedio(data):
	return sum(data)/len(data)

def mediana(data):
	sortdata=sorted(data)
	n=len(sortdata)
	half=n//2
	if n%2==0:
		return (sortdata[half-1]+sortdata[half])/2
	else:
		return sortdata[half]
		
def moda(data):
	frec={}
	for val in data:
		frec[val]=frec.get(val,0)+1
	maxfrec=max(frec.values())
	modas=[k for k, v in frec.items() if v==maxfrec]
	#devuelve lista porsi hay multiples modas
	return modas

def rango(data):
	return max(datos)-min(datos)
	
def varianza(data):
	media=promedio(data)
	return sum((x-media)**2 for x in data)/len(data)
	
def desviacionstd(data):
	return varianza(data)**0.5 #es raiz cuadrada de varianza
	
def desviacionmad(data):
	med=mediana(data)
	desv=[abs(x-med) for x in data]
	return mediana(desv)

def percentil(data,p):
	#usando interp lineal
	if not 0<=p<=100:
		raise ValueError("percentil es entre 0 y 100, dummy")
	sortd=sorted(data)
	n=len(sortd)
	if n==1:
		return sortd[0]
	posi=(p/100)*(n-1)
	infer=int(posi)
	super=infer+1
	frac=posi-infer
	if super>=n:
		return sortd[infer]
	return sortd[infer]*(1-frac)+sortd[super]*frac

def rangoiqr(data):
	q1=percentil(data,25)
	q3=percentil(data, 75)
	return q3-q1
	
def covarianza(x,y):
	if len(x)!=len(y):
		raise ValueError("listas tienen q ser misma longitud, dummy")
	medx=promedio(x)
	medy=promedio(y)
	return sum((xi-medx)*(yi-medy) for xi,yi in zip(x,y))/len(x)

def correlacion(x,y):
	cov=covarianza(x,y)
	stdx=desviacionstd(x)
	stdy=desviacionstd(y)
	if stdx==0 or stdy==0:
		raise ValueError("desv std no puede ser 0, dummy")
	return cov/(stdx*stdy)
	
	
def covarianzam(x,y):
	if len(x)!=len(y):
		raise ValueError("listas tienen q ser misma longitud, dummy")
	if len(x)<2:
		raise ValueError("necesita al menos 2 datos, dummy")
	medx=promedio(x)
	medy=promedio(y)
	suma=sum((xi-medx)*(yi-medy) for xi,yi in zip(x,y))
	return suma/(len(x)-1)