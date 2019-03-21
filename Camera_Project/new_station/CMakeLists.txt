cmake_minimum_required(VERSION 3.8.0)

INCLUDE (hbe)

# convert relative paths to absolutes, also check if exists
CHECK_AND_SET_PATH(NAME CASSANDRA_ROOT ${CASSANDRA_ROOT})
CHECK_AND_SET_PATH(NAME CASSANDRA_LIBRARY_DIR ${CASSANDRA_LIBRARY_DIR})

SET(CMAKE_AUTOMOC True)

SET(HBE_CASSANDRA_WORKSPACE ${CMAKE_CURRENT_SOURCE_DIR})
include("./hbe/camera.cmake")

# add additional cmake files that will result in new cassandra plugins/dlls
