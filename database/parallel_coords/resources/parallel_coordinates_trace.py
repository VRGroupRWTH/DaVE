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


# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'NetCDF Reader'
reader = pvs.NetCDFReader(registrationName='spherical001.nc', FileName=[filepath])
reader.Dimensions = '(lat, r, lon)'

pvs.UpdatePipeline(time=0.0, proxy=reader)

# create a new 'Extract Subset'                                                                      
extractSubset1 = pvs.ExtractSubset(registrationName='ExtractSubset1', Input=reader)
extractSubset1.VOI = [0, 360, 0, 201, 90, 90]

pvs.UpdatePipeline(time=0.0, proxy=extractSubset1)

# ----------------------------------------------------------------
# setup the views
# ----------------------------------------------------------------

#### disable automatic camera reset on 'Show'
pvs._DisableFirstRenderCameraReset()
pvs.LoadPalette('WhiteBackground')

# Create a new 'Parallel Coordinates View'
parallelCoordinatesView1 = pvs.CreateView('ParallelCoordinatesChartView')
parallelCoordinatesView1.ViewSize = [1129, 1176]

# get the material library
materialLibrary1 = pvs.GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = pvs.CreateView('RenderView')
renderView1.ViewSize = [478, 570]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [-0.1220703125, 0.0, 0.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-98.41912938650825, 1605.5186315421029, -34850.71377638514]
renderView1.CameraFocalPoint = [-98.41912938650825, 1605.5186315421029, 0.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 9020.028460745267
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView2 = pvs.CreateView('RenderView')
renderView2.ViewSize = [478, 570]
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.CenterOfRotation = [-0.1220703125, 0.0, 0.0]
renderView2.StereoType = 'Crystal Eyes'
renderView2.CameraPosition = [-98.41912938650825, 1605.5186315421029, -34850.71377638514]
renderView2.CameraFocalPoint = [-98.41912938650825, 1605.5186315421029, 0.0]
renderView2.CameraFocalDisk = 1.0
renderView2.CameraParallelScale = 9020.028460745267
renderView2.BackEnd = 'OSPRay raycaster'
renderView2.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView3 = pvs.CreateView('RenderView')
renderView3.ViewSize = [478, 570]
renderView3.AxesGrid = 'GridAxes3DActor'
renderView3.CenterOfRotation = [-0.1220703125, 0.0, 0.0]
renderView3.StereoType = 'Crystal Eyes'
renderView3.CameraPosition = [-98.41912938650825, 1605.5186315421029, -34850.71377638514]
renderView3.CameraFocalPoint = [-98.41912938650825, 1605.5186315421029, 0.0]
renderView3.CameraFocalDisk = 1.0
renderView3.CameraParallelScale = 9020.028460745267
renderView3.BackEnd = 'OSPRay raycaster'
renderView3.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView4 = pvs.CreateView('RenderView')
renderView4.ViewSize = [478, 570]
renderView4.AxesGrid = 'GridAxes3DActor'
renderView4.CenterOfRotation = [-0.1220703125, 0.0, 0.0]
renderView4.StereoType = 'Crystal Eyes'
renderView4.CameraPosition = [-98.41912938650825, 1605.5186315421029, -34850.71377638514]
renderView4.CameraFocalPoint = [-98.41912938650825, 1605.5186315421029, 0.0]
renderView4.CameraFocalDisk = 1.0
renderView4.CameraParallelScale = 9020.028460745267
renderView4.BackEnd = 'OSPRay raycaster'
renderView4.OSPRayMaterialLibrary = materialLibrary1

# create new layout object 'Layout #1'
layout1 = pvs.CreateLayout(name='Layout #1')
layout1.SplitHorizontal(0, 0.460919)
layout1.SplitVertical(1, 0.500000)
layout1.SplitHorizontal(3, 0.500000)
layout1.AssignView(7, renderView1)
layout1.AssignView(8, renderView3)
layout1.SplitHorizontal(4, 0.500000)
layout1.AssignView(9, renderView2)
layout1.AssignView(10, renderView4)
layout1.AssignView(2, parallelCoordinatesView1)
layout1.SetSize(2087, 1176)



# ----------------------------------------------------------------
# setup the visualization in view 'parallelCoordinatesView1'
# ----------------------------------------------------------------

# show data from extractSubset1
extractSubset1Display = pvs.Show(extractSubset1, parallelCoordinatesView1, 'ParallelCoordinatesRepresentation')
extractSubset1Display.SeriesVisibility = ['temperature', 'temperature anomaly', 'thermal conductivity', 'thermal expansivity']
extractSubset1Display.Color = [0.0, 0.6666666666666666, 1.0]
extractSubset1Display.Opacity = 0.01

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# get 2D transfer function for 'temperature'
temperatureTF2D = pvs.GetTransferFunction2D('temperature')

# get color transfer function/color map for 'temperature'
temperatureLUT = pvs.GetColorTransferFunction('temperature')
temperatureLUT.TransferFunction2D = temperatureTF2D
temperatureLUT.RGBPoints = [293.0, 0.231373, 0.298039, 0.752941, 1950.171875, 0.865003, 0.865003, 0.865003, 3607.34375, 0.705882, 0.0156863, 0.14902]
temperatureLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'temperature'
temperaturePWF = pvs.GetOpacityTransferFunction('temperature')
temperaturePWF.Points = [293.0, 0.0, 0.5, 0.0, 3607.34375, 1.0, 0.5, 0.0]
temperaturePWF.ScalarRangeInitialized = 1

# show data from extractSubset1
extractSubset1Display_1 = pvs.Show(extractSubset1, renderView1, 'StructuredGridRepresentation')
extractSubset1Display_1.Representation = 'Surface'
extractSubset1Display_1.ColorArrayName = ['CELLS', 'temperature']
extractSubset1Display_1.LookupTable = temperatureLUT
extractSubset1Display_1.SelectTCoordArray = 'None'
extractSubset1Display_1.SelectNormalArray = 'None'
extractSubset1Display_1.SelectTangentArray = 'None'
extractSubset1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
extractSubset1Display_1.SelectOrientationVectors = 'None'
extractSubset1Display_1.ScaleFactor = 1275.6305636130483
extractSubset1Display_1.SelectScaleArray = 'None'
extractSubset1Display_1.GlyphType = 'Arrow'
extractSubset1Display_1.GlyphTableIndexArray = 'None'
extractSubset1Display_1.GaussianRadius = 63.781528180652415
extractSubset1Display_1.SetScaleArray = [None, '']
extractSubset1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
extractSubset1Display_1.OpacityArray = [None, '']
extractSubset1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
extractSubset1Display_1.DataAxesGrid = 'GridAxesRepresentation'
extractSubset1Display_1.PolarAxes = 'PolarAxesRepresentation'
extractSubset1Display_1.ScalarOpacityFunction = temperaturePWF
extractSubset1Display_1.ScalarOpacityUnitDistance = 102.56336101464876
extractSubset1Display_1.SelectInputVectors = [None, '']
extractSubset1Display_1.WriteLog = ''
extractSubset1Display_1.SetScalarBarVisibility(renderView1, True)

# setup the color legend parameters for each legend in this view

# get color legend/bar for temperatureLUT in view renderView1
temperatureLUTColorBar = pvs.GetScalarBar(temperatureLUT, renderView1)
temperatureLUTColorBar.Orientation = 'Horizontal'
temperatureLUTColorBar.WindowLocation = 'Any Location'
temperatureLUTColorBar.Position = [0.05956588526013498, 0.8678804153240243]
temperatureLUTColorBar.Title = 'temperature'
temperatureLUTColorBar.ComponentTitle = ''
temperatureLUTColorBar.ScalarBarLength = 0.864193548387096
temperatureLUTColorBar.Visibility = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# get 2D transfer function for 'thermalconductivity'
thermalconductivityTF2D = pvs.GetTransferFunction2D('thermalconductivity')

# get color transfer function/color map for 'thermalconductivity'
thermalconductivityLUT = pvs.GetColorTransferFunction('thermalconductivity')
thermalconductivityLUT.TransferFunction2D = thermalconductivityTF2D
thermalconductivityLUT.RGBPoints = [-0.5929329991340637, 0.231373, 0.298039, 0.752941, -0.0945453941822052, 0.865003, 0.865003, 0.865003, 0.4038422107696533, 0.705882, 0.0156863, 0.14902]
thermalconductivityLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'thermalconductivity'
thermalconductivityPWF = pvs.GetOpacityTransferFunction('thermalconductivity')
thermalconductivityPWF.Points = [-0.5929329991340637, 0.0, 0.5, 0.0, 0.4038422107696533, 1.0, 0.5, 0.0]
thermalconductivityPWF.ScalarRangeInitialized = 1

# show data from extractSubset1
extractSubset1Display_2 = pvs.Show(extractSubset1, renderView2, 'StructuredGridRepresentation')
extractSubset1Display_2.Representation = 'Surface'
extractSubset1Display_2.ColorArrayName = ['CELLS', 'thermal conductivity']
extractSubset1Display_2.LookupTable = thermalconductivityLUT
extractSubset1Display_2.SelectTCoordArray = 'None'
extractSubset1Display_2.SelectNormalArray = 'None'
extractSubset1Display_2.SelectTangentArray = 'None'
extractSubset1Display_2.OSPRayScaleFunction = 'PiecewiseFunction'
extractSubset1Display_2.SelectOrientationVectors = 'None'
extractSubset1Display_2.ScaleFactor = 1275.6307890537776
extractSubset1Display_2.SelectScaleArray = 'None'
extractSubset1Display_2.GlyphType = 'Arrow'
extractSubset1Display_2.GlyphTableIndexArray = 'None'
extractSubset1Display_2.GaussianRadius = 63.781539452688875
extractSubset1Display_2.SetScaleArray = [None, '']
extractSubset1Display_2.ScaleTransferFunction = 'PiecewiseFunction'
extractSubset1Display_2.OpacityArray = [None, '']
extractSubset1Display_2.OpacityTransferFunction = 'PiecewiseFunction'
extractSubset1Display_2.DataAxesGrid = 'GridAxesRepresentation'
extractSubset1Display_2.PolarAxes = 'PolarAxesRepresentation'
extractSubset1Display_2.ScalarOpacityFunction = thermalconductivityPWF
extractSubset1Display_2.ScalarOpacityUnitDistance = 432.91741789167685
extractSubset1Display_2.SelectInputVectors = [None, '']
extractSubset1Display_2.WriteLog = ''
extractSubset1Display_2.SetScalarBarVisibility(renderView2, True)

# get color legend/bar for thermalconductivityLUT in view renderView2
thermalconductivityLUTColorBar = pvs.GetScalarBar(thermalconductivityLUT, renderView2)
thermalconductivityLUTColorBar.Orientation = 'Horizontal'
thermalconductivityLUTColorBar.WindowLocation = 'Any Location'
thermalconductivityLUTColorBar.Position = [0.058716356107660406, 0.8396491228070173]
thermalconductivityLUTColorBar.Title = 'thermal conductivity'
thermalconductivityLUTColorBar.ComponentTitle = ''
thermalconductivityLUTColorBar.ScalarBarLength = 0.8714078674948267
thermalconductivityLUTColorBar.Visibility = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView3'
# ----------------------------------------------------------------

# get 2D transfer function for 'temperatureanomaly'
temperatureanomalyTF2D = pvs.GetTransferFunction2D('temperatureanomaly')

# get color transfer function/color map for 'temperatureanomaly'
temperatureanomalyLUT = pvs.GetColorTransferFunction('temperatureanomaly')
temperatureanomalyLUT.TransferFunction2D = temperatureanomalyTF2D
temperatureanomalyLUT.RGBPoints = [-1034.8974609375, 0.231373, 0.298039, 0.752941, -108.28192138671875, 0.865003, 0.865003, 0.865003, 818.3336181640625, 0.705882, 0.0156863, 0.14902]
temperatureanomalyLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'temperatureanomaly'
temperatureanomalyPWF = pvs.GetOpacityTransferFunction('temperatureanomaly')
temperatureanomalyPWF.Points = [-1034.8974609375, 0.0, 0.5, 0.0, 818.3336181640625, 1.0, 0.5, 0.0]
temperatureanomalyPWF.ScalarRangeInitialized = 1

# show data from extractSubset1
extractSubset1Display_3 = pvs.Show(extractSubset1, renderView3, 'StructuredGridRepresentation')
extractSubset1Display_3.Representation = 'Surface'
extractSubset1Display_3.ColorArrayName = ['CELLS', 'temperature anomaly']
extractSubset1Display_3.LookupTable = temperatureanomalyLUT
extractSubset1Display_3.SelectTCoordArray = 'None'
extractSubset1Display_3.SelectNormalArray = 'None'
extractSubset1Display_3.SelectTangentArray = 'None'
extractSubset1Display_3.OSPRayScaleFunction = 'PiecewiseFunction'
extractSubset1Display_3.SelectOrientationVectors = 'None'
extractSubset1Display_3.ScaleFactor = 1275.6307890537776
extractSubset1Display_3.SelectScaleArray = 'None'
extractSubset1Display_3.GlyphType = 'Arrow'
extractSubset1Display_3.GlyphTableIndexArray = 'None'
extractSubset1Display_3.GaussianRadius = 63.781539452688875
extractSubset1Display_3.SetScaleArray = [None, '']
extractSubset1Display_3.ScaleTransferFunction = 'PiecewiseFunction'
extractSubset1Display_3.OpacityArray = [None, '']
extractSubset1Display_3.OpacityTransferFunction = 'PiecewiseFunction'
extractSubset1Display_3.DataAxesGrid = 'GridAxesRepresentation'
extractSubset1Display_3.PolarAxes = 'PolarAxesRepresentation'
extractSubset1Display_3.ScalarOpacityFunction = temperatureanomalyPWF
extractSubset1Display_3.ScalarOpacityUnitDistance = 432.91741789167685
extractSubset1Display_3.SelectInputVectors = [None, '']
extractSubset1Display_3.WriteLog = ''
extractSubset1Display_3.SetScalarBarVisibility(renderView3, True)

# get color legend/bar for temperatureanomalyLUT in view renderView3
temperatureanomalyLUTColorBar = pvs.GetScalarBar(temperatureanomalyLUT, renderView3)
temperatureanomalyLUTColorBar.Orientation = 'Horizontal'
temperatureanomalyLUTColorBar.WindowLocation = 'Any Location'
temperatureanomalyLUTColorBar.Position = [0.10619246861924667, 0.8571929824561403]
temperatureanomalyLUTColorBar.Title = 'temperature anomaly'
temperatureanomalyLUTColorBar.ComponentTitle = ''
temperatureanomalyLUTColorBar.ScalarBarLength = 0.8174476987447701
temperatureanomalyLUTColorBar.Visibility = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView4'
# ----------------------------------------------------------------

# get 2D transfer function for 'thermalexpansivity'
thermalexpansivityTF2D = pvs.GetTransferFunction2D('thermalexpansivity')

# get color transfer function/color map for 'thermalexpansivity'
thermalexpansivityLUT = pvs.GetColorTransferFunction('thermalexpansivity')
thermalexpansivityLUT.TransferFunction2D = thermalexpansivityTF2D
thermalexpansivityLUT.RGBPoints = [-1.4406914488063194e-06, 0.231373, 0.298039, 0.752941, -5.022726980996595e-07, 0.865003, 0.865003, 0.865003, 4.3614605260700046e-07, 0.705882, 0.0156863, 0.14902]
thermalexpansivityLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'thermalexpansivity'
thermalexpansivityPWF = pvs.GetOpacityTransferFunction('thermalexpansivity')
thermalexpansivityPWF.Points = [-1.4406914488063194e-06, 0.0, 0.5, 0.0, 4.3614605260700046e-07, 1.0, 0.5, 0.0]
thermalexpansivityPWF.ScalarRangeInitialized = 1

# show data from extractSubset1
extractSubset1Display_4 = pvs.Show(extractSubset1, renderView4, 'StructuredGridRepresentation')
extractSubset1Display_4.Representation = 'Surface'
extractSubset1Display_4.ColorArrayName = ['CELLS', 'thermal expansivity']
extractSubset1Display_4.LookupTable = thermalexpansivityLUT
extractSubset1Display_4.SelectTCoordArray = 'None'
extractSubset1Display_4.SelectNormalArray = 'None'
extractSubset1Display_4.SelectTangentArray = 'None'
extractSubset1Display_4.OSPRayScaleFunction = 'PiecewiseFunction'
extractSubset1Display_4.SelectOrientationVectors = 'None'
extractSubset1Display_4.ScaleFactor = 1275.6307890537776
extractSubset1Display_4.SelectScaleArray = 'None'
extractSubset1Display_4.GlyphType = 'Arrow'
extractSubset1Display_4.GlyphTableIndexArray = 'None'
extractSubset1Display_4.GaussianRadius = 63.781539452688875
extractSubset1Display_4.SetScaleArray = [None, '']
extractSubset1Display_4.ScaleTransferFunction = 'PiecewiseFunction'
extractSubset1Display_4.OpacityArray = [None, '']
extractSubset1Display_4.OpacityTransferFunction = 'PiecewiseFunction'
extractSubset1Display_4.DataAxesGrid = 'GridAxesRepresentation'
extractSubset1Display_4.PolarAxes = 'PolarAxesRepresentation'
extractSubset1Display_4.ScalarOpacityFunction = thermalexpansivityPWF
extractSubset1Display_4.ScalarOpacityUnitDistance = 432.91741789167685
extractSubset1Display_4.SelectInputVectors = [None, '']
extractSubset1Display_4.WriteLog = ''
extractSubset1Display_4.SetScalarBarVisibility(renderView4, True)

# get color legend/bar for thermalexpansivityLUT in view renderView4
thermalexpansivityLUTColorBar = pvs.GetScalarBar(thermalexpansivityLUT, renderView4)
thermalexpansivityLUTColorBar.Orientation = 'Horizontal'
thermalexpansivityLUTColorBar.WindowLocation = 'Any Location'
thermalexpansivityLUTColorBar.Position = [0.06644351464435139, 0.8466666666666666]
thermalexpansivityLUTColorBar.Title = 'thermal expansivity'
thermalexpansivityLUTColorBar.ComponentTitle = ''
thermalexpansivityLUTColorBar.ScalarBarLength = 0.8530125523012553
thermalexpansivityLUTColorBar.Visibility = 1

# save screenshot
pvs.SaveScreenshot("./output/parallel_coordinates.png", layout1)
