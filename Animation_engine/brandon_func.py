

def hex_to_RGB(hex : str):
    def hex_helper(numstr : str):
        mapping = {
            'a' : 10
            ,'b' : 11
            ,'c' : 12
            ,'d' : 13
            ,'e' : 14
            ,'f' : 15    
        }
        n = len(numstr)
        power = 0
        result = 0
        for i in range(-1,-(n+1),-1):
            val = mapping[numstr[i].lower()] if numstr[i].lower() in mapping else int(numstr[i])
            result += val * 16**power
            power +=1 
        return result
    if len(hex) != 6 :
        raise Exception('Invalid hex string input.')
    r = hex[0:2]
    g = hex[2:4]
    b = hex[4:]
    return (hex_helper(r),hex_helper(g),hex_helper(b))

