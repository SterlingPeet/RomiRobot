#include <iostream>
#include "RomiRobot/RomiRobot.hpp"

int main() {
  int result = RomiRobot::add_one(1);
  std::cout << "1 + 1 = " << result << std::endl;
}
