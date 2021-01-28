from astropy.io import fits 
from io import BytesIO
from os import listdir
import base64

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.widgets import Slider
from matplotlib.colors import SymLogNorm
from numpy import full, min, shape
from astropy.visualization import make_lupton_rgb

# folder that contains your FITS images
fpath = '/arch/'  

def search_fits(n):
    f = 2
    for f_name in listdir(fpath):
        # in my case, file names begin with '<number>-'
        if f_name.startswith(str(n)+'-'):
            f = f_name
            break
    return f

def print_fig(fig):
    #Convert plot to PNG image
    pngImage = BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    
    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

    return pngImageB64String

def plot(k, band, style):
    # image in 3 bands: g,r,i.
    dic = {1:'g',2:'r',3:'i'}
    
    #load data
    fits_name = search_fits(int(3*k)+int(band)-2)
    hdul = fits.open(str(fpath)+str(fits_name))
    img = hdul[1].data
    #log_img = logscale(img)
    
    fig = Figure()
    min_c = style[0]
    max_c = style[1]
    ax = fig.add_subplot(1,1,1)
    ax.axis('off')
    fig.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
    ax.imshow(img, 
              cmap='gray',
              aspect='auto', 
              norm=SymLogNorm(linthresh=0.3, linscale=1, 
                              vmin=min_c, vmax=max_c),
              )
    
    return print_fig(fig)
    
def RGB(k,sty):
    stretch = 2/(int(sty)+4)**1.5
    fits_names = ['']*3
    hduls = [None]*3
    for band in range(3):
        fits_names[band] = search_fits(int(3*k)+band-1)
        hduls[band] = fits.open(str(fpath)+str(fits_names[band]))

    image = make_lupton_rgb((hduls[2])[1].data,
                            (hduls[1])[1].data,
                            (hduls[0])[1].data,
                            stretch=stretch)
    
    fig = Figure()
    ax = fig.add_subplot(1,1,1)
    ax.axis('off')
    fig.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
    ax.imshow(image,aspect='auto')

    return print_fig(fig)
