##### create camera #####
INCLUDE (cassandra)

HBE_PROJECT (camera)

HBE_TARGET_ADD_DEPENDENCIES (cassandra) 
HBE_target_add_include_directories (
	"./include"
)

file(GLOB HEADER "include/*.h")
file(GLOB SOURCES "src/*.h" "src/*.cpp")
HBE_TARGET_ADD_SOURCEFILES (${SOURCES} FOLDER src)
HBE_TARGET_ADD_SOURCEFILES (${HEADER} FOLDER include)

HBE_TARGET_CREATE_CASSANDRA_LIBRARY(NAME camera PROJECT_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/..)
