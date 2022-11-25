from PIL import Image, ImageDraw

ListePoint = [[3,5],[4,5],[4,7],[7,5],[8,5],[7,6],[12,5],[12,6],[11,6],[17,5],[18,6],[15,12],[18,12],[20,13],[20,14],[20,17],[20,21],[21,26],[25,26],[27,26],[26,29],[28,29],[28,31],[28,34],[28,36],[28,37],[28,39],[28,41],[32,26],[36,26],[39,26],[40,26],[39,28],[38,30],[39,30],[39,33],[39,36],[39,39],[39,41],[26,6],[27,6],[28,6],[29,6],[33,6]]
ListeLiaision = [[[3,5],[4,5]], #deffinistion des liaison
                [[3,5],[4,7]],
                [[4,7],[4,5]],
                [[4,5],[7,5]],
                [[4,5],[7,6]],
                [[7,5],[7,6]],
                [[7,5],[8,5]],
                [[8,5],[12,5]],
                [[7,6],[11,6]],
                [[12,6],[18,6]],
                [[26,29],[28,29]],
                [[38,30],[39,30]],
                [[7,6],[8,5]],
                [[8,5],[11,6]],
                [[11,6],[12,5]],
                [[11,6],[12,6]],
                [[12,5],[17,5]],
                [[12,6],[17,5]],
                [[17,5],[18,6]],
                [[18,6],[26,6]],
                [[26,6],[27,6]],
                [[27,6],[28,6]],
                [[28,6],[29,6]],
                [[29,6],[33,6]],
                [[18,6],[18,12]],
                [[18,12],[15,12]],
                [[18,12],[20,13]],
                [[20,13],[20,14]],
                [[20,14],[20,17]],
                [[20,17],[20,21]],
                [[20,21],[21,26]],
                [[21,26],[25,26]],
                [[25,26],[27,26]],
                [[27,26],[26,29]],
                [[27,26],[28,29]],
                [[27,26],[31,26]],
                [[31,26],[36,26]],
                [[36,26],[39,26]],
                [[39,26],[40,26]],
                [[39,26],[39,28]],
                [[28,29],[28,30]],
                [[28,30],[28,33]],
                [[28,33],[28,35]],
                [[28,35],[28,36]],
                [[28,36],[28,38]],
                [[28,38],[28,41]],
                [[39,28],[39,30]],
                [[39,28],[38,30]],
                [[39,30],[39,33]],
                [[39,33],[39,36]],
                [[39,36],[39,38]],
                [[39,38],[39,41]],
                ]



image = Image.open("../image/planCadriller.png")

# Obtention du contexte graphique
draw = ImageDraw.Draw(image)

RED = (255, 0, 0, 0)
for i in range(len(ListeLiaision)):
    coPt1 =[(ListeLiaision[i][0][0]+2)*11-6,(ListeLiaision[i][0][1]+1)*11-6]
    coPt2 =[(ListeLiaision[i][1][0]+2)*11-6,(ListeLiaision[i][1][1]+1)*11-6]
    draw.line((coPt1[0], coPt1[1], coPt2[0], coPt2[1]),fill=RED,width=2)

for i in range(len(ListePoint)):
    image.putpixel(((ListePoint[i][0]+2)*11-6,(ListePoint[i][1]+1)*11-6),(0,0,0))
    image.putpixel(((ListePoint[i][0]+2)*11-6+1,(ListePoint[i][1]+1)*11-6),(0,0,0))
    image.putpixel(((ListePoint[i][0]+2)*11-6,(ListePoint[i][1]+1)*11-6+1),(0,0,0))
    image.putpixel(((ListePoint[i][0]+2)*11-6+1,(ListePoint[i][1]+1)*11-6+1),(0,0,0))
    
    


image.show()
image.save("../image/planInfo.png", "png")