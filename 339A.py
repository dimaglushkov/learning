# 339A A. Математика спешит на помощь

# Начинающий математик Ксения учится в третьем классе. Сейчас в школе она проходит операцию сложения. Учитель за
# писал на доске сумму нескольких чисел, которую требуется посчитать. Чтобы было проще считать, в сумме использу
# ются только числа 1, 2 и 3. Но и этого Ксении мало. Ксения только учится считать, и поэтому она может посчитат
# ь сумму, только если слагаемые в сумме идут в порядке неубывания. Например, сумму 1+3+2+1 она посчитать не мож
# ет, а суммы 1+1+2 и 3+3 может.Вам задана сумма, которая записана на доске. Переставьте слагаемые и выведите ее
#  в виде, в котором Ксения сможет посчитать сумму.

# input_str = input()

input_str = '+' + input()
print(''.join(sorted([input_str[0+i:2+i] for i in range(0, len(input_str), 2)]))[1:])
