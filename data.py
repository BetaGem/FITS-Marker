from astropy.io import fits 
from numpy import sum

hdul = fits.open('galaxies.fits',mode='update')

def galinfo(k):
    '''显示星系参数'''
    data = hdul[1].data
    if k<len(hdul[1].data):
        return data[k]
    else:
        return [None]*52

def classify(k,val):
    '''判断结果写入文件'''
    hdul[1].data[k-1][51] = val
    
def stat():
    a = [0,0,0,0,0,0,0]
    for i in range(7):
        a[i] = sum(hdul[1].data['substr']==i)
    return a

def LIST(val):
    a = []
    for i in range(2088):
        if hdul[1].data['substr'][i] == int(val):
            a.append(i+1)
    return a
    