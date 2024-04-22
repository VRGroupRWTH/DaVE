# state file generated using paraview version 5.12.0
# import paraview
# paraview.compatibility.major = 5
# paraview.compatibility.minor = 12

import sys
from os.path import exists

#### import the simple module from the paraview
import paraview.simple as pvs


if len(sys.argv) < 2:
    print('no data file path provided - defaulting to "./data/brainData_all.vtk"')
    filepath = './data/brainData_all.vtk'
else:
    filepath = str(sys.argv[1])

file_exists = exists(filepath)
if not file_exists:
    print("file ", filepath," does not exist", file=sys.stderr)


# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Legacy VTK Reader'
reader = pvs.LegacyVTKReader(registrationName='brainData_all.vtk', FileNames=[filepath])

# create a new 'Glyph'
glyph1 = pvs.Glyph(registrationName='Glyph1', Input=reader, GlyphType='Sphere')
glyph1.OrientationArray = ['POINTS', 'No orientation array']
glyph1.ScaleArray = ['POINTS', 'No scale array']
glyph1.ScaleFactor = 18.667247009277343
glyph1.GlyphTransform = 'Transform2'
glyph1.GlyphMode = 'All Points'
glyph1.GlyphType.Radius = 0.08


# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

#### disable automatic camera reset on 'Show'
pvs._DisableFirstRenderCameraReset()
pvs.LoadPalette('WhiteBackground')

# Create a new 'Render View'
renderView1 = pvs.CreateView('RenderView')
renderView1.CameraPosition = [201.8962981554911, 428.0263262907966, 32.42807434152617]
renderView1.CameraFocalPoint = [93.33623504638663, 73.32450866699216, 77.18654632568361]
renderView1.CameraViewUp = [-0.011136481538551998, 0.12853993605242348, 0.9916418020729967]
renderView1.CameraParallelScale = 141.58354169032876

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

# get 2D transfer function for 'Area'
areaTF2D = pvs.GetTransferFunction2D('Area')                            # OWN_DATA: change field

# get color transfer function/color map for 'Area'
areaLUT = pvs.GetColorTransferFunction('Area')                          # OWN_DATA: change field
areaLUT.TransferFunction2D = areaTF2D
areaLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 23.5, 0.865003, 0.865003, 0.865003, 47.0, 0.705882, 0.0156863, 0.14902]     # OWN_DATA: change range of field; format is [value, R, G, B, ...]
areaLUT.ScalarRangeInitialized = 1.0

# show data from reader
readerDisplay = pvs.Show(reader, renderView1, 'GeometryRepresentation')
readerDisplay.Representation = 'Surface'
readerDisplay.AmbientColor = [0.0, 0.0, 0.0]
readerDisplay.ColorArrayName = ['POINTS', 'Area']
readerDisplay.DiffuseColor = [0.0, 0.0, 0.0]
readerDisplay.LookupTable = areaLUT
readerDisplay.Opacity = 0.1
readerDisplay.LineWidth = 3.0
readerDisplay.SetScalarBarVisibility(renderView1, False)

# get 2D transfer function for 'Calcium_Target'
calcium_TargetTF2D = pvs.GetTransferFunction2D('Calcium_Target')        # OWN_DATA: change field

# get color transfer function/color map for 'Calcium_Target'
calcium_TargetLUT = pvs.GetColorTransferFunction('Calcium_Target')      # OWN_DATA: change field
calcium_TargetLUT.TransferFunction2D = calcium_TargetTF2D
calcium_TargetLUT.RGBPoints = [0.6000019907951355, 0.231373, 0.298039, 0.752941, 0.8500010073184967, 0.865003, 0.865003, 0.865003, 1.100000023841858, 0.705882, 0.0156863, 0.14902]         # OWN_DATA: change range of field; format is [value, R, G, B, ...]
calcium_TargetLUT.ScalarRangeInitialized = 1.0

# show data from glyph1
glyph1Display = pvs.Show(glyph1, renderView1, 'GeometryRepresentation')
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = ['POINTS', 'Calcium_Target']             # OWN_DATA: change field
glyph1Display.LookupTable = calcium_TargetLUT
glyph1Display.SetScalarBarVisibility(renderView1, True)

# get color legend/bar for calcium_TargetLUT in view renderView1
calcium_TargetLUTColorBar = pvs.GetScalarBar(calcium_TargetLUT, renderView1)
calcium_TargetLUTColorBar.Title = 'Calcium_Target'                      # OWN_DATA: change title
calcium_TargetLUTColorBar.ComponentTitle = ''
calcium_TargetLUTColorBar.Visibility = 1
calcium_TargetLUTColorBar.WindowLocation = 'Any Location'
calcium_TargetLUTColorBar.Position = [0.94, 0.1]
calcium_TargetLUTColorBar.ScalarBarLength = 0.8
calcium_TargetLUTColorBar.ScalarBarThickness = 10
calcium_TargetLUTColorBar.TitleFontSize = 18
calcium_TargetLUTColorBar.LabelFontSize = 12

#pvs.ResetCamera(renderView1)                                            # OWN_DATA: if the original view does not fit ResetCamera can be used to focus on the visible data

# save screenshot
pvs.SaveScreenshot('./output/point_connectivity_brain.png', 
    layout1, 
    ImageResolution=[1920, 1080],
    FontScaling='Do not scale fonts')