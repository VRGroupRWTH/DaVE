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
reader.PointArrayStatus = ['ImageFile']                                             # OWN_DATA: every field has a name in a .vti file. Replace 'Scalars_' by the corresponding name
reader.TimeArray = 'None'

# create a new 'Glyph'
glyph1 = pvs.Glyph(registrationName='Glyph1', Input=reader, GlyphType='Arrow')
glyph1.OrientationArray = ['POINTS', 'ImageFile']
glyph1.ScaleArray = ['POINTS', 'ImageFile']
glyph1.ScaleFactor = 0.024047037060938886
glyph1.GlyphTransform = 'Transform2'

pvs.UpdatePipeline(time=0.0, proxy=glyph1)

# ----------------------------------------------------------------
# setup the views
# ----------------------------------------------------------------

#### disable automatic camera reset on 'Show'
pvs._DisableFirstRenderCameraReset()
pvs.LoadPalette('WhiteBackground')

renderView1 = pvs.GetActiveViewOrCreate('RenderView')
renderView1.CameraPosition = [4.5, 1.0381428503314964, 0.5006610233103856]
renderView1.CameraFocalPoint = [0.4906297167763114, 1.0381428503314964, 0.5006610233103856]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraViewAngle = 20.36067481093659
renderView1.CameraParallelScale = 1.263494633251814

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

# get color transfer function/color map for 'ImageFile'
imageFileLUT = pvs.GetColorTransferFunction('ImageFile')                # OWN_DATA: change field name

# show data from reader
readerDisplay = pvs.Show(reader, renderView1, 'UniformGridRepresentation')
readerDisplay.Representation = 'Outline'

# show data from glyph1
glyph1Display = pvs.Show(glyph1, renderView1, 'GeometryRepresentation')
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = ['POINTS', 'ImageFile']                  # OWN_DATA: change field
glyph1Display.LookupTable = imageFileLUT
glyph1Display.SelectOrientationVectors = 'ImageFile'                    # OWN_DATA: change field for orientation
glyph1Display.ScaleFactor = 0.2231481334194541
glyph1Display.SelectScaleArray = 'ImageFile'                            # OWN_DATA: change field for scaling
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'ImageFile'                        # OWN_DATA: change field

# get color legend/bar for imageFileLUT in view renderView1
imageFileLUTColorBar = pvs.GetScalarBar(imageFileLUT, renderView1)
imageFileLUTColorBar.Title = 'Velocity'                                 # OWN_DATA: change the name of the color bar accoridng to what value is visualized
imageFileLUTColorBar.WindowLocation = 'Any Location'
imageFileLUTColorBar.Position = [0.94, 0.1]
imageFileLUTColorBar.ScalarBarLength = 0.8
imageFileLUTColorBar.ScalarBarThickness = 10
imageFileLUTColorBar.TitleFontSize = 18
imageFileLUTColorBar.LabelFontSize = 12

pvs.ResetCamera(renderView1)                                            # OWN_DATA: if the original view does not fit ResetCamera can be used to focus on the visible data

# save screenshot
pvs.SaveScreenshot('./output/glyphs.png', 
    layout1, 
    ImageResolution=[1920, 1080],
    FontScaling='Do not scale fonts')
