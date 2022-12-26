FITS-Marker Version 0.1.0  
-----------
Update: 01/28/2021

**Description**

This is a program for FITS images labeling and categorizing, especially useful for a large amount (~ thousands) of FITS images.

It's written according to this book: *Flask Web Development: Developing Web Applications with Python* by Miguel Grinberg.

In my case, I use it to mark 3649 galaxies from HSC-SSP, with 4 images (g, r, i, RGB) for each galaxy. I save the results into a FITS table. (See https://iopscience.iop.org/article/10.3847/1538-4365/ac85b1 for more detail.)

Additional features: Image contrast adjustment. Statistical tool for counting the number of galaxies in each type.

**Installation (Linux)**

You should have ```numpy, matplotlib, astropy, flask, flask-bootstrap, flask-wtf```  installed first.

Follow chapter 1 to 4 of the book mentioned above, **OR**:

In the installation path:
  1) create a virtual environment (venv):```$ python3 -m venv venv```, then activate it: ```$ source venv/bin/activate``` 
  2) ```(venv) $ export FLASK_APP=main.py```
  3) ```(venv) $ export FLASK_ENV=development```
  4) ```(venv) $ flask run```
  
Then in the web browser, enter this URL: localhost:5000/1

**Notice:** Path to the folder containing FITS images and to the FITS table should be specified in the source code. 
