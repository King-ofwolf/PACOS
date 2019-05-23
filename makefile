all : Layout_make MPIPP_make

mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
srcdir := $(dir $(mkfile_path))

Layout_make : 
	$(MAKE) -C $(srcdir)Layout/

MPIPP_make :
	$(MAKE) -C $(srcdir)Algorithm/MapMPIPP/
