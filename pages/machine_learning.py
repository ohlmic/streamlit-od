import streamlit as st
import numpy as np
import pandas as pd
import gluoncv as gcv
from gluoncv.utils import viz
from matplotlib import pyplot as plt

def app():
     st.subheader('Object detection inference')
     classes = ['tension_clamp', 'kpo', 'cable']
     net = gcv.model_zoo.get_model('ssd_512_mobilenet1.0_custom', classes=classes, pretrained_base=False)
     net.load_parameters('saved_models/ssd_512_mobilenet1.2_railway.params')
     x, image = gcv.data.transforms.presets.ssd.load_test('od_rail_dataset-holdout-test_01/11003.jpg', 512)
     cid, score, bbox = net(x)
     fig = plt.gcf()
     ax = viz.plot_bbox(image, bbox[0], score[0], cid[0], class_names=classes)
     st.pyplot(fig)
     #plt.show()

