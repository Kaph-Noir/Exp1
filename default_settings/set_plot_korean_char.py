import matplotlib as mpl
import matplotlib.font_manager as fm


fm.get_fontconfig_fonts()
font_location = 'C:/Windows/Fonts/malgun.ttf'  # For Windows
font_name = fm.FontProperties(fname=font_location).get_name()

mpl.rc('font', family=font_name)
mpl.rcParams['axes.unicode_minus'] = False