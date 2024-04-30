# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10
import sys
from os import listdir
from os.path import exists
from os.path import isfile, join

#### import the simple module from the paraview
import paraview.simple as pvs

if len(sys.argv) < 2:
    print('no data file path provided - defaulting to "./data/"')
    path = './data/'
else:
    path = str(sys.argv[1])
if not exists(path):
    print("file(path) ", path," does not exist", file=sys.stderr)

input_files = [path+f for f in listdir(path) if isfile(join(path, f))]
input_files.sort()

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Image Data Reader'
reader = pvs.XMLImageDataReader(registrationName='reader', FileName=input_files)
reader.PointArrayStatus = ['ImageFile']                                 # OWN_DATA: every field has a name in a .vti file. Replace 'Scalars_' by the corresponding name

pvs.UpdatePipeline(time=0.0, proxy=reader)

# create a new 'Temporal Shift Scale'
temporalShiftScale1 = pvs.TemporalShiftScale(registrationName='TemporalShiftScale1', Input=reader)
temporalShiftScale1.PreShift = 0.0
temporalShiftScale1.PostShift = 0.0
temporalShiftScale1.Scale = 0.003
temporalShiftScale1.Periodic = 0
temporalShiftScale1.PeriodicEndCorrection = 1
temporalShiftScale1.MaximumNumberOfPeriods = 1.0

pvs.UpdatePipeline(time=0.0, proxy=temporalShiftScale1)

# create a new 'Disk'
disk1 = pvs.Disk(registrationName='Disk1')
disk1.InnerRadius = 0.0
disk1.OuterRadius = 0.14
disk1.RadialResolution = 20
disk1.CircumferentialResolution = 20

pvs.UpdatePipeline(time=0.0, proxy=disk1)

# create a new 'Transform'
transform1 = pvs.Transform(registrationName='Transform1', Input=disk1)
transform1.Transform = 'Transform'
transform1.Transform.Translate = [0.5, 0.1, 0.5]                        # OWN_DATA: This specifies the position and rotation of the disk that we use to seed the streamlines.
transform1.Transform.Rotate = [90.0, 0.0, 0.0]                          # OWN_DATA: For your application other positions or even other sources might be advantageous.

pvs.UpdatePipeline(time=0.0, proxy=transform1)

# create a new 'Mask Points'
maskPoints1 = pvs.MaskPoints(registrationName='MaskPoints1', Input=transform1)
maskPoints1.MaximumNumberofPoints = 99                              # OWN_DATA: for more pathlines increase the number of points here.
maskPoints1.RandomSampling = 1
maskPoints1.RandomSamplingMode = 'Random Sampling'

pvs.UpdatePipeline(time=0.0, proxy=maskPoints1)

# create a new 'ParticleTracer'
particleTracer1 = pvs.ParticleTracer(registrationName='ParticleTracer1', Input=temporalShiftScale1, SeedSource=maskPoints1)
particleTracer1.StaticSeeds = 1

pvs.UpdatePipeline(time=0.0, proxy=particleTracer1)

# create a new 'Temporal Particles To Pathlines'
temporalParticlesToPathlines1 = pvs.TemporalParticlesToPathlines(registrationName='TemporalParticlesToPathlines1', Input=particleTracer1, Selection=None)
temporalParticlesToPathlines1.MaskPoints = 1
temporalParticlesToPathlines1.MaxTrackLength = 150
temporalParticlesToPathlines1.MaxStepDistance = [1.0, 1.0, 1.0]
temporalParticlesToPathlines1.IdChannelArray = 'Global or Local IDs'

# ----------------------------------------------------------------
# setup the views
# ----------------------------------------------------------------

#### disable automatic camera reset on 'Show'
pvs._DisableFirstRenderCameraReset()
pvs.LoadPalette('WhiteBackground')

animationScene1 = pvs.GetAnimationScene()
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get 2D transfer function for 'Vorticity'
vorticityTF2D = GetTransferFunction2D('Vorticity')

# get color transfer function/color map for 'Vorticity'
vorticityLUT = GetColorTransferFunction('Vorticity')
vorticityLUT.TransferFunction2D = vorticityTF2D
vorticityLUT.RGBPoints = [-550, 0.231373, 0.298039, 0.752941, -7.13165283203125, 0.865003, 0.865003, 0.865003, 550, 0.705882, 0.0156863, 0.14902]
vorticityLUT.ScalarRangeInitialized = 1.0

renderView1 = pvs.GetActiveViewOrCreate('RenderView')
renderView1.OrientationAxesVisibility = 0
renderView1.CameraPosition = [0.5, 1.0, 2.5]                        # OWN_DATA: depending on the data another camera view is needed
renderView1.CameraFocalPoint = [0.5, 1.0, 0.5]
renderView1.CameraViewUp = [-1.0, 0.0, 0.0]
renderView1.CameraParallelScale = 1.2182888727290784

temporalParticlesToPathlines1Display_1 = pvs.Show(pvs.OutputPort(temporalParticlesToPathlines1, 0), renderView1, 'GeometryRepresentation')
temporalParticlesToPathlines1Display_1.RenderLinesAsTubes = 1
temporalParticlesToPathlines1Display_1.LineWidth = 2.0
temporalParticlesToPathlines1Display.ColorArrayName = ['POINTS', 'Vorticity']
temporalParticlesToPathlines1Display.LookupTable = vorticityLUT
temporalParticlesToPathlines1Display.SetScalarBarVisibility(renderView1, True)

# get color legend/bar for vorticityLUT in view renderView1
vorticityLUTColorBar = GetScalarBar(vorticityLUT, renderView1)
vorticityLUTColorBar.Orientation = 'Horizontal'
vorticityLUTColorBar.WindowLocation = 'Any Location'
vorticityLUTColorBar.Position = [0.02019230769230771, 0.835244755244755]
vorticityLUTColorBar.Title = 'Vorticity'
vorticityLUTColorBar.ComponentTitle = ''
vorticityLUTColorBar.ScalarBarLength = 0.9357692307692308
vorticityLUTColorBar.Visibility = 1

# pvs.ResetCamera(renderView1)                                      # OWN_DATA: if the original view does not fit ResetCamera can be used to focus on the visible data

# save animation
pvs.SaveAnimation('./output/pathline.png', renderView1, ImageResolution=[1920, 1080],
    FontScaling='Do not scale fonts',
    StereoMode='No change',
    TransparentBackground=0,
    FrameRate=10)