import math
a=float(input('insira um angulo'))
seno=math.sin(math.radians(a))
cosseno=math.cos(math.radians(a))
tangente=math.tan(math.radians(a))
print("O angulo é {:.2f} e seu seno, cosseno e tangente são {:.2f"
      "},{:.2f} e {:.2f}, respecticamente".format(a, seno, cosseno, tangente))
