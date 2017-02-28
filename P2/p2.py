#!/usr/bin/env python
import sys


def distances(amt, src_unit, des_unit):
    '''amt src_unit = ? des_unit
    m (meters), cm (centimeters), mm (millimeters), km (kilometers),
    in (inches), ft (feet), yd (yards), mi (miles)'''
    map = {
        "m": 1,
        "mm": 0.001,
        "cm": 0.01,
        "km": 1000,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.3472
    }
    output = float(amt) * map[src_unit] / map[des_unit]
    return output


def volumes(amt, src_unit, des_unit):
    '''amt src_unit = ? des_unit
    L(liters), mL(millileters), floz(fluid
    ounces), cup(cups), pint(pints), qt(quarts), gal(gallons)'''
    map = {
        "l": 1,
        "ml": 1000,
        "floz": 0.0295735296,
        "cup": 0.25,
        "pint": 0.473176473,
        "qt": 0.946352946,
        "gal": 3.785411784,
    }
    output = float(amt) * map[src_unit] / map[des_unit]
    return output


def weights(amt, src_unit, des_unit):
    '''amt src_unit = ? des_unit
    g (grams), kg (kilograms), mg (milligrams), oz (ounces), lb (pounds)'''
    map = {
        "g": 1,
        "kg": 1000,
        "mg": 0.001,
        "oz": 28.349523125,
        "lb": 453.59237,
    }
    output = float(amt) * map[src_unit] / map[des_unit]
    return output


def main(argv):
    converted = False
    raw_distance = input("[amount] [source unit] in [destination unit]:")
    sep = str.split(raw_distance)
    amt = sep[0]
    src_unit = sep[1].lower()
    des_unit = sep[-1].lower()
    try:
        output = distances(amt, src_unit, des_unit)
        converted = True
    except:
        pass
    try:
        output = weights(amt, src_unit, des_unit)
        converted = True
    except:
        pass
    try:
        output = volumes(amt, src_unit, des_unit)
        converted = True
    except:
        pass
    if not converted:
        print("Invalid unit conversion")
    else:
        print(amt, src_unit, "=", output, des_unit)

if __name__ == '__main__':
    main(sys.argv[1:])
