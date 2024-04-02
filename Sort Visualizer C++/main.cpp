// Copyright 2022 Matt Serdukoff

#include <iostream>
#include <vector>
#include <stdlib.h>
#include <SFML/Graphics.hpp>
#include "Visualizer.h"

using std::cout;
using std::endl;
using std::vector;

void sort(Visualizer& pV, sf::RenderWindow &window);

int main() {

    // vector init
    vector <float> vect;
    // populate vector and print values
    for (int i = 0; i < 20; i++){
        vect.push_back(rand() % 200);
        cout << vect[i] << " ";
    }
    cout << endl;

    Visualizer visual(vect);

    sf::RenderWindow window(sf::VideoMode(SCREEN_SIZE, SCREEN_SIZE), "Sort Visualizer");
    window.setFramerateLimit(10);

    int x = 0;

    while (window.isOpen())  {
        sf::Event event;
		while (window.pollEvent(event)) {
			if (event.type == sf::Event::Closed) {
				window.close();
			}
		}
        window.clear();
        window.draw(*visual.return_buff(1));
        if (x == 0) {
            sort(visual, window);
        }
        x = 1;
	}
    return 0;
}

void sort(Visualizer& pV, sf::RenderWindow &window) {
    int min_index;
    float temp;
    for (int i = 0; i < 19; i++) {
        min_index = i;
        for (int j = i + 1; j < 20; j++) {
            if (pV.return_vect(j) < pV.return_vect(min_index)) {
                min_index = j;
            }
        }
        cout << "Swapping " << pV.return_vect(i + 1) << " and " << pV.return_vect(min_index) << endl;
        window.draw(pV);
        window.display();
        temp = pV.return_vect(min_index);
        pV.set_vect(min_index, pV.return_vect(i));
        pV.set_vect(i, temp);
        
        cout << "Array after swap: ";
        for (int k = 0; k < 20; k++) {
            cout << pV.return_vect(k) << " ";
        }
        cout << endl;
    }
}