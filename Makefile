##
## EPITECH PROJECT, 2020
## make
## File description:
## make
##

MAIN 	= exo2.py

EXEC 	= crypto

TEMP_F 	= \#*\# *~ *.swp .vscode package*.json

all: build

build:
	cp $(MAIN) $(EXEC)
	chmod +x $(EXEC)

clean:
	rm -rf $(TEMP_F)

fclean: clean
