# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10
import sys
from os.path import exists

#### import the simple module from the paraview
import paraview.simple as pvs

if len(sys.argv) < 2:
    print('no data file path provided - defaulting to "./data/ctBones.vti"')
    filepath = './data/ctBones.vti'
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
reader.PointArrayStatus = ['Scalars_']                                                      # OWN_DATA: every field has a name in a .vti file. Replace 'Scalars_' by the corresponding name

# ----------------------------------------------------------------
# setup the views
# ----------------------------------------------------------------

#### disable automatic camera reset on 'Show'
pvs._DisableFirstRenderCameraReset()
pvs.LoadPalette('WhiteBackground')

# get active view
renderView1 = pvs.GetActiveViewOrCreate('RenderView')
renderView1.OrientationAxesVisibility = 0

# current camera placement for renderView1
renderView1.CameraPosition = [-423.3902339590129, 198.44191188274755, 304.85091798628196]       # OWN_DATA: change camera position if needed
renderView1.CameraFocalPoint = [120.98375218527654, 119.8419039072476, 112.21062642326825]
renderView1.CameraViewUp = [-0.26270924860874034, -0.8866291025912916, -0.3806214459717057]
renderView1.CameraParallelScale = 220.83647796503186

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

# get 2D transfer function for 'Scalars_'                                                            
scalars_TF2D = pvs.GetTransferFunction2D('Scalars_')                    # OWN_DATA: change field
scalars_TF2D.ScalarRangeInitialized = 1
scalars_TF2D.Range = [0.0, 255.0, 0.0, 1.0]

# get color transfer function/color map for 'Scalars_'                                               
scalars_LUT = pvs.GetColorTransferFunction('Scalars_')                  # OWN_DATA: change field
scalars_LUT.AutomaticRescaleRangeMode = 'Never'
scalars_LUT.TransferFunction2D = scalars_TF2D
scalars_LUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 127.5, 0.865003, 0.865003, 0.865003, 255.0, 0.705882, 0.0156863, 0.14902]
scalars_LUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Scalars_'                                           
scalars_PWF = pvs.GetOpacityTransferFunction('Scalars_')                # OWN_DATA: change field
scalars_PWF.Points = [0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]
scalars_PWF.ScalarRangeInitialized = 1

# show data in view
ctBonesvtiDisplay = pvs.Show(reader, renderView1)
ctBonesvtiDisplay.Representation = 'Volume'
ctBonesvtiDisplay.ColorArrayName = ['POINTS', 'Scalars_']
ctBonesvtiDisplay.LookupTable = scalars_LUT
ctBonesvtiDisplay.OpacityArray = ['POINTS', 'Scalars_']                 # OWN_DATA: change field
ctBonesvtiDisplay.OpacityTransferFunction = 'PiecewiseFunction'
ctBonesvtiDisplay.ScalarOpacityUnitDistance = 1.7320508075688774
ctBonesvtiDisplay.ScalarOpacityFunction = scalars_PWF
ctBonesvtiDisplay.TransferFunction2D = scalars_TF2D
ctBonesvtiDisplay.OpacityArrayName = ['POINTS', 'Scalars_']             # OWN_DATA: change field

# get color legend/bar for scalars_LUT in view renderView1
scalars_LUTColorBar = pvs.GetScalarBar(scalars_LUT, renderView1)
scalars_LUTColorBar.WindowLocation = 'Any Location'
scalars_LUTColorBar.Position = [0.8755364806866953, 0.022857142857142857]
scalars_LUTColorBar.Title = 'density'                                   # OWN_DATA: change title
scalars_LUTColorBar.ComponentTitle = ''
scalars_LUTColorBar.ScalarBarLength = 0.9147619047619047
scalars_LUTColorBar.Visibility = 1

pvs.ResetCamera(renderView1)                                            # OWN_DATA: if the original view does not fit ResetCamera can be used to focus on the visible data

# save screenshot
pvs.SaveScreenshot('./output/volumerender.png', 
    layout1, 
    FontScaling='Do not scale fonts')
