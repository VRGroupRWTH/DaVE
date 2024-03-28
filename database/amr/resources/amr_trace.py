# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10
import sys
from os.path import exists

#### import the simple module from the paraview
import paraview.simple as pvs

if len(sys.argv) < 2:
    print('no data file path provided - defaulting to "./data/amr_mesh.vthb"')
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
reader.CellArrayStatus = ['vtkGhostType', 'VectorXYZ', 'TestX', 'BlockId', 'Depth', 'Fractal Volume Fraction']       # OWN_DATA: change fields
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
renderView1.CameraPosition = [-0.5, 0.0, 6.830127018922194]             # OWN_DATA: change camera position if needed
renderView1.CameraFocalPoint = [-0.5, 0.0, 0.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 1.3879576132984246

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

# get 2D transfer function for 'Depth'
depthTF2D = pvs.GetTransferFunction2D('Depth')                          # OWN_DATA: change field

# get color transfer function/color map for 'Depth'
depthLUT = pvs.GetColorTransferFunction('Depth')                        # OWN_DATA: change field
depthLUT.TransferFunction2D = depthTF2D
depthLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 4.0, 0.865003, 0.865003, 0.865003, 8.0, 0.705882, 0.0156863, 0.14902]      # OWN_DATA: change range of field; format is [value, R, G, B, ...]
depthLUT.ScalarRangeInitialized = 1.0

# show data from reader
readerDisplay = pvs.Show(reader, renderView1, 'AMRRepresentation')
readerDisplay.Representation = 'Wireframe'
readerDisplay.ColorArrayName = ['CELLS', 'Depth']
readerDisplay.LookupTable = depthLUT
readerDisplay.SetScalarBarVisibility(renderView1, True)

# get color legend/bar for depthLUT in view renderView1
depthLUTColorBar = pvs.GetScalarBar(depthLUT, renderView1)
depthLUTColorBar.WindowLocation = 'Any Location'
depthLUTColorBar.Position = [0.7600950118764845, 0.04761904761904768]
depthLUTColorBar.Title = 'Depth'                                        # OWN_DATA: change title
depthLUTColorBar.ComponentTitle = ''
depthLUTColorBar.ScalarBarLength = 0.9031292517006804
depthLUTColorBar.AutomaticLabelFormat = 0
depthLUTColorBar.LabelFormat = '%-6.0f'
depthLUTColorBar.UseCustomLabels = 1                                    # OWN_DATA: remove for automatic labels
depthLUTColorBar.CustomLabels = list(range(9))                          # OWN_DATA: change field range
depthLUTColorBar.AddRangeLabels = 0
depthLUTColorBar.Visibility = 1


pvs.ResetCamera(renderView1)
# save screenshot
pvs.SaveScreenshot("./output/amr.png", layout1)
