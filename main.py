from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import random
 
width = 95
height = 35
 
drunk = {
    'wallCountdown': 1500,
    'padding': 2,
    'x': int( width / 2 ),
    'y': int( height / 2 )
}
 
def getLevelRow():
    return ['#'] * width
 
level = [getLevelRow() for _ in range(height)]
 
while drunk['wallCountdown'] >= 0:
    x = drunk['x']
    y = drunk['y']
    
    if level[y][x] == '#':
        level[y][x] = ' '
        drunk['wallCountdown'] -= 1
    
    roll = random.randint(1, 4)
    
    if roll == 1 and x > drunk['padding']:
        drunk['x'] -= 1
    
    if roll == 2 and x < width - 1 - drunk['padding']:
        drunk['x'] += 1
    
    if roll == 3 and y > drunk['padding']:
        drunk['y'] -= 1
    
    if roll == 4 and y < height - 1 - drunk['padding']:
        drunk['y'] += 1
 
for row in level:
    print( ''.join(row) )

arr=np.array([[1,0]*200,[0,1]*200]*200)
plt.imsave("img.png",arr,cmap="Blues")


img = Image.open("img.png")
img = img.convert("RGB")
d = img.getdata()
print(d)

new_image = []
for item in d:
   
    # change all white (also shades of whites)
    # pixels to yellow
    if item[0] in list(range(200, 256)):
        new_image.append((0, 255, 0))
    else:
        new_image.append(item)
img.putdata(new_image)
 
# save new image
img.save("flower_image_altered.png")