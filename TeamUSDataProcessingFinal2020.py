# Lee Bradley, Martha Gizaw, Nate Winneg
# Engineering Physics Capstone Project
# Unstable Seniors: Data Processing
# May 2020

# Import the libraries below
from DebugSubroutinesTeamUS import PlotThigh, PlotCalf, PlotFoot, PlotLegRaising

# Turn on/off the following debug variables to control which human feature to
# look at.
debugThigh = False # Change to True if you wish to visualize the thigh data.
debugCalf = False # Change to True if you wish to visualize the calf data.
debugFoot = False # Change to True if you wish to visualize the foot data.
debugLeg = False # Change to True if you wish to visualize the raising leg data.

# Initialize the following variables as empty arrays.
xRoll = []
yRoll = []

xPitch = []
yPitch = []

xYaw = []
yYaw = []

xQuatW = []
yQuatW = []

xQuatX = []
yQuatX = []

xQuatY = []
yQuatY = []

xQuatZ = []
yQuatZ = []

netAngleChange = []
pointsMinMax = []

# Call the subroutines by turning on only one debug value for any human feature.
if (debugThigh == True) and (debugCalf == False) and (debugFoot == False) and (debugLeg == False):
    thigh = PlotThigh()
    thigh.euler_angle_thigh(xRoll, yRoll, xPitch, yPitch, xYaw, yYaw)
    thigh.quaternion_thigh(xQuatW, yQuatW, xQuatX, yQuatX, xQuatY, yQuatY, xQuatZ, yQuatZ)
    thigh.dot_product_thigh(xQuatW, yQuatW, xQuatX, yQuatX, xQuatY, yQuatY, xQuatZ, yQuatZ, netAngleChange)
    thigh.euler_combo_thigh(xRoll, yRoll, yPitch, yYaw, yQuatY, yQuatZ)
    
elif (debugThigh == False) and (debugCalf == True) and (debugFoot == False) and (debugLeg == False):
    calf = PlotCalf()
    calf.euler_angle_calf(xRoll, yRoll, xPitch, yPitch, xYaw, yYaw)
    calf.quaternion_calf(xQuatW, yQuatW, xQuatX, yQuatX, xQuatY, yQuatY, xQuatZ, yQuatZ)
    calf.dot_product_calf(xQuatW, yQuatW, xQuatX, yQuatX, xQuatY, yQuatY, xQuatZ, yQuatZ, netAngleChange)
    calf.euler_combo_calf(xRoll, yRoll, yPitch, yYaw, yQuatY, yQuatZ)
    
elif (debugThigh == False) and (debugCalf == False) and (debugFoot == True) and (debugLeg == False):
    foot = PlotFoot()
    foot.euler_angle_foot(xRoll, yRoll, xPitch, yPitch, xYaw, yYaw)
    foot.quaternion_foot(xQuatW, yQuatW, xQuatX, yQuatX, xQuatY, yQuatY, xQuatZ, yQuatZ)
    foot.dot_product_foot(xQuatW, yQuatW, xQuatX, yQuatX, xQuatY, yQuatY, xQuatZ, yQuatZ, netAngleChange)
    foot.euler_combo_foot(xRoll, yRoll, yPitch, yYaw, yQuatY, yQuatZ)

elif (debugThigh == False) and (debugCalf == False) and (debugFoot == False) and (debugLeg == True):
    leg = PlotLegRaising()
    leg.leg_quat_analysis(xQuatW, yQuatW, xQuatX, yQuatX, xQuatY, yQuatY, xQuatZ, yQuatZ)
    leg.leg_net_angles(xQuatW, yQuatW, xQuatX, yQuatX, xQuatY, yQuatY, xQuatZ, yQuatZ, netAngleChange, pointsMinMax)
    
else:
    print("Sorry, but you would rather want to look at the plots one human" +
          " feature at a time and explain them before moving on. Please turn" +
          " off or turn on any of the debug variables provided to you, and" +
          " have only one of them turned on to plot the desired data.")
