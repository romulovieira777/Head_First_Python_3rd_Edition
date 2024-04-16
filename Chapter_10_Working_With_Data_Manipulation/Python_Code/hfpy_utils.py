def convert2range(v, f_min, f_max, t_min, t_max):
    """
    Give a value (v) in the range f_min to f_max, convert to its equivalent value in the range t_min to t_max.

    Based on the technique described here:
        http://james-ramsden.com/map-a-value-from-one-number-scale-to-another-formula-and-c-code/
    """
    return round(t_min + (t_max - t_min) * ((v - f_min) / (f_max - f_min)), 2)
