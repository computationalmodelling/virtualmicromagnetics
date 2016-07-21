PDFLATEX_FLAGS = -synctex=1 -interaction=nonstopmode

all: vm_graph.png container_graph.png

clean:
	@rm -rf *.pdf *.png
	@for FL in $$(ls vm_graph*); do if [ "$$FL" != "vm_graph.tex" ];\
     then rm $$FL; fi; done
	@for FL in $$(ls container_graph*);\
	 do if [ "$$FL" != "container_graph.tex" ];\
     then rm $$FL; fi; done

container_graph.png: container_graph.pdf
	@convert -density 450 container_graph.pdf -quality 100 container_graph.png

container_graph.pdf: container_run.pdf container_build.pdf
	@pdflatex $(PDFLATEX_FLAGS) container_graph.tex

container_build.pdf:
	@dot -Tpdf container_build.dot -o container_build.pdf

container_run.pdf:
	@dot -Tpdf container_run.dot -o container_run.pdf

vm_graph.png: vm_graph.pdf
	@convert -density 450 vm_graph.pdf -quality 100 vm_graph.png

vm_graph.pdf: vm_run.pdf vm_build.pdf
	@pdflatex $(PDFLATEX_FLAGS) vm_graph.tex

vm_build.pdf:
	@dot -Tpdf vm_build.dot -o vm_build.pdf

vm_run.pdf:
	@dot -Tpdf vm_run.dot -o vm_run.pdf

.PHONY: all clean