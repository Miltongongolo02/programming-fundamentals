def main():
    print ('Kryptonite phase classifier')

    #input
    T = int(input('Temperature (K)?  '))
    P = int(input('Pressure (Kpa)? '))

    # Determine the phase
    k = P / 2 #
    if P > 50 and T > 400:
        phase = 'Liquid'
    elif T < 400:
        phase = 'solid'
    else:
        phase = 'Gas'
        
    #Output.  (There's a subtle syntax error here!)
    print("At {:.1f} K and {:.3f} kPa, Kryptonite is in the {} phase.".format(T, P, phase))

if __name__ == '__main__':
    main()