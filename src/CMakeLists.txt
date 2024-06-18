add_library(RomiRobot RomiRobot.cpp)
target_include_directories(
  RomiRobot PUBLIC $<BUILD_INTERFACE:${CMAKE_SOURCE_DIR}/include/>
                   $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>)
