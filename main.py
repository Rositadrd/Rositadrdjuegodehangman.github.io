import time

name=input("Cual es tu nombre?")
print("Hola 👋,"+name, "Bienvenido al juego  🙂 , es hora de jugar Hangman!")

time.sleep(1)
print("Empieza a adivinar...")
time.sleep(1)


word=("gato")
guesses= ''

turns=5
while turns>0:
 failed=0

for character in word:
  if character in guesses:
    print (character,end="")
else:
   print ("___",end="");
   failed +=1
if failed == 0: 
  print("Ganaste!")

'break'

guess = input("Adivina una letra:")
guesses += guess
if guess not in word:
  turns -= 1
  print ("Respuesta Incorrecta")
  print ("Tienes", +turns, 'oportunidades adicionales' )
  if turns == 0: 
    print("Perdiste!")