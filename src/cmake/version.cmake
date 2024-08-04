# Pull the git describe data and put it into a string for compilation
# into the final binary.  The clean/dirty status of the local repo is
# not included in the describe output, so it gets check separately and
# appended if the repo is dirty.
#
# NOTE:  This will likely fail in an odd way if it is exported from git

execute_process(
  COMMAND git log --pretty=format:'%h' -n 1
  OUTPUT_VARIABLE GIT_REV
  ERROR_QUIET)

# Check whether we got any revision (which isn't always the case, e.g. when
# someone downloaded a zip file from Github instead of a checkout)
if("${GIT_REV}" STREQUAL "")
  set(GIT_REV "N/A")
  set(GIT_DIFF "")
  set(GIT_TAG "N/A")
  set(GIT_BRANCH "N/A")
else()
  execute_process(COMMAND bash -c "git diff --quiet --exit-code || echo +dirty"
                  OUTPUT_VARIABLE GIT_DIFF)
  execute_process(
    COMMAND git describe --tags
    OUTPUT_VARIABLE GIT_TAG
    ERROR_QUIET)
  execute_process(COMMAND git rev-parse --abbrev-ref HEAD
                  OUTPUT_VARIABLE GIT_BRANCH)

  string(STRIP "${GIT_REV}" GIT_REV)
  string(SUBSTRING "${GIT_REV}" 1 7 GIT_REV)
  string(STRIP "${GIT_DIFF}" GIT_DIFF)
  string(STRIP "${GIT_TAG}" GIT_TAG)
  string(STRIP "${GIT_BRANCH}" GIT_BRANCH)
endif()

set(VERSION
    "const char* GIT_REV=\"${GIT_REV}${GIT_DIFF}\";
const char* GIT_TAG=\"${GIT_TAG}${GIT_DIFF}\";
const char* GIT_BRANCH=\"${GIT_BRANCH}\";
")

if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/romirobot_version.c)
  file(READ ${CMAKE_CURRENT_SOURCE_DIR}/romirobot_version.c VERSION_)
else()
  set(VERSION_ "")
endif()

if(NOT "${VERSION}" STREQUAL "${VERSION_}")
  file(WRITE ${CMAKE_CURRENT_SOURCE_DIR}/romirobot_version.c "${VERSION}")
endif()

message(STATUS "RomiRobot Library Version is: ${GIT_TAG}${GIT_DIFF}")
