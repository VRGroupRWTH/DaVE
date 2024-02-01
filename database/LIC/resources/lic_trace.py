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

# create a new 'NetCDF Reader'
reader = pvs.NetCDFReader(registrationName='spherical001.nc', FileName=[filepath])
reader.Dimensions = '(lat, r, lon)'

# create a new 'Calculator'
calculator1 = pvs.Calculator(registrationName='Calculator1', Input=reader)
calculator1.AttributeType = 'Cell Data'
calculator1.ResultArrayName = 'velocity'
calculator1.Function = '(iHat*vx + jHat*vy + kHat*vz) * 1e9'

# create a new 'Clip'
clip1 = pvs.Clip(registrationName='Clip1', Input=calculator1)
clip1.ClipType = 'Box'
clip1.Invert = 0
clip1.ClipType.Length = [12756.185782244429, 12756.307890537775, 12756.305636130483]
clip1.HyperTreeGridClipper.Origin = [-0.12210887778564938, 0.0, 0.0]

# create a new 'Clip'
clip2 = pvs.Clip(registrationName='Clip2', Input=calculator1)
clip2.ClipType = 'Sphere'
clip2.ClipType.Center = [-0.12210887778564938, 0.0, 0.0]
clip2.ClipType.Radius = 3490.0
clip2.HyperTreeGridClipper.Origin = [-0.12210887778564938, 0.0, 0.0]

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = pvs.CellDatatoPointData(registrationName='CellDatatoPointData1', Input=clip1)
cellDatatoPointData1.CellDataArraytoprocess = ['velocity']

# |                       |
# | rendering stuff below |
# v                       v

#### disable automatic camera reset on 'Show'
pvs._DisableFirstRenderCameraReset()
pvs.LoadPalette('WhiteBackground')
renderView1 = pvs.GetActiveViewOrCreate('RenderView')
renderView1.OrientationAxesVisibility = 0
renderView1.ViewSize = [1920,1080]

# get 2D transfer function for 'velocity'
velocityTF2D = pvs.GetTransferFunction2D('velocity')

# get color transfer function/color map for 'velocity'
velocityLUT = pvs.GetColorTransferFunction('velocity')
velocityLUT.TransferFunction2D = velocityTF2D
velocityLUT.RGBPoints = [0.00017033977330598138, 0.231373, 0.298039, 0.752941, 5.070484048900841, 0.865003, 0.865003, 0.865003, 10.140797758028375, 0.705882, 0.0156863, 0.14902]
velocityLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'velocity'
velocityPWF = pvs.GetOpacityTransferFunction('velocity')
velocityPWF.Points = [0.00017033977330598138, 0.0, 0.5, 0.0, 10.140797758028375, 1.0, 0.5, 0.0]
velocityPWF.ScalarRangeInitialized = 1

# get color legend/bar for velocityLUT in view renderView1
velocityLUTColorBar = GetScalarBar(velocityLUT, renderView1)
velocityLUTColorBar.WindowLocation = 'Upper Right Corner'
velocityLUTColorBar.Position = [0.9, 0.1]
velocityLUTColorBar.Title = 'velocity'
velocityLUTColorBar.ComponentTitle = 'Magnitude'
velocityLUTColorBar.ScalarBarLength = 0.8
velocityLUTColorBar.Visibility = 1

cellDatatoPointData1Display = pvs.Show(cellDatatoPointData1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
cellDatatoPointData1Display.Representation = 'Surface LIC'
cellDatatoPointData1Display.ColorArrayName = ['POINTS', 'velocity']
cellDatatoPointData1Display.LookupTable = velocityLUT
cellDatatoPointData1Display.SelectTCoordArray = 'None'
cellDatatoPointData1Display.SelectNormalArray = 'None'
cellDatatoPointData1Display.SelectTangentArray = 'None'
cellDatatoPointData1Display.OSPRayScaleArray = 'spin transition-induced density anomaly'
cellDatatoPointData1Display.OSPRayScaleFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.SelectOrientationVectors = 'velocity'
cellDatatoPointData1Display.ScaleFactor = 1275.6307890537776
cellDatatoPointData1Display.SelectScaleArray = 'None'
cellDatatoPointData1Display.GlyphType = 'Arrow'
cellDatatoPointData1Display.GlyphTableIndexArray = 'None'
cellDatatoPointData1Display.GaussianRadius = 63.781539452688875
cellDatatoPointData1Display.SetScaleArray = ['POINTS', 'spin transition-induced density anomaly']
cellDatatoPointData1Display.ScaleTransferFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.OpacityArray = ['POINTS', 'spin transition-induced density anomaly']
cellDatatoPointData1Display.OpacityTransferFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.DataAxesGrid = 'GridAxesRepresentation'
cellDatatoPointData1Display.PolarAxes = 'PolarAxesRepresentation'
cellDatatoPointData1Display.ScalarOpacityFunction = velocityPWF
cellDatatoPointData1Display.ScalarOpacityUnitDistance = 98.02154370149897
cellDatatoPointData1Display.OpacityArrayName = ['POINTS', 'spin transition-induced density anomaly']
cellDatatoPointData1Display.SelectInputVectors = ['POINTS', 'velocity']
cellDatatoPointData1Display.LICIntensity = 0.5
cellDatatoPointData1Display.EnhanceContrast = 'LIC and Color'
cellDatatoPointData1Display.MaskOnSurface = 0
cellDatatoPointData1Display.MaskThreshold = 0.01
cellDatatoPointData1Display.NoiseGrainSize = 1
cellDatatoPointData1Display.WriteLog = ''

# show data from clip2
clip2Display = pvs.Show(clip2, renderView1, 'UnstructuredGridRepresentation')
clip2Display.Representation = 'Surface'
# clip2Display.ColorArrayName = ['CELLS', 'temperature']
clip2Display.ColorArrayName = ['POINTS', '']
clip2Display.DiffuseColor = [0.0, 0.0, 0.0]
# clip2Display.LookupTable = temperatureLUT
clip2Display.SelectTCoordArray = 'None'
clip2Display.SelectNormalArray = 'None'
clip2Display.SelectTangentArray = 'None'
clip2Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip2Display.SelectOrientationVectors = 'None'
clip2Display.ScaleFactor = 697.992928559976
clip2Display.SelectScaleArray = 'None'
clip2Display.GlyphType = 'Arrow'
clip2Display.GlyphTableIndexArray = 'None'
clip2Display.GaussianRadius = 34.8996464279988
clip2Display.SetScaleArray = [None, '']
clip2Display.ScaleTransferFunction = 'PiecewiseFunction'
clip2Display.OpacityArray = [None, '']
clip2Display.OpacityTransferFunction = 'PiecewiseFunction'
clip2Display.DataAxesGrid = 'GridAxesRepresentation'
clip2Display.PolarAxes = 'PolarAxesRepresentation'
# clip2Display.ScalarOpacityFunction = temperaturePWF
clip2Display.ScalarOpacityUnitDistance = 238.89583706950714
clip2Display.OpacityArrayName = ['CELLS', 'spin transition-induced density anomaly']
clip2Display.SelectInputVectors = [None, '']
clip2Display.WriteLog = ''

renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [3188.9853911222144, 3189.076972634444, 3189.0764090326206]
renderView1.Exposure = 1.1
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [13753.608458927734, 11769.453858771536, 13166.256540152988]
renderView1.CameraFocalPoint = [3677.7997430754835, 3264.3641288520075, 2659.373734152541]
renderView1.CameraViewUp = [-0.36756198218116604, 0.8631511241486457, -0.34622005449710963]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 4363.638893631146
renderView1.UseAmbientOcclusion = 0
# renderView1.BackEnd = 'OSPRay raycaster'
# renderView1.OSPRayMaterialLibrary = materialLibrary1

# save screenshot
pvs.SaveScreenshot('./output/lic.png', 
    renderView1, 
    ImageResolution=[1920, 1080],
    FontScaling='Do not scale fonts')
