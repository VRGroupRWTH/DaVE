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

# create a new 'XML Image Data Reader'
reader = pvs.XMLImageDataReader(registrationName='reader', FileName=[filepath])
reader.PointArrayStatus = ['ImageFile']                                 # OWN_DATA: every field has a name in a .vti file. Replace 'Scalars_' by the corresponding name
reader.TimeArray = 'None'

# create a new 'Glyph'
glyph1 = pvs.Glyph(registrationName='Glyph1', Input=reader,
    GlyphType='Arrow')
glyph1.OrientationArray = ['POINTS', 'ImageFile']
glyph1.ScaleArray = ['POINTS', 'ImageFile']
glyph1.ScaleFactor = 0.024047037060938886
glyph1.GlyphTransform = 'Transform2'

pvs.UpdatePipeline(time=0.0, proxy=glyph1)

# |                       |
# | rendering stuff below |
# v                       v

#### disable automatic camera reset on 'Show'
pvs._DisableFirstRenderCameraReset()
pvs.LoadPalette('WhiteBackground')
renderView1 = pvs.GetActiveViewOrCreate('RenderView')
renderView1.ViewSize = [990, 789]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [0.4906297167763114, 1.0381428503314964, 0.5006610233103856]
renderView1.StereoType = 'Crystal Eyes'
# renderView1.CameraPosition = [5.372398107318557, 1.0381428503314964, 0.5006610233103856]
renderView1.CameraPosition = [4.5, 1.0381428503314964, 0.5006610233103856]
renderView1.CameraFocalPoint = [0.4906297167763114, 1.0381428503314964, 0.5006610233103856]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraViewAngle = 20.36067481093659
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 1.263494633251814
renderView1.OrientationAxesVisibility = 0

imageFileLUT = pvs.GetColorTransferFunction('ImageFile')                # OWN_DATA: every field has a name in a .vti file. Replace 'Scalars_' by the corresponding name
imageFileLUTColorBar = pvs.GetScalarBar(imageFileLUT, renderView1)
imageFileLUTColorBar.Title = 'Velocity'                                 # OWN_DATA: change the name of the color bar accoridng to what value is visualized
imageFileLUTColorBar.WindowLocation = 'Any Location'
imageFileLUTColorBar.Position = [0.94, 0.1]
imageFileLUTColorBar.ScalarBarLength = 0.8
imageFileLUTColorBar.ScalarBarThickness = 10
imageFileLUTColorBar.TitleFontSize = 18
imageFileLUTColorBar.LabelFontSize = 12

readerDisplay = pvs.Show(reader, renderView1, 'UniformGridRepresentation')
readerDisplay.Representation = 'Outline'

glyph1Display = pvs.Show(glyph1, renderView1, 'GeometryRepresentation')
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = ['POINTS', 'ImageFile']
glyph1Display.LookupTable = imageFileLUT
glyph1Display.SelectTCoordArray = 'None'
glyph1Display.SelectNormalArray = 'None'
glyph1Display.SelectTangentArray = 'None'
glyph1Display.OSPRayScaleArray = 'ImageFile'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'ImageFile'
glyph1Display.ScaleFactor = 0.2231481334194541
glyph1Display.SelectScaleArray = 'ImageFile'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'ImageFile'
glyph1Display.GaussianRadius = 0.011157406670972704
glyph1Display.SetScaleArray = ['POINTS', 'ImageFile']
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityArray = ['POINTS', 'ImageFile']
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display.PolarAxes = 'PolarAxesRepresentation'
glyph1Display.SelectInputVectors = ['POINTS', 'ImageFile']
glyph1Display.WriteLog = ''

# save screenshot
pvs.SaveScreenshot('./output/glyphs.png', 
    renderView1, 
    ImageResolution=[1920, 1080],
    FontScaling='Do not scale fonts')
