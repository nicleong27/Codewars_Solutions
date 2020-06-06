# When working with color values it can sometimes be useful to extract 
# the individual red, green, and blue (RGB) component values for a color. 
# Implement a function that meets these requirements:

# Accepts a case-insensitive hexadecimal color string as its parameter 
# (ex. "#FF9933" or "#ff9933").
# Returns an object with the structure {r: 255, g: 153, b: 51} 
# where r, g, and b range from 0 through 255
# Note: your implementation does not need to support the shorthand 
# form of hexadecimal notation (ie "#FFF")

def hex_string_to_RGB(hex_string): 
    val = hex_string.lstrip('#')
    lv = len(val)
    
    rgb = [int(val[i:i + lv // 3], 16) for i in range(0, lv, lv // 3)]
    
    output = {'r': rgb[0], 'g': rgb[1], 'b': rgb[2]}
    
    return output