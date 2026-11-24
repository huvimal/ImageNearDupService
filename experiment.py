import numpy as np
from common import *

def phash(image):
    from PIL import Image
    small=np.asarray(image.convert('L').resize((32,32)),dtype=float)
    n=np.arange(32);k=np.arange(8)[:,None];basis=np.cos(np.pi*(2*n+1)*k/64);dct=basis@small@basis.T
    values=dct.flatten()[1:];return values>np.median(values)
def run():
    from PIL import Image,ImageDraw,ImageFilter
    r=rng(57);images=[]
    for i in range(16):
        image=Image.new('RGB',(64,64),'white');draw=ImageDraw.Draw(image)
        for _ in range(5):
            x,y=r.integers(0,45,2);draw.rectangle((int(x),int(y),int(x+12),int(y+12)),fill=tuple(r.integers(0,220,3).tolist()))
        images.append(image)
    hashes=np.array([phash(im) for im in images]);dev=[];test=[]
    for i,image in enumerate(images):
        for name,changed in [('blur',image.filter(ImageFilter.GaussianBlur(1.2))),('rotate',image.rotate(12,fillcolor='white')),('resize',image.resize((40,40)).resize((64,64)))]:
            d=np.sum(hashes!=phash(changed),axis=1);pred=int(np.argmin(d));row={'source':i,'transform':name,'top_match':pred,'distance':int(d[pred]),'correct':pred==i}
            (dev if i<8 else test).append(row)
    threshold=max(row['distance'] for row in dev if row['correct'])
    return {'development_selected_hamming_threshold':threshold,'test_cases':test,
            'test_top1':sum(row['correct'] for row in test)/len(test),
            'checks':[check(len(hashes[0])==63,'Actual DC-excluded DCT perceptual hash'),check(len(test)==24,'Separate source-image slice for evaluation')],
            'scope':'Local perceptual-hash retrieval core over authored geometric images. No network service, learned image embedding, general transformation invariance or production service claim.'}
