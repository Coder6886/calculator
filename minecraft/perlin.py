import random
import matplotlib.pyplot as plt
def interpolate(a,b,x):
    return (b-a)*smoothstep(x)+a
def smoothstep(x):
    return 3*x**2-2*x**3
    #return x
def perlin(flatness,flatpoint,smoothness,start,octaves):
    #flatness is how much the noise is flattened
    #flatpoint is the "0" point at which all the points are flattened towards it
    #smootness is the smoothness of the curve
    #start is the start of the octaves
    #octaves is the intricateness of the terrain
    noise = []
    octaves-=1
    for i in range(2**octaves+1):
        noise.append(0.0)
    for i in range(start,octaves+1):
        lenbetween = 2**(octaves-i)
        noisepartial = []
        for j in range(2**octaves+1):
            noisepartial.append(0.0)
        for j in range(2**i+1):
            noisepartial[j*lenbetween] = random.random()
        for j in range(2**octaves+1):
            if j % lenbetween>0:
                noisepartial[j]=interpolate(noisepartial[(j//lenbetween)*lenbetween],noisepartial[(j//lenbetween+1)*lenbetween],(j-lenbetween*(j//lenbetween))/lenbetween)
            noise[j] += noisepartial[j]/smoothness**(i-start)
    for i in range(len(noise)):
        noise[i] = flatness*noise[i]-flatness*flatpoint+flatpoint
    return noise
if __name__ == '__main__':
    randomseed = 8432085257290
    random.seed(randomseed)
    noiseperlin = perlin(0.3,1,2,5,10)
    for i in range(len(noiseperlin)):
        plt.plot(1/(len(noiseperlin)-1)*i,noiseperlin[i],'bo')    #print(noiseperlin[i])
    plt.show()
        
        
