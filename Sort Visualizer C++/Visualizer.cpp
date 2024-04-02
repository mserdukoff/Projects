// Copyright 2022 Matt Serdukoff

#include <iostream>
#include <vector>
#include <SFML/Graphics.hpp>
#include "Visualizer.h"

Visualizer::Visualizer(vector<float> pVector) {
     for (int i = 0; i < 20; i++) {
        Buffer* temp = new Buffer(pVector[i]);
        temp->setPos(i);
        _vector.push_back(temp);
     }   
}

float Visualizer::return_vect(int _i) {
    return this->_vector[_i]->getVal();
}

// used for testing
Buffer* Visualizer::return_buff(int _i) {
    return this->_vector[_i];
}

void Visualizer::set_vect(int _i, float input) {
    this->_vector[_i]->setVal(input);
}

void Visualizer::draw(sf::RenderTarget &target, sf::RenderStates states) const {
    for (int i = 0; i < 20; i++) {
        target.draw(*_vector[i], states);
    }
}