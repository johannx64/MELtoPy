import maya.cmds as cmds

# This is a paid script pack and is not free to use.
m341_unWrapperVersion = "unWrapper v2.5"


# Help function
def helpmaUnwrapper():
    m341_unWrapper_HelpWindow = "m341_unWrapper_HelpWindow"

    if cmds.window(m341_unWrapper_HelpWindow, exists=True):
        cmds.deleteUI(m341_unWrapper_HelpWindow)

    m341_unWrapperVersion = "Your_Tool_Version"
    m341_unWrapper_HelpWindow = cmds.window(title=("Help " + m341_unWrapperVersion), leftEdge=900, topEdge=115, toolbox=True,
                                            sizeable=False, resizeToFitChildren=False, widthHeight=(800, 800))
    cmds.scrollLayout()
    cmds.rowColumnLayout(numberOfColumns=1)

    # Loading the toolbox without the UV editor
    cmds.text(align="left", wordWrap=True, width=780, hl=True, font="boldLabelFont", label="LOADING THE TOOLBOX WITHOUT THE UV EDITOR")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
                label="-If you'd like to load the toolbox without attaching it to the UV editor, right click the unwrap shelf button and choose Load without UV editor.\n\n")

    # RESET
    cmds.text(align="left", wordWrap=True, width=780, hl=True, font="boldLabelFont", label="RESET")
    cmds.text(align="left", wordWrap=True, width=780, hl=True, label="-Resets the toolbox back to default settings.\n\n")

    # CHECKER MAP
    cmds.text(align="left", wordWrap=True, width=780, hl=True, font="boldLabelFont", label="CHECKER MAP")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
                label="-Toggles the checker map on/off, press the plus or minus buttons to increase or decrease the checker map size.\n\n")

    # PLANAR MAP CAMERA
    cmds.text(align="left", wordWrap=True, width=780, hl=True, font="boldLabelFont", label="PLANAR MAP CAMERA")
    cmds.text(align="left", wordWrap=True, width=780, hl=True, label="-Applies a camera-based planar projection.\n\n")

    # UVS BY ANGLE CHECKBOX
    cmds.text(align="left", wordWrap=True, width=780, hl=True, font="boldLabelFont", label="UVS BY ANGLE CHECKBOX")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
                label="-Turn on if you want the easy UVs button to create angle-based UV mapping.\n")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
                label="-Type a number into the input field to define what angle the UV shells will be cut at; a good value to start with is 30, then adjust from there to increase or decrease the number of shells created.\n")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
                label="-The min value is 0, and the max value is 180. 0 makes a shell for every polygon, and 180 makes a single shell for the whole mesh.\n\n")

    # UVS BY HARD EDGES CHECKBOX
    cmds.text(align="left", wordWrap=True, width=780, hl=True, font="boldLabelFont", label="UVS BY HARD EDGES CHECKBOX")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
                label="-Turn on if you want the easy UVs button to cut UV shells where it finds hard edges.\n\n")

    # AUTO CUT SEAMS CHECKBOX
    cmds.text(align="left", wordWrap=True, width=780, hl=True, font="boldLabelFont", label="AUTO CUT SEAMS CHECKBOX")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
                label="-Turn on if you want the easy UVs button to automatically create UV seams for you so cylindrical and spherical shapes can be unwrapped automatically.\n\n")
    cmds.showWindow(m341_unWrapper_HelpWindow)

    # KEEP NORMALS CHECKBOX
    cmds.text(align="left", wordWrap=True, width=780, hl=True, font="boldLabelFont", label="KEEP NORMALS CHECKBOX")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
            label="-Turn on if you want the easy UVs button to keep your current mesh normals instead of replacing them with the value from the UVs by angle input field.\n\n")

    # KEEP CURRENT SEAMS CHECKBOX
    cmds.text(align="left", wordWrap=True, width=780, hl=True, font="boldLabelFont", label="KEEP CURRENT SEAMS CHECKBOX")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
            label="-Turn on if you want the easy UVs button to keep your existing UV cut edges.\n\n")

    # EASY UVS
    cmds.text(align="left", wordWrap=True, width=780, hl=True, font="boldLabelFont", label="EASY UVS")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
            label="-Automatically creates UVs for your mesh, use the checkboxes above the easy UVs button to configure how you'd like the easy UVs to be created, different checkbox combinations will create different results. By default, the mesh normals are set to an angle of 30 and UV shells are created using that same angle with automatic seams for cylindrical shapes.\n\n")

    # SPIN, SPIN
    cmds.text(align="left", wordWrap=True, width=780, hl=True, font="boldLabelFont", label="SPIN, SPIN")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
            label="-Rotates selected UVs left or right 90 degrees. The left spin button rotates left, and the right spin button rotates right.\n\n")

    # HIDE EDGES
    cmds.text(align="left", wordWrap=True, width=780, hl=True, font="boldLabelFont", label="HIDE EDGES")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
            label="-Toggles visibility of polygon edges when an object is selected.\n\n")

    # SOFT
    cmds.text(align="left", wordWrap=True, width=780, hl=True, font="boldLabelFont", label="SOFT")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
            label="-Softens normals on selected components or mesh.\n\n")

    # HARD
    cmds.text(align="left", wordWrap=True, width=780, hl=True, font="boldLabelFont", label="HARD")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
            label="-Hardens normals on selected components or mesh.\n\n")

    # HRD BORDER
    cmds.text(align="left", wordWrap=True, width=780, hl=True, font="boldLabelFont", label="HRD BORDER")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
            label="-Hardens normals on all UV border edges.\n\n")

    # UNFOLD UV
    cmds.text(align="left", wordWrap=True, width=780, hl=True, font="boldLabelFont", label="UNFOLD UV")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
            label="-Unfolds selected UVs.\n\n")

    # STRAIGHTEN UV
    cmds.text(align="left", wordWrap=True, width=780, hl=True, font="boldLabelFont", label="STRAIGHTEN UV")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
            label="-Straightens selected UVs.\n\n")

    # STRAIGHTEN SHELL
    cmds.text(align="left", wordWrap=True, width=780, hl=True, font="boldLabelFont", label="STRAIGHTEN SHELL")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
            label="-Straightens the current UV shell based on the edge loop you select first. A tolerance of 30 is used for the straighten.\n\n")

    # CREATE SHELL
    cmds.text(align="left", wordWrap=True, width=780, hl=True, font="boldLabelFont", label="CREATE SHELL")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
            label="-Converts selected components into a new UV shell, for best results select faces first.\n\n")

    # ORIENT
    cmds.text(align="left", wordWrap=True, width=780, hl=True, font="boldLabelFont", label="ORIENT")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
            label="-Orients the current UV shell to a right angle based on a single selected edge or two selected UVs on the same shell.\n\n")

    # 3D CUT AND SEW
    cmds.text(align="left", wordWrap=True, width=780, hl=True, font="boldLabelFont", label="3D CUT AND SEW")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
            label="-Enters the 3D cut and sew tool and enables the checker map. While the 3D cut and sew tool is active, the following hotkeys become available.\n")
    cmds.text(align="left", wordWrap=True, width=780, hl=True, label="-Double click an edge loop in the 3D viewport to cut those UV edges.\n")
    cmds.text(align="left", wordWrap=True, width=780, hl=True, label="-Hold Ctrl and double click an edge loop in the 3D viewport to sew those UV edges.\n")
    cmds.text(align="left", wordWrap=True, width=780, hl=True, label="-Select any number of edges and press x on the keyboard to cut those UV edges.\n")
    cmds.text(align="left", wordWrap=True, width=780, hl=True, label="-Hold Ctrl and single click any edge to sew that UV edge.\n")
    cmds.text(align="left", wordWrap=True, width=780, hl=True, label="-Drag select edges to cut those UV edges.\n")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
            label="-Hold Ctrl and drag select edges to sew those UV edges.\n\n")

    # EXIT
    cmds.text(align="left", wordWrap=True, width=780, hl=True, font="boldLabelFont", label="EXIT")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
            label="-Exits the 3D cut and sew tool; clicking the exit button will also exit any component mode and take you back to object mode.\n\n")

    # UNFOLD CHECKBOX
    cmds.text(align="left", wordWrap=True, width=780, hl=True, font="boldLabelFont", label="UNFOLD CHECKBOX")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
            label="-Turn on if you want the unwrap button and easy UVs button to unfold UVs during UV layout.\n\n")

    # CURVED CHECKBOX
    cmds.text(align="left", wordWrap=True, width=780, hl=True, font="boldLabelFont", label="CURVED CHECKBOX")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
            label="-Turn on if you want the unfold checkbox to use the curved method during UV layout. If the unfold checkbox is turned off the curved checkbox has no effect.\n\n")

    # SPIN CHECKBOX
    cmds.text(align="left", wordWrap=True, width=780, hl=True, font="boldLabelFont", label="SPIN CHECKBOX")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
            label="-Turn on if you want the unwrap button and easy UVs button to rotate UV shells for the best fit during UV layout.\n\n")

    # SCALE CHECKBOX
    cmds.text(align="left", wordWrap=True, width=780, hl=True, font="boldLabelFont", label="SCALE CHECKBOX")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
            label="-Turn on if you want the unwrap button and easy UVs button to scale UV shells to the correct 3D ratios in the 0-1 UV space.\n\n")

    # ALL CHECKBOX
    cmds.text(align="left", wordWrap=True, width=780, hl=True, font="boldLabelFont", label="ALL CHECKBOX")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
            label="-Turn on if you want the unwrap button to layout all UVs on the current mesh. Turn off if you want the unwrap button to layout selected UVs.\n")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
            label="-If the 3D cut and sew tool is active, the unwrap button will always layout all UVs even if the checkbox is turned off. This prevents the unwrap process from failing when using the 3D cut and sew tool because that tool doesn't let you select UVs or shells when it's active.\n\n")

    # MAP SIZE
    cmds.text(align="left", wordWrap=True, width=780, hl=True, font="boldLabelFont", label="MAP SIZE")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
            label="-The map size drop-down allows you to control how padding works relative to what the final texture size is you're going to apply to the model. Set map size to the final resolution you plan to use on your model.\n\n")

    # PADDING
    cmds.text(align="left", wordWrap=True, width=780, hl=True, font="boldLabelFont", label="PADDING")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
            label="-Padding controls the amount of space between each UV shell and is relative to what you set the map size to. UV tile boundary spacing will automatically be half of whatever you set padding to.\n\n")

    # UNWRAP
    cmds.text(align="left", wordWrap=True, width=780, hl=True, font="boldLabelFont", label="UNWRAP")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
            label="-Performs layout UVs with the checkbox features you've configured above.\n")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
            label="-By default, shells are unfolded, rotated, and scaled so you can click unwrap after every edit you make using 3D cut and sew to see an update and visualize your unwrap as you work.\n")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
            label="-After pressing the unwrap button once you can then press the g key on the keyboard to unwrap the mesh again and again each time you make a new edit using the 3D cut and sew tool. Using the g key workflow can save a lot of time.\n")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
            label="-To fine-tune your unwrap turn off the unfold, spin, and scale checkboxes to make custom edits to your UV shells without losing those edits next time you press the unwrap button.\n\n")

    # YOUTUBE VIDEOS HERE
    cmds.text(align="left", wordWrap=True, width=780, hl=True, font="boldLabelFont", label="YOUTUBE VIDEOS HERE")
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
            label='<a href="https://youtu.be/6tYpY3kVLn8?list=PLAUgGUDpaMENfz8Nd7Zw-LxDK_v5ZflY6" style="color:rgb(187,187,187);">https://youtu.be/6tYpY3kVLn8?list=PLAUgGUDpaMENfz8Nd7Zw-LxDK_v5ZflY6</a><br>')
    cmds.text(align="left", wordWrap=True, width=780, hl=True,
            label='<a href="https://youtu.be/XsJ_2ClVzIw?list=PLAUgGUDpaMENfz8Nd7Zw-LxDK_v5ZflY6" style="color:rgb(187,187,187);">https://youtu.be/XsJ_2ClVzIw?list=PLAUgGUDpaMENfz8Nd7Zw-LxDK_v5ZflY6</a><br><br>')

    # Show the help window
    cmds.showWindow("$m341_unWrapper_HelpWindow")



# Window and Buttons
def m341_launch_UnwrapperInterface():
    global m341_unWrapperVersion

    # Switch to load with texture editor or not
    textureEditor = 1

    if textureEditor == 1:
        # Yes texture editor
        cmds.TextureViewWindow()
        cmds.window(title=m341_unWrapperVersion, parent="polyTexturePlacementPanel1Window", toolbox=True, sizeable=True, resizeToFitChildren=True)
    else:
        # No texture editor
        cmds.window(title=m341_unWrapperVersion, toolbox=True, sizeable=True, resizeToFitChildren=True)

    cmds.columnLayout(adjustableColumn=True)
    cmds.text(label="by johann9616")

    cmds.setParent("..")
    cmds.rowColumnLayout(numberOfRows=1)

    cmds.iconTextButton(style="textOnly", labelOffset=30, label="click for help", backgroundColor=(0.51, 0.51, 0.51), width=83, height=15, command="helpmaUnwrapper;")
    cmds.separator(width=1, style="none")

    cmds.iconTextButton(style="textOnly", labelOffset=30, label="reset", backgroundColor=(0.51, 0.51, 0.51), width=40, height=15, command="m341_unWrapper_Reset;")

    cmds.setParent("..")
    cmds.rowColumnLayout(numberOfRows=1)

    cmds.iconTextButton(style="textOnly", label="checker map", backgroundColor=(0.427, 0.643, 0.643), width=76, command="button1unWrapper;", commandRepeatable=0)
    cmds.separator(width=1, style="none")

    cmds.iconTextButton(style="textOnly", label="+", backgroundColor=(0.427, 0.643, 0.643), width=23, command="button2unWrapper;", commandRepeatable=0)
    cmds.separator(width=1, style="none")

    cmds.iconTextButton(style="textOnly", label="-", backgroundColor=(0.427, 0.643, 0.643), width=23, command="button3unWrapper;", commandRepeatable=0)

    cmds.setParent("..")
    cmds.rowColumnLayout(numberOfRows=1)

    cmds.iconTextButton(style="textOnly", label="planar map camera", labelOffset=30, backgroundColor=(0.32, 0.59, 0.72), width=124, command="m341_unWrapper_planarMapCamera;", commandRepeatable=1)

    cmds.setParent("..")
    cmds.rowColumnLayout(numberOfRows=1, height=18)

    # Save preferences UVs by angle checkbox
    unWrapper_uvsByAngle_CheckBoxValue = 1
    m341_unWrapper_uvsByAngle_UserInput = 0
    unWrapper_uvsByAngle_OptionVar = cmds.optionVar(exists="m341_unWrapper_uvsByAngleCheckBox_VarName")

    if not unWrapper_uvsByAngle_OptionVar:
        # Set default value
        cmds.optionVar(intValue=("m341_unWrapper_uvsByAngleCheckBox_VarName", 1))
        unWrapper_uvsByAngle_CheckBoxValue = cmds.optionVar(query="m341_unWrapper_uvsByAngleCheckBox_VarName")
    else:
        # Query from prefs file
        unWrapper_uvsByAngle_CheckBoxValue = cmds.optionVar(query="m341_unWrapper_uvsByAngleCheckBox_VarName")

    unWrapper_uvsByAngle_CheckBoxName = cmds.checkBox(label="", value=unWrapper_uvsByAngle_CheckBoxValue, changeCommand="m341_unWrapper_uvsByAngle_ValueChanged();")    
    cmds.text(label=" UVs by angle ")

    # Save preferences angle int field
    unWrapper_angle_intFieldValue = 30
    m341_unWrapper_angle_UserInput = 0
    unWrapper_angle_OptionVar = cmds.optionVar(exists="m341_unWrapper_angleIntField_VarName")

    if not unWrapper_angle_OptionVar:
        # Set default value
        cmds.optionVar(intValue=("m341_unWrapper_angleIntField_VarName", 30))
        unWrapper_angle_intFieldValue = cmds.optionVar(query="m341_unWrapper_angleIntField_VarName")
    else:
        # Query from prefs file
        unWrapper_angle_intFieldValue = cmds.optionVar(query="m341_unWrapper_angleIntField_VarName")

    unwrapper_angle_IntFieldName = cmds.intField(value=unWrapper_angle_intFieldValue, minValue=0, maxValue=180, width=30, height=17, changeCommand="m341_unWrapper_angle_ValueChanged();")

    cmds.setParent("..")
    cmds.rowColumnLayout(numberOfRows=1, height=17)

    # Save preferences UVs by hard edges checkbox
    unWrapper_uvsByHardEdges_CheckBoxValue = 0
    m341_unWrapper_uvsByHardEdges_userInput = 0
    unWrapper_uvsByHardEdges_OptionVar = cmds.optionVar(exists="m341_unWrapper_uvsByHardEdgesCheckBox_VarName")

    if not unWrapper_uvsByHardEdges_OptionVar:
        # Set default value
        cmds.optionVar(intValue=("m341_unWrapper_uvsByHardEdgesCheckBox_VarName", 0))
        unWrapper_uvsByHardEdges_CheckBoxValue = cmds.optionVar(query="m341_unWrapper_uvsByHardEdgesCheckBox_VarName")
    else:
        # Query from prefs file
        unWrapper_uvsByHardEdges_CheckBoxValue = cmds.optionVar(query="m341_unWrapper_uvsByHardEdgesCheckBox_VarName")

    unWrapper_uvsByHardEdges_CheckBoxName = cmds.checkBox(label="", value=unWrapper_uvsByHardEdges_CheckBoxValue, changeCommand="m341_unWrapper_uvsByHardEdges_ValueChanged();")
    cmds.text(label=" UVs by hard edges")

    cmds.setParent("..")
    cmds.rowColumnLayout(numberOfRows=1, height=17)

    # Save preferences auto cut seams checkbox
    unWrapper_autoCutSeams_CheckBoxValue = 1
    m341_unWrapper_autoCutSeams_userInput = 0
    unWrapper_autoCutSeams_OptionVar = cmds.optionVar(exists="m341_unWrapper_autoCutSeamsCheckBox_VarName")

    if not unWrapper_autoCutSeams_OptionVar:
        # Set default value
        cmds.optionVar(intValue=("m341_unWrapper_autoCutSeamsCheckBox_VarName", 1))
        unWrapper_autoCutSeams_CheckBoxValue = cmds.optionVar(query="m341_unWrapper_autoCutSeamsCheckBox_VarName")
    else:
        # Query from prefs file
        unWrapper_autoCutSeams_CheckBoxValue = cmds.optionVar(query="m341_unWrapper_autoCutSeamsCheckBox_VarName")

    unWrapper_autoCutSeams_CheckBoxName= cmds.checkBox(label="", value=unWrapper_autoCutSeams_CheckBoxValue, changeCommand="m341_unWrapper_autoCutSeams_ValueChanged();")
    cmds.text(label=" auto cut seams")

    cmds.setParent("..")
    cmds.rowColumnLayout(numberOfRows=1, height=17)

    # Save preferences keep normals checkbox
    unWrapper_keepNormals_CheckBoxValue = 0
    m341_unWrapper_keepNormals_userInput = 0
    unWrapper_keepNormals_OptionVar = cmds.optionVar(exists="m341_unWrapper_keepNormalsCheckBox_VarName")

    if not unWrapper_keepNormals_OptionVar:
        # Set default value
        cmds.optionVar(intValue=("m341_unWrapper_keepNormalsCheckBox_VarName", 0))
        unWrapper_keepNormals_CheckBoxValue = cmds.optionVar(query="m341_unWrapper_keepNormalsCheckBox_VarName")
    else:
        # Query from prefs file
        unWrapper_keepNormals_CheckBoxValue = cmds.optionVar(query="m341_unWrapper_keepNormalsCheckBox_VarName")

    unWrapper_keepNormals_CheckBoxName = cmds.checkBox(label="", value=unWrapper_keepNormals_CheckBoxValue, changeCommand="m341_unWrapper_keepNormals_ValueChanged();")
    cmds.text(label=" keep normals")

    cmds.setParent("..")
    cmds.rowColumnLayout(numberOfRows=1, height=17)

    # Save preferences keep current seams checkbox
    unWrapper_keepCurrentSeams_CheckBoxValue = 0
    m341_unWrapper_keepCurrentSeams_userInput = 0
    unWrapper_keepCurrentSeams_OptionVar = cmds.optionVar(exists="m341_unWrapper_keepCurrentSeamsCheckBox_VarName")

    if not unWrapper_keepCurrentSeams_OptionVar:
        # Set default value
        cmds.optionVar(intValue=("m341_unWrapper_keepCurrentSeamsCheckBox_VarName", 0))
        unWrapper_keepCurrentSeams_CheckBoxValue = cmds.optionVar(query="m341_unWrapper_keepCurrentSeamsCheckBox_VarName")
    else:
        # Query from prefs file
        unWrapper_keepCurrentSeams_CheckBoxValue = cmds.optionVar(query="m341_unWrapper_keepCurrentSeamsCheckBox_VarName")

    unWrapper_keepCurrentSeams_CheckBoxName = cmds.checkBox(label="", value=unWrapper_keepCurrentSeams_CheckBoxValue, changeCommand="m341_unWrapper_keepCurrentSeams_ValueChanged();")
    cmds.text(label=" keep current seams")

    cmds.setParent("..")
    cmds.rowColumnLayout(numberOfRows=1)

    # Easy UVs button
    cmds.iconTextButton(style="textOnly", label="easy UVs", labelOffset=0, backgroundColor=(0.59, 0.53, 0.74), width=124, command="m341_unWrapper_EasyUVs;", commandRepeatable=1)

    cmds.setParent("..")
    cmds.rowColumnLayout(numberOfRows=1)

    # 3D cut and sew button
    cmds.iconTextButton(style="textOnly", label="3d cut and sew", labelOffset=30, backgroundColor=(0.772, 0.521, 0.302), width=91, command="m341_unWrapper_3dCutAndSew;", commandRepeatable=0)
    cmds.separator(width=1, style="none")

    # Exit button
    cmds.iconTextButton(style="textOnly", label="exit", backgroundColor=(0.772, 0.521, 0.302), width=32, command="m341_unWrapper_Exit;", commandRepeatable=0)

    cmds.setParent("..")
    cmds.rowColumnLayout(numberOfRows=1, height=17)

    # Save preferences unfold checkbox
    unWrapper_unfold_CheckBoxValue = 1
    m341_unWrapper_unfold_userInput = 0
    unWrapper_unfold_OptionVar = cmds.optionVar(exists="m341_unWrapper_unfoldCheckBox_VarName")

    if not unWrapper_unfold_OptionVar:
        # Set default value
        cmds.optionVar(intValue=("m341_unWrapper_unfoldCheckBox_VarName", 1))
        unWrapper_unfold_CheckBoxValue = cmds.optionVar(query="m341_unWrapper_unfoldCheckBox_VarName")
    else:
        # Query from prefs file
        unWrapper_unfold_CheckBoxValue = cmds.optionVar(query="m341_unWrapper_unfoldCheckBox_VarName")

    unWrapper_unfold_CheckBoxName = cmds.checkBox(label="", value=unWrapper_unfold_CheckBoxValue, changeCommand="m341_unWrapper_unfold_ValueChanged();")
    cmds.text(label=" unfold   ")

    # Save preferences curved checkbox
    unWrapper_curved_CheckBoxValue = 1
    m341_unWrapper_curved_userInput = 0
    unWrapper_curved_OptionVar = cmds.optionVar(exists="m341_unWrapper_curvedCheckBox_VarName")

    if not unWrapper_curved_OptionVar:
        # Set default value
        cmds.optionVar(intValue=("m341_unWrapper_curvedCheckBox_VarName", 1))
        unWrapper_curved_CheckBoxValue = cmds.optionVar(query="m341_unWrapper_curvedCheckBox_VarName")
    else:
        # Query from prefs file
        unWrapper_curved_CheckBoxValue = cmds.optionVar(query="m341_unWrapper_curvedCheckBox_VarName")

    unWrapper_curved_CheckBoxName = cmds.checkBox(label="", value=unWrapper_curved_CheckBoxValue, changeCommand="m341_unWrapper_curved_ValueChanged();")
    cmds.text(label=" curved")

    cmds.setParent("..")
    cmds.rowColumnLayout(numberOfRows=1, height=17)

    # Save preferences spin checkbox
    unWrapper_spin_CheckBoxValue = 1
    m341_unWrapper_spin_userInput = 0
    unWrapper_spin_OptionVar = cmds.optionVar(exists="m341_unWrapper_spinCheckBox_VarName")

    if not unWrapper_spin_OptionVar:
        # Set default value
        cmds.optionVar(intValue=("m341_unWrapper_spinCheckBox_VarName", 1))
        unWrapper_spin_CheckBoxValue = cmds.optionVar(query="m341_unWrapper_spinCheckBox_VarName")
    else:
        # Query from prefs file
        unWrapper_spin_CheckBoxValue = cmds.optionVar(query="m341_unWrapper_spinCheckBox_VarName")

    unWrapper_spin_CheckBoxName = cmds.checkBox(label="", value=unWrapper_spin_CheckBoxValue, changeCommand="m341_unWrapper_spin_ValueChanged();")
    cmds.text(label=" spin  ")

    cmds.setParent("..")
    cmds.rowColumnLayout(numberOfRows=1, height=17)

    # Save preferences scale checkbox
    unWrapper_scale_CheckBoxValue = 1
    m341_unWrapper_scale_userInput = 0
    unWrapper_scale_OptionVar = cmds.optionVar(exists="m341_unWrapper_scaleCheckBox_VarName")

    if not unWrapper_scale_OptionVar:
        # Set default value
        cmds.optionVar(intValue=("m341_unWrapper_scaleCheckBox_VarName", 1))
        unWrapper_scale_CheckBoxValue = cmds.optionVar(query="m341_unWrapper_scaleCheckBox_VarName")
    else:
        # Query from prefs file
        unWrapper_scale_CheckBoxValue = cmds.optionVar(query="m341_unWrapper_scaleCheckBox_VarName")

    unWrapper_scale_CheckBoxName = cmds.checkBox(label="", value=unWrapper_scale_CheckBoxValue, changeCommand="m341_unWrapper_scale_ValueChanged();")
    cmds.text(label=" scale  ")

    # Save preferences all checkbox
    unWrapper_all_CheckBoxValue = 1
    m341_unWrapper_all_userInput = 0
    unWrapper_all_OptionVar = cmds.optionVar(exists="m341_unWrapper_allCheckBox_VarName")

    if not unWrapper_all_OptionVar:
        # Set default value
        cmds.optionVar(intValue=("m341_unWrapper_allCheckBox_VarName", 1))
        unWrapper_all_CheckBoxValue = cmds.optionVar(query="m341_unWrapper_allCheckBox_VarName")
    else:
        # Query from prefs file
        unWrapper_all_CheckBoxValue = cmds.optionVar(query="m341_unWrapper_allCheckBox_VarName")

    # Checkbox
    checkbox_value = cmds.checkBox(
        label="all", 
        value=unWrapper_all_CheckBoxValue, 
        changeCommand="m341_unWrapper_all_ValueChanged();"
    )

    cmds.setParent("..")
    cmds.rowLayout(numberOfColumns=2, columnAttach2=("left", "left"), columnOffset2=(5, 0), columnWidth=(1, 67), columnWidth2=(2, 30))
    # Map Size Option Menu
    map_size_option_menu = cmds.optionMenu(w=118, label="map size", height=17)
    for label in ["4096", "2048", "1024", "512", "256", "128", "64", "32"]:
        cmds.menuItem(label=label)

    cmds.optionMenu(map_size_option_menu, edit=True, select=2)

    cmds.setParent("..")
    cmds.rowLayout(numberOfColumns=2, columnAttach2=("left", "left"), columnOffset2=(5, 0), columnWidth=(1, 67), columnWidth2=(2, 30))
    # Padding Option Menu
    padding_option_menu = cmds.optionMenu(w=118, label="padding", height=17)
    for label in ["32 pix", "26 pix", "20 pix", "16 pix", "12 pix", "10 pix", "8 pix", "4 pix"]:
        cmds.menuItem(label=label)

    cmds.optionMenu(padding_option_menu, edit=True, select=7)

    # Unwrap Button
    cmds.setParent("..")

    cmds.rowLayout(numberOfColumns=1, columnAttach2=("left", "left"), columnOffset2=(5, 0), columnWidth=(1, 50), columnWidth2=(2, 30))

    cmds.iconTextButton(style="textOnly",
                        label="unwrap",
                        labelOffset=30,
                        backgroundColor=(0.72, 0.68, 0.39),
                        width=124,
                        command="m341_unWrapper_Unwrap;",
                        commandRepeatable=1)

    cmds.showWindow()

    
                       

# Launch Window
if cmds.window("unWrapper_windowName", exists=True):
    cmds.deleteUI("unWrapper_windowName")

loadedPlugInsUnwrapButtons = cmds.pluginInfo("Unfold3D.mll", query=True, loaded=True)

if loadedPlugInsUnwrapButtons == 1:
    m341_launch_UnwrapperInterface()
    print("Toolbox loaded " + m341_unWrapperVersion + "\n")
elif loadedPlugInsUnwrapButtons == 0:
    cmds.loadPlugin("Unfold3D.mll")
    cmds.pluginInfo("Unfold3D.mll", edit=True, autoload=True)
    m341_launch_UnwrapperInterface()
    print("Unfold3D.mll loaded, toolbox loaded " + m341_unWrapperVersion + "\n")
