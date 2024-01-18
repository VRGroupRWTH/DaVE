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

# create a new 'XML Image Data Reader'
reader = pvs.XMLImageDataReader(registrationName='reader', FileName=[filepath])
reader.PointArrayStatus = ['Scalars_']

# Properties modified on ctBonesvti
# reader.TimeArray = 'None'

pvs.UpdatePipeline(time=0.0, proxy=reader)

# create a new 'Contour'
contour1 = pvs.Contour(registrationName='Contour1', Input=reader)
contour1.ContourBy = ['POINTS', 'Scalars_']                         # OWN_DATA: every field has a name in a .vti file. Replace 'Scalars_' by the corresponding name
contour1.Isosurfaces = [100.0]                                      # OWN_DATA: depending on the data other iso values might be of interes which can be specified here
contour1.PointMergeMethod = 'Uniform Binning'

pvs.UpdatePipeline(time=0.0, proxy=contour1)

# |                       |
# | rendering stuff below |
# v                       v

#### disable automatic camera reset on 'Show'
pvs._DisableFirstRenderCameraReset()
pvs.LoadPalette('WhiteBackground')
renderView1 = pvs.GetActiveViewOrCreate('RenderView')
renderView1.OrientationAxesVisibility = 0

# contour1Display = pvs.Show(contour1, renderView1, 'GeometryRepresentation')
contour1Display = pvs.Show(contour1, renderView1)

# current camera placement for renderView1
renderView1.CameraPosition = [-450.09328651352865, 187.0918092385905, 76.60307205636042]
renderView1.CameraFocalPoint = [127.00789008867332, 118.83463710226165, 120.49464749112177]
renderView1.CameraViewUp = [-0.11763147206941053, -0.9930545901265777, 0.002327618378984832]
renderView1.CameraParallelScale = 220.83647796503186

# save screenshot
pvs.SaveScreenshot('./output/isocontour.png', 
    renderView1, 
    ImageResolution=[1920, 1080],
    FontScaling='Do not scale fonts')
