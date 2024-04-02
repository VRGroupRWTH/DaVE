# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10
import sys
from os.path import exists

#### import the simple module from the paraview
import paraview.simple as pvs

if len(sys.argv) < 2:
    print('no data file path provided - defaulting to "./data/jet.vti"')
    filepath = './data/jet.vti'
else:
    filepath = str(sys.argv[1])

file_exists = exists(filepath)
if not file_exists:
    print("file ", filepath," does not exist", file=sys.stderr)

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Image Data Reader'
reader = pvs.XMLImageDataReader(registrationName='reader', FileName=[filepath])
reader.PointArrayStatus = ['ImageFile']                                     # OWN_DATA: every field has a name in a .vti file. Replace 'Scalars_' by the corresponding name
reader.TimeArray = 'None'

# create a new 'Calculator'
calculator1 = pvs.Calculator(registrationName='Calculator1', Input=reader)
calculator1.ResultArrayName = 'velocity magnitude'
calculator1.Function = 'mag(ImageFile)'

# create a new 'Compute Derivatives'
computeDerivatives1 = pvs.ComputeDerivatives(registrationName='ComputeDerivatives1', Input=calculator1)
computeDerivatives1.Scalars = ['POINTS', 'velocity magnitude']
computeDerivatives1.Vectors = ['POINTS', 'ImageFile']                       # OWN_DATA: change field name

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = pvs.CellDatatoPointData(registrationName='CellDatatoPointData1', Input=computeDerivatives1)
cellDatatoPointData1.CellDataArraytoprocess = ['ScalarGradient', 'VectorGradient']

# create a new 'Mask Points'
maskPoints1 = pvs.MaskPoints(registrationName='MaskPoints1', Input=cellDatatoPointData1)
maskPoints1.RandomSampling = 1

# create a new 'Tensor Glyph'
tensorGlyph1 = pvs.TensorGlyph(registrationName='TensorGlyph1', Input=maskPoints1, GlyphType='Sphere')
tensorGlyph1.Tensors = ['POINTS', 'VectorGradient']
tensorGlyph1.Scalars = ['POINTS', 'velocity magnitude']                     
tensorGlyph1.ScaleFactor = 0.001

# ----------------------------------------------------------------
# setup the views
# ----------------------------------------------------------------

#### disable automatic camera reset on 'Show'
pvs._DisableFirstRenderCameraReset()
pvs.LoadPalette('WhiteBackground')

# get the material library
materialLibrary1 = pvs.GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = pvs.CreateView('RenderView')
renderView1.CameraPosition = [5.250449021464962, 1.001732429373078, 0.5004422459169291]
renderView1.CameraFocalPoint = [0.49976657320803497, 1.001732429373078, 0.5004422459169291]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraViewAngle = 16.42121931908155

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = pvs.CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(1920, 1080)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from reader
readerDisplay = pvs.Show(reader, renderView1, 'UniformGridRepresentation')
readerDisplay.Representation = 'Outline'

# get 2D transfer function for 'velocitymagnitude'
velocitymagnitudeTF2D = pvs.GetTransferFunction2D('velocitymagnitude')

# get color transfer function/color map for 'velocitymagnitude'
velocitymagnitudeLUT = pvs.GetColorTransferFunction('velocitymagnitude')
velocitymagnitudeLUT.TransferFunction2D = velocitymagnitudeTF2D
velocitymagnitudeLUT.RGBPoints = [0.003872480197107731, 0.231373, 0.298039, 0.752941, 7.073654456040937, 0.865003, 0.865003, 0.865003, 14.143436431884766, 0.705882, 0.0156863, 0.14902]
velocitymagnitudeLUT.ScalarRangeInitialized = 1.0

# show data from tensorGlyph1
tensorGlyph1Display = pvs.Show(tensorGlyph1, renderView1, 'GeometryRepresentation')
tensorGlyph1Display.Representation = 'Surface'
tensorGlyph1Display.ColorArrayName = ['POINTS', 'velocity magnitude']
tensorGlyph1Display.LookupTable = velocitymagnitudeLUT
tensorGlyph1Display.SetScalarBarVisibility(renderView1, True)

# get color legend/bar for velocitymagnitudeLUT in view renderView1
velocitymagnitudeLUTColorBar = pvs.GetScalarBar(velocitymagnitudeLUT, renderView1)
velocitymagnitudeLUTColorBar.Orientation = 'Horizontal'
velocitymagnitudeLUTColorBar.WindowLocation = 'Any Location'
velocitymagnitudeLUTColorBar.Position = [0.043990498812351606, 0.9311904761904762]
velocitymagnitudeLUTColorBar.Title = 'velocity magnitude'                           # OWN_DATA: change color bar title
velocitymagnitudeLUTColorBar.ComponentTitle = ''
velocitymagnitudeLUTColorBar.ScalarBarLength = 0.9124228028503563
velocitymagnitudeLUTColorBar.Visibility = 1

# save screenshot
pvs.SaveScreenshot("./output/velocity_gradient_tensor.png", layout1)
