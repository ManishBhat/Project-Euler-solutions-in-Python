import time

def romanToInt(s: str) -> int:

     roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }    
     num = 0

     s = s.replace("IV", "IIII").replace("IX", "VIIII")
     s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
     s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

     for x in s:
        num += roman[x]

     return num


def intToRoman(x: int) -> str:
	ans = ''
	y = x//1000
	arr = "IVXLCDM"
	#print(y)
	ans += "M"*y
	for i in range(3):
		x = x%(10**(3-i))
		y = x//(10**(2-i))
		if x == 0:
			break
		if y<5:
			if y==4:
				ans += arr[4-2*i] + arr[5-2*i]
			else:
				ans += arr[4-2*i]*y
		else:
			if y == 9:
				ans += arr[4-2*i] + arr[6-2*i]
			else:
				ans += arr[5-2*i] + arr[4-2*i]*(y-5)
	return ans






def q89():
	fhand = open("p089_roman.txt",'r')
	ans = 0
	for line in fhand:
		line = line.strip()
		init_len = len(line)
		final_len = len(intToRoman(romanToInt(line)))
		ans += init_len - final_len
	print(ans)

if __name__ =="__main__":
	start_time = time.time()
	q89()
	#print(intToRoman(2994))
	print("Time taken in sec:", time.time()-start_time)