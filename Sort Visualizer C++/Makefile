CC = g++
CFLAGS = -Wall -Werror -pedantic -std=c++14
SFML = -lsfml-graphics -lsfml-window -lsfml-system

all: prj1

prj1: main.o Buffer.o Visualizer.o
	$(CC) main.o Buffer.o Visualizer.o -o prj1 $(SFML)

main.o: main.cpp Visualizer.h Buffer.h
	$(CC) $(CFLAGS) -c main.cpp Visualizer.h Buffer.h

Buffer.o: Buffer.cpp Buffer.h Visualizer.h
	$(CC) $(CFLAGS) -c Buffer.cpp Buffer.h Visualizer.h
Visualizer.o: Visualizer.cpp Buffer.h Visualizer.h
	$(CC) $(CFLAGS) -c Visualizer.cpp Buffer.h Visualizer.h

clean:
	rm main.o
	rm Buffer.o
	rm Visualizer.o
	rm *.gch
	rm prj1