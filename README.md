FITS-Marker Version 0.1.0  
-----------
Update: 01/28/2021

**Description**

This is a python written program for FITS images labeling and categorizing, especially useful for a large amount of FITS images.

It's written following this book: *Flask Web Development: Developing Web Applications with Python* by Miguel Grinberg.

In my case, I use it to mark 2187 galaxies from HSC-SSP, with 4 images (g, r, i, RGB) for each galaxy. I save the results into a FITS table.

Additional features: Image contrast adjustable. Statistical tool that can count the number of galaxies in each type.

**Installation**

You should have ```numpy, matplotlib, astropy, flask, flask-bootstrap, flask-wtf```  installed first.

Follow chapter 1 to 4 of the book mentioned above, **OR**:

In the installation path:
  1) create a virtual environment (venv):```$ python3 -m venv venv```, then activate it: ```$ source venv/bin/activate``` 
  2) ```(venv) $ export FLASK_APP=main.py```
  3) ```(venv) $ export FLASK_ENV=development```
  4) ```(venv) $ flask run```
  
Then in the web browser, enter URL: localhost:5000/1

**Notice:** Path to the folder containing FITS images and to the FITS table should be specified in the source code. 
