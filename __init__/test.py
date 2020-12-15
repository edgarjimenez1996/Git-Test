print (__name__)

print ("El primer modulo se llama:{}.py".format(__name__))

if __name__ == '__main__':                   #¿Es este modulo ejecutado directamente por Python o es un modulo importado?
	print("Este es el modulo principal")              #Si es así entonces este es el modulo main o principal.
else:
	print("Este modulo No corre directamente, sino que es importado")