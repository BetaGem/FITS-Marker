FITS-Marker Version 0.0.1  
-----------
Update: 01/28/2021

**Discription**

This is a program for FITS images categorizing, especially useful if you are working on a large amount of FITS images.

It's written with anaconda 3 following this book: *Flask Web Development: Developing Web Applications with Python* by Miguel Grinberg.

In my case, I use it to mark 2088 galaxies from HSC-SSP, with 4 images (g, r, i, RGB) for each galaxy. I save the results into a FITS table.

Image contrast adjustable. Statistical tool available.

**Installation**

You should have ```numpy, matplotlib, astropy, flask, flask-bootstrap, flask-wtf```  installed first.

Follow chapter 1 to 4 of the book mentioned above, **OR**:

In the installation path:
  1) create a virtual environment (venv):```$ python3 -m venv venv```, then activate it: ```$ source venv/bin/activate``` 
  2) ```(venv) $ export FLASK_APP=main.py```
  3) ```(venv) $ export FLASK_ENV=development```
  4) ```(venv) $ flask run```
  
Then in the web browser, enter URL: localhost:5000/1

**Notice:** Path to the folder containing FITS images and to the FITS table should be specified in source code. 
