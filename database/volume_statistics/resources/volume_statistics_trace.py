# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10
import sys
from os.path import exists
import numpy as np

#### import the simple module from the paraview
import paraview.simple as pvs

if len(sys.argv) < 2:
    print('no data file path provided - defaulting to "./data/miranda.nhdr"')
    filepath = './data/miranda.nhdr'
else:
    filepath = str(sys.argv[1])

file_exists = exists(filepath)
if not file_exists:
    print("file ", filepath," does not exist", file=sys.stderr)

reader = pvs.NrrdReader(registrationName='reader', FileName=[filepath])
reader.DataVOI = [400, 600]*3

# create a new 'Iso Volume'
isoVolume1 = pvs.IsoVolume(registrationName='IsoVolume1', Input=reader)
isoVolume1.InputScalars = ['POINTS', 'ImageFile']
isoVolume1.ThresholdRange = [2.0, 3.000028610229492]

# create a new 'Connectivity'
connectivity1 = pvs.Connectivity(registrationName='Connectivity1', Input=isoVolume1)

# create a new 'Cell Size'
cellSize1 = pvs.CellSize(registrationName='CellSize1', Input=connectivity1)
cellSize1.ComputeVertexCount = 0
cellSize1.ComputeLength = 0
cellSize1.ComputeArea = 0

# create a new 'Programmable Filter'
programmableFilter1 = pvs.ProgrammableFilter(registrationName='ProgrammableFilter1', Input=cellSize1)
programmableFilter1.Script = """import numpy as np

input0 = inputs[0]

cellRegion = input0.CellData["RegionId"].copy()
cellVolume = input0.CellData["Volume"].copy()

maxID = int(max(cellRegion))
outField = np.zeros(maxID+1)

for cellID in range(len(cellRegion)):
    outField[cellRegion[cellID]] += cellVolume[cellID]

for cellID in range(len(cellRegion)):
    cellVolume[cellID] = outField[cellRegion[cellID]]

output.FieldData.append(outField,"ConnectedComponentVolume")
output.CellData.append(cellVolume,"ConnectedComponentVolume")"""
programmableFilter1.RequestInformationScript = ''
programmableFilter1.RequestUpdateExtentScript = ''
programmableFilter1.CopyArrays = 1
programmableFilter1.PythonPath = ''

full_volume_range = list(programmableFilter1.GetCellDataInformation().GetArray("ConnectedComponentVolume").GetRange(0))
full_volume_range[1] -= 1 # offset by one to exclude largest volume

# create a new 'Threshold'
threshold1 = pvs.Threshold(registrationName='Threshold1', Input=programmableFilter1)
threshold1.Scalars = ['CELLS', 'ConnectedComponentVolume']
threshold1.LowerThreshold = full_volume_range[0]
threshold1.UpperThreshold = full_volume_range[1]
threshold1.AllScalars = 1

pvs.UpdatePipeline(time=0.0, proxy=threshold1)

volume_range = list(threshold1.GetCellDataInformation().GetArray("ConnectedComponentVolume").GetRange(0))

# |                       |
# | rendering stuff below |
# v                       v

## SETUP VIEWS

# Create a new 'Histogram View'
histogramView1 = pvs.CreateView('XYHistogramChartView')
histogramView1.ViewSize = [1418, 334]
histogramView1.LegendPosition = [1022, 325]
histogramView1.LeftAxisTitle = 'number of connected components'
histogramView1.LeftAxisRangeMaximum = 35000.0
histogramView1.BottomAxisTitle = 'volume of component'
histogramView1.BottomAxisRangeMaximum = 580000.0
histogramView1.RightAxisRangeMaximum = 6.66
histogramView1.TopAxisRangeMaximum = 6.66

# get the material library
materialLibrary1 = pvs.GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = pvs.CreateView('RenderView')
renderView1.ViewSize = [704, 419]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [-0.49999999999914735, -0.49999999999914735, -0.49999999999914735]
renderView1.StereoType = 'Crystal Eyes'
#renderView1.CameraPosition = [2641.7014621601697, 1643.2793258062434, -185.36681586420255]
renderView1.CameraPosition = [600, 300, -30]
#renderView1.CameraFocalPoint = [346.3329677501051, 2.561290863151319, 20.21414698168813]
renderView1.CameraFocalPoint = [0,0,0]
renderView1.CameraViewUp = [-0.06427978297148634, -0.03503559979728816, -0.9973167080962712]
renderView1.CameraViewAngle = 24.733637747336378
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 885.9439880714822
#renderView1.LegendGrid = 'LegendGridActor'
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView2 = pvs.CreateView('RenderView')
renderView2.ViewSize = [704, 419]
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.CenterOfRotation = [-0.49999999999914735, -0.49999999999914735, -0.49999999999914735]
renderView2.StereoType = 'Crystal Eyes'
#renderView2.CameraPosition = [2641.7014621601697, 1643.2793258062434, -185.36681586420255]
renderView2.CameraPosition = [600, 300, -30]
#renderView2.CameraFocalPoint = [346.3329677501051, 2.561290863151319, 20.21414698168813]
renderView2.CameraFocalPoint = [0,0,0]
renderView2.CameraViewUp = [-0.06427978297148634, -0.03503559979728816, -0.9973167080962712]
renderView2.CameraViewAngle = 24.733637747336378
renderView2.CameraFocalDisk = 1.0
renderView2.CameraParallelScale = 885.9439880714822
#renderView2.LegendGrid = 'LegendGridActor'
renderView2.BackEnd = 'OSPRay raycaster'
renderView2.OSPRayMaterialLibrary = materialLibrary1

pvs.SetActiveView(None)

# create new layout object 'Layout #1'
layout1 = pvs.CreateLayout(name='Layout #1')
layout1.SplitVertical(0, 0.551766)
layout1.SplitHorizontal(1, 0.500000)
layout1.AssignView(3, renderView1)
layout1.AssignView(4, renderView2)
layout1.AssignView(2, histogramView1)
layout1.SetSize(1418, 754)

#### disable automatic camera reset on 'Show'
pvs._DisableFirstRenderCameraReset()
pvs.LoadPalette('WhiteBackground')

## HISTOGRAM VIEW

# show data from threshold1
threshold1Display = pvs.Show(threshold1, histogramView1, 'HistogramChartRepresentation')
threshold1Display.SelectInputArray = ['FIELD', 'ConnectedComponentVolume']
threshold1Display.UseCustomBinRanges = 1
threshold1Display.CustomBinRanges = volume_range
threshold1Display.BinCount = 20
threshold1Display.HistogramColor = [0.4470588235294118, 0.4823529411764706, 0.6901960784313725]

## THRESHOLDED VOLUME VIEW

# show data from reader
readerDisplay = pvs.Show(reader, renderView1, 'UniformGridRepresentation')
readerDisplay.Representation = 'Outline'
readerDisplay.ColorArrayName = ['POINTS', '']
readerDisplay.SelectTCoordArray = 'None'
readerDisplay.SelectNormalArray = 'None'
readerDisplay.SelectTangentArray = 'None'
readerDisplay.OSPRayScaleArray = 'ImageFile'
readerDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
# readerDisplay.Assembly = ''
readerDisplay.SelectOrientationVectors = 'None'
readerDisplay.ScaleFactor = 102.30000000000001
readerDisplay.SelectScaleArray = 'ImageFile'
readerDisplay.GlyphType = 'Arrow'
readerDisplay.GlyphTableIndexArray = 'ImageFile'
readerDisplay.GaussianRadius = 5.115
readerDisplay.SetScaleArray = ['POINTS', 'ImageFile']
readerDisplay.ScaleTransferFunction = 'PiecewiseFunction'
readerDisplay.OpacityArray = ['POINTS', 'ImageFile']
readerDisplay.OpacityTransferFunction = 'PiecewiseFunction'
readerDisplay.DataAxesGrid = 'GridAxesRepresentation'
readerDisplay.PolarAxes = 'PolarAxesRepresentation'
readerDisplay.ScalarOpacityUnitDistance = 8.90395967911036
readerDisplay.OpacityArrayName = ['POINTS', 'ImageFile']
readerDisplay.ColorArray2Name = ['POINTS', 'ImageFile']
readerDisplay.IsosurfaceValues = [1.999913215637207]
readerDisplay.SliceFunction = 'Plane'
readerDisplay.Slice = 99
readerDisplay.SelectInputVectors = [None, '']
readerDisplay.WriteLog = ''
readerDisplay.ScaleTransferFunction.Points = [0.9997978210449219, 0.0, 0.5, 0.0, 3.000028610229492, 1.0, 0.5, 0.0]
readerDisplay.OpacityTransferFunction.Points = [0.9997978210449219, 0.0, 0.5, 0.0, 3.000028610229492, 1.0, 0.5, 0.0]
readerDisplay.SliceFunction.Origin = [-0.5, -0.5, -0.5]

# get 2D transfer function for 'ConnectedComponentVolume'
connectedComponentVolumeTF2D = pvs.GetTransferFunction2D('ConnectedComponentVolume')
connectedComponentVolumeLUT = pvs.GetColorTransferFunction('ConnectedComponentVolume')
connectedComponentVolumeLUT.TransferFunction2D = connectedComponentVolumeTF2D
vpoints = list(np.linspace(volume_range[0], volume_range[1], 17))
connectedComponentVolumeLUT.RGBPoints = [vpoints[0], 0.5151, 0.0482, 0.6697, vpoints[1], 0.520711, 0.168955, 0.800574, vpoints[2], 0.493694, 0.278596, 0.911824, vpoints[3], 0.440026, 0.369475, 0.984978, vpoints[4], 0.398932, 0.457593, 0.987053, vpoints[5], 0.350651, 0.540644, 0.929608, vpoints[6], 0.298827, 0.615625, 0.857729, vpoints[7], 0.239928, 0.685061, 0.769531, vpoints[8], 0.228832, 0.739349, 0.673287, vpoints[9], 0.263297, 0.78608, 0.569988, vpoints[10], 0.298107, 0.828337, 0.460214, vpoints[11], 0.33092, 0.864071, 0.352674, vpoints[12], 0.38306, 0.898169, 0.287309, vpoints[13], 0.49023, 0.917481, 0.307961, vpoints[14], 0.62372, 0.926026, 0.332309, vpoints[15], 0.717458, 0.92527, 0.342476, vpoints[16], 0.8, 0.9255, 0.3529]
connectedComponentVolumeLUT.ColorSpace = 'Lab'
connectedComponentVolumeLUT.NanColor = [1.0, 0.0, 0.0]
connectedComponentVolumeLUT.ScalarRangeInitialized = 1.0#1.0

# get opacity transfer function/opacity map for 'ConnectedComponentVolume'
connectedComponentVolumePWF = pvs.GetOpacityTransferFunction('ConnectedComponentVolume')
connectedComponentVolumePWF.Points = [2.6636420068959723e-09, 0.0, 0.5, 0.0, 574056.8409635996, 1.0, 0.5, 0.0]
#connectedComponentVolumePWF.Points = [volume_range[0], 0.0, 0.5, 0.0, volume_range[1], 1.0, 0.5, 0.0]
connectedComponentVolumePWF.ScalarRangeInitialized = 1

# show data from threshold1
threshold1Display_1 = pvs.Show(threshold1, renderView1, 'UnstructuredGridRepresentation')
threshold1Display_1.Representation = 'Surface'
threshold1Display_1.ColorArrayName = ['CELLS', 'ConnectedComponentVolume']
threshold1Display_1.LookupTable = connectedComponentVolumeLUT
threshold1Display_1.SelectTCoordArray = 'None'
threshold1Display_1.SelectNormalArray = 'None'
threshold1Display_1.SelectTangentArray = 'None'
threshold1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
# threshold1Display_1.Assembly = ''
threshold1Display_1.SelectOrientationVectors = 'None'
threshold1Display_1.ScaleFactor = 102.30000000000018
threshold1Display_1.SelectScaleArray = 'None'
threshold1Display_1.GlyphType = 'Arrow'
threshold1Display_1.GlyphTableIndexArray = 'None'
threshold1Display_1.GaussianRadius = 5.115000000000008
threshold1Display_1.SetScaleArray = [None, '']
threshold1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
threshold1Display_1.OpacityArray = [None, '']
threshold1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
threshold1Display_1.DataAxesGrid = 'GridAxesRepresentation'
threshold1Display_1.PolarAxes = 'PolarAxesRepresentation'
threshold1Display_1.ScalarOpacityFunction = connectedComponentVolumePWF
threshold1Display_1.ScalarOpacityUnitDistance = 32.817603998524866
threshold1Display_1.OpacityArrayName = ['CELLS', 'ConnectedComponentVolume']
threshold1Display_1.SelectInputVectors = [None, '']
threshold1Display_1.WriteLog = ''
threshold1Display_1.SetScalarBarVisibility(renderView1, True)

# get color legend/bar for connectedComponentVolumeLUT in view renderView1
connectedComponentVolumeLUTColorBar = pvs.GetScalarBar(connectedComponentVolumeLUT, renderView1)
connectedComponentVolumeLUTColorBar.WindowLocation = 'Any Location'
connectedComponentVolumeLUTColorBar.Position = [0.8352272727272727, 0.05707762557077625]
connectedComponentVolumeLUTColorBar.Title = 'ConnectedComponentVolume'
connectedComponentVolumeLUTColorBar.ComponentTitle = ''
connectedComponentVolumeLUTColorBar.ScalarBarLength = 0.8893607305936072
connectedComponentVolumeLUTColorBar.Visibility = 1

## VOLUME VIEW

# get 2D transfer function for 'ImageFile'
imageFileTF2D = pvs.GetTransferFunction2D('ImageFile')

# get color transfer function/color map for 'ImageFile'
imageFileLUT = pvs.GetColorTransferFunction('ImageFile')
imageFileLUT.TransferFunction2D = imageFileTF2D
imageFileLUT.RGBPoints = [2.0, 0.231373, 0.298039, 0.752941, 2.500014305114746, 0.865003, 0.865003, 0.865003, 3.000028610229492, 0.705882, 0.0156863, 0.14902]
imageFileLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'ImageFile'
imageFilePWF = pvs.GetOpacityTransferFunction('ImageFile')
imageFilePWF.Points = [2.0, 0.0, 0.5, 0.0, 3.000028610229492, 1.0, 0.5, 0.0]
imageFilePWF.ScalarRangeInitialized = 1

# show data from programmableFilter1
programmableFilter1Display = pvs.Show(programmableFilter1, renderView2, 'UnstructuredGridRepresentation')
programmableFilter1Display.Representation = 'Surface'
programmableFilter1Display.ColorArrayName = ['POINTS', 'ImageFile']
programmableFilter1Display.LookupTable = imageFileLUT
programmableFilter1Display.SelectTCoordArray = 'None'
programmableFilter1Display.SelectNormalArray = 'None'
programmableFilter1Display.SelectTangentArray = 'None'
programmableFilter1Display.OSPRayScaleFunction = 'PiecewiseFunction'
# programmableFilter1Display.Assembly = ''
programmableFilter1Display.SelectOrientationVectors = 'None'
programmableFilter1Display.ScaleFactor = 102.30000000000018
programmableFilter1Display.SelectScaleArray = 'None'
programmableFilter1Display.GlyphType = 'Arrow'
programmableFilter1Display.GlyphTableIndexArray = 'None'
programmableFilter1Display.GaussianRadius = 5.115000000000008
programmableFilter1Display.SetScaleArray = [None, '']
programmableFilter1Display.ScaleTransferFunction = 'PiecewiseFunction'
programmableFilter1Display.OpacityArray = [None, '']
programmableFilter1Display.OpacityTransferFunction = 'PiecewiseFunction'
programmableFilter1Display.DataAxesGrid = 'GridAxesRepresentation'
programmableFilter1Display.PolarAxes = 'PolarAxesRepresentation'
programmableFilter1Display.ScalarOpacityFunction = imageFilePWF
programmableFilter1Display.ScalarOpacityUnitDistance = 9.772160239561401
programmableFilter1Display.OpacityArrayName = ['CELLS', 'ConnectedComponentVolume']
programmableFilter1Display.SelectInputVectors = [None, '']
programmableFilter1Display.WriteLog = ''
programmableFilter1Display.SetScalarBarVisibility(renderView2, True)

# show data from reader
readerDisplay_1 = pvs.Show(reader, renderView2, 'UniformGridRepresentation')
readerDisplay_1.Representation = 'Outline'
readerDisplay_1.ColorArrayName = ['POINTS', '']
readerDisplay_1.SelectTCoordArray = 'None'
readerDisplay_1.SelectNormalArray = 'None'
readerDisplay_1.SelectTangentArray = 'None'
readerDisplay_1.OSPRayScaleArray = 'ImageFile'
readerDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
# readerDisplay_1.Assembly = ''
readerDisplay_1.SelectOrientationVectors = 'None'
readerDisplay_1.ScaleFactor = 102.30000000000001
readerDisplay_1.SelectScaleArray = 'ImageFile'
readerDisplay_1.GlyphType = 'Arrow'
readerDisplay_1.GlyphTableIndexArray = 'ImageFile'
readerDisplay_1.GaussianRadius = 5.115
readerDisplay_1.SetScaleArray = ['POINTS', 'ImageFile']
readerDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
readerDisplay_1.OpacityArray = ['POINTS', 'ImageFile']
readerDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
readerDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
readerDisplay_1.PolarAxes = 'PolarAxesRepresentation'
readerDisplay_1.ScalarOpacityUnitDistance = 8.90395967911036
readerDisplay_1.OpacityArrayName = ['POINTS', 'ImageFile']
readerDisplay_1.ColorArray2Name = ['POINTS', 'ImageFile']
readerDisplay_1.IsosurfaceValues = [1.999913215637207]
readerDisplay_1.SliceFunction = 'Plane'
readerDisplay_1.Slice = 99
readerDisplay_1.SelectInputVectors = [None, '']
readerDisplay_1.WriteLog = ''
readerDisplay_1.ScaleTransferFunction.Points = [0.9997978210449219, 0.0, 0.5, 0.0, 3.000028610229492, 1.0, 0.5, 0.0]
readerDisplay_1.OpacityTransferFunction.Points = [0.9997978210449219, 0.0, 0.5, 0.0, 3.000028610229492, 1.0, 0.5, 0.0]
readerDisplay_1.SliceFunction.Origin = [-0.5, -0.5, -0.5]

# get color legend/bar for imageFileLUT in view renderView2
imageFileLUTColorBar = pvs.GetScalarBar(imageFileLUT, renderView2)
imageFileLUTColorBar.WindowLocation = 'Any Location'
imageFileLUTColorBar.Position = [0.8352272727272727, 0.0273972602739726]
imageFileLUTColorBar.Title = 'Density'
imageFileLUTColorBar.ComponentTitle = ''
imageFileLUTColorBar.ScalarBarLength = 0.9144748858447489
imageFileLUTColorBar.Visibility = 1

# save screenshot
pvs.SaveScreenshot("./output/volume_statistics.png", layout1)
