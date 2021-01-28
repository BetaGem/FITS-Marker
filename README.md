FITS-Marker Version 1.0  
-----------
Update: 01/28/2021

**Discription**

This is a program for FITS images categorizing, especially useful if you are working on a large ammount of FITS images.

It's written in JupyterLab in anaconda3 following *Flask Web Development* by Miguel Grinberg.

In my case, I use it to mark 2088 galaxies from HSC-SSP, with 4 images (g, r, i, RGB) for each galaxy. I save the results into a FITS table.

Image contrast adjustable. Statistical tool available.

**Installation**

You should have ```numpy, matplotlib, astropy, flask, flask-bootstrap, flask-wtf```  installed first.

In the installation path:
  1) create a virtual environment(venv), activate it: source <name>/bin/activate
  2) export FLASK_APP=main.py
  3) export FLASK_ENV=development
  4) flask run
  
Then in the web browser: localhost:5000
