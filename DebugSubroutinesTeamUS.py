# Lee Bradley, Martha Gizaw, Nate Winneg
# Engineering Physics Capstone Project
# Unstable Seniors: Data Processing
# May 2020

# Import the following libraries.
import matplotlib.pyplot as plt
import numpy as np
import csv
import math

class PlotThigh:
    # PURPOSE: Plot the total angle change about the axis of the thigh.

    # Initialize the Euler and quaternion CSV input variables as empty arrays.
    def __init__(self, xThighRoll = [], yThighRoll = [], xThighPitch = [],
                 yThighPitch = [], xThighYaw = [], yThighYaw = [],
                 xThighW = [], yThighW = [], xThighX = [], yThighX = [],
                 xThighY = [], yThighY = [], xThighZ = [], yThighZ = [],
                 changeThigh = []):
        # Euler angles
        self.xThighRoll = xThighRoll
        self.yThighRoll = yThighRoll
        self.xThighPitch = xThighPitch
        self.yThighPitch = yThighPitch
        self.xThighYaw = xThighYaw
        self.yThighYaw = yThighYaw

        # W, X, Y, and Z coordinates in a quaternion
        self.xThighW = xThighW
        self.yThighW = yThighW
        self.xThighX = xThighX
        self.yThighX = yThighX
        self.xThighY = xThighY
        self.yThighY = yThighY
        self.xThighZ = xThighZ
        self.yThighZ = yThighZ

        # For finding the net angles changes about the limb's axis
        self.changeThigh = changeThigh

    # Execute the CSV readers, and append the data to the appropriate arrays
    # for each Euler angle to be plotted.
    # For presentation purposes, set the Euler angles
    # to zero at the initial time of the user selected interval, where we can describe
    # the events of a single cycle of leg motion (eg, walking, sitting, etc.)
    def euler_angle_thigh(self, xThighRoll, yThighRoll, xThighPitch, yThighPitch, xThighYaw, yThighYaw):
        figThigh, axsThigh = plt.subplots(3, sharex = True, sharey = False)
        figThigh.suptitle('Euler Axis Rotations for THIGH')
        
        with open('angles_thigh_roll2.csv', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            for row in plots:
                xThighRoll.append(float(row[0]))
                yThighRoll.append(float(row[1]))
        setRoll2Zero = []
        for t in range(0, len(xThighRoll)):
            setRoll2Zero.append(yThighRoll[t]-yThighRoll[500])
        axsThigh[0].plot(xThighRoll, setRoll2Zero, linewidth = 2, color='teal')
        axsThigh[0].set(xlabel='', ylabel='Roll')
        axsThigh[0].set_xlim(500, 750)
        axsThigh[0].set_ylim(20, -20)

        with open('angles_thigh_pitch2.csv', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            for row in plots:
                xThighPitch.append(float(row[0]))
                yThighPitch.append(float(row[1]))
        setPitch2Zero = []
        for t in range(0, len(xThighPitch)):
            setPitch2Zero.append(yThighPitch[t]-yThighPitch[500])
        axsThigh[1].plot(xThighPitch, setPitch2Zero, linewidth = 2, color='magenta')
        axsThigh[1].set(xlabel='', ylabel='Pitch')
        axsThigh[1].set_xlim(500, 750)
        axsThigh[1].set_ylim(50, -50)

        with open('angles_thigh_yaw2.csv', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            for row in plots:
                xThighYaw.append(float(row[0]))
                yThighYaw.append(float(row[1]))
        setYaw2Zero = []
        for t in range(0, len(xThighYaw)):
            setYaw2Zero.append(yThighYaw[t]-yThighYaw[500])
        axsThigh[2].plot(xThighYaw, setYaw2Zero, linewidth = 2, color='black')
        axsThigh[2].set(xlabel='', ylabel='Yaw')
        axsThigh[2].set_xlim(500, 750)
        axsThigh[2].set_ylim(20, -20)

        # Optional!
        # figThigh.show()

    # Execute the CSV readers, and append the data to the appropriate arrays
    # for each quaternion to be plotted.
    def quaternion_thigh(self, xThighW, yThighW, xThighX, yThighX, xThighY,
                         yThighY, xThighZ, yThighZ):
        figQuats, axsQuats = plt.subplots(4, sharex = True, sharey = False)
        figQuats.suptitle('Quaternion Axis Rotations for THIGH')

        with open('angles_thigh_W2.csv', 'r') as csvfile:
            plots= csv.reader(csvfile, delimiter=',')
            for row in plots:
                xThighW.append(float(row[0]))
                yThighW.append(float(row[1]))
        axsQuats[0].plot(xThighW, yThighW, color='blue')
        axsQuats[0].set(xlabel='', ylabel='W')
        axsQuats[0].set_xlim(500, 750)

        with open('angles_thigh_X2.csv', 'r') as csvfile:
            plots= csv.reader(csvfile, delimiter=',')
            for row in plots:
                xThighX.append(float(row[0]))
                yThighX.append(float(row[1]))
        axsQuats[1].plot(xThighX, yThighX, color='red')
        axsQuats[1].set(xlabel='', ylabel='X')
        axsQuats[1].set_xlim(500, 750)

        with open('angles_thigh_Y2.csv', 'r') as csvfile:
            plots= csv.reader(csvfile, delimiter=',')
            for row in plots:
                xThighY.append(float(row[0]))
                yThighY.append(float(row[1]))
        axsQuats[2].plot(xThighY, yThighY, color='green')
        axsQuats[2].set(xlabel='', ylabel='Y')
        axsQuats[2].set_xlim(500, 750)

        with open('angles_thigh_Z2.csv', 'r') as csvfile:
            plots= csv.reader(csvfile, delimiter=',')
            for row in plots:
                xThighZ.append(float(row[0]))
                yThighZ.append(float(row[1]))
        axsQuats[3].plot(xThighZ, yThighZ, color='orange')
        axsQuats[3].set(xlabel='Time (count)', ylabel='Z')
        axsQuats[3].set_xlim(500, 750)

        # Optional!
        # figQuats.show()

    # Calculate 2 times the inverse cosine
    # of the dot product between two quaternions, and convert the net angle
    # change to degrees. Show the plots!
    def dot_product_thigh(self, xThighW, yThighW, xThighX, yThighX, xThighY,
                         yThighY, xThighZ, yThighZ, changeThigh):
        oneRad2Degrees = 57.296
        changeThighFix = []
        for t1 in range(0, len(xThighW)):    
            changeThigh.append(np.arccos(np.minimum(1, yThighW[0]*yThighW[t1] +
                                           yThighX[0]*yThighX[t1] +
                                           yThighY[0]*yThighY[t1] +
                                           yThighZ[0]*yThighZ[t1]))*(180/np.pi)-(oneRad2Degrees/2))

        for t2 in range(0, len(xThighW)):
            changeThighFix.append(changeThigh[t2]-changeThigh[500])

        fig, axs = plt.subplots()
        axs.set_title('Quaternion-Based Net Angle Changes for THIGH')
        axs.plot(changeThighFix, color='blue')
        axs.set_xlim(500, 750)
        axs.set_ylim(-20, 20)
        axs.set(xlabel='Time (seconds)', ylabel='Total Angle Change (degrees)')
        axs.invert_yaxis()
        positions = (500, 550, 600, 650, 700, 750)
        labels = (14.42, 15.86, 17.30, 18.75, 20.19, 21.63)
        plt.xticks(positions, labels)
        fig.show()

    # Combine the Euler angles when more than one are changing significantly.
    def euler_combo_thigh(self, xThighRoll, yThighRoll, yThighPitch, yThighYaw,
                          yThighY, yThighZ):

        # Initialize the following variables for Euler-based net angle changes.
        theta_array = []
        R = []

        combinedEulerX = []
        combinedEulerY = []
        combinedEulerZ = []

        combinedNetAngle = []
        undoCombinedCos = []
        undoCombinedSin = []

        combinedQuatW = []
        combinedQuatX = []
        combinedQuatY = []
        combinedQuatZ = []

        rebuildCombined = []
        rebuildCombinedFix = []

        # Convert the original Euler angles into rotation matrices to be all
        # multiplied.
        for t3 in range(0, len(xThighRoll)):
            theta = [yThighRoll[t3] * (np.pi/180), yThighPitch[t3]* (np.pi/180), yThighYaw[t3]* (np.pi/180)]
            theta_array.append(theta)

            R_x = np.array([[1,         0,                  0                   ],
                            [0,         math.cos(theta[0]), -math.sin(theta[0]) ],
                            [0,         math.sin(theta[0]), math.cos(theta[0])  ]
                            ])
                
                
                            
            R_y = np.array([[math.cos(theta[1]),    0,      math.sin(theta[1])  ],
                            [0,                     1,      0                   ],
                            [-math.sin(theta[1]),   0,      math.cos(theta[1])  ]
                            ])
                        
            R_z = np.array([[math.cos(theta[2]),    -math.sin(theta[2]),    0],
                            [math.sin(theta[2]),    math.cos(theta[2]),     0],
                            [0,                     0,                      1]
                            ])

            R.append(np.dot(R_x, np.dot(R_y, R_z)))

            # Report the new Euler rotations about their axes from the resultant
            # rotation matrix.
            combinedEulerX.append(math.atan2(R[t3][2,1], R[t3][2,2]))
            combinedEulerY.append(math.asin(R[t3][0,2]))
            combinedEulerZ.append(math.atan2(R[t3][1,0], R[t3][0,0]))

            # Obtain the cosine and sin of half of one of the new Euler rotations.
            combinedNetAngle.append(combinedEulerY[t3] * (180/np.pi))
            undoCombinedCos.append(np.cos(combinedNetAngle[t3] * (np.pi/360)))
            undoCombinedSin.append(np.sin(combinedNetAngle[t3] * (np.pi/360)))

            # Compute all 4 quaternion coordinates.
            combinedQuatW.append(undoCombinedCos[t3])
            combinedQuatX.append(undoCombinedSin[t3] * np.sin(0.5*np.pi) * np.cos(np.pi))
            combinedQuatY.append(0.01 * (yThighY[t3] / 2) * np.cos(yThighY[t3]/(undoCombinedSin[t3])))
            combinedQuatZ.append(0.01 * (yThighZ[t3] / 2) * np.cos(yThighZ[t3]/(undoCombinedSin[t3])))

            # Use the coordinates above to find the combined-Euler based net angle change.
            rebuildCombined.append(np.arccos(np.minimum(1,
                                    combinedQuatW[0]*combinedQuatW[t3] +
                                    combinedQuatX[0]*combinedQuatX[t3] +
                                    combinedQuatY[0]*combinedQuatY[t3] +
                                    combinedQuatZ[0]*combinedQuatZ[t3])) *(180/np.pi))

        # Set the net angle change to zero at the beginning of the plot interval.
        for t4 in range(0, len(xThighRoll)):
            rebuildCombinedFix.append(rebuildCombined[t4]-rebuildCombined[500])

        # Show the plots!
        fig, axs = plt.subplots()
        axs.set_title('Euler-Based Net Angle Changes for THIGH')
        axs.plot(rebuildCombinedFix, color='violet')
        axs.set_xlim(500, 750)
        axs.set_ylim(-20, 20)
        axs.set(xlabel='Time (seconds)', ylabel='Total Angle Change (degrees)')
        axs.invert_yaxis()
        positions = (500, 550, 600, 650, 700, 750)
        labels = (14.42, 15.86, 17.30, 18.75, 20.19, 21.63)
        plt.xticks(positions, labels)
        fig.show()

class PlotCalf:
    # PURPOSE: Plot the total angle change about the axis of the calf.

    def __init__(self, xCalfRoll = [], yCalfRoll = [], xCalfPitch = [],
                 yCalfPitch = [], xCalfYaw = [], yCalfYaw = [],
                 xCalfW = [], yCalfW = [], xCalfX = [], yCalfX = [],
                 xCalfY = [], yCalfY = [], xCalfZ = [], yCalfZ = [],
                 changeCalf = []):
        self.xCalfRoll = xCalfRoll
        self.yCalfRoll = yCalfRoll
        self.xCalfPitch = xCalfPitch
        self.yCalfPitch = yCalfPitch
        self.xCalfYaw = xCalfYaw
        self.yCalfYaw = yCalfYaw
        
        self.xCalfW = xCalfW
        self.yCalfW = yCalfW
        self.xCalfX = xCalfX
        self.yCalfX = yCalfX
        self.xCalfY = xCalfY
        self.yCalfY = yCalfY
        self.xCalfZ = xCalfZ
        self.yCalfZ = yCalfZ

        self.changeCalf = changeCalf

    def euler_angle_calf(self, xCalfRoll, yCalfRoll, xCalfPitch, yCalfPitch, xCalfYaw, yCalfYaw):
        figCalf, axsCalf = plt.subplots(3, sharex = True, sharey = False)
        figCalf.suptitle('Euler Axis Rotations for CALF')
        
        with open('angles_calf_roll2.csv', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            for row in plots:
                xCalfRoll.append(float(row[0]))
                yCalfRoll.append(float(row[1]))
        setRoll2Zero = []
        for t in range(0, len(xCalfRoll)):
            setRoll2Zero.append(yCalfRoll[t]-yCalfRoll[500])
        axsCalf[0].plot(xCalfRoll, setRoll2Zero, linewidth = 2, color='teal')
        axsCalf[0].set(xlabel='', ylabel='Roll')
        axsCalf[0].set_xlim(500, 750)
        axsCalf[0].set_ylim(20, -20)

        with open('angles_calf_pitch2.csv', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            for row in plots:
                xCalfPitch.append(float(row[0]))
                yCalfPitch.append(float(row[1]))
        setPitch2Zero = []
        for t in range(0, len(xCalfPitch)):
            setPitch2Zero.append(yCalfPitch[t]-yCalfPitch[500])
        axsCalf[1].plot(xCalfPitch, setPitch2Zero, linewidth = 2, color='magenta')
        axsCalf[1].set(xlabel='', ylabel='Pitch')
        axsCalf[1].set_xlim(500, 750)
        axsCalf[1].set_ylim(50, -50)

        with open('angles_calf_yaw2.csv', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            for row in plots:
                xCalfYaw.append(float(row[0]))
                yCalfYaw.append(float(row[1]))
        setYaw2Zero = []
        for t in range(0, len(xCalfYaw)):
            setYaw2Zero.append(yCalfYaw[t]-yCalfYaw[500])
        axsCalf[2].plot(xCalfYaw, setYaw2Zero, linewidth = 2, color='black')
        axsCalf[2].set(xlabel='', ylabel='Yaw')
        axsCalf[2].set_xlim(500, 750)
        axsCalf[2].set_ylim(20, -20)

        # Optional!
        # figCalf.show()

    def quaternion_calf(self, xCalfW, yCalfW, xCalfX, yCalfX, xCalfY,
                         yCalfY, xCalfZ, yCalfZ):
        figQuats, axsQuats = plt.subplots(4, sharex = True, sharey = False)
        figQuats.suptitle('Quaternion Axis Rotations for CALF')

        with open('angles_calf_W2.csv', 'r') as csvfile:
            plots= csv.reader(csvfile, delimiter=',')
            for row in plots:
                xCalfW.append(float(row[0]))
                yCalfW.append(float(row[1]))
        axsQuats[0].plot(xCalfW, yCalfW, color='blue')
        axsQuats[0].set(xlabel='', ylabel='W')
        axsQuats[0].set_xlim(500, 750)

        with open('angles_calf_X2.csv', 'r') as csvfile:
            plots= csv.reader(csvfile, delimiter=',')
            for row in plots:
                xCalfX.append(float(row[0]))
                yCalfX.append(float(row[1]))
        axsQuats[1].plot(xCalfX, yCalfX, color='red')
        axsQuats[1].set(xlabel='', ylabel='X')
        axsQuats[1].set_xlim(500, 750)

        with open('angles_calf_Y2.csv', 'r') as csvfile:
            plots= csv.reader(csvfile, delimiter=',')
            for row in plots:
                xCalfY.append(float(row[0]))
                yCalfY.append(float(row[1]))
        axsQuats[2].plot(xCalfY, yCalfY, color='green')
        axsQuats[2].set(xlabel='', ylabel='Y')
        axsQuats[2].set_xlim(500, 750)

        with open('angles_calf_Z2.csv', 'r') as csvfile:
            plots= csv.reader(csvfile, delimiter=',')
            for row in plots:
                xCalfZ.append(float(row[0]))
                yCalfZ.append(float(row[1]))
        axsQuats[3].plot(xCalfZ, yCalfZ, color='orange')
        axsQuats[3].set(xlabel='Time (count)', ylabel='Z')
        axsQuats[3].set_xlim(500, 750)

        # Optional!
        # figQuats.show()

    def dot_product_calf(self, xCalfW, yCalfW, xCalfX, yCalfX, xCalfY,
                         yCalfY, xCalfZ, yCalfZ, changeCalf):
        oneRad2Degrees = 57.296
        changeCalfFix = []
        for t1 in range(0, len(xCalfW)):    
            changeCalf.append(np.arccos(np.minimum(1, yCalfW[0]*yCalfW[t1] +
                                           yCalfX[0]*yCalfX[t1] +
                                           yCalfY[0]*yCalfY[t1] +
                                           yCalfZ[0]*yCalfZ[t1]))*(180/np.pi)-(oneRad2Degrees/2))

        for t2 in range(0, len(xCalfW)):
            changeCalfFix.append(changeCalf[t2]-changeCalf[500])

        fig, axs = plt.subplots()
        axs.set_title('Quaternion-Based Net Angle Changes for CALF')
        axs.plot(changeCalfFix, color='blue')
        axs.set_xlim(500, 750)
        axs.set_ylim(-20, 20)
        axs.set(xlabel='Time (seconds)', ylabel='Total Angle Change (degrees)')
        axs.invert_yaxis()
        positions = (500, 550, 600, 650, 700, 750)
        labels = (14.42, 15.86, 17.30, 18.75, 20.19, 21.63)
        plt.xticks(positions, labels)
        fig.show()

    def euler_combo_calf(self, xCalfRoll, yCalfRoll, yCalfPitch, yCalfYaw,
                          yCalfY, yCalfZ):
        theta_array = []
        R = []

        combinedEulerX = []
        combinedEulerY = []
        combinedEulerZ = []

        combinedNetAngle = []
        undoCombinedCos = []
        undoCombinedSin = []

        combinedQuatW = []
        combinedQuatX = []
        combinedQuatY = []
        combinedQuatZ = []

        rebuildCombined = []
        rebuildCombinedFix = []

        for t3 in range(0, len(xCalfRoll)):
            theta = [yCalfRoll[t3] * (np.pi/180), yCalfPitch[t3]* (np.pi/180), yCalfYaw[t3]* (np.pi/180)]
            theta_array.append(theta)

            R_x = np.array([[1,         0,                  0                   ],
                            [0,         math.cos(theta[0]), -math.sin(theta[0]) ],
                            [0,         math.sin(theta[0]), math.cos(theta[0])  ]
                            ])
                
                
                            
            R_y = np.array([[math.cos(theta[1]),    0,      math.sin(theta[1])  ],
                            [0,                     1,      0                   ],
                            [-math.sin(theta[1]),   0,      math.cos(theta[1])  ]
                            ])
                        
            R_z = np.array([[math.cos(theta[2]),    -math.sin(theta[2]),    0],
                            [math.sin(theta[2]),    math.cos(theta[2]),     0],
                            [0,                     0,                      1]
                            ])

            R.append(np.dot(R_x, np.dot(R_y, R_z)))

            combinedEulerX.append(math.atan2(R[t3][2,1], R[t3][2,2]))
            combinedEulerY.append(math.asin(R[t3][0,2]))
            combinedEulerZ.append(math.atan2(R[t3][1,0], R[t3][0,0]))

            combinedNetAngle.append(combinedEulerY[t3] * (180/np.pi))
            undoCombinedCos.append(np.cos(combinedNetAngle[t3] * (np.pi/360)))
            undoCombinedSin.append(np.sin(combinedNetAngle[t3] * (np.pi/360)))

            combinedQuatW.append(undoCombinedCos[t3])
            combinedQuatX.append(undoCombinedSin[t3] * np.sin(0.5*np.pi) * np.cos(np.pi))
            combinedQuatY.append(0.01 * (yCalfY[t3] / 2) * np.cos(yCalfY[t3]/(undoCombinedSin[t3])))
            combinedQuatZ.append(0.01 * (yCalfZ[t3] / 2) * np.cos(yCalfZ[t3]/(undoCombinedSin[t3])))

            rebuildCombined.append(np.arccos(np.minimum(1,
                                    combinedQuatW[0]*combinedQuatW[t3] +
                                    combinedQuatX[0]*combinedQuatX[t3] +
                                    combinedQuatY[0]*combinedQuatY[t3] +
                                    combinedQuatZ[0]*combinedQuatZ[t3])) *(180/np.pi))

        for t4 in range(0, len(xCalfRoll)):
            rebuildCombinedFix.append(rebuildCombined[t4]-rebuildCombined[500])

        fig, axs = plt.subplots()
        axs.set_title('Euler-Based Net Angle Changes for CALF')
        axs.plot(rebuildCombinedFix, color='violet')
        axs.set_xlim(500, 750)
        axs.set_ylim(-20, 20)
        axs.set(xlabel='Time (seconds)', ylabel='Total Angle Change (degrees)')
        axs.invert_yaxis()
        positions = (500, 550, 600, 650, 700, 750)
        labels = (14.42, 15.86, 17.30, 18.75, 20.19, 21.63)
        plt.xticks(positions, labels)
        fig.show()

class PlotFoot:
    # PURPOSE: Plot the total angle change about the axis of the foot.

    def __init__(self, xFootRoll = [], yFootRoll = [], xFootPitch = [],
                 yFootPitch = [], xFootYaw = [], yFootYaw = [],
                 xFootW = [], yFootW = [], xFootX = [], yFootX = [],
                 xFootY = [], yFootY = [], xFootZ = [], yFootZ = [],
                 changeFoot = []):
        self.xFootRoll = xFootRoll
        self.yFootRoll = yFootRoll
        self.xFootPitch = xFootPitch
        self.yFootPitch = yFootPitch
        self.xFootYaw = xFootYaw
        self.yFootYaw = yFootYaw
        
        self.xFootW = xFootW
        self.yFootW = yFootW
        self.xFootX = xFootX
        self.yFootX = yFootX
        self.xFootY = xFootY
        self.yFootY = yFootY
        self.xFootZ = xFootZ
        self.yFootZ = yFootZ

        self.changeFoot = changeFoot

    def euler_angle_foot(self, xFootRoll, yFootRoll, xFootPitch, yFootPitch, xFootYaw, yFootYaw):
        figFoot, axsFoot = plt.subplots(3, sharex = True, sharey = False)
        figFoot.suptitle('Euler Axis Rotations for FOOT')
        
        with open('angles_foot_roll2.csv', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            for row in plots:
                xFootRoll.append(float(row[0]))
                yFootRoll.append(float(row[1]))
        setRoll2Zero = []
        for t in range(0, len(xFootRoll)):
            setRoll2Zero.append(yFootRoll[t]-yFootRoll[500])
        axsFoot[0].plot(xFootRoll, setRoll2Zero, linewidth = 2, color='teal')
        axsFoot[0].set(xlabel='', ylabel='Roll')
        axsFoot[0].set_xlim(500, 750)
        axsFoot[0].set_ylim(20, -20)

        with open('angles_foot_pitch2.csv', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            for row in plots:
                xFootPitch.append(float(row[0]))
                yFootPitch.append(float(row[1]))
        setPitch2Zero = []
        for t in range(0, len(xFootPitch)):
            setPitch2Zero.append(yFootPitch[t]-yFootPitch[500])
        axsFoot[1].plot(xFootPitch, setPitch2Zero, linewidth = 2, color='magenta')
        axsFoot[1].set(xlabel='', ylabel='Pitch')
        axsFoot[1].set_xlim(500, 750)
        axsFoot[1].set_ylim(50, -50)

        with open('angles_foot_yaw2.csv', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            for row in plots:
                xFootYaw.append(float(row[0]))
                yFootYaw.append(float(row[1]))
        setYaw2Zero = []
        for t in range(0, len(xFootYaw)):
            setYaw2Zero.append(yFootYaw[t]-yFootYaw[500])
        axsFoot[2].plot(xFootYaw, setYaw2Zero, linewidth = 2, color='black')
        axsFoot[2].set(xlabel='', ylabel='Yaw')
        axsFoot[2].set_xlim(500, 750)
        axsFoot[2].set_ylim(20, -20)

        # Optional!
        # figFoot.show()

    def quaternion_foot(self, xFootW, yFootW, xFootX, yFootX, xFootY,
                         yFootY, xFootZ, yFootZ):
        figQuats, axsQuats = plt.subplots(4, sharex = True, sharey = False)
        figQuats.suptitle('Quaternion Axis Rotations for FOOT')

        with open('angles_foot_W2.csv', 'r') as csvfile:
            plots= csv.reader(csvfile, delimiter=',')
            for row in plots:
                xFootW.append(float(row[0]))
                yFootW.append(float(row[1]))
        axsQuats[0].plot(xFootW, yFootW, color='blue')
        axsQuats[0].set(xlabel='', ylabel='W')
        axsQuats[0].set_xlim(500, 750)

        with open('angles_foot_X2.csv', 'r') as csvfile:
            plots= csv.reader(csvfile, delimiter=',')
            for row in plots:
                xFootX.append(float(row[0]))
                yFootX.append(float(row[1]))
        axsQuats[1].plot(xFootX, yFootX, color='red')
        axsQuats[1].set(xlabel='', ylabel='X')
        axsQuats[1].set_xlim(500, 750)

        with open('angles_foot_Y2.csv', 'r') as csvfile:
            plots= csv.reader(csvfile, delimiter=',')
            for row in plots:
                xFootY.append(float(row[0]))
                yFootY.append(float(row[1]))
        axsQuats[2].plot(xFootY, yFootY, color='green')
        axsQuats[2].set(xlabel='', ylabel='Y')
        axsQuats[2].set_xlim(500, 750)

        with open('angles_foot_Z2.csv', 'r') as csvfile:
            plots= csv.reader(csvfile, delimiter=',')
            for row in plots:
                xFootZ.append(float(row[0]))
                yFootZ.append(float(row[1]))
        axsQuats[3].plot(xFootZ, yFootZ, color='orange')
        axsQuats[3].set(xlabel='Time (count)', ylabel='Z')
        axsQuats[3].set_xlim(500, 750)

        # Optional!
        # figQuats.show()

    def dot_product_foot(self, xFootW, yFootW, xFootX, yFootX, xFootY,
                         yFootY, xFootZ, yFootZ, changeFoot):
        oneRad2Degrees = 57.296
        changeFootFix = []
        for t1 in range(0, len(xFootW)):    
            changeFoot.append(np.arccos(np.minimum(1, yFootW[0]*yFootW[t1] +
                                           yFootX[0]*yFootX[t1] +
                                           yFootY[0]*yFootY[t1] +
                                           yFootZ[0]*yFootZ[t1]))*(180/np.pi)-(oneRad2Degrees/2))

        for t2 in range(0, len(xFootW)):
            changeFootFix.append(changeFoot[t2]-changeFoot[500])

        fig, axs = plt.subplots()
        axs.set_title('Quaternion-Based Net Angle Changes for FOOT')
        axs.plot(changeFootFix, color='blue')
        axs.set_xlim(500, 750)
        axs.set_ylim(-20, 20)
        axs.set(xlabel='Time (seconds)', ylabel='Total Angle Change (degrees)')
        axs.invert_yaxis()
        positions = (500, 550, 600, 650, 700, 750)
        labels = (14.42, 15.86, 17.30, 18.75, 20.19, 21.63)
        plt.xticks(positions, labels)
        fig.show()

    def euler_combo_foot(self, xFootRoll, yFootRoll, yFootPitch, yFootYaw,
                          yFootY, yFootZ):
        theta_array = []
        R = []

        combinedEulerX = []
        combinedEulerY = []
        combinedEulerZ = []

        combinedNetAngle = []
        undoCombinedCos = []
        undoCombinedSin = []

        combinedQuatW = []
        combinedQuatX = []
        combinedQuatY = []
        combinedQuatZ = []

        rebuildCombined = []
        rebuildCombinedFix = []

        for t3 in range(0, len(xFootRoll)):
            theta = [yFootRoll[t3] * (np.pi/180), yFootPitch[t3]* (np.pi/180), yFootYaw[t3]* (np.pi/180)]
            theta_array.append(theta)

            R_x = np.array([[1,         0,                  0                   ],
                            [0,         math.cos(theta[0]), -math.sin(theta[0]) ],
                            [0,         math.sin(theta[0]), math.cos(theta[0])  ]
                            ])
                
                
                            
            R_y = np.array([[math.cos(theta[1]),    0,      math.sin(theta[1])  ],
                            [0,                     1,      0                   ],
                            [-math.sin(theta[1]),   0,      math.cos(theta[1])  ]
                            ])
                        
            R_z = np.array([[math.cos(theta[2]),    -math.sin(theta[2]),    0],
                            [math.sin(theta[2]),    math.cos(theta[2]),     0],
                            [0,                     0,                      1]
                            ])

            R.append(np.dot(R_x, np.dot(R_y, R_z)))

            combinedEulerX.append(math.atan2(R[t3][2,1], R[t3][2,2]))
            combinedEulerY.append(math.asin(R[t3][0,2]))
            combinedEulerZ.append(math.atan2(R[t3][1,0], R[t3][0,0]))

            combinedNetAngle.append(combinedEulerY[t3] * (180/np.pi))
            undoCombinedCos.append(np.cos(combinedNetAngle[t3] * (np.pi/360)))
            undoCombinedSin.append(np.sin(combinedNetAngle[t3] * (np.pi/360)))

            combinedQuatW.append(undoCombinedCos[t3])
            combinedQuatX.append(undoCombinedSin[t3] * np.sin(0.5*np.pi) * np.cos(np.pi))
            combinedQuatY.append(0.01 * (yFootY[t3] / 2) * np.cos(yFootY[t3]/(undoCombinedSin[t3])))
            combinedQuatZ.append(0.01 * (yFootZ[t3] / 2) * np.cos(yFootZ[t3]/(undoCombinedSin[t3])))

            rebuildCombined.append(np.arccos(np.minimum(1,
                                    combinedQuatW[0]*combinedQuatW[t3] +
                                    combinedQuatX[0]*combinedQuatX[t3] +
                                    combinedQuatY[0]*combinedQuatY[t3] +
                                    combinedQuatZ[0]*combinedQuatZ[t3])) *(180/np.pi))

        for t4 in range(0, len(xFootRoll)):
            rebuildCombinedFix.append(rebuildCombined[t4]-rebuildCombined[500])

        fig, axs = plt.subplots()
        axs.set_title('Euler-Based Net Angle Changes for FOOT')
        axs.plot(rebuildCombinedFix, color='violet')
        axs.set_xlim(500, 750)
        axs.set_ylim(-20, 20)
        axs.set(xlabel='Time (seconds)', ylabel='Total Angle Change (degrees)')
        axs.invert_yaxis()
        positions = (500, 550, 600, 650, 700, 750)
        labels = (14.42, 15.86, 17.30, 18.75, 20.19, 21.63)
        plt.xticks(positions, labels)
        fig.show()

class PlotLegRaising:
    # PURPOSE: Plot the total angle change for when a person is sitting and
    # raising a leg by up to 90 degrees.

    def __init__(self, xLegW = [], yLegW = [], xLegX = [], yLegX = [],
                 xLegY = [], yLegY = [], xLegZ = [], yLegZ = [],
                 changeLeg = [], pointsMinMax = []):
        self.xLegW = xLegW
        self.yLegW = yLegW
        self.xLegX = xLegX
        self.yLegX = yLegX
        self.xLegY = xLegY
        self.yLegY = yLegY
        self.xLegZ = xLegZ
        self.yLegZ = yLegZ

        self.changeLeg = changeLeg
        self.pointsMinMax = pointsMinMax

    def leg_quat_analysis(self, xLegW, yLegW, xLegX, yLegX, xLegY,
                           yLegY, xLegZ, yLegZ):
        figLeg, axsLeg = plt.subplots(4, sharex = True, sharey = False)
        figLeg.suptitle('Sitting/Leg Raising Quaternions')

        with open('test_quat_wholeleg_w.csv', 'r') as csvfile:
            plots= csv.reader(csvfile, delimiter=',')
            for row in plots:
                xLegW.append(float(row[0]))
                yLegW.append(float(row[1]))
        axsLeg[0].plot(xLegW,yLegW,linewidth=2, color='teal')
        axsLeg[0].set(xlabel='', ylabel="Quat'n (W)")
        axsLeg[0].set_xlim(50, 100)

        with open('test_quat_wholeleg_x.csv', 'r') as csvfile:
            plots= csv.reader(csvfile, delimiter=',')
            for row in plots:
                xLegX.append(float(row[0]))
                yLegX.append(float(row[1]))
        axsLeg[1].plot(xLegX,yLegX,linewidth=2, color='red')
        axsLeg[1].set(xlabel='', ylabel="Quat'n (X)")
        axsLeg[1].set_xlim(50, 100)

        with open('test_quat_wholeleg_y.csv', 'r') as csvfile:
            plots= csv.reader(csvfile, delimiter=',')
            for row in plots:
                xLegY.append(float(row[0]))
                yLegY.append(float(row[1]))
        axsLeg[2].plot(xLegY,yLegY,linewidth=2, color='green')
        axsLeg[2].set(xlabel='', ylabel="Quat'n (Y)")
        axsLeg[2].set_xlim(50, 100)

        with open('test_quat_wholeleg_z.csv', 'r') as csvfile:
            plots= csv.reader(csvfile, delimiter=',')
            for row in plots:
                xLegZ.append(float(row[0]))
                yLegZ.append(float(row[1]))
        axsLeg[3].plot(xLegZ,yLegZ,linewidth=2, color='orange')
        axsLeg[3].set(xlabel='Time (Count)', ylabel="Quat'n (Z)")
        axsLeg[3].set_xlim(50, 100)
        # Display the matplotlab figure showing quaternion behaviors in the
        # raising leg (optional).
        # figLeg.show()

    def leg_net_angles(self, xLegW, yLegW, xLegX, yLegX, xLegY,
                           yLegY, xLegZ, yLegZ, changeLeg, pointsMinMax):
        # Append changeLeg with the total angle change, which equates to
        # the inverse cosine of the dot product for each quaternion at the
        # initial and final time points, all multiplied by 360 degrees over
        # pi (for converting from radians to degrees).
        for t1 in range(0, len(xLegW)):
            changeLeg.append(np.arccos(np.minimum(1, yLegW[0] * yLegW[t1] +
                          yLegX[0] * yLegX[t1] +
                          yLegY[0] * yLegY[t1] +
                          yLegZ[0] * yLegZ[t1]))*(360/np.pi))

        # Plot the total angle change for the raising leg based on the
        # quaternions using the changeLeg array. Limit the x-axis to
        # 50-100, and invert and limit the y-axis to 90-0.
        figAngleLeg, axsAngleLeg = plt.subplots()
        axsAngleLeg.set_title('Sitting/Leg-Raising')
        axsAngleLeg.set_ylabel("Total Angle Change (Degrees)")
        axsAngleLeg.set_xlabel('Time (Count)')
        axsAngleLeg.plot(changeLeg, color='blue')
        axsAngleLeg.set_xlim(50, 100)
        axsAngleLeg.set_ylim(90, 0)

        # Narrow down the time interval to 50-100, and append pointMinMax with
        # the y-values occuring within that interval.
        for t2 in range(50, 101):
            pointsMinMax.append(changeLeg[t2])

        # Determine the highest and lowest values of pointMinMax, and find their
        # locations within the x-axis.
        xmax = pointsMinMax.index(max(pointsMinMax))+50
        ymax = max(pointsMinMax)
        xmin = pointsMinMax.index(min(pointsMinMax))+50
        ymin = min(pointsMinMax)

        # Annotate the highest point in the plot within the selected interval.
        text1= "Max Angle: {:.3f}° \nTime: {:.3f}".format(ymax, xmax)
        bbox_props1 = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
        arrowprops1=dict(arrowstyle="->", lw=1.5)
        kw1 = dict(xycoords='data',textcoords="axes fraction",
                  arrowprops=arrowprops1, bbox=bbox_props1, ha="left", va="top")
        axsAngleLeg.annotate(text1, xytext=(0.4, 0.0925), xy=(xmax, ymax), **kw1)

        # Annotate the lowest point in the plot within the selected interval.
        text2= "Min Angle: {:.3f}° \nTime: {:.3f}".format(ymin, xmin)
        bbox_props2 = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
        arrowprops2=dict(arrowstyle="->", lw=1.5)
        kw2 = dict(xycoords='data',textcoords="axes fraction",
                  arrowprops=arrowprops2, bbox=bbox_props2, ha="left", va="bottom")
        axsAngleLeg.annotate(text2, xytext=(0.18, 0.85), xy=(xmin, ymin), **kw2)

        # Display the matplotlab figure showing the total angle change in the
        # raising leg.
        figAngleLeg.show()
        
