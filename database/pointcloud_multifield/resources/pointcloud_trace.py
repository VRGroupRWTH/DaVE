# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10
import sys
from os.path import exists

#### import the simple module from the paraview
import paraview.simple as pvs

if len(sys.argv) < 2:
    print('no data file path provided - defaulting to "./data/spherical001.nc"')
    filepath = './data/spherical001.nc'
else:
    filepath = str(sys.argv[1])

file_exists = exists(filepath)
if not file_exists:
    print("file ", filepath," does not exist", file=sys.stderr)

# create a new 'XML Unstructured Grid Reader'
reader = pvs.XMLUnstructuredGridReader(registrationName='pointcloud.vtu', FileName=[filepath])
reader.PointArrayStatus = ['concentration', 'velocity']
reader.TimeArray = 'None'

# create a new 'Glyph'
glyph1 = pvs.Glyph(registrationName='Glyph1', Input=reader, GlyphType='Arrow')
glyph1.OrientationArray = ['POINTS', 'velocity']
glyph1.ScaleArray = ['POINTS', 'velocity']
glyph1.ScaleFactor = 0.2
glyph1.GlyphTransform = 'Transform2'

# create a new 'Cylinder'
cylinder1 = pvs.Cylinder(registrationName='Cylinder1')
cylinder1.Resolution = 100
cylinder1.Height = 10.1
cylinder1.Radius = 5.05
cylinder1.Center = [0.0, 0.0, 5.0]

# create a new 'Transform'
transform1 = pvs.Transform(registrationName='Transform1', Input=cylinder1)
transform1.Transform = 'Transform'
transform1.Transform.Translate = [0.0, 5.0, 5.0]
transform1.Transform.Rotate = [90.0, 0.0, 0.0]

# |                       |
# | rendering stuff below |
# v                       v

#### disable automatic camera reset on 'Show'
pvs._DisableFirstRenderCameraReset()
pvs.LoadPalette('WhiteBackground')
renderView1 = pvs.GetActiveViewOrCreate('RenderView')
renderView1.OrientationAxesVisibility = 0
renderView1.ViewSize = [1920,1080]

# get 2D transfer function for 'concentration'
concentrationTF2D = pvs.GetTransferFunction2D('concentration')

# get color transfer function/color map for 'concentration'
concentrationLUT = pvs.GetColorTransferFunction('concentration')
concentrationLUT.TransferFunction2D = concentrationTF2D
concentrationLUT.RGBPoints = [0.0, 0.968627, 0.988235, 0.941176, 21.01116610861203, 0.926182, 0.971626, 0.902422, 43.42305281179809, 0.880907, 0.95391, 0.861084, 65.8349395149841, 0.841215, 0.938055, 0.817885, 88.24700481317136, 0.801845, 0.922307, 0.774579, 110.65889151635741, 0.732457, 0.895302, 0.74253, 133.07077821954346, 0.661592, 0.867743, 0.711034, 155.48266492272947, 0.573702, 0.83451, 0.738178, 177.89462842176607, 0.485121, 0.801046, 0.767705, 200.3066169241028, 0.39654, 0.752326, 0.797232, 222.7185036272888, 0.307958, 0.703114, 0.826759, 245.13039033047485, 0.238601, 0.62699, 0.787082, 267.54227703366087, 0.169704, 0.550219, 0.745744, 289.9541637368469, 0.100807, 0.479262, 0.710219, 312.36622903503417, 0.031911, 0.408397, 0.674787, 334.7781157382202, 0.031373, 0.329719, 0.590527, 357.19000244140625, 0.031373, 0.25098, 0.505882]
concentrationLUT.ColorSpace = 'Lab'
concentrationLUT.NanColor = [0.25, 0.0, 0.0]
concentrationLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'concentration'
concentrationPWF = pvs.GetOpacityTransferFunction('concentration')
concentrationPWF.Points = [0.0, 0.0, 0.5, 0.0, 357.19000244140625, 1.0, 0.5, 0.0]
concentrationPWF.ScalarRangeInitialized = 1

# show data from reader
readerDisplay = pvs.Show(reader, renderView1, 'UnstructuredGridRepresentation')
readerDisplay.Representation = 'Point Gaussian'
readerDisplay.ColorArrayName = ['POINTS', 'concentration']
readerDisplay.LookupTable = concentrationLUT
readerDisplay.SelectTCoordArray = 'None'
readerDisplay.SelectNormalArray = 'None'
readerDisplay.SelectTangentArray = 'None'
readerDisplay.OSPRayScaleArray = 'concentration'
readerDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
readerDisplay.SelectOrientationVectors = 'None'
readerDisplay.SelectScaleArray = 'None'
readerDisplay.GlyphType = 'Arrow'
readerDisplay.GlyphTableIndexArray = 'None'
readerDisplay.GaussianRadius = 0.05
readerDisplay.ShaderPreset = 'Black-edged circle'
readerDisplay.CustomTriangleScale = 10
readerDisplay.ScaleByArray = 1
readerDisplay.SetScaleArray = ['POINTS', 'concentration']
readerDisplay.ScaleTransferFunction = 'PiecewiseFunction'
readerDisplay.OpacityArray = ['POINTS', 'concentration']
readerDisplay.OpacityTransferFunction = 'PiecewiseFunction'
readerDisplay.DataAxesGrid = 'GridAxesRepresentation'
readerDisplay.PolarAxes = 'PolarAxesRepresentation'
readerDisplay.ScalarOpacityFunction = concentrationPWF
readerDisplay.ScalarOpacityUnitDistance = 17.319866903494006
readerDisplay.OpacityArrayName = ['POINTS', 'concentration']
readerDisplay.SelectInputVectors = ['POINTS', 'velocity']
readerDisplay.WriteLog = ''
readerDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 118.40552520751953, 0.4895833432674408, 0.5, 0.0, 357.19000244140625, 1.0, 0.5, 0.0]
readerDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 357.19000244140625, 1.0, 0.5, 0.0]


# get 2D transfer function for 'velocity'
velocityTF2D = pvs.GetTransferFunction2D('velocity')

# get color transfer function/color map for 'velocity'
velocityLUT = pvs.GetColorTransferFunction('velocity')
velocityLUT.TransferFunction2D = velocityTF2D
velocityLUT.RGBPoints = [0.003026407144074399, 0.0, 0.0, 0.0, 3.3797723175764762, 0.901960784314, 0.0, 0.0, 6.756518228008878, 0.901960784314, 0.901960784314, 0.0, 8.44489118322508, 1.0, 1.0, 1.0]
velocityLUT.ColorSpace = 'RGB'
velocityLUT.NanColor = [0.0, 0.498039215686, 1.0]
velocityLUT.ScalarRangeInitialized = 1.0

# show data from glyph1
glyph1Display = pvs.Show(glyph1, renderView1, 'GeometryRepresentation')
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = ['POINTS', 'velocity']
glyph1Display.LookupTable = velocityLUT
glyph1Display.SelectTCoordArray = 'None'
glyph1Display.SelectNormalArray = 'None'
glyph1Display.SelectTangentArray = 'None'
glyph1Display.OSPRayScaleArray = 'concentration'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'None'
glyph1Display.ScaleFactor = 1.0982380867004395
glyph1Display.SelectScaleArray = 'None'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'None'
glyph1Display.GaussianRadius = 0.05491190433502197
glyph1Display.SetScaleArray = ['POINTS', 'concentration']
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityArray = ['POINTS', 'concentration']
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display.PolarAxes = 'PolarAxesRepresentation'
glyph1Display.SelectInputVectors = ['POINTS', 'velocity']
glyph1Display.WriteLog = ''
glyph1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 357.19000244140625, 1.0, 0.5, 0.0]
glyph1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 357.19000244140625, 1.0, 0.5, 0.0]

# show data from transform1
transform1Display = pvs.Show(transform1, renderView1, 'GeometryRepresentation')
transform1Display.Representation = 'Surface'
transform1Display.ColorArrayName = ['POINTS', '']
transform1Display.SelectTCoordArray = 'TCoords'
transform1Display.SelectNormalArray = 'Normals'
transform1Display.SelectTangentArray = 'None'
transform1Display.BackfaceRepresentation = 'Cull Frontface'
transform1Display.OSPRayScaleArray = 'Normals'
transform1Display.OSPRayScaleFunction = 'PiecewiseFunction'
transform1Display.SelectOrientationVectors = 'None'
transform1Display.ScaleFactor = 1.0000000000000002
transform1Display.SelectScaleArray = 'None'
transform1Display.GlyphType = 'Arrow'
transform1Display.GlyphTableIndexArray = 'None'
transform1Display.GaussianRadius = 0.05000000000000001
transform1Display.SetScaleArray = ['POINTS', 'Normals']
transform1Display.ScaleTransferFunction = 'PiecewiseFunction'
transform1Display.OpacityArray = ['POINTS', 'Normals']
transform1Display.OpacityTransferFunction = 'PiecewiseFunction'
transform1Display.DataAxesGrid = 'GridAxesRepresentation'
transform1Display.PolarAxes = 'PolarAxesRepresentation'
transform1Display.SelectInputVectors = ['POINTS', 'Normals']
transform1Display.WriteLog = ''
transform1Display.ScaleTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
transform1Display.OpacityTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for concentrationLUT in view renderView1
concentrationLUTColorBar = pvs.GetScalarBar(concentrationLUT, renderView1)
concentrationLUTColorBar.WindowLocation = 'Any Location'
concentrationLUTColorBar.Position = [0.15532178217821782, 0.14510204081632638]
concentrationLUTColorBar.Title = 'concentration'
concentrationLUTColorBar.ComponentTitle = ''
concentrationLUTColorBar.ScalarBarLength = 0.6905442176870749
concentrationLUTColorBar.Visibility = 1

# get color legend/bar for velocityLUT in view renderView1
velocityLUTColorBar = pvs.GetScalarBar(velocityLUT, renderView1)
velocityLUTColorBar.WindowLocation = 'Any Location'
velocityLUTColorBar.Position = [0.7639356435643564, 0.12840136054421752]
velocityLUTColorBar.Title = 'velocity'
velocityLUTColorBar.ComponentTitle = 'Magnitude'
velocityLUTColorBar.ScalarBarLength = 0.7050000000000005
velocityLUTColorBar.Visibility = 1

# show color legend
readerDisplay.SetScalarBarVisibility(renderView1, True)

# show color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'velocity'
velocityPWF = pvs.GetOpacityTransferFunction('velocity')
velocityPWF.Points = [0.003026407144074399, 0.0, 0.5, 0.0, 8.44489118322508, 1.0, 0.5, 0.0]
velocityPWF.ScalarRangeInitialized = 1


renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [0.0, 0.007591962814331055, 4.885129779577255]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-28.157227993824886, -0.2490307073232333, 5.257232651276721]
renderView1.CameraFocalPoint = [0.0, -0.2490307073232333, 5.257232651276721]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 8.818028503135828
renderView1.UseAmbientOcclusion = 0
# renderView1.BackEnd = 'OSPRay raycaster'
# renderView1.OSPRayMaterialLibrary = materialLibrary1



## create a new key frame                                                                                                                    
keyFrame26616 = pvs.CameraKeyFrame()
keyFrame26616.KeyTime = 0.0
keyFrame26616.KeyValues = [0.0]
keyFrame26616.Position = [-24.0246, 0.0, 4.93976]
keyFrame26616.FocalPoint = [0.0, 0.0, 5.0]
keyFrame26616.ViewUp = [0.0, 0.0, 1.0]
keyFrame26616.ViewAngle = 30.0
keyFrame26616.ParallelScale = 8.78178
keyFrame26616.PositionPathPoints = [-24.0246, 0.0, 4.93976, -14.979093093735331, -18.783188633701428, 4.93976, 5.3459764299268695, -23.422253119003443, 4.93976, 21.645416663808458, -10.423883278803693, 4.93976, 21.645416663808465, 10.423883278803679, 4.93976, 5.345976429926882, 23.42225311900344, 4.93976, -14.979093093735324, 18.78318863370144, 4.93976 , -14.979093093735324, 18.78318863370144, 4.93976]
keyFrame26616.FocalPathPoints = [0.0, 0.0, 5.0]
keyFrame26616.PositionMode = 'Path'
keyFrame26616.FocalPointMode = 'Path'
keyFrame26616.ClosedFocalPath = 0
keyFrame26616.ClosedPositionPath = 1

# create a new key frame                                                                                                                    
keyFrame26617 = pvs.CameraKeyFrame()
keyFrame26617.KeyTime = 1.0
keyFrame26617.KeyValues = [0.0]
keyFrame26617.Position = [-24.0246, 0.0, 4.93976]
keyFrame26617.FocalPoint = [0.0, 0.0, 5.0]
keyFrame26617.ViewUp = [0.0, 0.0, 1.0]
keyFrame26617.ViewAngle = 30.0
keyFrame26617.ParallelScale = 8.78178
keyFrame26617.PositionPathPoints = [5.0, 0.0, 0.0, 5.0, 5.0, 0.0, 5.0, 0.0, 0.0]
keyFrame26617.FocalPathPoints = [0.0, 0.0, 0.0, 1.0, 0.0, 0.0]
keyFrame26617.PositionMode = 'Path'
keyFrame26617.FocalPointMode = 'Path'
keyFrame26617.ClosedFocalPath = 0
keyFrame26617.ClosedPositionPath = 0

cameraAnimationCue1 = pvs.GetCameraTrack(view=renderView1)
cameraAnimationCue1.TimeMode = 'Normalized'
cameraAnimationCue1.StartTime = 0.0
cameraAnimationCue1.EndTime = 1.0
cameraAnimationCue1.Enabled = 1
cameraAnimationCue1.Mode = 'Path-based'
cameraAnimationCue1.Interpolation = 'Spline'
cameraAnimationCue1.KeyFrames = [keyFrame26616, keyFrame26617]
cameraAnimationCue1.DataSource = None

animationScene1 = pvs.GetAnimationScene()
animationScene1.NumberOfFrames=100
animationScene1.StartTime=0.0
animationScene1.EndTime=1.0

pvs.SaveAnimation('./output/pointcloud.png',
  renderView1,
  scene=animationScene1,
  ImageResolution=[1920, 1080])

# save screenshot
# pvs.SaveScreenshot('./output/pointcloud.png', 
#     renderView1, 
#     ImageResolution=[1920, 1080],
#     FontScaling='Do not scale fonts')