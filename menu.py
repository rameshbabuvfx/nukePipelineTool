import pipelineMain

menu = nuke.menu("Nuke")
menu.addCommand("Pipeline/Launcher", "pipelineMain.main()")
