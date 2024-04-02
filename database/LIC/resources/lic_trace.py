# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10
import sys
from os.path import exists

#### import the simple module from the paraview
import paraview.simple as pvs

if len(sys.argv) < 2:
    print('no data file path provided - defaulting to "./data/spherical001.nc"')
    filepath = './data/spherical001.nc'
else:
    filepath = str(sys.argv[1])

file_exists = exists(filepath)
if not file_exists:
    print("file ", filepath," does not exist", file=sys.stderr)

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'NetCDF Reader'
reader = pvs.NetCDFReader(registrationName='spherical001.nc', FileName=[filepath])
reader.Dimensions = '(lat, r, lon)'                                 # OWN_DATA: the example data specifies the dimensions in latitude, radius and longitude; change as needed

# create a new 'Calculator'
calculator1 = pvs.Calculator(registrationName='Calculator1', Input=reader)
calculator1.AttributeType = 'Cell Data'
calculator1.ResultArrayName = 'velocity'
calculator1.Function = '(iHat*vx + jHat*vy + kHat*vz) * 1e9'        # OWN_DATA: depending on the data velocity may be retrieved differently
    

# create a new 'Clip'
clip1 = pvs.Clip(registrationName='Clip1', Input=calculator1)
clip1.ClipType = 'Box'
clip1.Invert = 0
clip1.ClipType.Length = [12756.185782244429, 12756.307890537775, 12756.305636130483]

# create a new 'Clip'
clip2 = pvs.Clip(registrationName='Clip2', Input=calculator1)
clip2.ClipType = 'Sphere'
clip2.ClipType.Center = [-0.12210887778564938, 0.0, 0.0]
clip2.ClipType.Radius = 3490.0

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = pvs.CellDatatoPointData(registrationName='CellDatatoPointData1', Input=clip1)
cellDatatoPointData1.CellDataArraytoprocess = ['velocity']

# ----------------------------------------------------------------
# setup the views
# ----------------------------------------------------------------

#### disable automatic camera reset on 'Show'
pvs._DisableFirstRenderCameraReset()
pvs.LoadPalette('WhiteBackground')

renderView1 = pvs.GetActiveViewOrCreate('RenderView')
renderView1.OrientationAxesVisibility = 0
renderView1.CameraPosition = [13753.608458927734, 11769.453858771536, 13166.256540152988]           # OWN_DATA: depending on the data another camera view is needed
renderView1.CameraFocalPoint = [3677.7997430754835, 3264.3641288520075, 2659.373734152541]
renderView1.CameraViewUp = [-0.36756198218116604, 0.8631511241486457, -0.34622005449710963]
renderView1.CameraParallelScale = 4363.638893631146

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

# get 2D transfer function for 'velocity'
velocityTF2D = pvs.GetTransferFunction2D('velocity')

# get color transfer function/color map for 'velocity'
velocityLUT = pvs.GetColorTransferFunction('velocity')
velocityLUT.TransferFunction2D = velocityTF2D
velocityLUT.RGBPoints = [0.00017033977330598138, 0.231373, 0.298039, 0.752941, 5.070484048900841, 0.865003, 0.865003, 0.865003, 10.140797758028375, 0.705882, 0.0156863, 0.14902]
velocityLUT.ScalarRangeInitialized = 1.0

# show data from cellDatatoPointData1
cellDatatoPointData1Display = pvs.Show(cellDatatoPointData1, renderView1, 'UnstructuredGridRepresentation')
cellDatatoPointData1Display.Representation = 'Surface LIC'
cellDatatoPointData1Display.ColorArrayName = ['POINTS', 'velocity']
cellDatatoPointData1Display.LookupTable = velocityLUT
cellDatatoPointData1Display.SelectInputVectors = ['POINTS', 'velocity']
cellDatatoPointData1Display.LICIntensity = 0.5
cellDatatoPointData1Display.EnhanceContrast = 'LIC and Color'

# show data from clip2
clip2Display = pvs.Show(clip2, renderView1, 'UnstructuredGridRepresentation')
clip2Display.Representation = 'Surface'
clip2Display.ColorArrayName = ['POINTS', '']
clip2Display.DiffuseColor = [0.0, 0.0, 0.0]

# get color legend/bar for velocityLUT in view renderView1
velocityLUTColorBar = pvs.GetScalarBar(velocityLUT, renderView1)
velocityLUTColorBar.WindowLocation = 'Upper Right Corner'
velocityLUTColorBar.Position = [0.9, 0.1]
velocityLUTColorBar.Title = 'velocity'
velocityLUTColorBar.ComponentTitle = 'Magnitude'
velocityLUTColorBar.ScalarBarLength = 0.8
velocityLUTColorBar.Visibility = 1

#pvs.ResetCamera(renderView1)                           # OWN_DATA: if the original view does not fit ResetCamera can be used to focus on the visible data

# save screenshot
pvs.SaveScreenshot('./output/lic.png', 
    layout1, 
    FontScaling='Do not scale fonts')
