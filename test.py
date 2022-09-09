import bd
import os

path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(path, 'DEFUN 1998-1999')

bd.createDefunciones(path)