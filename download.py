import os
os.environ['OPENXLAB_AK'] = "gnoewxwn5dznke163mxz"
os.environ['OPENXLAB_SK'] = "qk5ok2gvwpyabxe7qw60qgogk36rlagojernmwdj"
from openxlab.model import download
download(model_repo='yixinsong/Falcon-40B', model_name='Falcon-40B')