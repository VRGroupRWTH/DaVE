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
reader.Dimensions = '(lat, r, lon)'                     # OWN_DATA: the example data specifies the dimensions in latitude, radius and longitude; change as needed

pvs.UpdatePipeline(time=0.0, proxy=reader)

# create a new 'Extract Subset'                                                                      
extractSubset1 = pvs.ExtractSubset(registrationName='ExtractSubset1', Input=reader)
extractSubset1.VOI = [0, 360, 0, 201, 90, 90]           # OWN_DATA: change the extracted subset

# create a new 'Scatter Plot'
scatterPlot1 = pvs.ScatterPlot(registrationName='ScatterPlot1', Input=extractSubset1)

pvs.UpdatePipeline(time=0.0, proxy=scatterPlot1)

# ----------------------------------------------------------------
# setup the views
# ----------------------------------------------------------------

#### disable automatic camera reset on 'Show'
pvs._DisableFirstRenderCameraReset()
pvs.LoadPalette('WhiteBackground')


# Create a new 'Plot Matrix View'
plotMatrixView1 = pvs.CreateView('PlotMatrixView')
plotMatrixView1.ViewSize = [1129, 1176] # [1047, 1176]
plotMatrixView1.ScatterPlotSelectedRowColumnColor = [0.8, 0.0, 0.0, 0.11764705882352941]
plotMatrixView1.ScatterPlotSelectedActiveColor = [0.0, 0.8, 0.0, 0.19607843137254902]
plotMatrixView1.ActivePlotGridColor = [0.8627450980392157, 0.8627450980392157, 0.8627450980392157]
plotMatrixView1.ScatterPlotGridColor = [0.8627450980392157, 0.8627450980392157, 0.8627450980392157]
plotMatrixView1.HistogramBackgroundColor = [1.0, 1.0, 1.0, 0.4]
plotMatrixView1.HistogramGridColor = [0.8627450980392157, 0.8627450980392157, 0.8627450980392157]

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

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

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
layout1.AssignView(2, plotMatrixView1)
layout1.SetSize(2087, 1176)

# ----------------------------------------------------------------
# setup the visualization in view 'plotMatrixView1'
# ----------------------------------------------------------------

# show data from scatterPlot1
scatterPlot1Display = pvs.Show(scatterPlot1, plotMatrixView1, 'PlotMatrixRepresentation')

# trace defaults for the display properties.
scatterPlot1Display.FieldAssociation = 'Cell Data'
# the first two entries determine whats visible in the larger plot
scatterPlot1Display.SeriesVisibility = ['spin transition-induced density anomaly', 'temperature', 'temperature anomaly', 'thermal conductivity', 'thermal expansivity'] # OWN_DATA: change field name
scatterPlot1Display.ScatterPlotsColor = [0.3215686274509804, 0.48627450980392156, 0.7843137254901961]
scatterPlot1Display.HistogramColor = [0.0, 0.0, 1.0]
scatterPlot1Display.ScatterPlotMarkerSize = 2.0
scatterPlot1Display.ActivePlotColor = [0.8627450980392157, 0.0, 0.0]
scatterPlot1Display.ActivePlotMarkerStyle = 'Cross'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# get 2D transfer function for 'temperature'
temperatureTF2D = pvs.GetTransferFunction2D('temperature')          # OWN_DATA: change field name

# get color transfer function/color map for 'temperature'
temperatureLUT = pvs.GetColorTransferFunction('temperature')        # OWN_DATA: change field name
temperatureLUT.TransferFunction2D = temperatureTF2D
temperatureLUT.RGBPoints = [293.0, 0.231373, 0.298039, 0.752941, 1950.171875, 0.865003, 0.865003, 0.865003, 3607.34375, 0.705882, 0.0156863, 0.14902]
temperatureLUT.ScalarRangeInitialized = 1.0

# show data from extractSubset1
extractSubset1Display_1 = pvs.Show(extractSubset1, renderView1, 'StructuredGridRepresentation')
extractSubset1Display_1.Representation = 'Surface'
extractSubset1Display_1.ColorArrayName = ['CELLS', 'temperature']   # OWN_DATA: change field name
extractSubset1Display_1.LookupTable = temperatureLUT
extractSubset1Display_1.SetScalarBarVisibility(renderView1, True)

# setup the color legend parameters for each legend in this view

# get color legend/bar for temperatureLUT in view renderView1
temperatureLUTColorBar = pvs.GetScalarBar(temperatureLUT, renderView1)
temperatureLUTColorBar.Orientation = 'Horizontal'
temperatureLUTColorBar.WindowLocation = 'Any Location'
temperatureLUTColorBar.Position = [0.05956588526013498, 0.8678804153240243]
temperatureLUTColorBar.Title = 'temperature'                        # OWN_DATA: change color bar title
temperatureLUTColorBar.ComponentTitle = ''
temperatureLUTColorBar.ScalarBarLength = 0.864193548387096
temperatureLUTColorBar.Visibility = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# get 2D transfer function for 'thermalconductivity'
thermalconductivityTF2D = pvs.GetTransferFunction2D('thermalconductivity')      # OWN_DATA: change field name

# get color transfer function/color map for 'thermalconductivity'
thermalconductivityLUT = pvs.GetColorTransferFunction('thermalconductivity')    # OWN_DATA: change field name
thermalconductivityLUT.TransferFunction2D = thermalconductivityTF2D
thermalconductivityLUT.RGBPoints = [-0.5929329991340637, 0.231373, 0.298039, 0.752941, -0.0945453941822052, 0.865003, 0.865003, 0.865003, 0.4038422107696533, 0.705882, 0.0156863, 0.14902]
thermalconductivityLUT.ScalarRangeInitialized = 1.0

# show data from extractSubset1
extractSubset1Display_2 = pvs.Show(extractSubset1, renderView2, 'StructuredGridRepresentation')
extractSubset1Display_2.Representation = 'Surface'
extractSubset1Display_2.ColorArrayName = ['CELLS', 'thermal conductivity']      # OWN_DATA: change field name
extractSubset1Display_2.LookupTable = thermalconductivityLUT
extractSubset1Display_2.SetScalarBarVisibility(renderView2, True)

# get color legend/bar for thermalconductivityLUT in view renderView2
thermalconductivityLUTColorBar = pvs.GetScalarBar(thermalconductivityLUT, renderView2)
thermalconductivityLUTColorBar.Orientation = 'Horizontal'
thermalconductivityLUTColorBar.WindowLocation = 'Any Location'
thermalconductivityLUTColorBar.Position = [0.058716356107660406, 0.8396491228070173]
thermalconductivityLUTColorBar.Title = 'thermal conductivity'                   # OWN_DATA: change color bar title
thermalconductivityLUTColorBar.ComponentTitle = ''
thermalconductivityLUTColorBar.ScalarBarLength = 0.8714078674948267
thermalconductivityLUTColorBar.Visibility = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView3'
# ----------------------------------------------------------------

# get 2D transfer function for 'temperatureanomaly'
temperatureanomalyTF2D = pvs.GetTransferFunction2D('temperatureanomaly')        # OWN_DATA: change field name

# get color transfer function/color map for 'temperatureanomaly'
temperatureanomalyLUT = pvs.GetColorTransferFunction('temperatureanomaly')      # OWN_DATA: change field name
temperatureanomalyLUT.TransferFunction2D = temperatureanomalyTF2D
temperatureanomalyLUT.RGBPoints = [-1034.8974609375, 0.231373, 0.298039, 0.752941, -108.28192138671875, 0.865003, 0.865003, 0.865003, 818.3336181640625, 0.705882, 0.0156863, 0.14902]
temperatureanomalyLUT.ScalarRangeInitialized = 1.0

# show data from extractSubset1
extractSubset1Display_3 = pvs.Show(extractSubset1, renderView3, 'StructuredGridRepresentation')
extractSubset1Display_3.Representation = 'Surface'
extractSubset1Display_3.ColorArrayName = ['CELLS', 'temperature anomaly']       # OWN_DATA: change field name
extractSubset1Display_3.LookupTable = temperatureanomalyLUT
extractSubset1Display_3.SetScalarBarVisibility(renderView3, True)

# get color legend/bar for temperatureanomalyLUT in view renderView3
temperatureanomalyLUTColorBar = pvs.GetScalarBar(temperatureanomalyLUT, renderView3)
temperatureanomalyLUTColorBar.Orientation = 'Horizontal'
temperatureanomalyLUTColorBar.WindowLocation = 'Any Location'
temperatureanomalyLUTColorBar.Position = [0.10619246861924667, 0.8571929824561403]
temperatureanomalyLUTColorBar.Title = 'temperature anomaly'                     # OWN_DATA: change color bar title
temperatureanomalyLUTColorBar.ComponentTitle = ''
temperatureanomalyLUTColorBar.ScalarBarLength = 0.8174476987447701
temperatureanomalyLUTColorBar.Visibility = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView4'
# ----------------------------------------------------------------

# get 2D transfer function for 'thermalexpansivity'
thermalexpansivityTF2D = pvs.GetTransferFunction2D('thermalexpansivity')        # OWN_DATA: change field name

# get color transfer function/color map for 'thermalexpansivity'
thermalexpansivityLUT = pvs.GetColorTransferFunction('thermalexpansivity')      # OWN_DATA: change field name
thermalexpansivityLUT.TransferFunction2D = thermalexpansivityTF2D
thermalexpansivityLUT.RGBPoints = [-1.4406914488063194e-06, 0.231373, 0.298039, 0.752941, -5.022726980996595e-07, 0.865003, 0.865003, 0.865003, 4.3614605260700046e-07, 0.705882, 0.0156863, 0.14902]
thermalexpansivityLUT.ScalarRangeInitialized = 1.0

# show data from extractSubset1
extractSubset1Display_4 = pvs.Show(extractSubset1, renderView4, 'StructuredGridRepresentation')
extractSubset1Display_4.Representation = 'Surface'
extractSubset1Display_4.ColorArrayName = ['CELLS', 'thermal expansivity']       # OWN_DATA: change field name
extractSubset1Display_4.LookupTable = thermalexpansivityLUT
extractSubset1Display_4.SetScalarBarVisibility(renderView4, True)

# get color legend/bar for thermalexpansivityLUT in view renderView4
thermalexpansivityLUTColorBar = pvs.GetScalarBar(thermalexpansivityLUT, renderView4)
thermalexpansivityLUTColorBar.Orientation = 'Horizontal'
thermalexpansivityLUTColorBar.WindowLocation = 'Any Location'
thermalexpansivityLUTColorBar.Position = [0.06644351464435139, 0.8466666666666666]
thermalexpansivityLUTColorBar.Title = 'thermal expansivity'                     # OWN_DATA: change color bar title
thermalexpansivityLUTColorBar.ComponentTitle = ''
thermalexpansivityLUTColorBar.ScalarBarLength = 0.8530125523012553
thermalexpansivityLUTColorBar.Visibility = 1

# save screenshot
pvs.SaveScreenshot("./output/scatterplots.png", layout1)
