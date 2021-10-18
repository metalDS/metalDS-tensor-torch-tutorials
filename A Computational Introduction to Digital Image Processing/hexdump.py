def hexdump(file, num):
    from math import ceil
    f = open(file, 'rb')
    h = f.read(num)
    #ord converts a character into it's unicode value
    hl = [hex(ord(c))[2:].zfill(2) for c in h] #all the bytes as 2 character hex strings
    hl2 = hl + (-len(hl)%16)*['  '] #fill up to a multple of width 16
    asc = ['.']*num

    for i in range(num):
        #creates ascii values (if printable) of bytes
        ii = int(hl[i], 16) #convert each into a base 16 integer
        if ii >= 32 and ii <= 126:
            asc[i] = chr(ii)

        asc = asc + (-len(hl)%16)*[' ']

        for n in range(int(ceil(num/16.0))):
            print( hex(n*16)[2:].zfill(6)+': ',
            ' '.join([hl2[16*n+2*i]+hl2[16*n+2*i+1] for i in range(8)]),
            ' |'+''.join([asc[16*n+i] for i in range(16)])+'|')
 