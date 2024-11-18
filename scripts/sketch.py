import cadquery as cq
from cadquery.vis import show, show_object
import pyvista as pv


def sketch():

  result = (
      cq.Sketch()
      .trapezoid(4, 3, 90)
      .vertices()
      .circle(0.5, mode="s")
      .reset()
      .vertices()
      .fillet(0.25)
      .reset()
      .rarray(0.6, 1, 5, 1)
      .slot(1.5, 0.4, mode="s", angle=90)
  )


  return result

def block():
  result = cq.Workplane("front").box(2.0, 2.0, 0.5)
 

  return result

if __name__ =="__main__":
  m = block()
  # creating shape
  shape =  m.val()


  # creating mesh
  mesh = shape.tessellate(tolerance=0.01)
  # creating vtk poly data
  vtkPolydata = shape.toVtkPolyData(tolerance=0.01)

  # show mesh model
  pv_polydata = pv.wrap(vtkPolydata)
  pv_polydata.plot()

  # showing cad model
  show_object(shape)




  
