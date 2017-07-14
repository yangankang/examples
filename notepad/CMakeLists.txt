cmake_minimum_required(VERSION 3.7)
project(notepad)

set(CMAKE_CXX_STANDARD 14)

set(CMAKE_INCLUDE_CURRENT_DIR ON)
#打开Qt的MOC功能和UI文件处理功能
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
#查找Qt的库
find_package(Qt5Widgets REQUIRED)

set(SOURCE_FILES main.cpp MainDialog.cpp MainDialog.h HtmlFinder.cpp HtmlFinder.h)
qt5_add_resources(SOURCE_FILES resource.qrc)
add_executable(notepad ${SOURCE_FILES})

target_link_libraries(
        notepad
        Qt5::Widgets
)
