# Dockerfile for using OpenCV for image recognition training
# Based on the Dockerfile by Johannes Schickling's OpenCV dockerfile which can be found at
# https://hub.docker.com/r/schickling/opencv/dockerfile
#
# Changes made to the original was updating the base version of Debian and updating the version
# of OpenCV being used.
#
# author: Collin Bolles

FROM debian:buster
LABEL maintainer="Collin Bolles <collinbolles@gmail.com>"

# Versions
ARG OPENCV_VERSION="4.1.1"
ARG CMAKE_VERSION="3.15.3"

# Install Dependencies
RUN apt-get update
RUN apt-get install -y libopencv-dev yasm libjpeg-dev libpng16-16 libavcodec-dev libavformat-dev \\
    libswscale-dev libdc1394-22-dev libv4l-dev python-dev python-numpy libtbb-dev libqt4-dev libgtk2.0-dev \\
    libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev \\
    x264 v4l-utils pkg-config curl build-essential cmake

# Update cmake
RUN apt remove cmake --assume-yes && \
    curl -L -o \
        /tmp/cmake-$CMAKE_VERSION.sh \
        https://github.com/Kitware/CMake/releases/download/v$CMAKE_VERSION/cmake-$CMAKE_VERSION-Linux-x86_64.sh && \
    chmod +x /tmp/cmake-$CMAKE_VERSION.sh && \
    sh /tmp/cmake-$CMAKE_VERSION.sh --skip-license && \
    ln -s /root/cmake-#CMAKE_VERSION-Linux-x86_64/bin/* /usr/bin

# Download OpenCV
RUN curl -sL https://github.com/Itseez/opencv/archive/$OPENCV_VERSION.tar.gz | tar xvz -C /tmp
RUN mkdir -p /tmp/opencv-$OPENCV_VERSION/build

WORKDIR /tmp/opencv-$OPENCV_VERSION/build

# Install OpenCV
RUN cmake -DWITH_FFMPEG=OFF -DWITH_OPENEXR=OFF -DBUILD_TIFF=OFF -DWITH_CUDA=OFF -DWITH_NVCUVID=OFF -DBUILD_PNG=OFF ..
RUN make
RUN make install

# Configure
RUN echo "/usr/local/lib" > /etc/ld.so.conf.d/opencv.conf
RUN ldconfig
RUN ln /dev/null /dev/raw1394 # hide warning - http://stackoverflow.com/questions/12689304/ctypes-error-libdc1394-error-failed-to-initialize-libdc1394

# Cleanup Package Manager
RUN apt-get remove --purge -y curl build-essential cmake
RUN apt-get autoclean && apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Prepare Source Directory
RUN mkdir /source

VOLUME ["/source"]
WORKDIR /source
CMD ["bash"]
