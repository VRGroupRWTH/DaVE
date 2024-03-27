# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10
import sys
from os.path import exists

#### import the simple module from the paraview
import paraview.simple as pvs

if len(sys.argv) < 2:
    print('no data file path provided - defaulting to "./data/miranda.nhdr"')
    filepath = './data/miranda.nhdr'
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
reader.PointArrayStatus = ['ImageFile']
reader.TimeArray = 'None'

# create a new 'Calculator'
calculator1 = pvs.Calculator(registrationName='Calculator1', Input=reader)
calculator1.ResultArrayName = 'velocity magnitude'
calculator1.Function = 'mag(ImageFile)'

# create a new 'Compute Derivatives'
computeDerivatives1 = pvs.ComputeDerivatives(registrationName='ComputeDerivatives1', Input=calculator1)
computeDerivatives1.Scalars = ['POINTS', 'velocity magnitude']
computeDerivatives1.Vectors = ['POINTS', 'ImageFile']

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
renderView1.ViewSize = [2105, 1176]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [0.49976657320803497, 1.001732429373078, 0.5004422459169291]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [5.250449021464962, 1.001732429373078, 0.5004422459169291]
renderView1.CameraFocalPoint = [0.49976657320803497, 1.001732429373078, 0.5004422459169291]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraViewAngle = 16.42121931908155
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 1.2295670948431632
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = pvs.CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(2105, 1176)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from reader
readerDisplay = pvs.Show(reader, renderView1, 'UniformGridRepresentation')
readerDisplay.Representation = 'Outline'
readerDisplay.ColorArrayName = ['POINTS', '']
readerDisplay.SelectTCoordArray = 'None'
readerDisplay.SelectNormalArray = 'None'
readerDisplay.SelectTangentArray = 'None'
readerDisplay.OSPRayScaleArray = 'ImageFile'
readerDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
readerDisplay.SelectOrientationVectors = 'ImageFile'
readerDisplay.ScaleFactor = 0.2003921759
readerDisplay.SelectScaleArray = 'ImageFile'
readerDisplay.GlyphType = 'Arrow'
readerDisplay.GlyphTableIndexArray = 'ImageFile'
readerDisplay.GaussianRadius = 0.010019608795
readerDisplay.SetScaleArray = ['POINTS', 'ImageFile']
readerDisplay.ScaleTransferFunction = 'PiecewiseFunction'
readerDisplay.OpacityArray = ['POINTS', 'ImageFile']
readerDisplay.OpacityTransferFunction = 'PiecewiseFunction'
readerDisplay.DataAxesGrid = 'GridAxesRepresentation'
readerDisplay.PolarAxes = 'PolarAxesRepresentation'
readerDisplay.ScalarOpacityUnitDistance = 0.007629149036258721
readerDisplay.OpacityArrayName = ['POINTS', 'ImageFile']
readerDisplay.ColorArray2Name = ['POINTS', 'ImageFile']
readerDisplay.IsosurfaceValues = [2.9499926567077637]
readerDisplay.SliceFunction = 'Plane'
readerDisplay.Slice = 127
readerDisplay.SelectInputVectors = ['POINTS', 'ImageFile']
readerDisplay.WriteLog = ''
readerDisplay.ScaleTransferFunction.Points = [-11.504826545715332, 0.0, 0.5, 0.0, 17.40481185913086, 1.0, 0.5, 0.0]
readerDisplay.OpacityTransferFunction.Points = [-11.504826545715332, 0.0, 0.5, 0.0, 17.40481185913086, 1.0, 0.5, 0.0]
readerDisplay.SliceFunction.Origin = [0.5000000474999999, 1.0019608795, 0.5000000474999999]

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
tensorGlyph1Display.SelectTCoordArray = 'None'
tensorGlyph1Display.SelectNormalArray = 'Normals'
tensorGlyph1Display.SelectTangentArray = 'None'
tensorGlyph1Display.OSPRayScaleArray = 'velocity magnitude'
tensorGlyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tensorGlyph1Display.SelectOrientationVectors = 'None'
tensorGlyph1Display.ScaleFactor = 0.20093630144838245
tensorGlyph1Display.SelectScaleArray = 'velocity magnitude'
tensorGlyph1Display.GlyphType = 'Arrow'
tensorGlyph1Display.GlyphTableIndexArray = 'velocity magnitude'
tensorGlyph1Display.GaussianRadius = 0.010046815072419122
tensorGlyph1Display.SetScaleArray = ['POINTS', 'velocity magnitude']
tensorGlyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
tensorGlyph1Display.OpacityArray = ['POINTS', 'velocity magnitude']
tensorGlyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
tensorGlyph1Display.DataAxesGrid = 'GridAxesRepresentation'
tensorGlyph1Display.PolarAxes = 'PolarAxesRepresentation'
tensorGlyph1Display.SelectInputVectors = ['POINTS', 'Normals']
tensorGlyph1Display.WriteLog = ''
tensorGlyph1Display.ScaleTransferFunction.Points = [0.0038724802434444427, 0.0, 0.5, 0.0, 14.143436431884766, 1.0, 0.5, 0.0]
tensorGlyph1Display.OpacityTransferFunction.Points = [0.0038724802434444427, 0.0, 0.5, 0.0, 14.143436431884766, 1.0, 0.5, 0.0]
tensorGlyph1Display.SetScalarBarVisibility(renderView1, True)

# get color legend/bar for velocitymagnitudeLUT in view renderView1
velocitymagnitudeLUTColorBar = pvs.GetScalarBar(velocitymagnitudeLUT, renderView1)
velocitymagnitudeLUTColorBar.Orientation = 'Horizontal'
velocitymagnitudeLUTColorBar.WindowLocation = 'Any Location'
velocitymagnitudeLUTColorBar.Position = [0.043990498812351606, 0.9311904761904762]
velocitymagnitudeLUTColorBar.Title = 'velocity magnitude'
velocitymagnitudeLUTColorBar.ComponentTitle = ''
velocitymagnitudeLUTColorBar.ScalarBarLength = 0.9124228028503563
velocitymagnitudeLUTColorBar.Visibility = 1

# get opacity transfer function/opacity map for 'velocitymagnitude'
velocitymagnitudePWF = pvs.GetOpacityTransferFunction('velocitymagnitude')
velocitymagnitudePWF.Points = [0.003872480197107731, 0.0, 0.5, 0.0, 14.143436431884766, 1.0, 0.5, 0.0]
velocitymagnitudePWF.ScalarRangeInitialized = 1

# save screenshot
pvs.SaveScreenshot("./output/velocity_gradient_tensor.png", layout1)
