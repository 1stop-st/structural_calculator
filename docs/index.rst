.. structural_calculator documentation master file, created by
   sphinx-quickstart on Sat Jul  6 21:20:10 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to structural_calculator's documentation!
=================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Classes
=======

.. graphviz::

   strict digraph "Class Diagram" {
      node [shape=record]
      "Node" [label="{\N | + position \l| + displacement() :np.ndarray[np.double] \l}"]
      "Mass" [label="{\N | + mass \l}"]
      "Member" [label="{\N | + fixed() :np.ndarray[np.bool] \l + stiffness() :np.ndarray[np.double] \l + load() :np.ndarray[np.double] \l}"]
      "Bearing" [label="{\N | + fixed() :np.ndarray[np.bool] \l + stiffness() :np.ndarray[np.double] \l}"]
      "Beam" [label="{\N | + stiffness() :np.ndarray[np.double] \l}"]
      "Section" [label="{\N}"]
      "Shape" [label="{\N}"]
      "Density" [label="{\N | + density \l}"]
      "Elasticity" [label="{\N | + elasticity :np.double \l + poisson :np.double \l}"]
      "Material" [label="{\N}"]
      "Load" [label="{\N}"]
      "GravityLoad" [label="{\N | + acceleration :numpy.ndarray[np.double] \l}"]
      "Member" -> "Node" [arrowhead=none, taillabel="1..*", headlabel="2"]
      "Section" -> "Beam" [arrowhead=odiamond]
      "Mass" -> "Member" [arrowhead=odiamond]
      "GravityLoad" -> "Load" [style=dashed, arrowhead=onormal]
      "Density" -> "Material" [arrowhead=odiamond]
      "Material" -> "Section" [arrowhead=odiamond]
      "Elasticity" -> "Material" [arrowhead=odiamond]
      "Load" -> "Member" [arrowhead=none taillabel="0..*", headlabel="0..*"]
      "Shape" -> "Section" [arrowhead=odiamond]
      "Beam" -> "Member" [style=dashed, arrowhead=onormal]
      "Bearing" -> "Member" [style=dashed, arrowhead=onormal]
   }



APIs
====
.. automodule:: structural_calculator
   :members:
