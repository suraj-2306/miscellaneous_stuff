SOURCES=sources
USER_DEP_SOURCES=$(SOURCES)/user_dep
ISIM_FILES=./isim/isim_generated_files
#Project file
PRJ=./$(SOURCES)/$(CUSTOM_TOP).prj
#Compiled executable
EXE=./$(ISIM_FILES)/$(CUSTOM_TOP).exe
#TCL commands that will run in the simulator
CMD=./$(SOURCES)/isim.cmd

#Temporary Command file
CMDTMP=./$(ISIM_FILES)/isim.tmp.cmd
#Waveform DataBase from simulation
WDB=./$(ISIM_FILES)/isim.wdb
#Log file from simulation
LOG=./$(ISIM_FILES)/isim.log
#Top-Level Entity
TOP=work.$(CUSTOM_TOP)
#Files created after compilation
RM_FILES= fuse.log fuse.xmsgs fuseRelaunch.cmd
RM_FOLDERS= isim/
FUSE_OPTIONS=-intstyle ise -incremental -lib unisims_ver -lib unimacro_ver -lib xilinxcorelib_ver -lib secureip
ISIM_OPTIONS=-intstyle ise -gui -tclbatch isim.cmd -wdb 
#Default action, just compile the files
#all: compile

#Compile with fuse
sim:simulate
compile: ./$(SOURCES)/$(CUSTOM_TOP).v
	mkdir -p ./isim/isim_generated_files
	fuse $(FUSE_OPTIONS) -o $(EXE)   -prj $(PRJ) $(TOP) work.glbl
	mv $(RM_FILES) $(RM_FOLDERS)

#Run the simulation and the command file
simulate: compile $(EXE) $(CMD)
	cat $(CMD) >> $(CMDTMP)
	echo "exit 0" >> $(CMDTMP)
	./$(EXE) -gui -tclbatch $(CMD) -log $(LOG) -wdb $(WDB)
	rm -f $(CMDTMP)

#Open the simulation to check out the waveform
view:$(WDB)
	isimgui -view $(WDB)

#For TDD
test: simulate $(LOG)
	grep "Error" $(LOG)

clear: $(EXE) 
	rm -f $(RM_FILES)
	rm -rf $(RM_FOLDERS)
