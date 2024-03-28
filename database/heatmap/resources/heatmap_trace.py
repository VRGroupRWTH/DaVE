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
reader.Dimensions = '(lat, r, lon)'         # OWN_DATA: the example data specifies the dimensions in latitude, radius and longitude; change as needed

# create a new 'Clip'
clip1 = pvs.Clip(registrationName='Clip1', Input=reader)
clip1.ClipType = 'Box'
clip1.Invert = 0
clip1.ClipType.Length = [12756.185782244429, 12756.307890537775, 12756.305636130483]

# create a new 'Clip'
clip2 = pvs.Clip(registrationName='Clip2', Input=reader)
clip2.ClipType = 'Sphere'
clip2.ClipType.Center = [-0.12210887778564938, 0.0, 0.0]
clip2.ClipType.Radius = 3490.0

# ----------------------------------------------------------------
# setup the views
# ----------------------------------------------------------------

#### disable automatic camera reset on 'Show'
pvs._DisableFirstRenderCameraReset()
pvs.LoadPalette('WhiteBackground')

renderView1 = pvs.GetActiveViewOrCreate('RenderView')
renderView1.OrientationAxesVisibility = 0
renderView1.UseAmbientOcclusion = 1

# OWN_DATA: depending on the data another camera view is needed
renderView1.CameraPosition = [13753.608458927734, 11769.453858771536, 13166.256540152988]
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

# get 2D transfer function for 'temperature'
temperatureTF2D = pvs.GetTransferFunction2D('temperature')                  # OWN_DATA: change field if needed

# get color transfer function/color map for 'temperature'
temperatureLUT = pvs.GetColorTransferFunction('temperature')                # OWN_DATA: change field if needed
temperatureLUT.TransferFunction2D = temperatureTF2D
temperatureLUT.RGBPoints = [293.0, 0.0, 0.0, 0.0, 1618.7375000000002, 0.901960784314, 0.0, 0.0, 2944.4750000000004, 0.901960784314, 0.901960784314, 0.0, 3607.34375, 1.0, 1.0, 1.0]    # OWN_DATA: change RGB points for transfer function depending on data, format is [value, R, G, B, ...]
temperatureLUT.ColorSpace = 'RGB'
temperatureLUT.NanColor = [0.0, 0.498039215686, 1.0]
temperatureLUT.ScalarRangeInitialized = 1.0

clip1Display = pvs.Show(clip1, renderView1, 'UnstructuredGridRepresentation')
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['CELLS', 'temperature']                      # OWN_DATA: change field if needed
clip1Display.LookupTable = temperatureLUT
clip1Display.SetScalarBarVisibility(renderView1, True)

# show data from clip2
clip2Display = pvs.Show(clip2, renderView1, 'UnstructuredGridRepresentation')
clip2Display.Representation = 'Surface'
clip2Display.ColorArrayName = ['CELLS', 'temperature']                      # OWN_DATA: change field if needed
clip2Display.LookupTable = temperatureLUT
clip2Display.SetScalarBarVisibility(renderView1, True)

# get color legend/bar for temperatureLUT in view renderView1
temperatureLUTColorBar = pvs.GetScalarBar(temperatureLUT, renderView1)
temperatureLUTColorBar.WindowLocation = 'Upper Right Corner'
temperatureLUTColorBar.Position = [0.9, 0.1]
temperatureLUTColorBar.Title = 'temperature'                                # OWN_DATA: change title depending on what field is shown
temperatureLUTColorBar.ComponentTitle = ''
temperatureLUTColorBar.ScalarBarLength = 0.8
temperatureLUTColorBar.Visibility = 1


pvs.ResetCamera(renderView1)

# save screenshot
pvs.SaveScreenshot('./output/heatmap.png', 
    renderView1, 
    ImageResolution=[1920, 1080],
    FontScaling='Do not scale fonts')
