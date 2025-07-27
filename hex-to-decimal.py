
def cleanHex(hex): 
	return ''.join( c for c in hex if c in '0123456789abcdefABCDEF')



def hexBytes(hex):
	return len(hex)//2



def hexToDec(hex): 
	return int(hex,16)





def output(inputHex): 
	cleaned=cleanHex(inputHex)
	print(cleaned)


	bytes=hexBytes(cleaned)
	print(f"\nnumber of hexadecimal bytes:  {bytes} ")
	

	deci=hexToDec(cleaned)
	print(f"\n decimal value : {deci}")








if __name__ == "__main__":
	import sys 
	print("write the hexadecimal value: ") 
	hexa=sys.stdin.read()

	output(hexa)





