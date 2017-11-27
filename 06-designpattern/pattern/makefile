d = .
eR = \e[0m
ecB = \e[0;30m
ecR = \e[0;31m
ecG = \e[0;32m
ecO = \e[0;33m
ecP = \e[0;35m
ecC = \e[0;36m

default:
	@echo -e "$(ecG)Decide $(eR)on a target"
ifdef f
	$(MAKE) file
else
	@echo -e "$(ecG)Run $(ecC)dir $(eR)on $(ecP). $(eR)by default"
	$(MAKE) dir
endif

all:
	$(MAKE) clean

file:
	@echo -e "$(ecG)Run $(eR)target $(ecC)file $(eR)on $(ecP)$(f)$(eR)"
	@echo -e "$(ecG)Build $(ecP)$(f) $(eR)into $(ecP).build$(eR)/$(ecP)$(f)$(eR)"
	@mkdir -p .build/$(d)/
	@mkdir -p .build/$(d)/$(f)
	# First run for simple compilation
	@pdflatex -file-line-error -interaction=batchmode -output-directory=.build/$(d)/$(f) $(d)/$(f).tex || echo -e "$(ecR)Error$(eR)"
	@cat .build/$(d)/$(f)/$(f).log | grep ".*:[0-9]*:.*" || echo -e "$(ecG)Everything ok$(eR)"
	# Second run for progressive compilation
	@pdflatex -file-line-error -interaction=batchmode -output-directory=.build/$(d)/$(f) $(d)/$(f).tex || echo -e "$(ecR)Error$(eR)"
	@cat .build/$(d)/$(f)/$(f).log | grep ".*:[0-9]*:.*" || echo -e "$(ecG)Everything ok$(eR)"
	@cp .build/$(d)/$(f)/$(f).pdf $(d)/$(f).pdf || echo -e "$(ecR)Missing $(ecP)$(f).pdf$(eR)"
	@echo -e "$(ecG)Remove $(ecP).build$(eR)"
	rm -rf .build

FILES = $(wildcard $(d)/*.tex)
dir:
	@echo -e "$(ecG)Run $(eR)target $(ecC)dir $(eR)on $(ecP)$(d)$(eR)"
	@echo -e "$(ecG)Found $(ecP)$(FILES)$(eR)" && $(foreach x, $(FILES), $(MAKE) file f="$(notdir $(basename $(x)))";)

clean:
	@echo -e "$(ecG)Clean$(eR) up directory"
	rm -rf .build
	rm -f *.acn *.acr *.aux *.bbl *.blg *-blx.bib *.bcf *.dvi *.glg *.glo *.gls *.glsdefs *.ist *.log *.out *.run.xml *.synctex.gz *.toc *.xdy
	rm -rf _minted*
