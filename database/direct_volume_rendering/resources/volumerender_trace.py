# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
import paraview.simple as pvs
#### disable automatic camera reset on 'Show'
pvs._DisableFirstRenderCameraReset()

# create a new 'XML Image Data Reader'
ctBonesvti = pvs.XMLImageDataReader(registrationName='ctBones.vti', FileName=['./ctBones.vti'])     # OWN_DATA: replace the filename './ctBones.vti' with yours. It has to be a .vti file
ctBonesvti.PointArrayStatus = ['Scalars_']                                                          # OWN_DATA: every field has a name in a .vti file. Replace 'Scalars_' by the corresponding name

# get active view
renderView1 = pvs.GetActiveViewOrCreate('RenderView')

# show data in view
ctBonesvtiDisplay = pvs.Show(ctBonesvti, renderView1)
ctBonesvtiDisplay.SetRepresentationType('Volume')
pvs.ColorBy(ctBonesvtiDisplay, ('POINTS', 'Scalars_'))                                              # OWN_DATA: every field has a name in a .vti file. Replace 'Scalars_' by the corresponding name

# current camera placement for renderView1
renderView1.CameraPosition = [-423.3902339590129, 198.44191188274755, 304.85091798628196]
renderView1.CameraFocalPoint = [120.98375218527654, 119.8419039072476, 112.21062642326825]
renderView1.CameraViewUp = [-0.26270924860874034, -0.8866291025912916, -0.3806214459717057]
renderView1.CameraParallelScale = 220.83647796503186
renderView1.Background = [1.0, 1.0, 1.0]
renderView1.OrientationAxesVisibility = 0

pvs.ResetCamera(renderView1)

# save screenshot
pvs.SaveScreenshot('./volumerender.png', renderView1, ImageResolution=[1920, 1080])