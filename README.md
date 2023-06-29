FITS-Marker Version 0.1.1  
-----------
Update: 03/29/2023

**Description**

This is a program for FITS image labeling and categorizing, especially useful for a large amount (~ thousands) of FITS images.

It's written based on the book: *Flask Web Development: Developing Web Applications with Python* by Miguel Grinberg.

For us, we used it to mark 3649 galaxies from HSC-SSP, with 4 images (g, r, i, RGB) for each galaxy, and saved the results into a FITS table. (See our paper https://iopscience.iop.org/article/10.3847/1538-4365/ac85b1 for more scientific details.)

Additional features: Image contrast adjustment. Statistical tool for counting the number of galaxies in each type.

**Installation (Linux)**

You should have ```numpy, matplotlib, astropy, flask, flask-bootstrap, flask-wtf```  installed first.

(If you meet this problem when you are installing packages listed above (eg:`pip install flask-bootstrap`) :
`Could not fetch URL https://pypi.org/simple/pip/: There was a problem confirming the ssl certificate`
try:`pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org flask-bootstrap`)

Follow chapters 1 to 4 of the book mentioned above (it's easy to read), **OR**:

In the installation path:
  1) create a virtual environment (venv):```$ python3 -m venv venv```, then activate it: ```$ source venv/bin/activate``` 
  2) ```(venv) $ export FLASK_APP=main.py```
  3) ```(venv) $ export FLASK_ENV=development```
  4) ```(venv) $ flask run```
  
Then open ```localhost:5000/1``` from your browser.

**Notice:** The path to the folder containing FITS images and to the FITS table should be specified in the source code. 
