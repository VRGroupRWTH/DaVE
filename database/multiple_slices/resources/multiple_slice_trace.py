# state file generated using paraview version 5.11.2
import paraview
import csv
import sys
from os.path import exists
# paraview.compatibility.major = 5
# paraview.compatibility.minor = 11

#### import the simple module from the paraview
import paraview.simple as pvs
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()


if len(sys.argv) < 2:
    print('no data file path provided - defaulting to "./data/ctBones.vti"')
    filepath = './data/ctBones.vti'
else:
    filepath = str(sys.argv[1])

file_exists = exists(filepath)
if not file_exists:
    print("file ", filepath," does not exist", file=sys.stderr)


# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = pvs.GetMaterialLibrary()

pvs.LoadPalette('WhiteBackground')

# Create a new 'Render View'
renderView1 = pvs.CreateView('RenderView')
renderView1.ViewSize = [1076, 570]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [127.0, 127.5, 127.5]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [823.6729559300638, 127.5, 127.5]
renderView1.CameraFocalPoint = [127.0, 127.5, 127.5]
renderView1.CameraViewUp = [0.0, 1.0, 0.0]
renderView1.CameraViewAngle = 22.748538011695906
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 141.64878824295428
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView2 = pvs.CreateView('RenderView')
renderView2.ViewSize = [1076, 570]
renderView2.InteractionMode = '2D'
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.CenterOfRotation = [127.5, 127.5, 127.0]
renderView2.StereoType = 'Crystal Eyes'
renderView2.CameraPosition = [127.5, 127.5, 823.6729559300638]
renderView2.CameraFocalPoint = [127.5, 127.5, 127.0]
renderView2.CameraFocalDisk = 1.0
renderView2.CameraParallelScale = 141.64878824295428
renderView2.BackEnd = 'OSPRay raycaster'
renderView2.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView3 = pvs.CreateView('RenderView')
renderView3.ViewSize = [1075, 570]
renderView3.InteractionMode = '2D'
renderView3.AxesGrid = 'GridAxes3DActor'
renderView3.CenterOfRotation = [127.0, 127.5, 127.5]
renderView3.StereoType = 'Crystal Eyes'
renderView3.CameraPosition = [529.2243186433548, 529.7243186433545, 529.7243186433548]
renderView3.CameraFocalPoint = [127.0, 127.5, 127.5]
renderView3.CameraViewUp = [-0.4082482904638631, 0.816496580927726, -0.40824829046386296]
renderView3.CameraFocalDisk = 1.0
renderView3.CameraParallelScale = 180.31222920256963
renderView3.BackEnd = 'OSPRay raycaster'
renderView3.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView4 = pvs.CreateView('RenderView')
renderView4.ViewSize = [1075, 570]
renderView4.InteractionMode = '2D'
renderView4.AxesGrid = 'GridAxes3DActor'
renderView4.CenterOfRotation = [127.5, 127.5, 127.5]
renderView4.StereoType = 'Crystal Eyes'
renderView4.CameraPosition = [127.5, 823.6729559300638, 127.5]
renderView4.CameraFocalPoint = [127.5, 127.0, 127.5]
renderView4.CameraViewUp = [0.0, 0.0, -1.0]
renderView4.CameraFocalDisk = 1.0
renderView4.CameraParallelScale = 141.64878824295428
renderView4.BackEnd = 'OSPRay raycaster'
renderView4.OSPRayMaterialLibrary = materialLibrary1

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
# layout1 = pvs.CreateLayout(name='Layout #1')
# layout1.SplitVertical(0, 0.500000)
# layout1.SplitHorizontal(1, 0.500000)
# layout1.AssignView(3, renderView1)
# layout1.AssignView(4, renderView4)
# layout1.SplitHorizontal(2, 0.500000)
# layout1.AssignView(5, renderView2)
# layout1.AssignView(6, renderView3)
# layout1.SetSize(1920, 1080)


# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

colorBarTitleFontSize = 16
colorBarLabelFontSize = 8
colorBarThickness = 16
colorBarPosition = [0.9, 0.3]
colorBarLength = 0.8
colorBarTitle = "Scalars"

# create a new 'Text'
text1 = pvs.Text(registrationName='Text1')
text1.Text = 'YZ plane'

text2 = pvs.Text(registrationName='Text2')
text2.Text = 'XZ plane'

text3 = pvs.Text(registrationName='Text3')
text3.Text = 'XY plane'

# create a new 'XML Image Data Reader'
ctBonesvti = pvs.XMLImageDataReader(registrationName='ctBones.vti', FileName=[filepath])
ctBonesvti.PointArrayStatus = ['Scalars_']
ctBonesvti.TimeArray = 'None'
pvs.UpdatePipeline(time=0.0, proxy=ctBonesvti)
extent = ctBonesvti.GetDataInformation().GetExtent()

# create a new 'Slice'
slice1 = pvs.Slice(registrationName='Slice1', Input=ctBonesvti)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]
slice1.SliceType.Origin = [127.0, 127.0, 127.0]
# slice1.HyperTreeGridSlicer.Origin = [127.5, 127.5, 127.5]

# create a new 'Slice'
slice2 = pvs.Slice(registrationName='Slice2', Input=ctBonesvti)
slice2.SliceType = 'Plane'
slice2.HyperTreeGridSlicer = 'Plane'
slice2.SliceOffsetValues = [0.0]
slice2.SliceType.Origin = [127.0, 127.0, 127.0]
slice2.SliceType.Normal = [0.0, 1.0, 0.0]
# slice2.HyperTreeGridSlicer.Origin = [127.5, 127.5, 127.5]

# create a new 'Slice'
slice3 = pvs.Slice(registrationName='Slice3', Input=ctBonesvti)
slice3.SliceType = 'Plane'
slice3.HyperTreeGridSlicer = 'Plane'
slice3.SliceOffsetValues = [0.0]
slice3.SliceType.Origin = [127.0, 127.0, 127.0]
slice3.SliceType.Normal = [0.0, 0.0, 1.0]
# slice3.HyperTreeGridSlicer.Origin = [127.5, 127.5, 127.5]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# get 2D transfer function for 'Scalars_'
scalars_TF2D = pvs.GetTransferFunction2D('Scalars_')
scalars_TF2D.ScalarRangeInitialized = 1
scalars_TF2D.Range = [0.0, 255.0, 0.0, 1.0]

# get color transfer function/color map for 'Scalars_'
scalars_LUT = pvs.GetColorTransferFunction('Scalars_')
scalars_LUT.TransferFunction2D = scalars_TF2D
scalars_LUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 127.5, 0.865003, 0.865003, 0.865003, 255.0, 0.705882, 0.0156863, 0.14902]
scalars_LUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Scalars_'
scalars_PWF = pvs.GetOpacityTransferFunction('Scalars_')
scalars_PWF.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]
scalars_PWF.ScalarRangeInitialized = 1

# get color legend/bar for scalars_LUT in view renderView1
scalars_LUTColorBar = pvs.GetScalarBar(scalars_LUT, renderView1)
scalars_LUTColorBar.WindowLocation = 'Upper Right Corner'
scalars_LUTColorBar.Position = colorBarPosition
scalars_LUTColorBar.ScalarBarLength = colorBarLength
scalars_LUTColorBar.ScalarBarThickness = colorBarThickness
scalars_LUTColorBar.TitleFontSize = colorBarTitleFontSize
scalars_LUTColorBar.LabelFontSize = colorBarLabelFontSize
scalars_LUTColorBar.Title = colorBarTitle
scalars_LUTColorBar.ComponentTitle = ''
scalars_LUTColorBar.Visibility = 1

# show data from text1
text1Display = pvs.Show(text1, renderView1, 'TextSourceRepresentation')

# show data from ctBonesvti
ctBonesvtiDisplay = pvs.Show(ctBonesvti, renderView1, 'UniformGridRepresentation')
ctBonesvtiDisplay.Representation = 'Slice'
ctBonesvtiDisplay.ColorArrayName = ['POINTS', 'Scalars_']
ctBonesvtiDisplay.LookupTable = scalars_LUT
ctBonesvtiDisplay.SelectTCoordArray = 'None'
ctBonesvtiDisplay.SelectNormalArray = 'None'
ctBonesvtiDisplay.SelectTangentArray = 'None'
ctBonesvtiDisplay.OSPRayScaleArray = 'Scalars_'
ctBonesvtiDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
ctBonesvtiDisplay.SelectOrientationVectors = 'None'
ctBonesvtiDisplay.ScaleFactor = 25.5
ctBonesvtiDisplay.SelectScaleArray = 'Scalars_'
ctBonesvtiDisplay.GlyphType = 'Arrow'
ctBonesvtiDisplay.GlyphTableIndexArray = 'Scalars_'
ctBonesvtiDisplay.GaussianRadius = 1.2750000000000001
ctBonesvtiDisplay.SetScaleArray = ['POINTS', 'Scalars_']
ctBonesvtiDisplay.ScaleTransferFunction = 'PiecewiseFunction'
ctBonesvtiDisplay.OpacityArray = ['POINTS', 'Scalars_']
ctBonesvtiDisplay.OpacityTransferFunction = 'PiecewiseFunction'
ctBonesvtiDisplay.DataAxesGrid = 'GridAxesRepresentation'
ctBonesvtiDisplay.PolarAxes = 'PolarAxesRepresentation'
ctBonesvtiDisplay.ScalarOpacityUnitDistance = 1.7320508075688774
ctBonesvtiDisplay.ScalarOpacityFunction = scalars_PWF
ctBonesvtiDisplay.TransferFunction2D = scalars_TF2D
ctBonesvtiDisplay.OpacityArrayName = ['POINTS', 'Scalars_']
ctBonesvtiDisplay.ColorArray2Name = ['POINTS', 'Scalars_']
ctBonesvtiDisplay.IsosurfaceValues = [127.5]
ctBonesvtiDisplay.SliceFunction = 'Plane'
ctBonesvtiDisplay.SliceMode = 'YZ Plane'
ctBonesvtiDisplay.Slice = 127
ctBonesvtiDisplay.SelectInputVectors = [None, '']
ctBonesvtiDisplay.WriteLog = ''
ctBonesvtiDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]
ctBonesvtiDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]
ctBonesvtiDisplay.SliceFunction.Origin = [127.5, 127.5, 127.5]
ctBonesvtiDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# get color legend/bar for scalars_LUT in view renderView2
scalars_LUTColorBar_1 = pvs.GetScalarBar(scalars_LUT, renderView2)
scalars_LUTColorBar_1.WindowLocation = 'Upper Right Corner'
scalars_LUTColorBar_1.Position = colorBarPosition
scalars_LUTColorBar_1.ScalarBarLength = colorBarLength
scalars_LUTColorBar_1.ScalarBarThickness = colorBarThickness
scalars_LUTColorBar_1.TitleFontSize = colorBarTitleFontSize
scalars_LUTColorBar_1.LabelFontSize = colorBarLabelFontSize
scalars_LUTColorBar_1.Title = colorBarTitle
scalars_LUTColorBar_1.ComponentTitle = ''
scalars_LUTColorBar_1.Visibility = 1

# show data from text3
text3Display = pvs.Show(text3, renderView2, 'TextSourceRepresentation')

# show data from ctBonesvti
ctBonesvtiDisplay_1 = pvs.Show(ctBonesvti, renderView2, 'UniformGridRepresentation')
ctBonesvtiDisplay_1.Representation = 'Slice'
ctBonesvtiDisplay_1.ColorArrayName = ['POINTS', 'Scalars_']
ctBonesvtiDisplay_1.LookupTable = scalars_LUT
ctBonesvtiDisplay_1.SelectTCoordArray = 'None'
ctBonesvtiDisplay_1.SelectNormalArray = 'None'
ctBonesvtiDisplay_1.SelectTangentArray = 'None'
ctBonesvtiDisplay_1.OSPRayScaleArray = 'Scalars_'
ctBonesvtiDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
ctBonesvtiDisplay_1.SelectOrientationVectors = 'None'
ctBonesvtiDisplay_1.ScaleFactor = 25.5
ctBonesvtiDisplay_1.SelectScaleArray = 'Scalars_'
ctBonesvtiDisplay_1.GlyphType = 'Arrow'
ctBonesvtiDisplay_1.GlyphTableIndexArray = 'Scalars_'
ctBonesvtiDisplay_1.GaussianRadius = 1.2750000000000001
ctBonesvtiDisplay_1.SetScaleArray = ['POINTS', 'Scalars_']
ctBonesvtiDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
ctBonesvtiDisplay_1.OpacityArray = ['POINTS', 'Scalars_']
ctBonesvtiDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
ctBonesvtiDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
ctBonesvtiDisplay_1.PolarAxes = 'PolarAxesRepresentation'
ctBonesvtiDisplay_1.ScalarOpacityUnitDistance = 1.7320508075688774
ctBonesvtiDisplay_1.ScalarOpacityFunction = scalars_PWF
ctBonesvtiDisplay_1.TransferFunction2D = scalars_TF2D
ctBonesvtiDisplay_1.OpacityArrayName = ['POINTS', 'Scalars_']
ctBonesvtiDisplay_1.ColorArray2Name = ['POINTS', 'Scalars_']
ctBonesvtiDisplay_1.IsosurfaceValues = [127.5]
ctBonesvtiDisplay_1.SliceFunction = 'Plane'
ctBonesvtiDisplay_1.Slice = 127
ctBonesvtiDisplay_1.SelectInputVectors = [None, '']
ctBonesvtiDisplay_1.WriteLog = ''
ctBonesvtiDisplay_1.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]
ctBonesvtiDisplay_1.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]
ctBonesvtiDisplay_1.SliceFunction.Origin = [127.5, 127.5, 127.5]
ctBonesvtiDisplay_1.SetScalarBarVisibility(renderView2, True)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView3'
# ----------------------------------------------------------------

# get color legend/bar for scalars_LUT in view renderView3
scalars_LUTColorBar_2 = pvs.GetScalarBar(scalars_LUT, renderView3)
scalars_LUTColorBar_2.WindowLocation = 'Upper Right Corner'
scalars_LUTColorBar_2.Position = colorBarPosition
scalars_LUTColorBar_2.ScalarBarLength = colorBarLength
scalars_LUTColorBar_2.ScalarBarThickness = colorBarThickness
scalars_LUTColorBar_2.TitleFontSize = colorBarTitleFontSize
scalars_LUTColorBar_2.LabelFontSize = colorBarLabelFontSize
scalars_LUTColorBar_2.Title = colorBarTitle
scalars_LUTColorBar_2.ComponentTitle = ''
scalars_LUTColorBar_2.Visibility = 1

# show data from slice1
slice1Display = pvs.Show(slice1, renderView3, 'GeometryRepresentation')
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = ['POINTS', 'Scalars_']
slice1Display.LookupTable = scalars_LUT
slice1Display.SelectTCoordArray = 'None'
slice1Display.SelectNormalArray = 'None'
slice1Display.SelectTangentArray = 'None'
slice1Display.OSPRayScaleArray = 'Scalars_'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'None'
slice1Display.ScaleFactor = 25.5
slice1Display.SelectScaleArray = 'Scalars_'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'Scalars_'
slice1Display.GaussianRadius = 1.2750000000000001
slice1Display.SetScaleArray = ['POINTS', 'Scalars_']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'Scalars_']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'
slice1Display.SelectInputVectors = [None, '']
slice1Display.WriteLog = ''
slice1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]
slice1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]

# show data from slice2
slice2Display = pvs.Show(slice2, renderView3, 'GeometryRepresentation')
slice2Display.Representation = 'Surface'
slice2Display.ColorArrayName = ['POINTS', 'Scalars_']
slice2Display.LookupTable = scalars_LUT
slice2Display.SelectTCoordArray = 'None'
slice2Display.SelectNormalArray = 'None'
slice2Display.SelectTangentArray = 'None'
slice2Display.OSPRayScaleArray = 'Scalars_'
slice2Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice2Display.SelectOrientationVectors = 'None'
slice2Display.ScaleFactor = 25.5
slice2Display.SelectScaleArray = 'Scalars_'
slice2Display.GlyphType = 'Arrow'
slice2Display.GlyphTableIndexArray = 'Scalars_'
slice2Display.GaussianRadius = 1.2750000000000001
slice2Display.SetScaleArray = ['POINTS', 'Scalars_']
slice2Display.ScaleTransferFunction = 'PiecewiseFunction'
slice2Display.OpacityArray = ['POINTS', 'Scalars_']
slice2Display.OpacityTransferFunction = 'PiecewiseFunction'
slice2Display.DataAxesGrid = 'GridAxesRepresentation'
slice2Display.PolarAxes = 'PolarAxesRepresentation'
slice2Display.SelectInputVectors = [None, '']
slice2Display.WriteLog = ''
slice2Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]
slice2Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]

# show data from slice3
slice3Display = pvs.Show(slice3, renderView3, 'GeometryRepresentation')
slice3Display.Representation = 'Surface'
slice3Display.ColorArrayName = ['POINTS', 'Scalars_']
slice3Display.LookupTable = scalars_LUT
slice3Display.SelectTCoordArray = 'None'
slice3Display.SelectNormalArray = 'None'
slice3Display.SelectTangentArray = 'None'
slice3Display.OSPRayScaleArray = 'Scalars_'
slice3Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice3Display.SelectOrientationVectors = 'None'
slice3Display.ScaleFactor = 25.5
slice3Display.SelectScaleArray = 'Scalars_'
slice3Display.GlyphType = 'Arrow'
slice3Display.GlyphTableIndexArray = 'Scalars_'
slice3Display.GaussianRadius = 1.2750000000000001
slice3Display.SetScaleArray = ['POINTS', 'Scalars_']
slice3Display.ScaleTransferFunction = 'PiecewiseFunction'
slice3Display.OpacityArray = ['POINTS', 'Scalars_']
slice3Display.OpacityTransferFunction = 'PiecewiseFunction'
slice3Display.DataAxesGrid = 'GridAxesRepresentation'
slice3Display.PolarAxes = 'PolarAxesRepresentation'
slice3Display.SelectInputVectors = [None, '']
slice3Display.WriteLog = ''
slice3Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]
slice3Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]

slice1Display.SetScalarBarVisibility(renderView3, True)
slice2Display.SetScalarBarVisibility(renderView3, True)
slice3Display.SetScalarBarVisibility(renderView3, True)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView4'
# ----------------------------------------------------------------

# get color legend/bar for scalars_LUT in view renderView4
scalars_LUTColorBar_3 = pvs.GetScalarBar(scalars_LUT, renderView4)
scalars_LUTColorBar_3.WindowLocation = 'Upper Right Corner'
scalars_LUTColorBar_3.Position = colorBarPosition
scalars_LUTColorBar_3.ScalarBarLength = colorBarLength
scalars_LUTColorBar_3.ScalarBarThickness = colorBarThickness
scalars_LUTColorBar_3.TitleFontSize = colorBarTitleFontSize
scalars_LUTColorBar_3.LabelFontSize = colorBarLabelFontSize
scalars_LUTColorBar_3.Title = colorBarTitle
scalars_LUTColorBar_3.ComponentTitle = ''
scalars_LUTColorBar_3.Visibility = 1

# show data from text2
text2Display = pvs.Show(text2, renderView4, 'TextSourceRepresentation')

# show data from ctBonesvti
ctBonesvtiDisplay_2 = pvs.Show(ctBonesvti, renderView4, 'UniformGridRepresentation')
ctBonesvtiDisplay_2.Representation = 'Slice'
ctBonesvtiDisplay_2.ColorArrayName = ['POINTS', 'Scalars_']
ctBonesvtiDisplay_2.LookupTable = scalars_LUT
ctBonesvtiDisplay_2.SelectTCoordArray = 'None'
ctBonesvtiDisplay_2.SelectNormalArray = 'None'
ctBonesvtiDisplay_2.SelectTangentArray = 'None'
ctBonesvtiDisplay_2.OSPRayScaleArray = 'Scalars_'
ctBonesvtiDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
ctBonesvtiDisplay_2.SelectOrientationVectors = 'None'
ctBonesvtiDisplay_2.ScaleFactor = 25.5
ctBonesvtiDisplay_2.SelectScaleArray = 'Scalars_'
ctBonesvtiDisplay_2.GlyphType = 'Arrow'
ctBonesvtiDisplay_2.GlyphTableIndexArray = 'Scalars_'
ctBonesvtiDisplay_2.GaussianRadius = 1.2750000000000001
ctBonesvtiDisplay_2.SetScaleArray = ['POINTS', 'Scalars_']
ctBonesvtiDisplay_2.ScaleTransferFunction = 'PiecewiseFunction'
ctBonesvtiDisplay_2.OpacityArray = ['POINTS', 'Scalars_']
ctBonesvtiDisplay_2.OpacityTransferFunction = 'PiecewiseFunction'
ctBonesvtiDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
ctBonesvtiDisplay_2.PolarAxes = 'PolarAxesRepresentation'
ctBonesvtiDisplay_2.ScalarOpacityUnitDistance = 1.7320508075688774
ctBonesvtiDisplay_2.ScalarOpacityFunction = scalars_PWF
ctBonesvtiDisplay_2.TransferFunction2D = scalars_TF2D
ctBonesvtiDisplay_2.OpacityArrayName = ['POINTS', 'Scalars_']
ctBonesvtiDisplay_2.ColorArray2Name = ['POINTS', 'Scalars_']
ctBonesvtiDisplay_2.IsosurfaceValues = [127.5]
ctBonesvtiDisplay_2.SliceFunction = 'Plane'
ctBonesvtiDisplay_2.SliceMode = 'XZ Plane'
ctBonesvtiDisplay_2.Slice = 127
ctBonesvtiDisplay_2.SelectInputVectors = [None, '']
ctBonesvtiDisplay_2.WriteLog = ''
ctBonesvtiDisplay_2.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]
ctBonesvtiDisplay_2.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]
ctBonesvtiDisplay_2.SliceFunction.Origin = [127.5, 127.5, 127.5]
ctBonesvtiDisplay_2.SetScalarBarVisibility(renderView4, True)

# ----------------------------------------------------------------
# create the Cinema databases for each view
# ----------------------------------------------------------------

x_range = list(extent[0:2])
y_range = list(extent[2:4])
z_range = list(extent[4:6])
x_range[0] += 1
y_range[0] += 1
z_range[0] += 1
step = int(min([x_range[1]-x_range[0],y_range[1]-y_range[0], z_range[1]-z_range[0]]) / 10) # minimum resolution of 10 steps in direction with lowest extent

data = []
data_xy = []
data_xz = []
data_yz = []

for XYSlice in range(z_range[0], z_range[1], step):
    ctBonesvtiDisplay_1.Slice = XYSlice # XY
    slice3.SliceType.Origin = [127.0, 127.0, XYSlice]
    imageName = "image/" + str(XYSlice) + ".png"
    pvs.SaveScreenshot('./output/sliceview1.cdb/' + imageName, renderView2, ImageResolution=[960, 540])
    data_xy.append([XYSlice, imageName])

    for XZSlice in range(y_range[0], y_range[1],step):
        ctBonesvtiDisplay_2.Slice = XZSlice # XZ
        slice2.SliceType.Origin = [127.0, XZSlice, 127.0]
        if XYSlice == z_range[0]:
            imageName = "image/" + str(XZSlice) + ".png"
            pvs.SaveScreenshot('./output/sliceview2.cdb/' + imageName, renderView4, ImageResolution=[960, 540])
            data_xz.append([XZSlice, imageName])

        for YZSlice in range(x_range[0], x_range[1],step):
            ctBonesvtiDisplay.Slice = YZSlice # YZ
            slice1.SliceType.Origin = [YZSlice, 127.0, 127.0]
            if XYSlice == z_range[0] and XZSlice == y_range[0]:
                imageName = "image/" + str(YZSlice) + ".png"
                pvs.SaveScreenshot('./output/sliceview3.cdb/' + imageName, renderView1, ImageResolution=[960, 540])
                data_yz.append([YZSlice, imageName])

            imageName = "image/" + str(XYSlice) + "_" + str(XZSlice) + "_" + str(YZSlice) + ".png"
            pvs.SaveScreenshot('./output/sliceview4.cdb/' + imageName, renderView3, ImageResolution=[960, 540])
            data.append([XYSlice, XZSlice, YZSlice, imageName])

with open('./output/sliceview4.cdb/data.csv', 'w', newline='') as csvfile:
    datawriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    datawriter.writerow(['xy_slice','xz_slice','yz_slice','FILE'])
    datawriter.writerows(data)

with open('./output/sliceview1.cdb/data.csv', 'w', newline='') as csvfile:
    datawriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    datawriter.writerow(['xy_slice','FILE'])
    datawriter.writerows(data_xy)

with open('./output/sliceview2.cdb/data.csv', 'w', newline='') as csvfile:
    datawriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    datawriter.writerow(['xz_slice','FILE'])
    datawriter.writerows(data_xz)

with open('./output/sliceview3.cdb/data.csv', 'w', newline='') as csvfile:
    datawriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    datawriter.writerow(['yz_slice','FILE'])
    datawriter.writerows(data_yz)