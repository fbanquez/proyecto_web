from math import sqrt

def cuadratica(a, b, c):
    if a != 0:
        x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
        x2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
        print 'Soluciones de la ecuacion: x1=%4.3f y x2=%4.3f ' % (x1, x2)
    else:
        if b != 0:
            x = -c/b
            print 'Solucion de la ecuacion: x=%4.3f ' % x
        else:
            if c != 0:
                print 'La ecuacion no tiene solucion.'
            else:
                print 'La ecuacion tiene infinitas soluciones.'


