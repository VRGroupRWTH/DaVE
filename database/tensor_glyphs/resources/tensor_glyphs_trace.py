# import paraview
# paraview.compatibility.major = 5
# paraview.compatibility.minor = 10

import sys
from os.path import exists

#### import the simple module from the paraview
import paraview.simple as pvs

if len(sys.argv) < 2:
    print('no data file path provided - defaulting to "./data/atoms.vtk"')
    filepath = './data/atoms.vtk'
else:
    filepath = str(sys.argv[1])

file_exists = exists(filepath)
if not file_exists:
    print("file ", filepath," does not exist", file=sys.stderr)

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Legacy VTK Reader'
reader = pvs.LegacyVTKReader(registrationName='reader', FileNames=[filepath])

# create a new 'Tensor Glyph'
tensorGlyph1 = pvs.TensorGlyph(registrationName='TensorGlyph1', Input=reader, GlyphType='Superquadric')
tensorGlyph1.Tensors = ['POINTS', 'STRESS']             # OWN_DATA: change the field name if your field is not named "STRESS"
tensorGlyph1.Scalars = ['POINTS', '1']
tensorGlyph1.Colorby = 'eigenvalues'
tensorGlyph1.ScaleFactor = 0.001255177081143987
tensorGlyph1.LimitScalingByEigenvalues = 1
tensorGlyph1.MaxScaleFactor = 2.0

# init the 'Superquadric' selected for 'GlyphType'
tensorGlyph1.GlyphType.Thickness = 0.480052
tensorGlyph1.GlyphType.Toroidal = 0

# ----------------------------------------------------------------
# setup the views
# ----------------------------------------------------------------

#### disable automatic camera reset on 'Show'
pvs._DisableFirstRenderCameraReset()
pvs.LoadPalette('WhiteBackground')

renderView1 = pvs.GetActiveViewOrCreate('RenderView')
renderView1.CameraPosition = [-62.273695794486905, 84.32590062949528, -70.08976914496148]
renderView1.CameraFocalPoint = [14.451357128357623, 15.786878937657141, 17.97062784513119]
renderView1.CameraViewUp = [0.31031897035270395, 0.8620974178744707, 0.4006122548467634]
renderView1.CameraParallelScale = 28.96664975823481

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

# get 2D transfer function for 'MaxEigenvalue'
maxEigenvalueTF2D = pvs.GetTransferFunction2D('MaxEigenvalue')

# get color transfer function/color map for 'MaxEigenvalue'
maxEigenvalueLUT = pvs.GetColorTransferFunction('MaxEigenvalue')
maxEigenvalueLUT.TransferFunction2D = maxEigenvalueTF2D
maxEigenvalueLUT.RGBPoints = [-1.973176121711731, 0.231373, 0.298039, 0.752941, 0.013411939144134521, 0.865003, 0.865003, 0.865003, 2.0, 0.705882, 0.0156863, 0.14902]
maxEigenvalueLUT.ScalarRangeInitialized = 1.0

# show data from tensorGlyph1
tensorGlyph1Display = pvs.Show(tensorGlyph1, renderView1, 'GeometryRepresentation')
tensorGlyph1Display.Representation = 'Surface'
tensorGlyph1Display.ColorArrayName = ['POINTS', 'MaxEigenvalue']
tensorGlyph1Display.LookupTable = maxEigenvalueLUT
tensorGlyph1Display.Interpolation = 'PBR'
tensorGlyph1Display.SelectScaleArray = 'None'
tensorGlyph1Display.SetScaleArray = ['POINTS', 'Normals']
tensorGlyph1Display.SetScalarBarVisibility(renderView1, True)

# get color legend/bar for maxEigenvalueLUT in view renderView1
maxEigenvalueLUTColorBar = pvs.GetScalarBar(maxEigenvalueLUT, renderView1)
maxEigenvalueLUTColorBar.WindowLocation = 'Any Location'
maxEigenvalueLUTColorBar.Position = [0.903968253968254, 0.015209125475285171]
maxEigenvalueLUTColorBar.Title = 'MaxEigenvalue'
maxEigenvalueLUTColorBar.ComponentTitle = ''
maxEigenvalueLUTColorBar.ScalarBarLength = 0.9523067173637516
maxEigenvalueLUTColorBar.Visibility = 1

pvs.ResetCamera(renderView1)                                            # OWN_DATA: if the original view does not fit ResetCamera can be used to focus on the visible data

# save screenshot
pvs.SaveScreenshot('./output/glyphs.png', 
    layout1, 
    ImageResolution=[1920, 1080],
    FontScaling='Do not scale fonts')