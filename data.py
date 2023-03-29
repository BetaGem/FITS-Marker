from astropy.io import fits
from numpy import sum

hdul = fits.open('data/galaxies.fits', mode='update')
def galnum():
    return len(hdul[1].data)

def galinfo(k):
    '''显示星系参数'''
    data = hdul[1].data
    if k < len(hdul[1].data):
        return data[k]
    else:
        return [None] * len(hdul[1].data[0])


def classify(k, val):
    '''判断结果写入文件'''
    hdul[1].data[k-1]['class'] = val


def stat():
    '''统计各类星系总数'''
    a = [0] * 7
    for i in range(len(a)):
        a[i] = sum(hdul[1].data['class'] == i)
    return a


def LIST(num,val):
    a = []
    for i in range(num):
        if hdul[1].data[i]['class'] == int(val):
            a.append(i+1)
    return a
