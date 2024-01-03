export OPENXLAB_AK="gnoewxwn5dznke163mxz"
export OPENXLAB_SK="qk5ok2gvwpyabxe7qw60qgogk36rlagojernmwdj"
openxlab model download --model-repo 'yixinsong/Falcon-40B' --model-name 'Falcon-40B'
CMAKE_ARGS="-DLLAMA_CUBLAS=on" python3 -m pip install git+https://github.com/hodlen/llama-cpp-python.git@perf --force-reinstall
