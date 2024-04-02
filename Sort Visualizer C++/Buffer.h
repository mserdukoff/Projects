// Copyright 2022 Matt Serdukoff

#include <iostream>
#include <vector>
#include <SFML/Graphics.hpp>

const float SCREEN_SIZE = 600;

using std::vector;

class Buffer: public sf::Drawable {
 public:
    Buffer(float input);
    void setPos(int pos);
    void setVal(float input);
    float getVal();
 private:
    float val;
    float posX;
    sf::RectangleShape rectangle;
    virtual void draw(sf::RenderTarget &target, sf::RenderStates states) const;
};