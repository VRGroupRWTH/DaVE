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
reader.PointArrayStatus = ['ImageFile']                                 # OWN_DATA: every field has a name in a .vti file. Replace 'Scalars_' by the corresponding name

# create a new 'Disk'
disk1 = pvs.Disk(registrationName='Disk1')
disk1.InnerRadius = 0.0
disk1.OuterRadius = 0.14
disk1.RadialResolution = 20
disk1.CircumferentialResolution = 20

# create a new 'Transform'
transform1 = pvs.Transform(registrationName='Transform1', Input=disk1)
transform1.Transform = 'Transform'
transform1.Transform.Translate = [0.5, 0.1, 0.5]                        # OWN_DATA: This specifies the position and rotation of the disk that we use to seed the streamlines.
transform1.Transform.Rotate = [90.0, 0.0, 0.0]                          # OWN_DATA: For your application other positions or even other sources might be advantageous.

# create a new 'Mask Points'
maskPoints1 = pvs.MaskPoints(registrationName='MaskPoints1', Input=transform1)
maskPoints1.MaximumNumberofPoints = 100                                 # OWN_DATA: for more streamlines increase the number of points here.
maskPoints1.RandomSampling = 1
maskPoints1.RandomSamplingMode = 'Random Sampling'

# create a new 'Stream Tracer With Custom Source'
streamTracerWithCustomSource1 = pvs.StreamTracerWithCustomSource(registrationName='StreamTracerWithCustomSource1', Input=reader,SeedSource=maskPoints1)
streamTracerWithCustomSource1.Vectors = ['POINTS', 'ImageFile']         # OWN_DATA: change field name
streamTracerWithCustomSource1.MaximumStreamlineLength = 1.9920580079400003
streamTracerWithCustomSource1.IntegrationDirection = 'FORWARD'

# ----------------------------------------------------------------
# setup the views
# ----------------------------------------------------------------

#### disable automatic camera reset on 'Show'
pvs._DisableFirstRenderCameraReset()
pvs.LoadPalette('WhiteBackground')

renderView1 = pvs.GetActiveViewOrCreate('RenderView')
renderView1.OrientationAxesVisibility = 0
renderView1.CameraPosition = [5.203168734535207, 1.0812357936491124, 0.4960619903367559]
renderView1.CameraFocalPoint = [0.4960619903367558, 1.0812357936491124, 0.4960619903367559]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraViewAngle = 20.244328097731238
renderView1.CameraParallelScale = 1.2182888727290784

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

readerDisplay = pvs.Show(reader, renderView1, 'UniformGridRepresentation')
streamTracerWithCustomSource1Display = pvs.Show(streamTracerWithCustomSource1, renderView1, 'GeometryRepresentation')
streamTracerWithCustomSource1Display.RenderLinesAsTubes = 1
streamTracerWithCustomSource1Display.LineWidth = 2.0

imageFileLUT = pvs.GetColorTransferFunction('ImageFile')                # OWN_DATA: every field has a name in a .vti file. Replace 'Scalars_' by the corresponding name
imageFileLUTColorBar = pvs.GetScalarBar(imageFileLUT, renderView1)
imageFileLUTColorBar.Title = 'Velocity'                                 # OWN_DATA: change the name of the color bar according to what value is visualized
imageFileLUTColorBar.WindowLocation = 'Any Location'
imageFileLUTColorBar.Position = [0.9, 0.1]
imageFileLUTColorBar.ScalarBarLength = 0.8
imageFileLUTColorBar.ScalarBarThickness = 4
imageFileLUTColorBar.TitleFontSize = 16
imageFileLUTColorBar.LabelFontSize = 12
imageFileLUTColorBar.Visibility = 1

# pvs.ResetCamera(renderView1)                                          # OWN_DATA: if the original view does not fit, ResetCamera can be used to focus on the visible data

# save screenshot
pvs.SaveScreenshot('./output/streamline.png', 
    layout1, 
    ImageResolution=[1920, 1080],
    FontScaling='Do not scale fonts')
