cmake_minimum_required (VERSION 2.6)
project (ShittyDB)

set (ROOT "${CMAKE_BINARY_DIR}/ShittyDB")
set (CMAKE_RUNTIME_OUTPUT_DIRECTORY "${ROOT}/bin")
set (CMAKE_LIBRARY_OUTPUT_DIRECTORY "${ROOT}/lib")
set (CMAKE_INSTALL_RPATH "${ROOT}/lib")

add_executable (tester tester.c shittydb.c)
add_library (shittydb SHARED shittydb.c)
target_link_libraries (tester shittydb)

install (TARGETS tester shittydb
         RUNTIME DESTINATION bin
         LIBRARY DESTINATION lib)
