// Copyright 2022 Matt Serdukoff

#include <iostream>
#include <vector>
#include <SFML/Graphics.hpp>
#include "Buffer.h"

using std::vector;

class Visualizer: public sf::Drawable {
 public:
    Visualizer(vector<float> pVector);
    float return_vect(int _i);
    Buffer* return_buff(int _i);
    void set_vect(int _i, float input);
 private:
    vector <Buffer*> _vector;
    virtual void draw(sf::RenderTarget &target, sf::RenderStates states) const;
};