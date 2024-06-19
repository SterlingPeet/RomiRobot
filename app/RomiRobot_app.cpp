#include <iostream>
#include "RomiRobot/RomiRobot.hpp"

int main() {
  int result = RomiRobot::add_one(1);
  std::cout << "RomiRobot version: " << romirobot_git_version() << std::endl;
  std::cout << "RomiRobot revision: " << romirobot_git_revision() << std::endl;
  std::cout << "RomiRobot branch: " << romirobot_git_branch() << std::endl;
  std::cout << "1 + 1 = " << result << std::endl;
}
