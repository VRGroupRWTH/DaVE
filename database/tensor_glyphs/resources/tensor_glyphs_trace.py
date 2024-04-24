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
renderView1.CenterOfRotation = [16.720206636353396, 16.720206578145735, 16.72025606688112]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-62.273695794486905, 84.32590062949528, -70.08976914496148]
renderView1.CameraFocalPoint = [14.451357128357623, 15.786878937657141, 17.97062784513119]
renderView1.CameraViewUp = [0.31031897035270395, 0.8620974178744707, 0.4006122548467634]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 28.96664975823481
renderView1.LegendGrid = 'Legend Grid Actor'
renderView1.EnableRayTracing = 1
renderView1.BackEnd = 'OptiX pathtracer'
renderView1.SamplesPerPixel = 2
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
atomsvtk = LegacyVTKReader(registrationName='atoms.vtk', FileNames=['D:/Projects/LAMMPS/atoms.vtk'])

# create a new 'Tensor Glyph'
tensorGlyph1 = TensorGlyph(registrationName='TensorGlyph1', Input=atomsvtk,
    GlyphType='Superquadric')
tensorGlyph1.Tensors = ['POINTS', 'STRESS']
tensorGlyph1.Scalars = ['POINTS', '1']
tensorGlyph1.Colorby = 'eigenvalues'
tensorGlyph1.ScaleFactor = 0.001255177081143987
tensorGlyph1.LimitScalingByEigenvalues = 1
tensorGlyph1.MaxScaleFactor = 2.0

# init the 'Superquadric' selected for 'GlyphType'
tensorGlyph1.GlyphType.Thickness = 0.480052
tensorGlyph1.GlyphType.Toroidal = 0

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from tensorGlyph1
tensorGlyph1Display = Show(tensorGlyph1, renderView1, 'GeometryRepresentation')

# get 2D transfer function for 'MaxEigenvalue'
maxEigenvalueTF2D = GetTransferFunction2D('MaxEigenvalue')

# get color transfer function/color map for 'MaxEigenvalue'
maxEigenvalueLUT = GetColorTransferFunction('MaxEigenvalue')
maxEigenvalueLUT.TransferFunction2D = maxEigenvalueTF2D
maxEigenvalueLUT.RGBPoints = [-1.973176121711731, 0.231373, 0.298039, 0.752941, 0.013411939144134521, 0.865003, 0.865003, 0.865003, 2.0, 0.705882, 0.0156863, 0.14902]
maxEigenvalueLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
tensorGlyph1Display.Representation = 'Surface'
tensorGlyph1Display.ColorArrayName = ['POINTS', 'MaxEigenvalue']
tensorGlyph1Display.LookupTable = maxEigenvalueLUT
tensorGlyph1Display.Interpolation = 'PBR'
tensorGlyph1Display.SelectTCoordArray = 'None'
tensorGlyph1Display.SelectNormalArray = 'Normals'
tensorGlyph1Display.SelectTangentArray = 'None'
tensorGlyph1Display.OSPRayScaleArray = 'Normals'
tensorGlyph1Display.OSPRayScaleFunction = 'Piecewise Function'
tensorGlyph1Display.Assembly = ''
tensorGlyph1Display.SelectOrientationVectors = 'None'
tensorGlyph1Display.ScaleFactor = 3.3455792147666217
tensorGlyph1Display.SelectScaleArray = 'None'
tensorGlyph1Display.GlyphType = 'Arrow'
tensorGlyph1Display.GlyphTableIndexArray = 'None'
tensorGlyph1Display.GaussianRadius = 0.1672789607383311
tensorGlyph1Display.SetScaleArray = ['POINTS', 'Normals']
tensorGlyph1Display.ScaleTransferFunction = 'Piecewise Function'
tensorGlyph1Display.OpacityArray = ['POINTS', 'Normals']
tensorGlyph1Display.OpacityTransferFunction = 'Piecewise Function'
tensorGlyph1Display.DataAxesGrid = 'Grid Axes Representation'
tensorGlyph1Display.PolarAxes = 'Polar Axes Representation'
tensorGlyph1Display.SelectInputVectors = ['POINTS', 'Normals']
tensorGlyph1Display.WriteLog = ''
tensorGlyph1Display.InputVectors = ['POINTS', 'Normals']

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
tensorGlyph1Display.ScaleTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
tensorGlyph1Display.OpacityTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for maxEigenvalueLUT in view renderView1
maxEigenvalueLUTColorBar = GetScalarBar(maxEigenvalueLUT, renderView1)
maxEigenvalueLUTColorBar.Title = 'MaxEigenvalue'
maxEigenvalueLUTColorBar.ComponentTitle = ''

# set color bar visibility
maxEigenvalueLUTColorBar.Visibility = 1

# show color legend
tensorGlyph1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity maps used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'MaxEigenvalue'
maxEigenvaluePWF = GetOpacityTransferFunction('MaxEigenvalue')
maxEigenvaluePWF.Points = [-1.973176121711731, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]
maxEigenvaluePWF.ScalarRangeInitialized = 1

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
SetActiveSource(tensorGlyph1)
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