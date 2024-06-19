# Add a custom command that produces version.cpp, plus a dummy output that's not
# actually produced, in order to force version.cmake to always be re-run before
# the build
add_custom_command(
  OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/version.cpp
         ${CMAKE_CURRENT_BINARY_DIR}/_version.cpp
  COMMAND ${CMAKE_COMMAND} -P ${CMAKE_CURRENT_SOURCE_DIR}/cmake/version.cmake
  COMMENT "Resolve dynamically generated version info into version.cpp")

add_library(RomiRobot RomiRobot.cpp ${CMAKE_CURRENT_BINARY_DIR}/version.cpp)
target_include_directories(
  RomiRobot PUBLIC $<BUILD_INTERFACE:${CMAKE_SOURCE_DIR}/include/>
                   $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>)
