RESX=64
RESY=48
BLOCKSIZE=8
TARGET_GLYPH_COUNT=256
FRAMECT=183 # Updated from 6570 to reflect actual frames in badderbaby.gif
RES=$(RESX)x$(RESY)x$(BLOCKSIZE)

all : video-$(RES).gif

# include ../common/make.inc

LDFLAGS:=-lm -lgdi32 -luser32 -lkernel32
CFLAGS:=-O2 -g  -Wall -Wno-unused-but-set-variable -Wno-unused-result -Wno-unused-variable -Wno-unused-function -mavx2 -DBLOCKSIZE=$(BLOCKSIZE) -I../common -DTARGET_GLYPH_COUNT=$(TARGET_GLYPH_COUNT) -DRESX=$(RESX) -DRESY=$(RESY) -DFRAMECT=$(FRAMECT)

hufftreegentest : hufftreegentest.c
	gcc $(CFLAGS) -o $@ $^

videoout-$(RES).dat : ../badderbaby.gif gif_to_dat.py
	python gif_to_dat.py

videocomp : videocomp.c ../common/bacommon.h
	gcc $(CFLAGS) -o $@ $< $(LDFLAGS)

stream-$(RES).dat tiles-$(RES).dat : videoout-$(RES).dat videocomp
	./videocomp videoout-$(RES).dat $(RESX) $(RESY) tiles-$(RES).dat stream-$(RES).dat

streamcomp : streamcomp.c ../common/bacommon.h
	gcc $(CFLAGS) -o $@ $< $(LDFLAGS)

video-$(RES).gif : streamcomp stream-$(RES).dat tiles-$(RES).dat
	./streamcomp stream-$(RES).dat tiles-$(RES).dat video-$(RES).gif $(RESX) $(RESY)

midclean :
	python clean.py test-$(RES).gif streamcomp # Use python script for clean-up

clean : midclean
	python clean.py # Use python script for clean-up