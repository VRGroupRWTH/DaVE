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
reader.PointArrayStatus = ['Scalars_']                              # OWN_DATA: every field has a name in a .vti file. Replace 'Scalars_' by the corresponding name

# create a new 'Contour'
contour1 = pvs.Contour(registrationName='Contour1', Input=reader)
contour1.ContourBy = ['POINTS', 'Scalars_']                         # OWN_DATA: every field has a name in a .vti file. Replace 'Scalars_' by the corresponding name
contour1.Isosurfaces = [100.0]                                      # OWN_DATA: depending on the data other iso values might be of interest which can be specified here
contour1.PointMergeMethod = 'Uniform Binning'

pvs.UpdatePipeline(time=0.0, proxy=contour1)

# ----------------------------------------------------------------
# setup the views
# ----------------------------------------------------------------

#### disable automatic camera reset on 'Show'
pvs._DisableFirstRenderCameraReset()
pvs.LoadPalette('WhiteBackground')

renderView1 = pvs.GetActiveViewOrCreate('RenderView')
renderView1.OrientationAxesVisibility = 0

# current camera placement for renderView1                          # OWN_DATA: depending on the data another camera view is needed
renderView1.CameraPosition = [-450.09328651352865, 187.0918092385905, 76.60307205636042]
renderView1.CameraFocalPoint = [127.00789008867332, 118.83463710226165, 120.49464749112177]
renderView1.CameraViewUp = [-0.11763147206941053, -0.9930545901265777, 0.002327618378984832]
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

# get color transfer function/color map for 'Scalars_'
scalars_LUT = pvs.GetColorTransferFunction('Scalars_')                  # OWN_DATA: change field
scalars_LUT.TransferFunction2D = scalars_TF2D
scalars_LUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 127.5, 0.865003, 0.865003, 0.865003, 255.0, 0.705882, 0.0156863, 0.14902]
scalars_LUT.ScalarRangeInitialized = 1.0

# show data from contour1
contour1Display = pvs.Show(contour1, renderView1, 'GeometryRepresentation')
contour1Display.Representation = 'Surface'
contour1Display.ColorArrayName = ['POINTS', 'Scalars_']                 # OWN_DATA: change field
contour1Display.SetScalarBarVisibility(renderView1, True)

# get color legend/bar for scalars_LUT in view renderView1
scalars_LUTColorBar = pvs.GetScalarBar(scalars_LUT, renderView1)
scalars_LUTColorBar.WindowLocation = 'Any Location'
scalars_LUTColorBar.Position = [0.8755364806866953, 0.022857142857142857]
scalars_LUTColorBar.Title = 'density'                                   # OWN_DATA: change title
scalars_LUTColorBar.ComponentTitle = ''
scalars_LUTColorBar.ScalarBarLength = 0.9147619047619047
scalars_LUTColorBar.Visibility = 1

# pvs.ResetCamera(renderView1)                                          # OWN_DATA: if the original view does not fit ResetCamera can be used to focus on the visible data

# save screenshot
pvs.SaveScreenshot('./output/isocontour.png', 
    layout1,
    FontScaling='Do not scale fonts')
