import maya.cmds as cmds
import maya.mel as mel

# This is a paid script pack and is not free to use.
m341_unWrapperVersion = "unWrapper v0.1"

unWrapper_uvsByAngle_CheckBoxName = None

# Help function
def helpmaUnwrapper():
    m341_unWrapper_HelpWindow = "m341_unWrapper_HelpWindow"

    if cmds.window(m341_unWrapper_HelpWindow, exists=True):
        cmds.deleteUI(m341_unWrapper_HelpWindow)

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
    cmds.showWindow(m341_unWrapper_HelpWindow)

#*******************************************************************************************************
#Reset 
def m341_unWrapper_Reset():
    # UVs by angle
    cmds.checkBox("unWrapper_uvsByAngle_CheckBoxName", edit=True, value=1)
    m341_unWrapper_uvsByAngle_UserInput = cmds.checkBox("unWrapper_uvsByAngle_CheckBoxName", query=True, value=True)
    cmds.optionVar(intValue=["m341_unWrapper_uvsByAngleCheckBox_VarName", m341_unWrapper_uvsByAngle_UserInput])

    # Angle float field
    cmds.intField("unwrapper_angle_IntFieldName", edit=True, value=30)
    m341_unWrapper_angle_UserInput = cmds.intField("unwrapper_angle_IntFieldName", query=True, value=True)
    cmds.optionVar(intValue=["m341_unWrapper_angleIntField_VarName", m341_unWrapper_angle_UserInput])

    # UVs by hard edges
    cmds.checkBox("unWrapper_uvsByHardEdges_CheckBoxName", edit=True, value=0)
    m341_unWrapper_uvsByHardEdges_userInput = cmds.checkBox("unWrapper_uvsByHardEdges_CheckBoxName", query=True, value=True)
    cmds.optionVar(intValue=["m341_unWrapper_uvsByHardEdgesCheckBox_VarName", m341_unWrapper_uvsByHardEdges_userInput])

    # Auto cut seams
    cmds.checkBox("unWrapper_autoCutSeams_CheckBoxName", edit=True, value=1)
    m341_unWrapper_autoCutSeams_userInput = cmds.checkBox("unWrapper_autoCutSeams_CheckBoxName", query=True, value=True)
    cmds.optionVar(intValue=["m341_unWrapper_autoCutSeamsCheckBox_VarName", m341_unWrapper_autoCutSeams_userInput])

    # Keep normals
    cmds.checkBox("unWrapper_keepNormals_CheckBoxName", edit=True, value=0)
    m341_unWrapper_keepNormals_userInput = cmds.checkBox("unWrapper_keepNormals_CheckBoxName", query=True, value=True)
    cmds.optionVar(intValue=["m341_unWrapper_keepNormalsCheckBox_VarName", m341_unWrapper_keepNormals_userInput])

    # Keep current seams
    cmds.checkBox("unWrapper_keepCurrentSeams_CheckBoxName", edit=True, value=0)
    m341_unWrapper_keepCurrentSeams_userInput = cmds.checkBox("unWrapper_keepCurrentSeams_CheckBoxName", query=True, value=True)
    cmds.optionVar(intValue=["m341_unWrapper_keepCurrentSeamsCheckBox_VarName", m341_unWrapper_keepCurrentSeams_userInput])

    # Unfold
    cmds.checkBox("unWrapper_unfold_CheckBoxName", edit=True, value=1)
    m341_unWrapper_unfold_userInput = cmds.checkBox("unWrapper_unfold_CheckBoxName", query=True, value=True)
    cmds.optionVar(intValue=["m341_unWrapper_unfoldCheckBox_VarName", m341_unWrapper_unfold_userInput])

    # Curved
    cmds.checkBox("unWrapper_curved_CheckBoxName", edit=True, value=1)
    m341_unWrapper_curved_userInput = cmds.checkBox("unWrapper_curved_CheckBoxName", query=True, value=True)
    cmds.optionVar(intValue=["m341_unWrapper_curvedCheckBox_VarName", m341_unWrapper_curved_userInput])

    # Spin
    cmds.checkBox("unWrapper_spin_CheckBoxName", edit=True, value=1)
    m341_unWrapper_spin_userInput = cmds.checkBox("unWrapper_spin_CheckBoxName", query=True, value=True)
    cmds.optionVar(intValue=["m341_unWrapper_spinCheckBox_VarName", m341_unWrapper_spin_userInput])

    # Scale
    cmds.checkBox("unWrapper_scale_CheckBoxName", edit=True, value=1)
    m341_unWrapper_scale_userInput = cmds.checkBox("unWrapper_scale_CheckBoxName", query=True, value=True)
    cmds.optionVar(intValue=["m341_unWrapper_scaleCheckBox_VarName", m341_unWrapper_scale_userInput])

    # All
    cmds.checkBox("unWrapper_all_CheckBoxName", edit=True, value=1)
    m341_unWrapper_all_userInput = cmds.checkBox("unWrapper_all_CheckBoxName", query=True, value=True)
    cmds.optionVar(intValue=["m341_unWrapper_allCheckBox_VarName", m341_unWrapper_all_userInput])

    m341_unWrapperVersion = cmds.optionVar(q="m341_unWrapperVersion")
    print(str(m341_unWrapperVersion) + " reset to default")

#***********************************************************************************************************************************************************
#checker map toggle
def button1unWrapper():
    if cmds.textureWindow('polyTexturePlacementPanel1', query=True, parent=True) == "":
        print("Please open UV editor first")
    else:
        uvToggleChecker = cmds.optionVar(query='uvToggleChecker')
        maCurrentMayaYearUVFix = cmds.about(product=True)

    # Check if the current Maya version is "*202*"
    if "202" in cmds.about(product=True):
        # TURN ON CHECKERS 2020
        if cmds.getModifiers() % 2:
            mel.eval("performTextureViewCheckerMapOptions(1);")
        else:
            mel.eval("textureWindowDisplayCheckered(1, 1);")
            mel.eval("textureWindow -edit -checkerColorMode 0 polyTexturePlacementPanel1;")
            mel.eval("performTextureViewCheckerMapOptions(0);")
        mel.eval("txtWndUpdateEditor(\"polyTexturePlacementPanel1\", \"textureWindow\", \"null\", 101);")
        
        mel.eval("""
            textureWindow -edit
            -checkerColorMode 0
            -checkerColor1 0.8 0.8 0.8
            -checkerColor2 0 0 0
            -cgo 1
            -checkerGradient1 1 1 1
            -checkerGradient2 0 0 0
            -checkerDrawTileLabels 1
            polyTexturePlacementPanel1;
        """)

        # TURN ON SHADED 2020
        mel.eval("textureWindow -edit -solidMapPerShell 1 polyTexturePlacementPanel1;")
        mel.eval("DisplayUVShaded;")

        # DIM IMAGE 2020
        if cmds.getModifiers() % 2:
            mel.eval("performTextureViewDimImageOptions(1);")
        else:
            mel.eval("textureWindowImageDimming(1, 1);")
            mel.eval("performTextureViewDimImageOptions(0);")
        mel.eval("txtWndUpdateEditor(\"polyTexturePlacementPanel1\", \"textureWindow\", \"null\", 101);")
        
        mel.eval("uvTbImageDimmingChangedCallback();")
        
        mel.eval("textureWindow -edit -ibc 0.4 0.4 0.4 polyTexturePlacementPanel1;")

        # TURN ON IMAGE 2020
        maCheckIfImageOn2020 = mel.eval("textureWindow -q -imageDisplay polyTexturePlacementPanel1;;")
        if maCheckIfImageOn2020 == 0:
            mel.eval("ToggleUVTextureImage;")


        # Continue the code for turning off UV editor image options (if uvToggleChecker == 1) for "2020"
        elif uvToggleChecker == 1:
            # Turn off checker for 2020
            mel.eval('textureWindowDisplayCheckered(1, 0)')
            
            # Turn off shaded for 2020
            mel.eval("DisplayUVWireframe;")
            
            # Turn off dim image for 2020
            mel.eval('textureWindow -e -imageDim 0 polyTexturePlacementPanel1; performTextureViewDimImageOptions 0;')
            mel.eval('performTextureViewDimImageOptions(0)')
            
            if cmds.getModifiers() % 2:
                mel.eval('performTextureViewDimImageOptions(1)')
            else:
                mel.eval('textureWindowImageDimming(1, 0)')
            mel.eval("txtWndUpdateEditor(\"polyTexturePlacementPanel1\", \"textureWindow\", \"null\", 101);")

        uvToggleChecker = 1 if uvToggleChecker == 0 else 0
        cmds.optionVar(intValue=['uvToggleChecker', uvToggleChecker])
        print("UV checker map", "on" if uvToggleChecker == 1 else "off")

#***********************************************************************************************************************************************************
#checker density up
def button2unWrapper():
    texWinName = cmds.getPanel(sty='polyTexturePlacementPanel')
    checkerDensityUp = mel.eval(f'textureWindow -q -checkerDensity {texWinName[0]};')

    if checkerDensityUp > 2048:
        mel.eval(f'textureWindow -e -checkerDensity 2048 {texWinName[0]};')
        print("Checker map set to 2048")

    if checkerDensityUp <= 1024:
        mel.eval(f'textureWindow -e -checkerDensity 2048 {texWinName[0]};')
        print("Checker map set to 2048")

    if checkerDensityUp <= 512:
        mel.eval(f'textureWindow -e -checkerDensity 1024 {texWinName[0]};')
        print("Checker map set to 1024")

    if checkerDensityUp <= 256:
        mel.eval(f'textureWindow -e -checkerDensity 512 {texWinName[0]};')
        print("Checker map set to 512")

    if checkerDensityUp <= 128:
        mel.eval(f'textureWindow -e -checkerDensity 256 {texWinName[0]};')
        print("Checker map set to 256")

    if checkerDensityUp <= 64:
        mel.eval(f'textureWindow -e -checkerDensity 128 {texWinName[0]};')
        print("Checker map set to 128")

    if checkerDensityUp <= 32:
        mel.eval(f'textureWindow -e -checkerDensity 64 {texWinName[0]};')
        print("Checker map set to 64")

    if checkerDensityUp <= 16:
        mel.eval(f'textureWindow -e -checkerDensity 32 {texWinName[0]};')
        print("Checker map set to 32")

    if checkerDensityUp <= 8:
        mel.eval(f'textureWindow -e -checkerDensity 16 {texWinName[0]};')
        print("Checker map set to 16")

    if checkerDensityUp <= 4:
        mel.eval(f'textureWindow -e -checkerDensity 8 {texWinName[0]};')
        print("Checker map set to 8")

    if checkerDensityUp <= 2:
        mel.eval(f'textureWindow -e -checkerDensity 4 {texWinName[0]};')
        print("Checker map set to 4")

    if checkerDensityUp <= 1:
        mel.eval(f'textureWindow -e -checkerDensity 2 {texWinName[0]};')
        print("Checker map set to 2")


#***********************************************************************************************************************************************************
#checker density down
def button3unWrapper():
    texWinName = cmds.getPanel(sty='polyTexturePlacementPanel')
    checkerDensityDown = mel.eval(f'textureWindow -q -checkerDensity {texWinName[0]};')

    if checkerDensityDown > 2048:
        mel.eval(f'textureWindow -e -checkerDensity 2048 {texWinName[0]};')
        print("Checker map set to 2048")

    if checkerDensityDown <= 2048:
        mel.eval(f'textureWindow -e -checkerDensity 1024 {texWinName[0]};')
        print("Checker map set to 1024")

    if checkerDensityDown <= 1024:
        mel.eval(f'textureWindow -e -checkerDensity 512 {texWinName[0]};')
        print("Checker map set to 512")

    if checkerDensityDown <= 512:
        mel.eval(f'textureWindow -e -checkerDensity 256 {texWinName[0]};')
        print("Checker map set to 256")

    if checkerDensityDown <= 256:
        mel.eval(f'textureWindow -e -checkerDensity 128 {texWinName[0]};')
        print("Checker map set to 128")

    if checkerDensityDown <= 128:
        mel.eval(f'textureWindow -e -checkerDensity 64 {texWinName[0]};')
        print("Checker map set to 64")

    if checkerDensityDown <= 64:
        mel.eval(f'textureWindow -e -checkerDensity 32 {texWinName[0]};')
        print("Checker map set to 32")

    if checkerDensityDown <= 32:
        mel.eval(f'textureWindow -e -checkerDensity 16 {texWinName[0]};')
        print("Checker map set to 16")

    if checkerDensityDown <= 16:
        mel.eval(f'textureWindow -e -checkerDensity 8 {texWinName[0]};')
        print("Checker map set to 8")

    if checkerDensityDown <= 8:
        mel.eval(f'textureWindow -e -checkerDensity 4 {texWinName[0]};')
        print("Checker map set to 4")

    if checkerDensityDown <= 4:
        mel.eval(f'textureWindow -e -checkerDensity 2 {texWinName[0]};')
        print("Checker map set to 2")

    if checkerDensityDown <= 2:
        mel.eval(f'textureWindow -e -checkerDensity 1 {texWinName[0]};')
        print("Checker map set to 1")


#***********************************************************************************************************************************************************
#Planar map camera
def m341_unWrapper_planarMapCamera():
    # Exit 3D cut and sew
    currentActiveTool = cmds.currentCtx()
    if 'superCutUVContext' in currentActiveTool or 'PolyCutUVCtx' in currentActiveTool:
        m341_unWrapper_Exit()

    mel.eval('ConvertSelectionToFaces')
    cmds.polyProjection(ch=0, type='Planar', ibd=True, kir=True, md='c')
    mel.eval('toggleSelMode()')
    mel.eval('toggleSelMode()')    
    cmds.selectMode(object=True)
    mel.eval('DeleteHistory()')
    print("Planar map Camera applied, keep width/height ratio on")

#***********************************************************************************************************************************************************
#Easy UVs
def m341_unWrapper_EasyUVs():
    # Exit 3D cut and sew
    currentActiveTool = cmds.currentCtx()
    if mel.eval(f'gmatch {currentActiveTool} "*superCutUVContext*"'):
        m341_unWrapper_Exit()
    
    if mel.eval(f'gmatch {currentActiveTool} "*PolyCutUVCtx*"'):
        m341_unWrapper_Exit()

    m341_unWrapper_angle_ValueChanged()

    mel.eval('toggleSelMode;')
    mel.eval('toggleSelMode;')
    cmds.selectMode(object=True)
    easyUVsSelectedOBJ = cmds.ls(sl=True)
    easyUVsFinalSelect = cmds.ls(sl=True)

    # Clean up mesh
    # Clean up holes, lamina, zero edges, zero geo face area, invalid components
    mel.eval('polyCleanupArgList 4 { "0","1","0","0","0","0","1","0","1","1e-06","1","1e-05","0","1e-05","0","-1","1","1" };')
	#Clean up non-manifold geo only
    mel.eval('polyCleanupArgList 4 { "0","1","0","0","0","0","0","0","0","1e-05","0","1e-05","0","1e-05","0","1","0","0" };')

    easyUVsSelectedOBJ = cmds.ls(sl=True)

    # Auto cut seams
    autoCutSeams_UnWrapperCheckMarkValue = cmds.checkBox('unWrapper_autoCutSeams_CheckBoxName', query=True, value=True)

    # Keep user cuts
    m341_userCutEdges = []
    keepUserCuts_UnWrapperCheckMarkValue = cmds.checkBox('unWrapper_keepCurrentSeams_CheckBoxName', query=True, value=True)
    if keepUserCuts_UnWrapperCheckMarkValue == 1:
        # Store user cut edges
        mel.eval('ConvertSelectionToEdges();')
        mel.eval('SelectUVBorderComponents();')
        m341_userCutEdges = cmds.ls(sl=True)
        cmds.select(easyUVsSelectedOBJ)

    # UVs by angle
    m341_keepNormalsEdges = []
    uvsByAngle_UnWrapperCheckMarkValue = int(cmds.checkBox('unWrapper_uvsByAngle_CheckBoxName', query=True, value=True))
    keepNormals_UnWrapperCheckMarkValue = int(cmds.checkBox('unWrapper_keepNormals_CheckBoxName', query=True, value=True))
    
    if uvsByAngle_UnWrapperCheckMarkValue == 1:
        if keepNormals_UnWrapperCheckMarkValue == 1:
            # Select hard edges and store them
            cmds.select(easyUVsSelectedOBJ)
            mel.eval('polySelectConstraint -m 3 -t 0x8000 -sm 1;')
            m341_keepNormalsEdges = cmds.ls(sl=True)
            mel.eval('resetPolySelectConstraint;')
            cmds.select(easyUVsSelectedOBJ)

        # Soften all edges
        mel.eval('polySoftEdge -a 180 -ch 0;')

    # Automatic map
    mel.eval('ConvertSelectionToFaces;')
    mel.eval('polyAutoProjection -lm 0 -pb 0 -ibd 1 -cm 0 -l 2 -sc 1 -o 1 -p 6 -ps 0.2 -ws 0;')

    # UVs by angle
    if uvsByAngle_UnWrapperCheckMarkValue == 1:
        # Sew soft edges
        mel.eval('polySelectConstraint -m 3 -t 0x8000 -sm 2;')
        mel.eval('resetPolySelectConstraint;')
        mel.eval('polyMapSewMove -nf 10 -lps 0 -ch 0;')

    # UVs by hard edges
    uvsByHardEdges_UnWrapperCheckMarkValue = cmds.checkBox('unWrapper_uvsByHardEdges_CheckBoxName', query=True, value=True)
    if uvsByHardEdges_UnWrapperCheckMarkValue == 1:
        # Sew soft edges
        mel.eval('polySelectConstraint -m 3 -t 0x8000 -sm 2;')
        mel.eval('resetPolySelectConstraint;')
        mel.eval('polyMapSewMove -nf 10 -lps 0 -ch 0;')

    cmds.select(easyUVsSelectedOBJ)
    mel.eval('DeleteHistory;')

    # UVs by angle 2
    m341_unWrapper_angle_UserInput = cmds.intField("unwrapper_angle_IntFieldName", query=True, value=True)
    if uvsByAngle_UnWrapperCheckMarkValue == 1:
        
        # Soften UVs from user input
        cmds.polySoftEdge(easyUVsSelectedOBJ, a=m341_unWrapper_angle_UserInput, ch=0)
        #mel.eval(f'polySoftEdge -a {m341_unWrapper_angle_UserInput} -ch 0;')
        # Select hard edges and cut UVs on them
        mel.eval('polySelectConstraint -m 3 -t 0x8000 -sm 1;')
        mel.eval('resetPolySelectConstraint;')
        mel.eval('polyMapCut;')

        # Cut using auto seams for cylinder shapes
        if autoCutSeams_UnWrapperCheckMarkValue == 1:
            # Find cylinder angles so auto seam only cuts pipe shapes
            cmds.select(easyUVsSelectedOBJ)
            mel.eval('ConvertSelectionToEdges')
            mel.eval('polySelectConstraint -mode 2 -type 0x8000 -smoothness 0 -angle true -anglebound 10 54;')
            mel.eval('resetPolySelectConstraint;')
            mel.eval('u3dAutoSeam -s 0 -p 1;')

        # Bring back original normals
        if keepNormals_UnWrapperCheckMarkValue == 1:
            # Select original hard edges and make them hard again
            cmds.select(easyUVsSelectedOBJ)
            mel.eval('PolygonSoftenEdge')
            cmds.select(m341_keepNormalsEdges)
            mel.eval('PolygonHardenEdge')
            cmds.select(easyUVsSelectedOBJ)

    # UVs by hard edges
    if uvsByHardEdges_UnWrapperCheckMarkValue == 1:
        # Select hard edges and cut UVs on them
        mel.eval('polySelectConstraint -m 3 -t 0x8000 -sm 1;')
        mel.eval('resetPolySelectConstraint;')
        mel.eval('polyMapCut;')

        # Cut using auto seams for cylinder shapes
        if autoCutSeams_UnWrapperCheckMarkValue == 1:
            # Find cylinder angles so auto seam only cuts pipe shapes
            cmds.select(easyUVsSelectedOBJ)
            mel.eval('ConvertSelectionToEdges')
            cmds.polySelectConstraint(mode=2, type=0x8000, smoothness=0, angle=True, anglebound=[10, 54])
            mel.eval('resetPolySelectConstraint;')
            mel.eval('u3dAutoSeam -s 0 -p 1;')

    # Keep user cuts
    if keepUserCuts_UnWrapperCheckMarkValue == 1:
        # Cut user cut edges from above
        cmds.select(m341_userCutEdges)
        mel.eval('polyMapCut;')

    # Run unwrap button
    cmds.select(easyUVsSelectedOBJ)
    m341_unWrapper_Unwrap()

    cmds.select(easyUVsSelectedOBJ)
    mel.eval('toggleSelMode;')
    mel.eval('toggleSelMode;')
    cmds.selectMode(object=True)
    mel.eval('DeleteHistory')

    cmds.select(easyUVsFinalSelect)

    print("Easy UVs complete")

#***********************************************************************************************************************************************************
#Change component select modes
def componentMode2_Shells():
    mel.eval('changeSelectMode -component;')
    mel.eval('setComponentPickMask "Facet" true;')
    cmds.selectType(ocm=True, alc=False)
    cmds.selectType(msh=True)

def componentMode2_Faces():
    mel.eval('changeSelectMode -component;')
    mel.eval('setComponentPickMask "Facet" true;')
    cmds.selectType(ocm=True, alc=False)
    cmds.selectType(ocm=True, facet=True)
    cmds.selectType(sf=False, se=False, suv=False, cv=False)

def componentMode2_Verts():
    mel.eval('changeSelectMode -component;')
    mel.eval('setComponentPickMask "Point" true;')
    cmds.selectType(ocm=True, alc=False)
    cmds.selectType(ocm=True, vertex=True)
    cmds.selectType(sf=False, se=False, suv=False, cv=False)

def componentMode2_Edges():
    mel.eval('changeSelectMode -component;')
    cmds.selectType(isoparm=0, surfaceEdge=1, polymeshEdge=1, subdivMeshEdge=1, springComponent=1)
    cmds.selectType(ocm=True, alc=False)
    cmds.selectType(ocm=True, edge=True)
    cmds.selectType(sf=False, se=False, suv=False, cv=False)

def componentMode2_UVs():
    mel.eval('changeSelectMode -component;')
    cmds.selectType(ocm=True, alc=False)
    cmds.selectType(alc=False)
    cmds.selectType(puv=True)
    cmds.selectType(suv=True)

#***********************************************************************************************************************************************************
#3d cut and sew tool
def m341_unWrapper_3dCutAndSew():
    if not cmds.textureWindow(q=True, parent='polyTexturePlacementPanel1'):
        print("Please open UV editor first")
    else:
        mel.eval('toggleSelMode')
        mel.eval('toggleSelMode')
        cmds.selectMode(object=True)
        mel.eval('SetCutSewUVTool')
        ma_current_maya_year_uv_fix = cmds.about(product=True)

        if '202' in ma_current_maya_year_uv_fix:
            # TURN ON CHECKERS 2020
            if cmds.getModifiers() % 2:
                mel.eval('performTextureViewCheckerMapOptions 1;')
            else:
                mel.eval('textureWindowDisplayCheckered(1,1);')
                mel.eval('textureWindow -edit -checkerColorMode 0 polyTexturePlacementPanel1;')
                mel.eval('performTextureViewCheckerMapOptions 0;')
            mel.eval('txtWndUpdateEditor("polyTexturePlacementPanel1", "textureWindow", "null", 101);')
            cmds.textureWindow(edit=True, checkerColorMode=0, checkerColor1=[0.8, 0.8, 0.8], checkerColor2=[0, 0, 0],
                               cgo=1, checkerGradient1=[1, 1, 1], checkerGradient2=[0, 0, 0], checkerDrawTileLabels=1,
                               polyTexturePlacementPanel1=True)
            # TURN ON SHADED 2020
            mel.eval('textureWindow -edit -solidMapPerShell 1 polyTexturePlacementPanel1;')
            mel.eval('DisplayUVShaded')
            # DIM IMAGE 2020
            if cmds.getModifiers() % 2:
                mel.eval('performTextureViewDimImageOptions 1;')
            else:
                mel.eval('textureWindowImageDimming(1,1);')
                mel.eval('performTextureViewDimImageOptions 0;')
            mel.eval('txtWndUpdateEditor("polyTexturePlacementPanel1", "textureWindow", "null", 101);')
            mel.eval('uvTbImageDimmingChangedCallback;')
            mel.eval('textureWindow -edit -ibc 0.4 0.4 0.4 polyTexturePlacementPanel1;')
            # TURN ON IMAGE 2020
            ma_check_if_image_on_2020 = mel.eval('textureWindow -q -imageDisplay polyTexturePlacementPanel1;')
            if ma_check_if_image_on_2020 == 0:
                mel.eval('ToggleUVTextureImage;')

        mel.eval('global int $uvToggleChecker;')
        mel.eval('$uvToggleChecker = 1;')
        print("3D Cut and Sew Tool loaded, checker map on")

#***********************************************************************************************************************************************************
#Exit
def m341_unWrapper_Exit():
    if not cmds.textureWindow(q=True, parent='polyTexturePlacementPanel1'):
        print("Please open UV editor first")
    else:
        mel.eval('setHUD3DCutSewUVActiveMesh( 0, "");')
        mel.eval('MoveTool;')
        mel.eval('toggleSelMode')
        mel.eval('toggleSelMode')
        cmds.selectMode(object=True)
        mel.eval('DeleteHistory')

        uv_toggle_checker = cmds.getAttr("globalVariable.uvToggleChecker")
        if uv_toggle_checker == 1:
            ma_current_maya_year_uv_fix = cmds.about(product=True)
            if '202' in ma_current_maya_year_uv_fix:
                # TURN ON CHECKERS 2020
                if cmds.getModifiers() % 2:
                    mel.eval('performTextureViewCheckerMapOptions 1;')
                else:
                    mel.eval('textureWindowDisplayCheckered(1,1);')
                    mel.eval('textureWindow -edit -checkerColorMode 0 polyTexturePlacementPanel1;')
                    mel.eval('performTextureViewCheckerMapOptions 0;')
                mel.eval('txtWndUpdateEditor("polyTexturePlacementPanel1", "textureWindow", "null", 101);')
                mel.eval('textureWindow -edit -checkerColorMode 0  -checkerColor1 0.8 0.8 0.8  -checkerColor2 0 0 0  -cgo 1  -checkerGradient1 1 1 1  -checkerGradient2 0 0 0 -checkerDrawTileLabels 1 polyTexturePlacementPanel1;')
                # TURN ON SHADED 2020
                mel.eval('textureWindow -edit -solidMapPerShell 1 polyTexturePlacementPanel1;')
                mel.eval('DisplayUVShaded')
                # DIM IMAGE 2020
                if cmds.getModifiers() % 2:
                    mel.eval('performTextureViewDimImageOptions 1;')
                else:
                    mel.eval('textureWindowImageDimming(1,1);')
                    mel.eval('performTextureViewDimImageOptions 0;')
                mel.eval('txtWndUpdateEditor("polyTexturePlacementPanel1", "textureWindow", "null", 101);')
                mel.eval('uvTbImageDimmingChangedCallback;')
                mel.eval('textureWindow -edit -ibc 0.4 0.4 0.4 polyTexturePlacementPanel1;')
                # TURN ON IMAGE 2020
                ma_check_if_image_on_2020 = mel.eval('textureWindow -q -imageDisplay polyTexturePlacementPanel1;')
                if ma_check_if_image_on_2020 == 0:
                    mel.eval('ToggleUVTextureImage;')

            uv_toggle_checker = 1
            print("3D Cut and Sew Tool exited")
        elif uv_toggle_checker == 0:
            ma_current_maya_year_uv_fix2 = cmds.about(product=True)
            if '202' in ma_current_maya_year_uv_fix2:
                # TURN OFF CHECKER 2020
                mel.eval('textureWindowDisplayCheckered(1,0);')
                # TURN OFF SHADED 2020
                mel.eval('DisplayUVWireframe;')
                # TURN OFF DIM IMAGE 2020
                mel.eval('textureWindow -e -imageDim 0 polyTexturePlacementPanel1; performTextureViewDimImageOptions 0;')
                mel.eval('performTextureViewDimImageOptions 0;')
                cmds.textureWindow(edit=True, ibc=[0.5, 0.5, 0.5], polyTexturePlacementPanel1=True)
            print("3D Cut and Sew Tool exited")

#***********************************************************************************************************************************************************
#Unwrap
def m341_unWrapper_Unwrap():
    # Check boxes
    unfold_unWrapper_check_mark_value = int(cmds.checkBox('unWrapper_unfold_CheckBoxName', query=True, value=True))
    curved_unWrapper_check_mark_value = int(cmds.checkBox('unWrapper_curved_CheckBoxName', query=True, value=True))
    unWrapper_spin_check_box_value = int(cmds.checkBox('unWrapper_spin_CheckBoxName', query=True, value=True))
    unWrapper_scale_check_box_value = int(cmds.checkBox('unWrapper_scale_CheckBoxName', query=True, value=True))
    unWrapper_all_check_box_value = int(cmds.checkBox('unWrapper_all_CheckBoxName', query=True, value=True))


    # Spacing arrays
    unWrapperSpacerIndex = mel.eval('optionMenu -query -select unWrapperUVSpacer;')
    unWrapperBorderIndex = mel.eval('optionMenu -query -select unWrapperUVSpacer;')
    unWrapperMapSizeIndex = mel.eval('optionMenu -query -select unWrapperMapSize;')
    print("##################################")
    print(unWrapperMapSizeIndex)

    m341_unWrapperSpacingArray = []
    m341_unWrapperBorderArray = []

    # Exit 3D cut and sew to fix unwrap bug
    current_active_tool = cmds.currentCtx()
    m341_unWrapper_CutSewSwitch = 0

    if mel.eval(f'gmatch {current_active_tool} "*superCutUVContext*";'):
        mel.eval('setHUD3DCutSewUVActiveMesh( 0, "");')
        mel.eval('MoveTool;')
        mel.eval('toggleSelMode')
        mel.eval('toggleSelMode')
        cmds.selectMode(object=True)
        mel.eval('DeleteHistory')
        m341_unWrapper_CutSewSwitch = 1

    if mel.eval(f'gmatch {current_active_tool} "*PolyCutUVCtx*";'):
        mel.eval('setHUD3DCutSewUVActiveMesh( 0, "");')
        mel.eval('MoveTool;')
        mel.eval('toggleSelMode')
        mel.eval('toggleSelMode')
        cmds.selectMode(object=True)
        mel.eval('DeleteHistory')
        m341_unWrapper_CutSewSwitch = 1

    # If transform selected, convert to UVs first
    xform_selected = cmds.ls(sl=True, exactType='transform') or []
    size_xform_selected = len(xform_selected)

    if size_xform_selected > 0:
        mel.eval('ConvertSelectionToUVs;')
        mel.eval('SelectUVMask;')

    # Query component mode
    component_face = cmds.selectType(q=True, facet=True)
    component_shell = cmds.selectType(q=True, meshUVShell=True)
    component_vert = cmds.selectType(q=True, vertex=True)
    component_edge = cmds.selectType(q=True, edge=True)
    component_uv = cmds.selectType(q=True, polymeshUV=True)
    component_multi = cmds.selectType(q=True, meshComponents=True)

    # Store user selected components
    components = cmds.ls(sl=True) or []

    # Update shell spacing values based on the chosen map size in UI
    unWrapperMapSizeIndex = mel.eval('optionMenu -query -select unWrapperMapSize;')

    # Map size 4096
    if unWrapperMapSizeIndex == 1:
        # UV spacing
        m341_unWrapperSpacingArray = [0.0078125, 0.00634765625, 0.0048828125, 0.00390625, 0.0029296875, 0.00244140625, 0.001953125, 0.0009765625]
        # Border spacing
        m341_unWrapperBorderArray = [0.00390625, 0.003173828125, 0.00244140625, 0.001953125, 0.00146484375, 0.001220703125, 0.0009765625, 0.00048828125]

    # Map size 2048
    elif unWrapperMapSizeIndex == 2:
        # UV spacing
        m341_unWrapperSpacingArray = [0.015625, 0.0126953125, 0.009765625, 0.0078125, 0.005859375, 0.0048828125, 0.00390625, 0.001953125]
        # Border spacing
        m341_unWrapperBorderArray = [0.0078125, 0.00634765625, 0.0048828125, 0.00390625, 0.0029296875, 0.00244140625, 0.001953125, 0.0009765625]

    # Map size 1024
    elif unWrapperMapSizeIndex == 3:
        # UV spacing
        m341_unWrapperSpacingArray = [0.03125, 0.025390625, 0.01953125, 0.015625, 0.01171875, 0.009765625, 0.0078125, 0.00390625]
        # Border spacing
        m341_unWrapperBorderArray = [0.015625, 0.0126953125, 0.009765625, 0.0078125, 0.005859375, 0.0048828125, 0.00390625, 0.001953125]

    # Map size 512
    elif unWrapperMapSizeIndex == 4:
        # UV spacing
        m341_unWrapperSpacingArray = [0.0625, 0.05078125, 0.0390625, 0.03125, 0.0234375, 0.01953125, 0.015625, 0.0078125]
        # Border spacing
        m341_unWrapperBorderArray = [0.03125, 0.025390625, 0.01953125, 0.015625, 0.01171875, 0.009765625, 0.0078125, 0.00390625]

    # Map size 256
    elif unWrapperMapSizeIndex == 5:
        # UV spacing
        m341_unWrapperSpacingArray = [0.125, 0.1015625, 0.078125, 0.0625, 0.046875, 0.0390625, 0.03125, 0.015625]
        # Border spacing
        m341_unWrapperBorderArray = [0.0625, 0.05078125, 0.0390625, 0.03125, 0.0234375, 0.01953125, 0.015625, 0.0078125]

    # Map size 128
    elif unWrapperMapSizeIndex == 6:
        # UV spacing
        m341_unWrapperSpacingArray = [0.25, 0.203125, 0.15625, 0.125, 0.09375, 0.078125, 0.0625, 0.03125]
        # Border spacing
        m341_unWrapperBorderArray = [0.125, 0.1015625, 0.078125, 0.0625, 0.046875, 0.0390625, 0.03125, 0.015625]

    # Map size 64
    elif unWrapperMapSizeIndex == 7:
        # UV spacing
        m341_unWrapperSpacingArray = [0.5, 0.40625, 0.3125, 0.25, 0.1875, 0.15625, 0.125, 0.0625]
        # Border spacing
        m341_unWrapperBorderArray = [0.25, 0.203125, 0.15625, 0.125, 0.09375, 0.078125, 0.0625, 0.03125]

    # Map size 32
    elif unWrapperMapSizeIndex == 8:
        # UV spacing
        m341_unWrapperSpacingArray = [0.5, 0.5, 0.625, 0.5, 0.375, 0.3125, 0.25, 0.125]
        # Border spacing
        m341_unWrapperBorderArray = [0.25, 0.40625, 0.3125, 0.25, 0.1875, 0.15625, 0.125, 0.0625]
        

    # Clean up mesh
    mel.eval('toggleSelMode')
    mel.eval('toggleSelMode')
    cmds.selectMode(object=True)
    clean_up_object = cmds.ls(sl=True) or []
    mel.eval('polyCleanupArgList 4 { "0","1","0","0","0","0","1","0","1","1e-06","1","1e-05","0","1e-05","0","-1","1","1" };')
    mel.eval('polyCleanupArgList 4 { "0","1","0","0","0","0","0","0","0","1e-05","0","1e-05","0","1e-05","0","1","0","0" };')
    cmds.select(clean_up_object)
   
    mel.eval('toggleSelMode')
    mel.eval('toggleSelMode')
    cmds.selectMode(object=True)
    mel.eval('SelectMeshUVShell;')
    mel.eval('SelectAll;')

    # Select only some UVs if not all checkbox
    if unWrapper_all_check_box_value == 0:
        cmds.select(components)

    # Select all UVs if 3D cut and sew tool is active
    if mel.eval(f'gmatch {current_active_tool} "*superCutUVContext*"'):
        mel.eval('toggleSelMode')
        mel.eval('toggleSelMode')
        cmds.selectMode(object=True)
        mel.eval('SelectMeshUVShell;')
        mel.eval('SelectAll;')

    if mel.eval(f'gmatch {current_active_tool} "*PolyCutUVCtx*"'):
        mel.eval('toggleSelMode')
        mel.eval('toggleSelMode')
        cmds.selectMode(object=True)
        mel.eval('SelectMeshUVShell;')
        mel.eval('SelectAll;')

    # Unfold
    if unfold_unWrapper_check_mark_value == 1:
        mel.eval('u3dUnfold -ite 1 -p 0 -bi 1 -tf 1 -ms 2048 -rs 8;')

        # Curved checkbox off tries to keep shells straight while unfolding
        if curved_unWrapper_check_mark_value == 0:
            cmds.unfold(i=5000, ss=0.001, gb=0, gmb=0.5, pub=0, ps=0, oa=0, us="off")

    # Spin UV shells
    if unWrapper_spin_check_box_value == 1:
        mel.eval('texOrientShells;')

    # Scale UV shells
    m341_unWrapper_scaleShells = 0

    if unWrapper_scale_check_box_value == 1:
        m341_unWrapper_scaleShells = 1

    spc = m341_unWrapperSpacingArray[unWrapperSpacerIndex-1]
    mar = m341_unWrapperBorderArray[unWrapperBorderIndex-1]
    mel.eval(f'u3dLayout -res 512 -scl {m341_unWrapper_scaleShells} -spc {spc} -mar {mar} -box 0 1 0 1;')
    mel.eval('toggleSelMode')
    mel.eval('toggleSelMode')
    cmds.selectMode(object=True)
    mel.eval('DeleteHistory')

    # Bring back original component mode user was in
    if component_face > 0:
        mel.eval('SelectFacetMask;')

    if component_shell > 0:
        mel.eval('SelectMeshUVShell;')

    if component_vert > 0:
        mel.eval('SelectVertexMask;')

    if component_edge > 0:
        mel.eval('SelectEdgeMask;')

    if component_uv > 0 or component_multi > 0:
        mel.eval('SelectUVMask;')

    cmds.select(components)

    # Enter 3D cut and sew if it was active above
    if m341_unWrapper_CutSewSwitch == 1:
        mel.eval('SetCutSewUVTool')
        mel.eval('SelectNone;')

    print("Unfold: {}, Curved: {}, Rotate: {}, Scale: {}, All UVs: {}, Layout Complete".format(
        "Yes" if unfold_unWrapper_check_mark_value == 1 else "No",
        "Yes" if curved_unWrapper_check_mark_value == 1 and unfold_unWrapper_check_mark_value == 1 else "No",
        "Yes" if unWrapper_spin_check_box_value == 1 else "No",
        "Yes" if unWrapper_scale_check_box_value == 1 else "No",
        "Yes" if unWrapper_all_check_box_value == 1 else "No"
    ))

#*******************************************************************************************************
# Update angle int field Value
def m341_unWrapper_angle_ValueChanged():
    # Query the value from the float field and store it in a variable
    m341_unWrapper_angle_UserInput = cmds.intField('unwrapper_angle_IntFieldName', query=True, value=True)
    cmds.optionVar(intValue=["m341_unWrapper_angleIntField_VarName", m341_unWrapper_angle_UserInput])
    # Print value
    print("UVs angle set to {}".format(m341_unWrapper_angle_UserInput))

#*******************************************************************************************************
# Update UVs by angle Checkbox Value
def m341_unWrapper_uvsByAngle_ValueChanged():    
    #Query the value of the checkbox and store in variable 
    m341_unWrapper_uvsByAngle_UserInput = int(cmds.checkBox('unWrapper_uvsByAngle_CheckBoxName', query=True, value=True))
    cmds.optionVar(intValue=('m341_unWrapper_uvsByAngleCheckBox_VarName', m341_unWrapper_uvsByAngle_UserInput))
    
    #Print value
    if m341_unWrapper_uvsByAngle_UserInput == 0:
        print("UVs by angle checkbox off")
    else:
        print("UVs by angle checkbox on")

#*******************************************************************************************************
# Update angle int field Value
def m341_unWrapper_angle_ValueChanged():
    # Query the value from the float field and store it in a variable
    m341_unWrapper_angle_UserInput = cmds.intField('unwrapper_angle_IntFieldName', query=True, value=True)
    cmds.optionVar(intValue=["m341_unWrapper_angleIntField_VarName", m341_unWrapper_angle_UserInput])
    # Print value
    print("UVs angle set to {}".format(m341_unWrapper_angle_UserInput))

#*******************************************************************************************************
# Update UVs by hard edges Checkbox Value
def m341_unWrapper_uvsByHardEdges_ValueChanged():
    # Query the value of the checkbox and store in a variable
    m341_unWrapper_uvsByHardEdges_userInput = cmds.checkBox('unWrapper_uvsByHardEdges_CheckBoxName', query=True, value=True)
    cmds.optionVar(intValue=["m341_unWrapper_uvsByHardEdgesCheckBox_VarName", m341_unWrapper_uvsByHardEdges_userInput])
    # Print value
    if m341_unWrapper_uvsByHardEdges_userInput == 0:
        print("UVs by hard edges checkbox off")
    else:
        print("UVs by hard edges checkbox on")

#*******************************************************************************************************
# Update auto cut seams Checkbox Value
def m341_unWrapper_autoCutSeams_ValueChanged():
    # Query the value of the checkbox and store in a variable
    m341_unWrapper_autoCutSeams_userInput = cmds.checkBox('unWrapper_autoCutSeams_CheckBoxName', query=True, value=True)
    cmds.optionVar(intValue=["m341_unWrapper_autoCutSeamsCheckBox_VarName", m341_unWrapper_autoCutSeams_userInput])
    # Print value
    if m341_unWrapper_autoCutSeams_userInput == 0:
        print("Auto cut seams checkbox off")
    else:
        print("Auto cut seams checkbox on")

#*******************************************************************************************************
# Update keep normals Checkbox Value
def m341_unWrapper_keepNormals_ValueChanged():
    # Query the value of the checkbox and store in a variable
    m341_unWrapper_keepNormals_userInput = cmds.checkBox('unWrapper_keepNormals_CheckBoxName', query=True, value=True)
    cmds.optionVar(intValue=["m341_unWrapper_keepNormalsCheckBox_VarName", m341_unWrapper_keepNormals_userInput])
    # Print value
    if m341_unWrapper_keepNormals_userInput == 0:
        print("Keep normals checkbox off")
    else:
        print("Keep normals checkbox on")

#*******************************************************************************************************
# Update keep current seams Checkbox Value
def m341_unWrapper_keepCurrentSeams_ValueChanged():
    # Query the value of the checkbox and store in a variable
    m341_unWrapper_keepCurrentSeams_userInput = cmds.checkBox('unWrapper_keepCurrentSeams_CheckBoxName', query=True, value=True)
    cmds.optionVar(intValue=["m341_unWrapper_keepCurrentSeamsCheckBox_VarName", m341_unWrapper_keepCurrentSeams_userInput])
    # Print value
    if m341_unWrapper_keepCurrentSeams_userInput == 0:
        print("Keep current seams checkbox off")
    else:
        print("Keep current seams checkbox on")

#*******************************************************************************************************
# Update unfold Checkbox Value
def m341_unWrapper_unfold_ValueChanged():
    # Query the value of the checkbox and store in a variable
    m341_unWrapper_unfold_userInput = cmds.checkBox('unWrapper_unfold_CheckBoxName', query=True, value=True)
    cmds.optionVar(intValue=["m341_unWrapper_unfoldCheckBox_VarName", m341_unWrapper_unfold_userInput])
    # Print value
    if m341_unWrapper_unfold_userInput == 0:
        print("Unfold checkbox off")
    else:
        print("Unfold checkbox on")

#*******************************************************************************************************
# Update curved Checkbox Value
def m341_unWrapper_curved_ValueChanged():
    # Query the value of the checkbox and store in a variable
    m341_unWrapper_curved_userInput = cmds.checkBox('unWrapper_curved_CheckBoxName', query=True, value=True)
    cmds.optionVar(intValue=["m341_unWrapper_curvedCheckBox_VarName", m341_unWrapper_curved_userInput])
    # Print value
    if m341_unWrapper_curved_userInput == 0:
        print("Curved checkbox off")
    else:
        print("Curved checkbox on")

#*******************************************************************************************************
# Update spin Checkbox Value
def m341_unWrapper_spin_ValueChanged():
    # Query the value of the checkbox and store in a variable
    m341_unWrapper_spin_userInput = cmds.checkBox('unWrapper_spin_CheckBoxName', query=True, value=True)
    cmds.optionVar(intValue=["m341_unWrapper_spinCheckBox_VarName", m341_unWrapper_spin_userInput])
    # Print value
    if m341_unWrapper_spin_userInput == 0:
        print("Spin checkbox off")
    else:
        print("Spin checkbox on")

#*******************************************************************************************************
# Update scale Checkbox Value
def m341_unWrapper_scale_ValueChanged():
    # Query the value of the checkbox and store in a variable
    m341_unWrapper_scale_userInput = cmds.checkBox('unWrapper_scale_CheckBoxName', query=True, value=True)
    cmds.optionVar(intValue=["m341_unWrapper_scaleCheckBox_VarName", m341_unWrapper_scale_userInput])
    # Print value
    if m341_unWrapper_scale_userInput == 0:
        print("Scale checkbox off")
    else:
        print("Scale checkbox on")

#*******************************************************************************************************
# Update All Checkbox Value
def m341_unWrapper_all_ValueChanged():
    # Query the value of the checkbox and store in a variable
    m341_unWrapper_all_userInput = cmds.checkBox('unWrapper_all_CheckBoxName', query=True, value=True)
    cmds.optionVar(intValue=["m341_unWrapper_allCheckBox_VarName", m341_unWrapper_all_userInput])
    # Print value
    if m341_unWrapper_all_userInput == 0:
        print("All checkbox off")
    else:
        print("All checkbox on")


#*******************************************************************************************************
# Window and Buttons
def m341_launch_UnwrapperInterface():
    global m341_unWrapperVersion

    # Switch to load with texture editor or not
    textureEditor = 1

    if textureEditor == 1:
        # Yes texture editor
        mel.eval('TextureViewWindow;')
        cmds.window(title=m341_unWrapperVersion, parent="polyTexturePlacementPanel1Window", toolbox=True, sizeable=True, resizeToFitChildren=True)
    else:
        # No texture editor
        cmds.window(title=m341_unWrapperVersion, toolbox=True, sizeable=True, resizeToFitChildren=True)

    cmds.columnLayout(adjustableColumn=True)
    cmds.text(label="by johann9616")

    cmds.setParent("..")
    cmds.rowColumnLayout(numberOfRows=1)

    cmds.iconTextButton(style="textOnly", labelOffset=30, label="click for help", backgroundColor=(0.51, 0.51, 0.51), width=83, height=15, command="helpmaUnwrapper();")
    cmds.separator(width=1, style="none")

    cmds.iconTextButton(style="textOnly", labelOffset=30, label="reset", backgroundColor=(0.51, 0.51, 0.51), width=40, height=15, command="m341_unWrapper_Reset();")

    cmds.setParent("..")
    cmds.rowColumnLayout(numberOfRows=1)

    cmds.iconTextButton(style="textOnly", label="checker map", backgroundColor=(0.427, 0.643, 0.643), width=76, command="button1unWrapper();", commandRepeatable=0)
    cmds.separator(width=1, style="none")

    cmds.iconTextButton(style="textOnly", label="+", backgroundColor=(0.427, 0.643, 0.643), width=23, command="button2unWrapper();", commandRepeatable=0)
    cmds.separator(width=1, style="none")

    cmds.iconTextButton(style="textOnly", label="-", backgroundColor=(0.427, 0.643, 0.643), width=23, command="button3unWrapper();", commandRepeatable=0)

    cmds.setParent("..")
    cmds.rowColumnLayout(numberOfRows=1)

    cmds.iconTextButton(style="textOnly", label="planar map camera", labelOffset=30, backgroundColor=(0.32, 0.59, 0.72), width=124, command="m341_unWrapper_planarMapCamera();", commandRepeatable=1)

    cmds.setParent("..")
    cmds.rowColumnLayout(numberOfRows=1, height=18)

    # Save preferences UVs by angle checkbox
    unWrapper_uvsByAngle_CheckBoxValue = 1
    m341_unWrapper_uvsByAngle_UserInput = 0
    unWrapper_uvsByAngle_OptionVar = int(cmds.optionVar(exists="m341_unWrapper_uvsByAngleCheckBox_VarName"))

    if not unWrapper_uvsByAngle_OptionVar:
        # Set default value
        cmds.optionVar(intValue=("m341_unWrapper_uvsByAngleCheckBox_VarName", 1))
        unWrapper_uvsByAngle_CheckBoxValue = int(cmds.optionVar(query="m341_unWrapper_uvsByAngleCheckBox_VarName"))
    else:
        # Query from prefs file
        unWrapper_uvsByAngle_CheckBoxValue = int(cmds.optionVar(query="m341_unWrapper_uvsByAngleCheckBox_VarName"))




    cmds.checkBox('unWrapper_uvsByAngle_CheckBoxName', 
              label='',
              value=unWrapper_uvsByAngle_CheckBoxValue, 
              changeCommand='m341_unWrapper_uvsByAngle_ValueChanged()')
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

    cmds.intField('unwrapper_angle_IntFieldName', value=unWrapper_angle_intFieldValue, minValue=0, maxValue=180, width=30, height=17, changeCommand="m341_unWrapper_angle_ValueChanged();")

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

    cmds.checkBox('unWrapper_uvsByHardEdges_CheckBoxName', label="", value=unWrapper_uvsByHardEdges_CheckBoxValue, changeCommand="m341_unWrapper_uvsByHardEdges_ValueChanged();")
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

    cmds.checkBox('unWrapper_autoCutSeams_CheckBoxName', label="", value=unWrapper_autoCutSeams_CheckBoxValue, changeCommand="m341_unWrapper_autoCutSeams_ValueChanged();")
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

    cmds.checkBox('unWrapper_keepNormals_CheckBoxName', label="", value=unWrapper_keepNormals_CheckBoxValue, changeCommand="m341_unWrapper_keepNormals_ValueChanged();")
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

    cmds.checkBox('unWrapper_keepCurrentSeams_CheckBoxName', label="", value=unWrapper_keepCurrentSeams_CheckBoxValue, changeCommand="m341_unWrapper_keepCurrentSeams_ValueChanged();")
    cmds.text(label=" keep current seams")

    cmds.setParent("..")
    cmds.rowColumnLayout(numberOfRows=1)

    # Easy UVs button
    cmds.iconTextButton(style="textOnly", label="easy UVs", labelOffset=0, backgroundColor=(0.59, 0.53, 0.74), width=124, command="m341_unWrapper_EasyUVs();", commandRepeatable=1)

    cmds.setParent("..")
    cmds.rowColumnLayout(numberOfRows=1)

    # 3D cut and sew button
    cmds.iconTextButton(style="textOnly", label="3d cut and sew", labelOffset=30, backgroundColor=(0.772, 0.521, 0.302), width=91, command="m341_unWrapper_3dCutAndSew();", commandRepeatable=0)
    cmds.separator(width=1, style="none")

    # Exit button
    cmds.iconTextButton(style="textOnly", label="exit", backgroundColor=(0.772, 0.521, 0.302), width=32, command="m341_unWrapper_Exit();", commandRepeatable=0)

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

    cmds.checkBox('unWrapper_unfold_CheckBoxName', label="", value=unWrapper_unfold_CheckBoxValue, changeCommand="m341_unWrapper_unfold_ValueChanged();")
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

    cmds.checkBox('unWrapper_curved_CheckBoxName', label="", value=unWrapper_curved_CheckBoxValue, changeCommand="m341_unWrapper_curved_ValueChanged();")
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

    cmds.checkBox('unWrapper_spin_CheckBoxName', label="", value=unWrapper_spin_CheckBoxValue, changeCommand="m341_unWrapper_spin_ValueChanged();")
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

    cmds.checkBox('unWrapper_scale_CheckBoxName', label="", value=unWrapper_scale_CheckBoxValue, changeCommand="m341_unWrapper_scale_ValueChanged();")
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
    cmds.checkBox(
        'unWrapper_all_CheckBoxName',
        label="all", 
        value=unWrapper_all_CheckBoxValue, 
        changeCommand="m341_unWrapper_all_ValueChanged();"
    )

    cmds.setParent("..")
    cmds.rowLayout('unWrapperMapSize', numberOfColumns=2, columnAttach2=("left", "left"), columnOffset2=(5, 0), columnWidth=(1, 67), columnWidth2=(2, 30))
    # Map Size Option Menu
    map_size_option_menu = cmds.optionMenu('unWrapperMapSize', w=118, label="map size", height=17)
    for label in ["4096", "2048", "1024", "512", "256", "128", "64", "32"]:
        cmds.menuItem(label=label)

    cmds.optionMenu( map_size_option_menu, edit=True, select=2)

    cmds.setParent("..")
    cmds.rowLayout(numberOfColumns=2, columnAttach2=("left", "left"), columnOffset2=(5, 0), columnWidth=(1, 67), columnWidth2=(2, 30))
    # Padding Option Menu
    padding_option_menu = cmds.optionMenu('unWrapperUVSpacer', w=118, label="padding", height=17)
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
                        command="m341_unWrapper_Unwrap();",
                        commandRepeatable=1)

    cmds.showWindow()

                   
#*******************************************************************************************************
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
