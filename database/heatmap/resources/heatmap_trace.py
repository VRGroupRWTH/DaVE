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

# create a new 'Clip'
clip1 = pvs.Clip(registrationName='Clip1', Input=reader)
clip1.ClipType = 'Box'
clip1.Invert = 0
clip1.ClipType.Length = [12756.185782244429, 12756.307890537775, 12756.305636130483]
clip1.HyperTreeGridClipper.Origin = [-0.12210887778564938, 0.0, 0.0]

# create a new 'Clip'
clip2 = pvs.Clip(registrationName='Clip2', Input=reader)
clip2.ClipType = 'Sphere'
clip2.ClipType.Center = [-0.12210887778564938, 0.0, 0.0]
clip2.ClipType.Radius = 3490.0
clip2.HyperTreeGridClipper.Origin = [-0.12210887778564938, 0.0, 0.0]

# |                       |
# | rendering stuff below |
# v                       v

#### disable automatic camera reset on 'Show'
pvs._DisableFirstRenderCameraReset()
pvs.LoadPalette('WhiteBackground')
renderView1 = pvs.GetActiveViewOrCreate('RenderView')
renderView1.OrientationAxesVisibility = 0

# get 2D transfer function for 'temperature'
temperatureTF2D = pvs.GetTransferFunction2D('temperature')

# get color transfer function/color map for 'temperature'
temperatureLUT = pvs.GetColorTransferFunction('temperature')
temperatureLUT.TransferFunction2D = temperatureTF2D
temperatureLUT.RGBPoints = [293.0, 0.0, 0.0, 0.0, 1618.7375000000002, 0.901960784314, 0.0, 0.0, 2944.4750000000004, 0.901960784314, 0.901960784314, 0.0, 3607.34375, 1.0, 1.0, 1.0]
temperatureLUT.ColorSpace = 'RGB'
temperatureLUT.NanColor = [0.0, 0.498039215686, 1.0]
temperatureLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'temperature'
temperaturePWF = pvs.GetOpacityTransferFunction('temperature')
temperaturePWF.Points = [293.0, 0.0, 0.5, 0.0, 3607.34375, 1.0, 0.5, 0.0]
temperaturePWF.ScalarRangeInitialized = 1

clip1Display = pvs.Show(clip1, renderView1, 'UnstructuredGridRepresentation')
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['CELLS', 'temperature']
clip1Display.LookupTable = temperatureLUT
clip1Display.Specular = 1.0
clip1Display.SpecularPower = 10.0
clip1Display.Roughness = 0.29
clip1Display.CoatStrength = 0.32
clip1Display.CoatIOR = 1.63
clip1Display.CoatRoughness = 0.48
clip1Display.SelectTCoordArray = 'None'
clip1Display.SelectNormalArray = 'None'
clip1Display.SelectTangentArray = 'None'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'None'
clip1Display.ScaleFactor = 637.8153945268888
clip1Display.SelectScaleArray = 'None'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'None'
clip1Display.GaussianRadius = 31.890769726344438
clip1Display.SetScaleArray = [None, '']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = [None, '']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = temperaturePWF
clip1Display.ScalarOpacityUnitDistance = 92.8847186728234
clip1Display.OpacityArrayName = ['CELLS', 'spin transition-induced density anomaly']
clip1Display.SelectInputVectors = [None, '']
clip1Display.WriteLog = ''

# show data from clip2
clip2Display = pvs.Show(clip2, renderView1, 'UnstructuredGridRepresentation')
clip2Display.Representation = 'Surface'
clip2Display.ColorArrayName = ['CELLS', 'temperature']
clip2Display.LookupTable = temperatureLUT
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
clip2Display.ScalarOpacityFunction = temperaturePWF
clip2Display.ScalarOpacityUnitDistance = 238.89583706950714
clip2Display.OpacityArrayName = ['CELLS', 'spin transition-induced density anomaly']
clip2Display.SelectInputVectors = [None, '']
clip2Display.WriteLog = ''

# setup the color legend parameters for each legend in this view

# get color legend/bar for temperatureLUT in view renderView1
temperatureLUTColorBar = pvs.GetScalarBar(temperatureLUT, renderView1)
temperatureLUTColorBar.WindowLocation = 'Upper Right Corner'
temperatureLUTColorBar.Position = [0.9, 0.1]
temperatureLUTColorBar.Title = 'temperature'
temperatureLUTColorBar.ComponentTitle = ''
temperatureLUTColorBar.ScalarBarLength = 0.8

# set color bar visibility
temperatureLUTColorBar.Visibility = 1

# show color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# show color legend
clip2Display.SetScalarBarVisibility(renderView1, True)

renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [3188.9853911222144, 3189.076972634444, 3189.0764090326206]
renderView1.Exposure = 1.1
renderView1.UseAmbientOcclusion = 1
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
pvs.SaveScreenshot('./output/heatmap.png', 
    renderView1, 
    ImageResolution=[1920, 1080],
    FontScaling='Do not scale fonts')
