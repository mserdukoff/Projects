// Copyright 2022 Matt Serdukoff

#include <iostream>
#include <vector>
#include <SFML/Graphics.hpp>
#include "Buffer.h"

Buffer::Buffer(float input) {
    this->val = input;
    rectangle.setSize(sf::Vector2f(30, val * 3));
    rectangle.setFillColor(sf::Color::White);
}

void Buffer::setPos(int pos) {
    this->posX = 0 + (30 * pos);
    rectangle.setPosition(posX, 600);
}

float Buffer::getVal() {
    return val;
}
void Buffer::setVal(float input) {
    this->val = input;
}

void Buffer::draw(sf::RenderTarget &target, sf::RenderStates states) const {
	target.draw(rectangle, states);
}