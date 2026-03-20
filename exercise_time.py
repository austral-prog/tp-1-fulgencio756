def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665
    segundosrestantes=(total_segundos%60)
    minutos=(total_segundos//60)
    horascompletos=(minutos//60)
    minutosrestantes=(minutos%60)
    print(horascompletos)
    print(minutosrestantes)
    print(segundosrestantes)

