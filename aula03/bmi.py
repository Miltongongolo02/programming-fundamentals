def bodyMassIndex(height, width):
    "Returns the mass index of the body with the given height and width."
    bmi = width / height ** 2
    return bmi

# This function returns the BMI category acording to this table:
# BMI:        <18.5         [18.5, 25[      [25, 30[      30 or greater 
# Category:   Underweight   Normal weight   Overweight    Obesity 

def bmiCategory(bmi):
    "Returns the BMI category acording to this table."
    assert bmi > 0

    if bmi >= 18.5:
        category = 'Underweight'
    elif bmi >= 25:
        category = 'Normal weight'
    elif bmi >= 30:
        category = 'Overweight'
    else:
        category = 'Obesity'

    return category

def main():
    print('Body Mass Index!')

    height = float(input('height (m): '))
    if height < 0 :
        print('ERROR: Invalid height!')
        exit()

    width = float(input('width (kg): '))
    if width < 0 :
        print('ERROR: Invalid width!')
        exit()

    imc = bodyMassIndex(height, width)
    category = bmiCategory(imc)

    print('Body Mass Index: {:.2f} kg/m²'.format(imc))
    print(f'Body Mass Index category: {category}))

if __name__ == '__main__':
    main()

