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
    filepath = './data/amr_mesh.vthb'
else:
    filepath = str(sys.argv[1])

file_exists = exists(filepath)
if not file_exists:
    print("file ", filepath," does not exist", file=sys.stderr)

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML UniformGrid AMR Reader'
reader = pvs.XMLUniformGridAMRReader(registrationName='amr_mesh.vthb', FileName=[filepath])
reader.CellArrayStatus = ['vtkGhostType', 'VectorXYZ', 'TestX', 'BlockId', 'Depth', 'Fractal Volume Fraction']
reader.DefaultNumberOfLevels = 9
reader.TimeArray = 'None'

# ----------------------------------------------------------------
# setup the views
# ----------------------------------------------------------------

#### disable automatic camera reset on 'Show'
pvs._DisableFirstRenderCameraReset()
pvs.LoadPalette('WhiteBackground')

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = pvs.GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = pvs.CreateView('RenderView')
renderView1.ViewSize = [2105, 1176]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [-0.5, 0.0, 0.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-0.5, 0.0, 6.830127018922194]
renderView1.CameraFocalPoint = [-0.5, 0.0, 0.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 1.3879576132984246
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

# get 2D transfer function for 'Depth'
depthTF2D = pvs.GetTransferFunction2D('Depth')

# get color transfer function/color map for 'Depth'
depthLUT = pvs.GetColorTransferFunction('Depth')
depthLUT.TransferFunction2D = depthTF2D
depthLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 4.0, 0.865003, 0.865003, 0.865003, 8.0, 0.705882, 0.0156863, 0.14902]
depthLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Depth'
depthPWF = pvs.GetOpacityTransferFunction('Depth')
depthPWF.Points = [0.0, 0.0, 0.5, 0.0, 8.0, 1.0, 0.5, 0.0]
depthPWF.ScalarRangeInitialized = 1

# show data from reader
readerDisplay = pvs.Show(reader, renderView1, 'AMRRepresentation')
readerDisplay.Representation = 'Wireframe'
readerDisplay.ColorArrayName = ['CELLS', 'Depth']
readerDisplay.LookupTable = depthLUT
readerDisplay.SelectTCoordArray = 'None'
readerDisplay.SelectNormalArray = 'None'
readerDisplay.SelectTangentArray = 'None'
readerDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
readerDisplay.SelectOrientationVectors = 'None'
readerDisplay.ScaleFactor = 0.25
readerDisplay.SelectScaleArray = 'None'
readerDisplay.GlyphType = 'Arrow'
readerDisplay.GlyphTableIndexArray = 'None'
readerDisplay.GaussianRadius = 0.0125
readerDisplay.SetScaleArray = [None, '']
readerDisplay.ScaleTransferFunction = 'PiecewiseFunction'
readerDisplay.OpacityArray = [None, '']
readerDisplay.OpacityTransferFunction = 'PiecewiseFunction'
readerDisplay.DataAxesGrid = 'GridAxesRepresentation'
readerDisplay.PolarAxes = 'PolarAxesRepresentation'
readerDisplay.ScalarOpacityUnitDistance = 0.7617076894725414
readerDisplay.ScalarOpacityFunction = depthPWF
readerDisplay.SetScalarBarVisibility(renderView1, True)

# get color legend/bar for depthLUT in view renderView1
depthLUTColorBar = pvs.GetScalarBar(depthLUT, renderView1)
depthLUTColorBar.WindowLocation = 'Any Location'
depthLUTColorBar.Position = [0.7600950118764845, 0.04761904761904768]
depthLUTColorBar.Title = 'Depth'
depthLUTColorBar.ComponentTitle = ''
depthLUTColorBar.ScalarBarLength = 0.9031292517006804
depthLUTColorBar.AutomaticLabelFormat = 0
depthLUTColorBar.LabelFormat = '%-6.0f'
depthLUTColorBar.UseCustomLabels = 1
depthLUTColorBar.CustomLabels = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 0.0]
depthLUTColorBar.AddRangeLabels = 0
depthLUTColorBar.Visibility = 1

# save screenshot
pvs.SaveScreenshot("./output/amr.png", layout1)
