from PIL import Image,ImageDraw, ImageFont
import argparse
def convert_img_to_ascii(image_path,width,height):
	# change to grayscale
	if not width: width=100
	if not height:height=100
	image=Image.open(image_path)
	image=image.convert("L")
	image=image.resize((width,height))
	print width,height
	color = "MNHQ$OC?7>!:-;. " ##16 value  
	ascii=[]
	for i in range(height):
		p=[]
		for j in range(width):
			p.append(color[image.getpixel((j,i))/16])
		ascii.append(''.join(p)+"\n")
	print ''.join(ascii)
	image.close()	
def convert_text_to_ascii(text,font,size):
	if  font:
		font = ImageFont.truetype(font,size)
	else :
		font = ImageFont.load_default()
	size=font.getsize(text)
	image = Image.new('1', size, 1)
	draw = ImageDraw.Draw(image)
	draw.text((0, 0), text, font=font)
	ascii=[]
	for i in range(size[1]):
		p=[]
		for j in range(size[0]):
			print image.getpixel((j,i))
			p.append(image.getpixel((j,i))==0 and '*' or ' ')
		ascii.append(''.join(p)+"\n")
	print ''.join(ascii)
	image.close()
	
'''
	usage: ascii_art [-i image_path -w widht -h height ] [-t text -font font_path -fsize] 
'''
if __name__=='__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument("-i")
	parser.add_argument("-width",default=100)
	parser.add_argument("-height",default=100)
	parser.add_argument("-t")
	parser.add_argument("-font")
	parser.add_argument("-fsize",default=12)
	argument= parser.parse_args()
	print argument
	if argument.i:
		convert_img_to_ascii(argument.i,argument.width,argument.height)
	elif argument["t"]:
		convert_text_to_ascii(argument.t,argument.font,argument.fsize)
	