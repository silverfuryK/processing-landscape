#TOTAL_DEGREES = height

def setup():
    global width, height, difference
    width = 3000
    height = width
    size(3000, 3000)
    background(0)
    #noFill()
    fill(0,100)
    #stroke(255,50)
    colorMode(HSB,255,255,100)
    strokeWeight(2)
    radius = height/100
    
    
def draw():
    #translate(0,frameCount+10)
    global TOTAL_DEGREES
    TOTAL_DEGREES = height
    # for j in range(TOTAL_DEGREES):
    #     beginShape()
    #     for i in range(TOTAL_DEGREES):
    #         noiseFactor = noise(i*0.02,float(frameCount)/200)
    #         x = i
    #         y = 
    #         curveVertex(x,y)
    #     endShape()
        #translate(0,frameCount+10)
    
    #translate(0,300)
    
    beginShape()
    for i in range(TOTAL_DEGREES):
        #noiseFactorX = noise(0,i*0.5)
        noiseFactorX = noise(i*0.1,float(frameCount) / 100)
        noiseFactorY = noise(i*0.05,float(frameCount) / 50)
        x = i * 10 + (noiseFactorX * 50)
        y =(1 * frameCount) + (noiseFactorY * 500)
        
        dev = (noiseFactorY*1)
        #radius = radius * cos(radians(i))
        stroke(map(dev,0,1,0,255),200,100)
        point(x,y)
        curveVertex(x,y)
        
    curveVertex(0,height)
    curveVertex(width,height)
    endShape()
    if frameCount == TOTAL_DEGREES:
        saveFrame("points1.png")
        noLoop()
        
        
        
        
        
        
