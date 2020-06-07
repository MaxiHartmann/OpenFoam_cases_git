#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get animation scene
animationScene1 = GetAnimationScene()

animationScene1.GoToLast()

animationScene1.GoToLast()

# find source
turbulentFlatPlate_1foam = FindSource('turbulentFlatPlate_1.foam')

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(Input=turbulentFlatPlate_1foam,
    Source='High Resolution Line Source')

# init the 'High Resolution Line Source' selected for 'Source'
plotOverLine1.Source.Point1 = [-0.3333333432674408, 0.0, 0.0]
plotOverLine1.Source.Point2 = [2.0, 1.0, 0.10000000149011612]

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1062, 820]

#change interaction mode for render view
renderView1.InteractionMode = '2D'

# reset view to fit data
renderView1.ResetCamera()

# set active source
SetActiveSource(turbulentFlatPlate_1foam)

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')

# get display properties
turbulentFlatPlate_1foamDisplay = GetDisplayProperties(turbulentFlatPlate_1foam, view=renderView1)

# change representation type
turbulentFlatPlate_1foamDisplay.SetRepresentationType('Wireframe')

# set active source
SetActiveSource(plotOverLine1)

# Properties modified on plotOverLine1.Source
plotOverLine1.Source.Point1 = [0.97, 0.0, 0.0]
plotOverLine1.Source.Point2 = [0.97, 0.015, 0.0]

# Properties modified on plotOverLine1.Source
plotOverLine1.Source.Point1 = [0.97, 0.0, 0.0]
plotOverLine1.Source.Point2 = [0.97, 0.015, 0.0]

# show data in view
plotOverLine1Display = Show(plotOverLine1, renderView1)
# trace defaults for the display properties.
plotOverLine1Display.Representation = 'Surface'
plotOverLine1Display.AmbientColor = [0.0, 0.0, 0.0]
plotOverLine1Display.ColorArrayName = ['POINTS', 'p']
plotOverLine1Display.LookupTable = pLUT
plotOverLine1Display.OSPRayScaleArray = 'p'
plotOverLine1Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1Display.SelectOrientationVectors = 'U'
plotOverLine1Display.ScaleFactor = 0.0014999999664723875
plotOverLine1Display.SelectScaleArray = 'p'
plotOverLine1Display.GlyphType = 'Arrow'
plotOverLine1Display.GlyphTableIndexArray = 'p'
plotOverLine1Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1Display.PolarAxes = 'PolarAxesRepresentation'
plotOverLine1Display.GaussianRadius = 0.0007499999832361937
plotOverLine1Display.SetScaleArray = ['POINTS', 'p']
plotOverLine1Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.OpacityArray = ['POINTS', 'p']
plotOverLine1Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
plotOverLine1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
plotOverLine1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
plotOverLine1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
plotOverLine1Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
plotOverLine1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
plotOverLine1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
plotOverLine1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
plotOverLine1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
plotOverLine1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
plotOverLine1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')
lineChartView1.ViewSize = [526, 820]
lineChartView1.LeftAxisRangeMaximum = 6.66
lineChartView1.BottomAxisRangeMaximum = 6.66
lineChartView1.RightAxisRangeMaximum = 6.66
lineChartView1.TopAxisRangeMaximum = 6.66

# get layout
layout1 = GetLayout()

# place view in the layout
layout1.AssignView(2, lineChartView1)

# show data in view
plotOverLine1Display_1 = Show(plotOverLine1, lineChartView1)
# trace defaults for the display properties.
plotOverLine1Display_1.CompositeDataSetIndex = [0]
plotOverLine1Display_1.UseIndexForXAxis = 0
plotOverLine1Display_1.XArrayName = 'arc_length'
plotOverLine1Display_1.SeriesVisibility = ['C_Magnitude', 'Cx', 'Cy', 'Cz', 'k', 'nut', 'omega', 'p', 'U_Magnitude', 'wallShearStress_Magnitude', 'yPlus']
plotOverLine1Display_1.SeriesLabel = ['arc_length', 'arc_length', 'C_X', 'C_X', 'C_Y', 'C_Y', 'C_Z', 'C_Z', 'C_Magnitude', 'C_Magnitude', 'Cx', 'Cx', 'Cy', 'Cy', 'Cz', 'Cz', 'k', 'k', 'nut', 'nut', 'omega', 'omega', 'p', 'p', 'U_X', 'U_X', 'U_Y', 'U_Y', 'U_Z', 'U_Z', 'U_Magnitude', 'U_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'wallShearStress_X', 'wallShearStress_X', 'wallShearStress_Y', 'wallShearStress_Y', 'wallShearStress_Z', 'wallShearStress_Z', 'wallShearStress_Magnitude', 'wallShearStress_Magnitude', 'yPlus', 'yPlus', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'C_X', '0.89', '0.1', '0.11', 'C_Y', '0.22', '0.49', '0.72', 'C_Z', '0.3', '0.69', '0.29', 'C_Magnitude', '0.6', '0.31', '0.64', 'Cx', '1', '0.5', '0', 'Cy', '0.65', '0.34', '0.16', 'Cz', '0', '0', '0', 'k', '0.89', '0.1', '0.11', 'nut', '0.22', '0.49', '0.72', 'omega', '0.3', '0.69', '0.29', 'p', '0.6', '0.31', '0.64', 'U_X', '1', '0.5', '0', 'U_Y', '0.65', '0.34', '0.16', 'U_Z', '0', '0', '0', 'U_Magnitude', '0.89', '0.1', '0.11', 'vtkValidPointMask', '0.22', '0.49', '0.72', 'wallShearStress_X', '0.3', '0.69', '0.29', 'wallShearStress_Y', '0.6', '0.31', '0.64', 'wallShearStress_Z', '1', '0.5', '0', 'wallShearStress_Magnitude', '0.65', '0.34', '0.16', 'yPlus', '0', '0', '0', 'Points_X', '0.89', '0.1', '0.11', 'Points_Y', '0.22', '0.49', '0.72', 'Points_Z', '0.3', '0.69', '0.29', 'Points_Magnitude', '0.6', '0.31', '0.64']
plotOverLine1Display_1.SeriesPlotCorner = ['arc_length', '0', 'C_X', '0', 'C_Y', '0', 'C_Z', '0', 'C_Magnitude', '0', 'Cx', '0', 'Cy', '0', 'Cz', '0', 'k', '0', 'nut', '0', 'omega', '0', 'p', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'wallShearStress_X', '0', 'wallShearStress_Y', '0', 'wallShearStress_Z', '0', 'wallShearStress_Magnitude', '0', 'yPlus', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesLabelPrefix = ''
plotOverLine1Display_1.SeriesLineStyle = ['arc_length', '1', 'C_X', '1', 'C_Y', '1', 'C_Z', '1', 'C_Magnitude', '1', 'Cx', '1', 'Cy', '1', 'Cz', '1', 'k', '1', 'nut', '1', 'omega', '1', 'p', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'wallShearStress_X', '1', 'wallShearStress_Y', '1', 'wallShearStress_Z', '1', 'wallShearStress_Magnitude', '1', 'yPlus', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display_1.SeriesLineThickness = ['arc_length', '2', 'C_X', '2', 'C_Y', '2', 'C_Z', '2', 'C_Magnitude', '2', 'Cx', '2', 'Cy', '2', 'Cz', '2', 'k', '2', 'nut', '2', 'omega', '2', 'p', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'U_Magnitude', '2', 'vtkValidPointMask', '2', 'wallShearStress_X', '2', 'wallShearStress_Y', '2', 'wallShearStress_Z', '2', 'wallShearStress_Magnitude', '2', 'yPlus', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['arc_length', '0', 'C_X', '0', 'C_Y', '0', 'C_Z', '0', 'C_Magnitude', '0', 'Cx', '0', 'Cy', '0', 'Cz', '0', 'k', '0', 'nut', '0', 'omega', '0', 'p', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'wallShearStress_X', '0', 'wallShearStress_Y', '0', 'wallShearStress_Z', '0', 'wallShearStress_Magnitude', '0', 'yPlus', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
lineChartView1.Update()

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['C_Magnitude', 'Cx', 'Cy', 'Cz', 'k', 'nut', 'omega', 'p', 'U_Magnitude', 'wallShearStress_Magnitude']
plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'C_X', '0.889998', '0.100008', '0.110002', 'C_Y', '0.220005', '0.489998', '0.719997', 'C_Z', '0.300008', '0.689998', '0.289998', 'C_Magnitude', '0.6', '0.310002', '0.639994', 'Cx', '1', '0.500008', '0', 'Cy', '0.650004', '0.340002', '0.160006', 'Cz', '0', '0', '0', 'k', '0.889998', '0.100008', '0.110002', 'nut', '0.220005', '0.489998', '0.719997', 'omega', '0.300008', '0.689998', '0.289998', 'p', '0.6', '0.310002', '0.639994', 'U_X', '1', '0.500008', '0', 'U_Y', '0.650004', '0.340002', '0.160006', 'U_Z', '0', '0', '0', 'U_Magnitude', '0.889998', '0.100008', '0.110002', 'vtkValidPointMask', '0.220005', '0.489998', '0.719997', 'wallShearStress_X', '0.300008', '0.689998', '0.289998', 'wallShearStress_Y', '0.6', '0.310002', '0.639994', 'wallShearStress_Z', '1', '0.500008', '0', 'wallShearStress_Magnitude', '0.650004', '0.340002', '0.160006', 'yPlus', '0', '0', '0', 'Points_X', '0.889998', '0.100008', '0.110002', 'Points_Y', '0.220005', '0.489998', '0.719997', 'Points_Z', '0.300008', '0.689998', '0.289998', 'Points_Magnitude', '0.6', '0.310002', '0.639994']
plotOverLine1Display_1.SeriesPlotCorner = ['C_Magnitude', '0', 'C_X', '0', 'C_Y', '0', 'C_Z', '0', 'Cx', '0', 'Cy', '0', 'Cz', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'k', '0', 'nut', '0', 'omega', '0', 'p', '0', 'vtkValidPointMask', '0', 'wallShearStress_Magnitude', '0', 'wallShearStress_X', '0', 'wallShearStress_Y', '0', 'wallShearStress_Z', '0', 'yPlus', '0']
plotOverLine1Display_1.SeriesLineStyle = ['C_Magnitude', '1', 'C_X', '1', 'C_Y', '1', 'C_Z', '1', 'Cx', '1', 'Cy', '1', 'Cz', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'arc_length', '1', 'k', '1', 'nut', '1', 'omega', '1', 'p', '1', 'vtkValidPointMask', '1', 'wallShearStress_Magnitude', '1', 'wallShearStress_X', '1', 'wallShearStress_Y', '1', 'wallShearStress_Z', '1', 'yPlus', '1']
plotOverLine1Display_1.SeriesLineThickness = ['C_Magnitude', '2', 'C_X', '2', 'C_Y', '2', 'C_Z', '2', 'Cx', '2', 'Cy', '2', 'Cz', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'arc_length', '2', 'k', '2', 'nut', '2', 'omega', '2', 'p', '2', 'vtkValidPointMask', '2', 'wallShearStress_Magnitude', '2', 'wallShearStress_X', '2', 'wallShearStress_Y', '2', 'wallShearStress_Z', '2', 'yPlus', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['C_Magnitude', '0', 'C_X', '0', 'C_Y', '0', 'C_Z', '0', 'Cx', '0', 'Cy', '0', 'Cz', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'k', '0', 'nut', '0', 'omega', '0', 'p', '0', 'vtkValidPointMask', '0', 'wallShearStress_Magnitude', '0', 'wallShearStress_X', '0', 'wallShearStress_Y', '0', 'wallShearStress_Z', '0', 'yPlus', '0']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['C_Magnitude', 'Cx', 'Cy', 'Cz', 'k', 'nut', 'omega', 'p', 'U_Magnitude']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['C_Magnitude', 'Cx', 'Cy', 'Cz', 'k', 'nut', 'omega', 'U_Magnitude']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['C_Magnitude', 'Cx', 'Cy', 'Cz', 'k', 'nut', 'U_Magnitude']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['C_Magnitude', 'Cx', 'Cy', 'Cz', 'k', 'U_Magnitude']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['C_Magnitude', 'Cx', 'Cy', 'Cz', 'U_Magnitude']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['C_Magnitude', 'Cx', 'Cy', 'Cz']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['C_Magnitude', 'Cx', 'Cy', 'Cz', 'U_X']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['C_Magnitude', 'Cx', 'Cy', 'U_X']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['C_Magnitude', 'Cx', 'U_X']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['C_Magnitude', 'U_X']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['U_X']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.XArrayName = 'Cy'

# Properties modified on lineChartView1
lineChartView1.BottomAxisLogScale = 1

# Properties modified on lineChartView1
lineChartView1.BottomAxisUseCustomRange = 1

# Properties modified on lineChartView1
lineChartView1.BottomAxisRangeMinimum = 0.001

# Properties modified on lineChartView1
lineChartView1.BottomAxisRangeMinimum = 0.0001

# Properties modified on lineChartView1
lineChartView1.BottomAxisRangeMinimum = 1e-05

# Properties modified on lineChartView1
lineChartView1.BottomAxisRangeMaximum = 0.02

# Properties modified on lineChartView1
lineChartView1.BottomAxisRangeMaximum = 0.1

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.XArrayName = 'arc_length'

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.AttributeType = 'Cell Data'

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.AttributeType = 'Field Data'

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.AttributeType = 'Point Data'

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [1.0025471576537972, -0.04562726941856429, 4.962825070100116]
renderView1.CameraFocalPoint = [1.0025471576537972, -0.04562726941856429, 0.042606087401509285]
renderView1.CameraParallelScale = 0.08830503730733955

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).