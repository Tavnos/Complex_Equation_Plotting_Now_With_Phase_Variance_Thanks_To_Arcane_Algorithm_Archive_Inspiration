import numpy as np
from IPython.display import HTML
import matplotlib.pyplot as plt
import matplotlib.colors as mpl_c
from matplotlib.cm import ScalarMappable as mpl_s_m

#heavily inspired from 
#https://www.algorithm-archive.org/contents/domain_coloring/domain_coloring.html

class Plot_Method():
    def __init__(self, linspz=(-2.0, 2.0, 2400)):
        self.fig, self.axes = plt.subplots()
        self.axes.set_xlabel("$Re(x)$")
        self.axes.set_ylabel("$Im(x)$")
        ls_hv = np.linspace(linspz[0], linspz[1], linspz[2])
        x_re, x_im = np.meshgrid(ls_hv, ls_hv)
        x_fn = x_re + 1j * x_im
        
        nh_fv = self.declare_f(x_fn)
        hc_va = self.d_color(nh_fv, -1)
        self.axes.imshow(hc_va,
                        extent=(-2.0, 2.0, -2.0, 2.0),
                        origin='lower', 
                        aspect='equal')
        self.fig.savefig('somename.png', dpi=430)
    def declare_f(self, x):
        return x**(2)
    def m_shading(self, h_var, c_val=.5, a_val=.5):
        hv_abs = np.abs(h_var)
        return c_val + a_val * (hv_abs - np.floor(hv_abs))
    def g_ln(self, h_var, h_tr_zh): 
        return (np.abs(np.sin(np.pi * np.real(h_var) ** h_tr_zh)) *
                np.abs(np.sin(np.pi * np.imag(h_var) ** h_tr_zh)))
    def d_color(self, h_var, h_tr_zh, c_t = 2.0, hp_w=(0, -1)):
        h_c = (np.pi - np.angle(h_var)) / (c_t * np.pi) # hue ? 
        s_c = self.m_shading(h_var)                     # saturation ?
        v_v = self.g_ln(h_var, h_tr_zh)                 # gridline value 
        h_s_v = np.moveaxis((h_c, s_c, v_v), hp_w[0], hp_w[1]) # hsv?
        return mpl_c.hsv_to_rgb(h_s_v)