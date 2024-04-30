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
# setup the data processing pipelines
# ----------------------------------------------------------------

colorBarTitleFontSize = 16
colorBarLabelFontSize = 8
colorBarThickness = 16
colorBarPosition = [0.9, 0.3]
colorBarLength = 0.8
colorBarTitle = "density"

# create a new 'Text'
text1 = pvs.Text(registrationName='Text1')
text1.Text = 'YZ plane'

text2 = pvs.Text(registrationName='Text2')
text2.Text = 'XZ plane'

text3 = pvs.Text(registrationName='Text3')
text3.Text = 'XY plane'

# create a new 'XML Image Data Reader'
reader = pvs.XMLImageDataReader(registrationName='ctBones.vti', FileName=[filepath])
reader.PointArrayStatus = ['Scalars_']                                                  # OWN_DATA: change field name
reader.TimeArray = 'None'
pvs.UpdatePipeline(time=0.0, proxy=reader)
extent = reader.GetDataInformation().GetExtent()

# create a new 'Slice'
slice1 = pvs.Slice(registrationName='Slice1', Input=reader)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]
slice1.SliceType.Origin = [127.0, 127.0, 127.0]

# create a new 'Slice'
slice2 = pvs.Slice(registrationName='Slice2', Input=reader)
slice2.SliceType = 'Plane'
slice2.HyperTreeGridSlicer = 'Plane'
slice2.SliceOffsetValues = [0.0]
slice2.SliceType.Origin = [127.0, 127.0, 127.0]
slice2.SliceType.Normal = [0.0, 1.0, 0.0]

# create a new 'Slice'
slice3 = pvs.Slice(registrationName='Slice3', Input=reader)
slice3.SliceType = 'Plane'
slice3.HyperTreeGridSlicer = 'Plane'
slice3.SliceOffsetValues = [0.0]
slice3.SliceType.Origin = [127.0, 127.0, 127.0]
slice3.SliceType.Normal = [0.0, 0.0, 1.0]


# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

pvs._DisableFirstRenderCameraReset()
pvs.LoadPalette('WhiteBackground')

# Create a new 'Render View'
renderView1 = pvs.CreateView('RenderView')
renderView1.ViewSize = [1076, 570]
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [823.6729559300638, 127.5, 127.5]
renderView1.CameraFocalPoint = [127.0, 127.5, 127.5]
renderView1.CameraViewUp = [0.0, 1.0, 0.0]
renderView1.CameraViewAngle = 22.748538011695906
renderView1.CameraParallelScale = 141.64878824295428

# Create a new 'Render View'
renderView2 = pvs.CreateView('RenderView')
renderView2.ViewSize = [1076, 570]
renderView2.InteractionMode = '2D'
renderView2.CameraPosition = [127.5, 127.5, 823.6729559300638]
renderView2.CameraFocalPoint = [127.5, 127.5, 127.0]
renderView2.CameraParallelScale = 141.64878824295428

# Create a new 'Render View'
renderView3 = pvs.CreateView('RenderView')
renderView3.ViewSize = [1075, 570]
renderView3.InteractionMode = '2D'
renderView3.CameraPosition = [529.2243186433548, 529.7243186433545, 529.7243186433548]
renderView3.CameraFocalPoint = [127.0, 127.5, 127.5]
renderView3.CameraViewUp = [-0.4082482904638631, 0.816496580927726, -0.40824829046386296]
renderView3.CameraParallelScale = 180.31222920256963

# Create a new 'Render View'
renderView4 = pvs.CreateView('RenderView')
renderView4.ViewSize = [1075, 570]
renderView4.InteractionMode = '2D'
renderView4.CameraPosition = [127.5, 823.6729559300638, 127.5]
renderView4.CameraFocalPoint = [127.5, 127.0, 127.5]
renderView4.CameraViewUp = [0.0, 0.0, -1.0]
renderView4.CameraParallelScale = 141.64878824295428

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# get 2D transfer function for 'Scalars_'
scalars_TF2D = pvs.GetTransferFunction2D('Scalars_')                # OWN_DATA: change field name
scalars_TF2D.ScalarRangeInitialized = 1
scalars_TF2D.Range = [0.0, 255.0, 0.0, 1.0]

# get color transfer function/color map for 'Scalars_'
scalars_LUT = pvs.GetColorTransferFunction('Scalars_')              # OWN_DATA: change field name
scalars_LUT.TransferFunction2D = scalars_TF2D
scalars_LUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 127.5, 0.865003, 0.865003, 0.865003, 255.0, 0.705882, 0.0156863, 0.14902]
scalars_LUT.ScalarRangeInitialized = 1.0

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

# show data from reader
readerDisplay = pvs.Show(reader, renderView1, 'UniformGridRepresentation')
readerDisplay.Representation = 'Slice'
readerDisplay.ColorArrayName = ['POINTS', 'Scalars_']           # OWN_DATA: change field name
readerDisplay.LookupTable = scalars_LUT
readerDisplay.SliceFunction = 'Plane'
readerDisplay.SliceMode = 'YZ Plane'
readerDisplay.Slice = 127
readerDisplay.SliceFunction.Origin = [127.5, 127.5, 127.5]
readerDisplay.SetScalarBarVisibility(renderView1, True)

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

# show data from reader
readerDisplay_1 = pvs.Show(reader, renderView2, 'UniformGridRepresentation')
readerDisplay_1.Representation = 'Slice'
readerDisplay_1.ColorArrayName = ['POINTS', 'Scalars_']         # OWN_DATA: change field name
readerDisplay_1.LookupTable = scalars_LUT
readerDisplay_1.SliceFunction = 'Plane'
readerDisplay_1.Slice = 127
readerDisplay_1.SliceFunction.Origin = [127.5, 127.5, 127.5]
readerDisplay_1.SetScalarBarVisibility(renderView2, True)

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
slice1Display.ColorArrayName = ['POINTS', 'Scalars_']               # OWN_DATA: change field name
slice1Display.LookupTable = scalars_LUT

# show data from slice2
slice2Display = pvs.Show(slice2, renderView3, 'GeometryRepresentation')
slice2Display.Representation = 'Surface'
slice2Display.ColorArrayName = ['POINTS', 'Scalars_']               # OWN_DATA: change field name
slice2Display.LookupTable = scalars_LUT

# show data from slice3
slice3Display = pvs.Show(slice3, renderView3, 'GeometryRepresentation')
slice3Display.Representation = 'Surface'
slice3Display.ColorArrayName = ['POINTS', 'Scalars_']               # OWN_DATA: change field name
slice3Display.LookupTable = scalars_LUT

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

# show data from reader
readerDisplay_2 = pvs.Show(reader, renderView4, 'UniformGridRepresentation')
readerDisplay_2.Representation = 'Slice'
readerDisplay_2.ColorArrayName = ['POINTS', 'Scalars_']         # OWN_DATA: change field name
readerDisplay_2.LookupTable = scalars_LUT
readerDisplay_2.SliceFunction = 'Plane'
readerDisplay_2.SliceMode = 'XZ Plane'
readerDisplay_2.Slice = 127
readerDisplay_2.SliceFunction.Origin = [127.5, 127.5, 127.5]
readerDisplay_2.SetScalarBarVisibility(renderView4, True)

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
    readerDisplay_1.Slice = XYSlice # XY
    slice3.SliceType.Origin = [127.0, 127.0, XYSlice]
    imageName = "image/" + str(XYSlice) + ".png"
    pvs.SaveScreenshot('./output/sliceview1.cdb/' + imageName, renderView2, ImageResolution=[960, 540])
    data_xy.append([XYSlice, imageName])

    for XZSlice in range(y_range[0], y_range[1],step):
        readerDisplay_2.Slice = XZSlice # XZ
        slice2.SliceType.Origin = [127.0, XZSlice, 127.0]
        if XYSlice == z_range[0]:
            imageName = "image/" + str(XZSlice) + ".png"
            pvs.SaveScreenshot('./output/sliceview2.cdb/' + imageName, renderView4, ImageResolution=[960, 540])
            data_xz.append([XZSlice, imageName])

        for YZSlice in range(x_range[0], x_range[1],step):
            readerDisplay.Slice = YZSlice # YZ
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