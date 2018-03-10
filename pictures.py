from PIL import Image, ImageFilter, ImageEnhance
im = Image.open("../assets/riika.jpg")
width, height = im.size
#----thumbnail----
im2 = im.resize((round(width/10), round(height/10)), Image.ANTIALIAS)
im2.save("riika_thumbnail.jpg")
#----black and white sharpen---- 
enhancer = ImageEnhance.Color(im)
im3 = enhancer.enhance(0)
im3 = im3.filter(ImageFilter.SHARPEN)
im3.save("riika_bw.jpg")
#----rotate blur----
im4 = im.rotate(90, resample=Image.BICUBIC, expand=True)
im4 = im4.filter(ImageFilter.BLUR)
im4.save("riika_rotate_blur.jpg")
