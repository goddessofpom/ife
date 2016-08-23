#!/usr/bin/env python
#-*- coding:utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

def add_num(img):
	draw = ImageDraw.Draw(img)    #创建绘画对象
	myfont = ImageFont.truetype('C:\Windows\Fonts\Arial\Arial 常规.tiff', size=40)  #使用矢量字体
	draw.text((width-50,0),'5',font=myfont,fill="#ff0000")
	img.save('result.jpg','jepg')

	return 0

if __name__ == '__main__':
	image = Image.open(r"C:\cspy\practice\1.jpg")
	add_num(image)