LC=rubber
LFLAGS=-d

all: writeup.pdf

%.pdf: %.tex refs.bib
	$(LC) $(LFLAGS) $<
