# This is a cross compile toolchain for compiling on macOS and targeting The RPi
# 2B (armv7, 32-bit).  To do so, a suitable sysroot must be available to compile
# and link against.  It is assumed to be in the root project folder, and named
# sysroot.  It uses the MacPorts clang version 17, installed in /opt/local.
#
# The linker lld is specified because the default linker does not seem to handle
# the sysroot argument for cross compilation.
#
# This file can serve as a template for similar toolchains, and are easy to
# convert to armv8, aarch64, or even different versions of clang.

set(TARGET_ARCH "armv7")
set(TARGET_SYSROOT ${CMAKE_CURRENT_LIST_DIR}/../sysroot)

set(CLANG_NAME "clang-mp-17")
set(CLANGXX_NAME "clang++-mp-17")
set(CLANG_PATH "/opt/local/bin/")
set(LINKER_NAME "lld-mp-17")

set(CMAKE_CROSSCOMPILING ON)
set(CMAKE_SYSTEM_NAME Linux)
set(CMAKE_SYSTEM_PROCESSOR ${TARGET_ARCH})

set(CMAKE_SYSROOT ${TARGET_SYSROOT})

set(TARGET_TRIPLE ${CMAKE_SYSTEM_PROCESSOR}-linux-gnueabihf)

set(CMAKE_C_COMPILER "${CLANG_PATH}${CLANG_NAME}")
set(CMAKE_C_COMPILER_TARGET ${TARGET_TRIPLE})
set(CMAKE_CXX_COMPILER "${CLANG_PATH}${CLANGXX_NAME}")
set(CMAKE_CXX_COMPILER_TARGET ${TARGET_TRIPLE})

set(CMAKE_C_FLAGS "-Wall -pedantic")
set(CMAKE_CXX_FLAGS ${CMAKE_C_FLAGS})

set(CMAKE_EXE_LINKER_FLAGS ${CMAKE_EXE_LINKER_FLAGS}
                           "-Wl -fuse-ld=${LINKER_NAME}")
set(CMAKE_SHARED_LINKER_FLAGS ${CMAKE_EXE_LINKER_FLAGS})
set(CMAKE_MODULE_LINKER_FLAGS ${CMAKE_EXE_LINKER_FLAGS})

# Don't look for programs in the sysroot and only use the libs/includes
set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_PACKAGE ONLY)
