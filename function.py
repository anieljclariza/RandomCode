def convert_temperature(int(temperature), scale):
    if scale == "C":
        return (temperature * 9/5) + 32
    elif scale == "F":
        return (temperature - 32) * 5/9
    
    else: 
        return "Invalid Scale"
    
print(convert_temperature("40", "C"))