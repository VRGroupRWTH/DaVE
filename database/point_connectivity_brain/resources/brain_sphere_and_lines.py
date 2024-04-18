# state file generated using paraview version 5.12.0
import paraview
paraview.compatibility.major = 5
paraview.compatibility.minor = 12

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1149, 785]
renderView1.AxesGrid = 'Grid Axes 3D Actor'
renderView1.CenterOfRotation = [93.33623504638672, 73.32450866699219, 77.1865463256836]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [201.8962981554911, 428.0263262907966, 32.42807434152617]
renderView1.CameraFocalPoint = [93.33623504638663, 73.32450866699216, 77.18654632568361]
renderView1.CameraViewUp = [-0.011136481538551998, 0.12853993605242348, 0.9916418020729967]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 141.58354169032876
renderView1.LegendGrid = 'Legend Grid Actor'
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(1149, 785)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Legacy VTK Reader'
brainData_allvtk = LegacyVTKReader(registrationName='brainData_all.vtk', FileNames=['D:/Projects/Brain/SciVisContest23/viz-calcium/brainData_all.vtk'])

# create a new 'Glyph'
glyph1 = Glyph(registrationName='Glyph1', Input=brainData_allvtk,
    GlyphType='Sphere')
glyph1.OrientationArray = ['POINTS', 'No orientation array']
glyph1.ScaleArray = ['POINTS', 'No scale array']
glyph1.ScaleFactor = 18.667247009277343
glyph1.GlyphTransform = 'Transform2'
glyph1.GlyphMode = 'All Points'

# init the 'Sphere' selected for 'GlyphType'
glyph1.GlyphType.Radius = 0.08

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from brainData_allvtk
brainData_allvtkDisplay = Show(brainData_allvtk, renderView1, 'GeometryRepresentation')

# get 2D transfer function for 'Area'
areaTF2D = GetTransferFunction2D('Area')

# get color transfer function/color map for 'Area'
areaLUT = GetColorTransferFunction('Area')
areaLUT.TransferFunction2D = areaTF2D
areaLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 23.5, 0.865003, 0.865003, 0.865003, 47.0, 0.705882, 0.0156863, 0.14902]
areaLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
brainData_allvtkDisplay.Representation = 'Surface'
brainData_allvtkDisplay.AmbientColor = [0.0, 0.0, 0.0]
brainData_allvtkDisplay.ColorArrayName = ['POINTS', 'Area']
brainData_allvtkDisplay.DiffuseColor = [0.0, 0.0, 0.0]
brainData_allvtkDisplay.LookupTable = areaLUT
brainData_allvtkDisplay.Opacity = 0.1
brainData_allvtkDisplay.LineWidth = 3.0
brainData_allvtkDisplay.SelectTCoordArray = 'None'
brainData_allvtkDisplay.SelectNormalArray = 'None'
brainData_allvtkDisplay.SelectTangentArray = 'None'
brainData_allvtkDisplay.OSPRayScaleArray = 'Calcium_Target'
brainData_allvtkDisplay.OSPRayScaleFunction = 'Piecewise Function'
brainData_allvtkDisplay.Assembly = ''
brainData_allvtkDisplay.SelectOrientationVectors = 'None'
brainData_allvtkDisplay.ScaleFactor = 18.667247009277343
brainData_allvtkDisplay.SelectScaleArray = 'Calcium_Target'
brainData_allvtkDisplay.GlyphType = 'Arrow'
brainData_allvtkDisplay.GlyphTableIndexArray = 'Calcium_Target'
brainData_allvtkDisplay.GaussianRadius = 0.9333623504638672
brainData_allvtkDisplay.SetScaleArray = ['POINTS', 'Calcium_Target']
brainData_allvtkDisplay.ScaleTransferFunction = 'Piecewise Function'
brainData_allvtkDisplay.OpacityArray = ['POINTS', 'Calcium_Target']
brainData_allvtkDisplay.OpacityTransferFunction = 'Piecewise Function'
brainData_allvtkDisplay.DataAxesGrid = 'Grid Axes Representation'
brainData_allvtkDisplay.PolarAxes = 'Polar Axes Representation'
brainData_allvtkDisplay.SelectInputVectors = [None, '']
brainData_allvtkDisplay.WriteLog = ''
brainData_allvtkDisplay.InputVectors = [None, '']

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
brainData_allvtkDisplay.ScaleTransferFunction.Points = [0.6000019907951355, 0.0, 0.5, 0.0, 1.100000023841858, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
brainData_allvtkDisplay.OpacityTransferFunction.Points = [0.6000019907951355, 0.0, 0.5, 0.0, 1.100000023841858, 1.0, 0.5, 0.0]

# show data from glyph1
glyph1Display = Show(glyph1, renderView1, 'GeometryRepresentation')

# get 2D transfer function for 'Calcium_Target'
calcium_TargetTF2D = GetTransferFunction2D('Calcium_Target')

# get color transfer function/color map for 'Calcium_Target'
calcium_TargetLUT = GetColorTransferFunction('Calcium_Target')
calcium_TargetLUT.TransferFunction2D = calcium_TargetTF2D
calcium_TargetLUT.RGBPoints = [0.6000019907951355, 0.231373, 0.298039, 0.752941, 0.8500010073184967, 0.865003, 0.865003, 0.865003, 1.100000023841858, 0.705882, 0.0156863, 0.14902]
calcium_TargetLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = ['POINTS', 'Calcium_Target']
glyph1Display.LookupTable = calcium_TargetLUT
glyph1Display.SelectTCoordArray = 'None'
glyph1Display.SelectNormalArray = 'Normals'
glyph1Display.SelectTangentArray = 'None'
glyph1Display.OSPRayScaleArray = 'Calcium_Target'
glyph1Display.OSPRayScaleFunction = 'Piecewise Function'
glyph1Display.Assembly = ''
glyph1Display.SelectOrientationVectors = 'None'
glyph1Display.ScaleFactor = 20.320386695861817
glyph1Display.SelectScaleArray = 'Calcium_Target'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'Calcium_Target'
glyph1Display.GaussianRadius = 1.0160193347930908
glyph1Display.SetScaleArray = ['POINTS', 'Calcium_Target']
glyph1Display.ScaleTransferFunction = 'Piecewise Function'
glyph1Display.OpacityArray = ['POINTS', 'Calcium_Target']
glyph1Display.OpacityTransferFunction = 'Piecewise Function'
glyph1Display.DataAxesGrid = 'Grid Axes Representation'
glyph1Display.PolarAxes = 'Polar Axes Representation'
glyph1Display.SelectInputVectors = ['POINTS', 'Normals']
glyph1Display.WriteLog = ''
glyph1Display.InputVectors = ['POINTS', 'Normals']

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
glyph1Display.ScaleTransferFunction.Points = [0.6001489758491516, 0.0, 0.5, 0.0, 1.0259729623794556, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
glyph1Display.OpacityTransferFunction.Points = [0.6001489758491516, 0.0, 0.5, 0.0, 1.0259729623794556, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for areaLUT in view renderView1
areaLUTColorBar = GetScalarBar(areaLUT, renderView1)
areaLUTColorBar.WindowLocation = 'Upper Right Corner'
areaLUTColorBar.Title = 'Area'
areaLUTColorBar.ComponentTitle = ''

# set color bar visibility
areaLUTColorBar.Visibility = 1

# get color legend/bar for calcium_TargetLUT in view renderView1
calcium_TargetLUTColorBar = GetScalarBar(calcium_TargetLUT, renderView1)
calcium_TargetLUTColorBar.Title = 'Calcium_Target'
calcium_TargetLUTColorBar.ComponentTitle = ''

# set color bar visibility
calcium_TargetLUTColorBar.Visibility = 1

# show color legend
brainData_allvtkDisplay.SetScalarBarVisibility(renderView1, True)

# show color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity maps used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'Calcium_Target'
calcium_TargetPWF = GetOpacityTransferFunction('Calcium_Target')
calcium_TargetPWF.Points = [0.6000019907951355, 0.0, 0.5, 0.0, 1.100000023841858, 1.0, 0.5, 0.0]
calcium_TargetPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'Area'
areaPWF = GetOpacityTransferFunction('Area')
areaPWF.Points = [0.0, 0.0, 0.5, 0.0, 47.0, 1.0, 0.5, 0.0]
areaPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup animation scene, tracks and keyframes
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get time animation track
timeAnimationCue1 = GetTimeTrack()

# initialize the animation scene

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# initialize the timekeeper

# initialize the animation track

# get animation scene
animationScene1 = GetAnimationScene()

# initialize the animation scene
animationScene1.ViewModules = renderView1
animationScene1.Cues = timeAnimationCue1
animationScene1.AnimationTime = 0.0

# ----------------------------------------------------------------
# restore active source
SetActiveSource(brainData_allvtk)
# ----------------------------------------------------------------


##--------------------------------------------
## You may need to add some code at the end of this python script depending on your usage, eg:
#
## Render all views to see them appears
# RenderAllViews()
#
## Interact with the view, usefull when running from pvpython
# Interact()
#
## Save a screenshot of the active view
# SaveScreenshot("path/to/screenshot.png")
#
## Save a screenshot of a layout (multiple splitted view)
# SaveScreenshot("path/to/screenshot.png", GetLayout())
#
## Save all "Extractors" from the pipeline browser
# SaveExtracts()
#
## Save a animation of the current active view
# SaveAnimation()
#
## Please refer to the documentation of paraview.simple
## https://kitware.github.io/paraview-docs/latest/python/paraview.simple.html
##--------------------------------------------