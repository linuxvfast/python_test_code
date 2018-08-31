import struct
import string

filename = 'fixed_width-1M.txt'
mask='9s15s6s' #根据特定的格式来分隔，s表示字符串，数字表示字符串的长度
with open(filename,'r') as f:
    for line in f:
        # fields = struct.Struct(mask).unpack_from(bytes(line,encoding='utf-8'))  #使用struct.Struct类面向对象
        fields = struct.unpack_from(mask,bytes(line,encoding='utf-8')) #使用非面向对象
        print('fields:',[field.strip() for field in fields])
